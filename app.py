import requests

OY_API_KEY = "4e333f7b-b4ab-4133-8f43-16aefac91e23"

headers = {
    "Authorization": f"Bearer {OY_API_KEY}",
    "Content-Type": "application/json"
}

payload = {
    "bank_code": "014",
    "account_number": "1234567890"
}

try:
    response = requests.post(
        "https://api-stg.oyindonesia.com/api/bank-account-inquiry",
        json=payload,
        headers=headers,
        timeout=10
    )
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")
except requests.exceptions.Timeout:
    print("Error: Request timeout")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
except ValueError:
    print(f"Non-JSON Response: {response.text}")
