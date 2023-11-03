# Controle de Livros em Flask

Uma aplicação simples de controle de livros desenvolvida em Flask, com suporte a um banco de dados PostgreSQL via SQLAlchemy e migrações usando Flask-Migrate.

## Pré-requisitos

- Python 3.x
- PostgreSQL instalado e configurado
- Pacotes Python listados em `requirements.txt`

## Configuração

1. Clone o repositório:

   ```bash
   git clone https://github.com/alan-vieira/api-rest-flask-mysql.git
   cd seu-projeto

2. Crie e ative um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows: venv\Scripts\activate

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt

4. Configure a variável de ambiente `FLASK_APP` para `app.py`:

   ```bash
   export FLASK_APP=app.py

5. Configure sua conexão com o banco de dados PostgreSQL em `mysqlpass.py`. Exemplo:

   ```bash
   mysqlpass = "postgresql://seu-usuario:senha@localhost:5432/livros-api-rest"

Certifique-se de que você tenha um banco de dados vazio chamado `livros-api-rest` configurado no PostgreSQL antes de prosseguir.

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

- Adicionar um novo livro:

   ```bash
   curl.exe -X POST -H "Content-Type: application/json" -d '{"autor": "J.R.R Tolkien", "titulo": "O Senhor dos Anéis - A Sociedade do Anel"}' http://localhost:5000/livros

   curl.exe -X POST -H "Content-Type: application/json" -d '{"autor": "J.K Howling", "titulo": "Harry Potter e a Pedra Filosofal"}' http://localhost:5000/livros
  
- Consultar todos os livros:

   ```bash
   curl.exe http://localhost:5000/livros
  
- Consultar um livro por ID:

   ```bash
   curl.exe http://localhost:5000/livros/4
  
- Atualizar um livro por ID:

   ```bash
   curl.exe -X PUT -H "Content-Type: application/json" -d '{"autor": "Clarice Lispector", "titulo": "Um Sopro de Vida"}' http://localhost:5000/livros/4
  
- Excluir um livro por ID:

   ```bash
   curl.exe -X DELETE http://localhost:5000/livros/4

Você pode usar ferramentas como `curl` para interagir com a API. 

Consulte o README.md para exemplos de comandos `curl`.

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](https://github.com/alan-vieira/api-rest-flask-mysql/blob/main/LICENSE) para detalhes.

## Autor

| [<img src="https://avatars.githubusercontent.com/alan-vieira" width=115><br><sub>Alan Vieira</sub>](https://github.com/alan-vieira) |
| :---: |
