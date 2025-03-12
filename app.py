import os
from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

# Carregar variáveis do .env
PORT = int(os.getenv("PORT", 5000))  # Se não achar no .env, usa 5000
DOWNLOAD_PATH = os.getenv("DOWNLOAD_PATH", "/app/downloads")

# Criar diretório se não existir
if not os.path.exists(DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Servidor rodando! Envie um POST para /download"}), 200

@app.route("/download", methods=["POST"])
def download_video():
    data = request.json
    urls = data.get("urls", [])

    if not urls:
        return jsonify({"error": "Nenhuma URL fornecida"}), 400

    ydl_opts = {
        'format': 'mp4',
        'outtmpl': f'{DOWNLOAD_PATH}/%(title)s.%(ext)s',
        'noplaylist': True,
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(urls)
        return jsonify({"message": "Download concluído!"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
