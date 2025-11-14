import requests
import threading
import queue
import time
from urllib.parse import urljoin

# Global settings
THREAD_COUNT = 20
TIMEOUT = 5
RETRY_LIMIT = 3

results = []
lock = threading.Lock()

def fetch(session, url, retries=0):
    """Send GET request with retry logic."""
    try:
        response = session.get(url, timeout=TIMEOUT)
        return response
    except requests.RequestException:
        if retries < RETRY_LIMIT:
            time.sleep(0.5)
            return fetch(session, url, retries + 1)
        return None

def worker(base_url, q):
    session = requests.Session()
    while True:
        try:
            path = q.get_nowait()
        except queue.Empty:
            return

        full_url = urljoin(base_url, path)
        response = fetch(session, full_url)

        if response:
            # Response fingerprinting
            length = len(response.text)
            status = response.status_code

            if status not in [404, 400]:
                with lock:
                    results.append({
                        "path": path,
                        "status": status,
                        "length": length
                    })

        q.task_done()

def run_bruteforce(base_url, wordlist_path):
    q = queue.Queue()

    # Load wordlist
    with open(wordlist_path, "r") as file:
        for line in file:
            q.put(line.strip())

    threads = []

    for _ in range(THREAD_COUNT):
        t = threading.Thread(target=worker, args=(base_url, q))
        t.start()
        threads.append(t)

    q.join()

    for t in threads:
        t.join()

    # Sort results by status + content length
    sorted_results = sorted(results, key=lambda x: (x["status"], x["length"]))

    print("\n=== Results ===")
    for r in sorted_results:
        print(f"{r['status']} - {r['length']} bytes - /{r['path']}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Multi-threaded Directory Bruteforcer")
    parser.add_argument("url", help="Base target URL")
    parser.add_argument("wordlist", help="Wordlist file path")

    args = parser.parse_args()

    run_bruteforce(args.url, args.wordlist)
