from typing import Union, List
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from datetime import datetime

models.Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/clientes/{id}/transacoes")
def transacoes(id: int, transacao: schemas.Transacao, db: Session = Depends(get_db)):
    cliente = crud.get_cliente(db, id)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    
    if transacao.tipo == "c":
        cliente = crud.update_credito(db, cliente, transacao)
    if transacao.tipo == "d":
        try:
            cliente = crud.update_debito(db, cliente, transacao)
        except Exception as e:
            raise HTTPException(status_code=422, detail=str(e))
    
    return schemas.RespostaTransacao(limite=cliente.limite, saldo=cliente.saldo)

@app.get("/clientes/{id}/extrato", response_model=schemas.RespostaExtrato)
def extrato(id: int, db: Session = Depends(get_db)):
    cliente = crud.get_cliente(db, id)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    saldo = schemas.Saldo(limite=cliente.limite, total=cliente.saldo, data_extrato=str(datetime.now()))
    ultimas_transacoes = crud.list_transacoes(db, cliente.id)
    
    return schemas.RespostaExtrato(saldo=saldo, ultimas_transacoes=ultimas_transacoes)