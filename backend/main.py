from fastapi import FastAPI
from pydantic import BaseModel
from backend.wallet import mint, burn, get_balance
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.mount("/static", StaticFiles(directory="frontend", html=True), name="static")


class MintRequest(BaseModel):
    to: str
    amount: int

class BurnRequest(BaseModel):
    from_addr: str
    amount: int

@app.post("/mint")
def mint_tokens(data: MintRequest):
    tx_hash = mint(data.to, data.amount)
    return {"status": "minted", "tx_hash": tx_hash}

@app.post("/burn")
def burn_tokens(data: BurnRequest):
    tx_hash = burn(data.from_addr, data.amount)
    return {"status": "burned", "tx_hash": tx_hash}

@app.get("/balance/{address}")
def balance(address: str):
    bal = get_balance(address)
    return {"balance": bal}
