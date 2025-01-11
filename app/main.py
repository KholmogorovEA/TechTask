from fastapi import FastAPI
from app.tariffs.router import router as router_tarrifs


app = FastAPI(title="Тарифы_TELFIN")

app.include_router(router_tarrifs)