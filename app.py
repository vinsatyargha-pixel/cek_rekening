from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OY_API_KEY = "4e333f7b-b4ab-4133-8f43-16aefac91e23"

@app.route('/cek-rekening', methods=['POST'])
def cek_rekening():
    data = request.get_json()
    headers = {
        "Authorization": f"Bearer {OY_API_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        "https://api-stg.oyindonesia.com/api/bank-account-inquiry",
        json=data,
        headers=headers
    )

    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({
            "error": "Gagal ambil data dari OY",
            "status_code": response.status_code,
            "text": response.text
        }), 500

