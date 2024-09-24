from flask import Flask, jsonify, request
from flask_restx import Api, Resource, fields
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///casos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

api = Api(app, version='1.0', title='API de Intolerancia Religiosa',
          description='API para registrar e consultar casos de intolerancia religiosa',
          doc='/swagger')

class CasoIntolerancia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    bairro = db.Column(db.String(50), nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    tipo_crime = db.Column(db.String(50), nullable=False)
    data_ocorrencia = db.Column(db.String(50), nullable=False)

with app.app_context():
    db.create_all()

caso_model = api.model('Caso', {
    'id': fields.Integer(readOnly=True, description='ID do caso'),
    'bairro': fields.String(required=True, description='Bairro aonde ocorreu o caso'),
    'estado': fields.String(required=True, description='Estado'),
    'descricao': fields.String(required=True, description='Descrição do caso'),
    'tipo_crime': fields.String(required=True, description='Tipo de crime'),
    'data_ocorrencia': fields.String(required=True, description='Data do caso'),
})

@api.route('/')  # Usando @api.route para a raiz
class Index(Resource):
    def get(self):
        return {"message": "Bem-vindo à API de Intolerância Aonde!"}

@api.route('/casos')
class CasosResources(Resource):
    @api.doc('list_casos')
    @api.marshal_list_with(caso_model)
    def get(self):
        '''Listar todos os casos'''
        casos = CasoIntolerancia.query.all()
        return casos, 200
    
    @api.doc('create_caso')
    @api.expect(caso_model)
    @api.marshal_with(caso_model, code=201)
    def post(self):
        '''Cadastrar um novo caso'''
        dados = api.payload
        novo_caso = CasoIntolerancia(
            bairro=dados['bairro'],
            estado=dados['estado'],
            descricao=dados['descricao'],
            tipo_crime=dados['tipo_crime'],
            data_ocorrencia=dados['data_ocorrencia'],
        )
        db.session.add(novo_caso)
        db.session.commit()
        return novo_caso, 201

@api.route('/casos/<int:id>')
@api.response(404, 'Caso não encontrado')
@api.param('id', 'Identificador do caso')
class CasoResource(Resource):
    @api.doc('get_caso')
    @api.marshal_with(caso_model)
    def get(self, id):
        '''Obter um caso específico por ID'''
        caso = CasoIntolerancia.query.get_or_404(id)
        return caso, 200

if __name__ == '__main__':
    app.run(debug=True)
