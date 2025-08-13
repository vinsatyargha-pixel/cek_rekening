import requests

OY_API_KEY = "4e333f7b-b4ab-4133-8f43-16aefac91e23"

headers = {
    "Authorization": f"Bearer 4e333f7b-b4ab-4133-8f43-16aefac91e23",
    "Content-Type": "application/json"
}

payload = {
    "bank_code": "014",          # contoh bank code yang valid, cek dokumentasi
    "account_number": "1234567890"  # contoh nomor rekening yang valid
}

try:
    response = requests.post(
        "https://api-stg.oyindonesia.com/api/bank-account-inquiry",
        json=payload,
        headers=headers,
        timeout=10  # timeout biar gak lama nge-hang kalau error
    )
    print(f"Status Code: {response.status_code}")
    print(f"Response JSON: {response.json()}")
except requests.exceptions.Timeout:
    print("Error: Request timeout")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
except ValueError:
    # Kalau response bukan JSON valid
    print(f"Non-JSON Response: {response.text}")