from pydantic import BaseModel
from typing import Union, List
import datetime

class Transacao(BaseModel):
    valor: int
    tipo: str
    descricao: Union[str, None] = None
    realizada_em: Union[datetime.datetime, None] = None

    class Config:
        orm_mode = True

class RespostaTransacao(BaseModel):
    limite: int
    saldo: int

class Saldo(BaseModel):
    total: int
    data_extrato: str
    limite: int

class RespostaExtrato(BaseModel):
    saldo: Saldo
    ultimas_transacoes: List[Transacao]

    class Config:
        orm_mode = True