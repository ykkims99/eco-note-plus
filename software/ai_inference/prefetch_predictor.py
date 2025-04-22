# prefetch_predictor.py
# Simulate prefetching of common URLs

import time

PREFETCH_LIST = [
    "https://www.wikipedia.org",
    "https://www.khanacademy.org",
    "https://www.raspberrypi.com"
]

def simulate_prefetch():
    print("Simulating prefetch of popular URLs:")
    for url in PREFETCH_LIST:
        print(f"Prefetching: {url} ...done")
        time.sleep(0.5)

if __name__ == "__main__":
    simulate_prefetch()
