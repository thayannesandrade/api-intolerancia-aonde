from app import db

class CasoIntolerancia(db.model):
    id = db.Column(db.integer, primary_key=True)
    bairro = db.Column(db.String(2), nullable=False)
    estado = db.Column(db.String(2), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    tipo_crime = db.Column(db.String(2), nullable=False)
    data_ocorrencia = db.Column(db.String(10), nullable=False)