from ..config import database
from .transacao import TransacaoModel

class ClienteModel(database.Model):
    __tablename__ = 'cliente'
    
    id = database.Column(database.Integer, primary_key=True)
    nome = database.Column(database.String)
    limite = database.Column(database.Integer)
    saldo = database.Column(database.Integer)
    
    # def __init__(self, id=id, nome=nome, limite=limite, saldo=saldo) -> None:
    #     super().__init__()
    #     self.id = id
    #     self.nome = nome
    #     self.limite = limite
    #     self.saldo = saldo
        
    def toJSON(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'limite': self.limite,
            'saldo': self.saldo
        }
        
    def updateSaldo(self, transacao: TransacaoModel):
        if transacao.tipo == 'd' and self.saldo - transacao.valor < self.limite * -1:
            return False
        
        if transacao.tipo == 'c':
            self.saldo += transacao.valor
        elif transacao.tipo == 'd':
            self.saldo -= transacao.valor
        
        return self

    def save(self):
        database.session.add(self)
        database.session.commit()
        
    @classmethod
    def findAll(cls):
        # return [item for item in cls.query.all()]
        return cls.query.all()
    
    @classmethod
    def findById(cls, id):
        return cls.query.filter_by(id=id).first()