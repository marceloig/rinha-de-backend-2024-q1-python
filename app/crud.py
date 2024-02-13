from sqlalchemy.orm import Session
from . import models, schemas


def get_cliente(db: Session, id: int):
    return db.query(models.Cliente).get(id)

def list_transacoes(db: Session, id: int):
    return db.query(models.Transacao).filter_by(cliente_id=id).limit(10).all()

def update_credito(db: Session, cliente: models.Cliente, transacao: schemas.Transacao): 
    cliente.saldo = models.Cliente.saldo + transacao.valor
    transacao = models.Transacao(cliente_id=cliente.id, tipo=transacao.tipo, valor=transacao.valor, descricao=transacao.descricao)
    db.add(transacao)
    db.commit()

    return cliente

def update_debito(db: Session, cliente: models.Cliente, transacao: schemas.Transacao):
    cliente.saldo = models.Cliente.saldo - transacao.valor
    db.flush()
    saldo = cliente.saldo
    limite = cliente.limite
    if abs(saldo) > limite:
        raise Exception("Debito acima do limite")
    transacao = models.Transacao(cliente_id= cliente.id, tipo=transacao.tipo, valor=transacao.valor, descricao=transacao.descricao)
    db.add(transacao)
    db.commit()

    return cliente