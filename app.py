from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Ganti API key dan URL sesuai environment
OY_API_KEY = "4e333f7b-b4ab-4133-8f43-16aefac91e23"  # Ganti sama Production API key lo
OY_API_URL = "https://partner.oyindonesia.com/api/bank-account-inquiry"  # Production URL

# Kalau mau pake staging:
# OY_API_KEY = "4e333f7b-b4ab-4133-8f43-16aefac91e23"
# OY_API_URL = "https://api-stg.oyindonesia.com/api/bank-account-inquiry"

@app.route('/cek-rekening', methods=['POST'])
def cek_rekening():
    try:
        data = request.get_json()
        bank_code = data.get('bank_code')
        account_number = data.get('account_number')

        if not bank_code or not account_number:
            return jsonify({"error": "bank_code dan account_number wajib diisi"}), 400

        headers = {
            "Authorization": f"Bearer {OY_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "bank_code": bank_code,
            "account_number": account_number
        }

        response = requests.post(OY_API_URL, json=payload, headers=headers)

        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({
                "error": "Gagal ambil data dari OY",
                "status_code": response.status_code,
                "text": response.text
            }), 500

    except Exception as e:
        return jsonify({"error": "Terjadi kesalahan pada server", "message": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
