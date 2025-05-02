from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

# Модель для валидации входных параметров
class GreetingRequest(BaseModel):
    name: Optional[str] = "Recruto"
    message: Optional[str] = "Давай дружить"

# GET-эндпоинт для обработки запроса
@app.get("/")
async def greet(req: GreetingRequest = Depends()): 
    # Формируем ответ
    response = f"Hello {req.name}! {req.message}!"
    return {"message": response}