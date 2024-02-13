from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.schema import FetchedValue

from .database import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True)
    nome = Column(String)
    saldo = Column(Integer)
    limite = Column(Integer)

class Transacao(Base):
    __tablename__ = "transacoes"

    id = Column(Integer, primary_key=True)
    cliente_id = Column(Integer)
    valor = Column(Integer)
    tipo = Column(String)
    descricao = Column(String)
    realizada_em = Column(DateTime, server_default=FetchedValue())