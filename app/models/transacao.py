from ..config import database
from datetime import datetime
from sqlalchemy.orm import validates
from sqlalchemy import desc

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

    @validates('valor')
    def validateValor(self, key, value):
        # return value
        if value - int(value) == 0:
            return value
        raise AssertionError('Campo \'{}\' fora da especificacao'.format(key))
    
    @validates('tipo')
    def validateDescricao(self, key, value):
        if value in ['c', 'd']:
            return value
        raise AssertionError('Campo {} fora da especificacao'.format(key))
    
    @validates('descricao')
    def validateDescricao(self, key, value):
        if value and 1 < len(value) <= 10:
            return value
        raise AssertionError('Campo {} fora da especificacao'.format(key))
    
    @classmethod
    def getAllByClientID(cls, client_id, limit=None):
        return cls.query.filter_by(cliente = client_id).order_by(desc(TransacaoModel.realizada_em)).limit(limit)
    
class CledsError(Exception):
    pass