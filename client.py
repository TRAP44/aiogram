import httpx
from dotenv import load_dotenv
import os

load_dotenv()

API_URL = os.getenv("API_URL")
   
async def get_all_products(order_by = "id", direction = "asc"):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{API_URL}/products", params={"order_by": order_by, "direction": direction})
            if response.status_code == 200:
                return response.json()
            return []
        except Exception as e:
            print("Ошибка при получении пользователей:", e)
            return []


async def get_all_orders():
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{API_URL}/orders")
            if response.status_code == 200:
                return response.json()
            return []
        except Exception as e:
            print("Ошибка при получении пользователей:", e)
            return []

async def get_product_by_title(product_title: str):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{API_URL}/product/search/{product_title}")
            if response.status_code == 200:
                return response.json()
            return []
        except Exception as e:
            print("Ошибка при получении пользователей:", e)
            return []
        

async def get_order_by_id(order_id: int):
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(f"{API_URL}/orders/{order_id}")
            if resp.status_code == 200:
                return resp.json()
        except Exception as e:
            print("Ошибка при получении заказа:", e)
        return None

async def create_order(user_id, items):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(f"{API_URL}/order/add", json={"user_id": user_id, "items": items})
            if response.status_code == 200:
                data = response.json()
                return data.get("id")
            else:
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None
        

async def create_product(data: dict):
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(f"{API_URL}/product/add", json=data)
            return response.status_code == 200
        except Exception as e:
            print(f"Error: {e}")
            return False
        

async def get_product_by_id(product_id: int):
    async with httpx.AsyncClient() as client:
        try:
            resp = await client.get(f"{API_URL}/product/{product_id}")
            if resp.status_code == 200:
                return resp.json()
        except Exception as e:
            print("Ошибка при получении товара:", e)
        return None