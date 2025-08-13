from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OY_API_KEY = "4e333f7b-b4ab-4133-8f43-16aefac91e23"  # ganti kalau mau pakai key lo sendiri

@app.route('/cek-rekening', methods=['POST'])
def cek_rekening():
    data = request.json
    bank_code = data.get('bank_code')
    account_number = data.get('account_number')

    headers = {
        "Authorization": f"Bearer {OY_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "bank_code": bank_code,
        "account_number": account_number
    }

    response = requests.post(
        "https://api.oyindonesia.com/api/bank-account-inquiry",
        json=payload,
        headers=headers
    )

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({
            "error": "Gagal ambil data dari OY",
            "status_code": response.status_code,

