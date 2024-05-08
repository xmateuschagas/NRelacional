from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@localhost/formulario_Aula'
db = SQLAlchemy(app)

class Funcionario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    primeiro_nome = db.Column(db.String(80), nullable=False)
    sobrenome = db.Column(db.String(80), nullable=False)
    data_admissao = db.Column(db.Date, nullable=False)
    id_setor = db.Column(db.String(80), nullable=False)
    id_cargo = db.Column(db.String(80), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_funcionario():
    funcionario = Funcionario(
        primeiro_nome=request.form['primeiro_nome'],
        sobrenome=request.form['sobrenome'],
        data_admissao=request.form['data_admissao'],
        id_setor=request.form['id_setor'],
        id_cargo=request.form['id_cargo']
    )
    db.session.add(funcionario)
    db.session.commit()
    return 'Funcionário adicionado com sucesso!'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Cria todas as tabelas definidas pelos modelos
    app.run(debug=True)
