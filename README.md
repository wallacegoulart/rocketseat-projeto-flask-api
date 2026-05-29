# Flask API — Projeto Exemplo

Este projeto é um exemplo simples de uma API construída com Flask em Python. Ele serve como ponto de partida para aprender a criar endpoints RESTful, organizar um projeto Flask e executar localmente.

**Funcionalidades**
- Estrutura mínima para uma API REST com Flask
- Exemplos de endpoints (GET, POST)
- Instruções de instalação e execução

**Requisitos**
- Python 3.8+
- pip

## Instalação
1. Crie e ative um ambiente virtual (Windows):

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

2. Instale dependências (se houver `requirements.txt`):

```powershell
pip install -r requirements.txt
```

Se não houver `requirements.txt`, instale Flask diretamente:

```powershell
pip install flask
```

## Estrutura sugerida do projeto

- app.py (ou package `app/`) — ponto de entrada do Flask
- requirements.txt — dependências
- README.md — documentação

Exemplo mínimo de `app.py`:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@app.route('/items', methods=['POST'])
def create_item():
    data = request.get_json() or {}
    # aqui você criaria o item (ex: salvar em DB)
    return jsonify({'item': data}), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
```

## Executando a API
Defina a variável de ambiente e rode diretamente com Python:

```powershell
python app.py
```

Ou usando o comando `flask` (quando `FLASK_APP` estiver configurado):

```powershell
set FLASK_APP=app.py
set FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
```

## Endpoints de exemplo
- GET `/health` — retorna status da API

```bash
curl http://localhost:5000/health
```

- POST `/items` — cria um item (JSON)

```bash
curl -X POST http://localhost:5000/items -H "Content-Type: application/json" -d '{"name":"Exemplo","value":123}'
```

## Boas práticas e próximos passos
- Adicionar `requirements.txt` com versões fixas
- Usar Blueprints para organizar rotas em módulos
- Adicionar tratamento de erros e validação (pydantic, marshmallow)
- Conectar a um banco de dados (SQLite, PostgreSQL)
- Escrever testes automatizados (pytest)
- Containerizar com Docker para facilitar deploy

## Contribuindo
Sinta-se à vontade para abrir issues ou pull requests com melhorias.

## Licença
Escolha e adicione uma licença (ex: MIT).
