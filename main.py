from fastapi import FastAPI

app = FastAPI()


# GET-эндпоинт для обработки запроса
@app.get("/greet")
async def greet(name: str = None, message: str = None):
    # Устанавливаем значения по умолчанию, если параметры не переданы
    name = name if name else "Recruto"
    message = message if message else "Давай дружить"
    
    # Формируем ответ
    response = f"Hello {name}! {message}!"
    return {"message": response}