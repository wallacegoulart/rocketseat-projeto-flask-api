# Flask API — Projeto Exemplo

Este repositório contém uma API simples em Flask para gerenciar tarefas (CRUD). O objetivo é servir como projeto didático para estudar criação de endpoints, execução local e testes básicos.

**Principais arquivos**
- `app.py` — aplicação Flask com endpoints (ponto de entrada).
- `models/task.py` — modelo `Task` e conversão para dicionário.
- `tests.py` — testes simples que usam `requests` para validar endpoints.
- `requirements.txt` — dependências do projeto.

**Requisitos**
- Python 3.8+
- pip

**Instalação rápida (Windows)**
1. Crie e ative um ambiente virtual:

```powershell
python -m venv venv
venv\Scripts\Activate.ps1
```

2. Instale as dependências:

```powershell
pip install -r requirements.txt
```

Observação: o arquivo `requirements.txt` pode estar em codificação UTF-16; se `pip` falhar ao ler, re-salve o arquivo em UTF-8 ou instale `flask` manualmente:

```powershell
pip install flask requests pytest
```

**Executando a API**
1. Inicie a aplicação (executa em `localhost:5000` por padrão):

```powershell
python app.py
```

2. Em outro terminal, execute os testes (certifique-se de que o servidor está em execução):

```powershell
pytest .\tests.py -v
```

**Endpoints**
- POST `/tasks` — criar tarefa
    - Payload JSON: `{"title": "Título", "description": "..."}`
    - Resposta: `{ "message": "Nova tarefa criada com sucesso", "id": <int> }`

```bash
curl -X POST http://127.0.0.1:5000/tasks -H "Content-Type: application/json" -d '{"title":"Teste","description":"desc"}'
```

- GET `/tasks` — listar tarefas
    - Resposta: `{ "tasks": [...], "total_tasks": <int> }`

```bash
curl http://127.0.0.1:5000/tasks
```

- GET `/tasks/<id>` — obter tarefa específica

```bash
curl http://127.0.0.1:5000/tasks/1
```

- PUT `/tasks/<id>` — atualizar tarefa
    - Payload JSON: `{"title": "novo", "description": "...", "completed": true}`

- DELETE `/tasks/<id>` — remover tarefa

**Observações e problemas conhecidos**
- O endpoint `GET /tasks` atualmente tem um bug de variável no código em `app.py`: a lista é construída com `tasks_list = [tasks.to_dict() for tasks in tasks]` — o correto é usar um nome de iteração diferente (`t.to_dict()`), veja [app.py](app.py#L1-L200).
- Alguns códigos de status retornados são `200` onde `201` poderia ser mais apropriado para criação; os testes atuais esperam `200` para criação.
- O arquivo `requirements.txt` parece estar em UTF-16; caso ocorra erro ao instalar, reencodifique como UTF-8.

**Melhorias sugeridas**
- Corrigir o bug em `GET /tasks` (substituir `tasks.to_dict()` por `t.to_dict()`).
- Adicionar validação de input e tratamento de erros (usar `pydantic` ou `marshmallow`).
- Persistir dados em um banco (SQLite para desenvolvimento).
- Melhorar status codes e mensagens (usar `201` em criação).
- Refatorar com Blueprints e separar rotas em módulos para escalar.

**Como contribuir**
Abra uma issue ou envie um pull request com melhorias. Para correções rápidas, edite `app.py` e rode os testes com `pytest`.

---
Arquivo atualizado automaticamente com base na análise do código.
