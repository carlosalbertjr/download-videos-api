# 📥 Download Videos API

Este projeto é uma API para baixar vídeos do YouTube e Dailymotion usando `yt-dlp`, desenvolvida em **Python** e **Flask**, com suporte a **Docker**.

---

## 🚀 Como Rodar o Projeto

### 1️⃣ **Clone o Repositório**

```sh
git clone https://github.com/seu-usuario/download-videos-api.git
cd download-videos
```

### 2️⃣ **Configure as Variáveis de Ambiente**

Crie um arquivo `.env` e defina as variáveis:

```ini
PORT=5000
DOWNLOAD_PATH=/app/downloads
```

### 3️⃣ **Rodando com Docker**

#### 📌 **Rodar em Background (Modo Detach)**

```sh
docker-compose up -d
```

#### 📌 **Parar o Container**

```sh
docker-compose down
```

---

## 🎯 Como Usar a API

### ✅ **Verificar se o Servidor está Rodando**

Acesse no navegador:

```
http://localhost:5000/
```

Deve retornar:

```json
{"message": "Servidor rodando! Envie um POST para /download"}
```

### 📥 **Baixar Vídeos via API**

#### 🔹 **POST /download**

**Exemplo de Requisição:**

```sh
curl -X POST http://localhost:5000/download \
     -H "Content-Type: application/json" \
     -d '{"urls": ["https://www.youtube.com/watch?v=VIDEO_ID"]}'
```

**Resposta de Sucesso:**

```json
{"message": "Download concluído!"}
```

**Erros Possíveis:**

```json
{"error": "Nenhuma URL fornecida"}  // Caso o JSON não tenha URLs
{"error": "Erro ao baixar o vídeo"}  // Caso ocorra falha no download
```

---

## 🛠 Tecnologias Utilizadas

- **Python 3.11**
- **Flask** (Framework Web)
- **yt-dlp** (Download de Vídeos)
- **Docker** + **Docker Compose**

---

## 📌 Estrutura dos Arquivos

```
download-videos/
│── app.py  # Código principal
│── requirements.txt  # Dependências do projeto
│── Dockerfile  # Configuração do Docker
│── docker-compose.yml  # Configuração do Docker Compose
│── .env  # Variáveis de ambiente
└── downloads/  # Pasta onde os vídeos serão salvos
```

---

## 🏗 Contribuições

Sinta-se à vontade para enviar **pull requests** e reportar **issues**. 😊

---

## 📜 Licença

Este projeto está licenciado sob a **MIT License**.

