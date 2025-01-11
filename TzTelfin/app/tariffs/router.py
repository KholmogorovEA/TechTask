import httpx
from fastapi import APIRouter, HTTPException, Query
from app.config import settings, HEADERS
import requests


router = APIRouter(
    prefix="/tariffs",
    tags=["Страницы с тарифами"]
)


# async вариант 
@router.get("/", description="Получите от компании TELFIN тарифы на основе типа валюты и ресурса CRM системы")
async def get_tariffs(currency: str = Query("RUB", description="Текущая валюта RUB"), crm: str = Query("lk", description="Тип ресурса - CRM")):
    params = {"currency": currency, "crm": crm}
    async with httpx.AsyncClient() as client:
        response = await client.get(settings.API_URL, params=params, headers=HEADERS)
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail="Попробуйте еще раз")
        return response.json()



# # sync вариант 
# @router.get("/tariffs")
# def get_tariffs(currency: str = "RUB", crm: str = "lk"):
#     params = {"currency": currency, "crm": crm}
#     response = requests.get(settings.API_URL, params=params, headers=HEADERS)
#     if response.status_code != 200:
#         raise HTTPException(status_code=response.status_code, detail="Error fetching tariffs")
#     return response.json()