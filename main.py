import requests
import time
import tqdm
url = "https://httpbin.org/get"
timeout_seconds = 9
mx_time = 0
mn_time = 100
total = 0
response = None  # Global variable to store the response
warmup_trials = 5
connection = True
print("warming up the fission chamber")
for _ in tqdm.tqdm(range(warmup_trials)):
    try:
        response = requests.get(url, timeout=timeout_seconds)
    except:
        print("connection timeout(check your internet connection)")
        connection = False
        break
    mx_time = max(mx_time, response.elapsed.total_seconds())
    mn_time = min(mn_time, response.elapsed.total_seconds())
    total += response.elapsed.total_seconds()
    time.sleep(0.01)
if connection:
    try:
        print("waiting for the atom to split")
        response = requests.get(url, timeout=timeout_seconds)
        resp_time = response.elapsed.total_seconds()
        resp_time = abs(resp_time - mn_time)/(mx_time - mn_time)
        print(resp_time)
    except:
        print("connection timeout(check your internet connection)")
        connection = False
        
