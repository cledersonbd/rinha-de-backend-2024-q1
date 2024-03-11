from ..config import database
from datetime import datetime
from sqlalchemy.orm import validates

class TransacaoModel(database.Model):
    __tablename__ = 'transacao'
    
    id = database.Column(database.Integer, primary_key=True)
    valor = database.Column(database.Integer)
    tipo = database.Column(database.String(1))
    descricao = database.Column(database.String(10))
    cliente = database.Column(database.Integer, database.ForeignKey('cliente.id'))
    realizada_em = database.Column(database.DateTime)        
    
    def save(self):
        self.realizada_em = datetime.now()
        database.session.add(self)
        database.session.commit()
    
    def toJSON(self):
        return {
            'valor': self.valor,
            'tipo': self.tipo,
            'descricao': self.descricao,
            'realizada_em': self.realizada_em
        }

    # @validates('descricao')
    # def validateDescricao(self, key, value):
        # if len(value) > 10:
            # raise CledsError('{} maior que 10 caracteres'.format(key))
        # return value
    
    @classmethod
    def getAllByClientID(cls, client_id, limit=None):
        return cls.query.filter_by(cliente = client_id).limit(limit)
    
class CledsError(Exception):
    pass