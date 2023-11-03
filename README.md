# Controle de Livros em Flask

Uma aplicação simples de controle de livros desenvolvida em Flask, com suporte a um banco de dados PostgreSQL via SQLAlchemy e migrações usando Flask-Migrate.

## Pré-requisitos

- Python 3.x
- PostgreSQL instalado e configurado
- Pacotes Python listados em `requirements.txt`

## Configuração

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/seu-projeto.git
   cd seu-projeto

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt

4. Configure a variável de ambiente `FLASK_APP` para `app.py´:

   ```bash
   export FLASK_APP=app.py

5. Configure sua conexão com o banco de dados PostgreSQL em `mysqlpass.py`. Exemplo:

   ```bash
   mysqlpass = "postgresql://seu-usuario:senha@localhost:5432/livros-api-rest"

6. Inicialize o banco de dados e execute as migrações:

   ```bash
   flask db init
   flask db migrate
   flask db upgrade

7. Inicie o servidor de desenvolvimento:

   ```bash
   flask run

A aplicação estará disponível em `http://localhost:5000`.

## Uso

A API permite gerenciar uma coleção de livros com as seguintes operações:

- `POST /livros`: Adicionar um novo livro.
- `GET /livros`: Consultar todos os livros.
- `GET /livros/<ID>`: Consultar um livro por ID.
- `PUT /livros/<ID>`: Atualizar um livro por ID.
- `DELETE /livros/<ID>`: Excluir um livro por ID.

Você pode usar ferramentas como `curl` para interagir com a API. 

Consulte o README.md para exemplos de comandos `curl`.
