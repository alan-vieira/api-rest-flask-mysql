"""
Aplicação de controle de livros em Flask
"""
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from mysqlpass import mysqlpass

app = Flask (__name__)

# conexão com o banco de dados
app.config["SQLALCHEMY_DATABASE_URI"] = mysqlpass
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class ColecaoLivros(db.Model):
    """
    Classe que representa a tabela de livros no banco de dados.

    Atributos:
    - id: ID único do livro.
    - autor: Nome do autor do livro.
    - titulo: Título do livro.
    """
    __tablename__ = 'livros'

    livro_id = db.Column(db.Integer, primary_key=True)
    autor = db.Column(db.String())
    titulo = db.Column(db.String())

    def __init__(self, autor, titulo):
        """
        Inicializa um novo objeto Livro.

        Parâmetros:
        - autor (str): Nome do autor do livro.
        - titulo (str): Título do livro.
        """
        self.autor = autor
        self.titulo = titulo

    def __repr__(self):
        """
        Representação em string do objeto Livro.
        """
        return f'<Livro {self.titulo}>'


# Consulta todos os livros ou adiciona um novo livro
@app.route('/livros', methods=['POST', 'GET'])
def manipular_livros():
    """
    Manipula solicitações para a coleção de livros.

    - Para solicitações POST, permite adicionar um novo livro à coleção.
    - Para solicitações GET, permite consultar todos os livros na coleção.

    Retorna um JSON com os livros ou uma mensagem de erro em caso de falha.
    """
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            novo_livro = ColecaoLivros(
                autor=data['autor'], titulo=data['titulo'])
            db.session.add(novo_livro)
            db.session.commit()
            return {
                'message': f'O livro {novo_livro.titulo} foi adicionado com sucesso'}

        return {'error': 'A requisição não possui um formato JSON'}

    if request.method == 'GET':
        livros = ColecaoLivros.query.all()
        resultado = [
            {
                'autor': livro.autor,
                'titulo': livro.titulo
            } for livro in livros]

        return {'count': len(resultado), 'livros': resultado}


# Consulta, atualiza ou remove um livro por ID
@app.route('/livros/<int:livro_id>', methods=['GET', 'PUT', 'DELETE'])
def manipular_livros_por_id(livro_id):
    """
    Manipula solicitações para um livro específico por ID.

    - Para solicitações GET, permite consultar um livro por ID.
    - Para solicitações PUT, permite atualizar as informações de um livro por
    ID.
    - Para solicitações DELETE, permite excluir um livro por ID.

    Parâmetros:
    - id (int): ID do livro a ser consultado, atualizado ou excluído.

    Retorna um JSON com os dados do livro consultado, uma mensagem de sucesso
    ao atualizar ou excluir,
    ou uma mensagem de erro em caso de falha.
    """
    livro = ColecaoLivros.query.get_or_404(livro_id)

    if request.method == 'GET':
        response = {
            'autor': livro.autor,
            'titulo': livro.titulo
            }

        return {'message': 'sucesso', 'livro': response}

    if request.method == 'PUT':
        data = request.get_json()
        livro.autor = data['autor']
        livro.titulo = data['titulo']
        db.session.add(livro)
        db.session.commit()
        return {
            'message': f'O livro {livro.titulo} foi atualizado com sucesso'}

    if request.method == 'DELETE':
        db.session.delete(livro)
        db.session.commit()
        return {
            'message': f'O livro {livro.titulo} foi removido com sucesso'}


if __name__ == '__main__':
    app.run(debug=True)
