import re

from fastapi import FastAPI

from schemas import MCPRequest, MCPResponse, Segment

app = FastAPI()


@app.post("/mcp", response_model=MCPResponse)
async def handle_mcp(request: MCPRequest):
    # Получаем последнее сообщение пользователя
    last_user_message = next(
        (
            seg.content
            for seg in reversed(request.context.segments)
            if seg.role == "user"
        ),
        "",
    )

    # Парсим два числа из текста (очень просто)
    numbers = list(map(int, re.findall(r"\d+", last_user_message)))
    if len(numbers) >= 2:
        result = numbers[0] + numbers[1]
        answer = f"Результат: {result}"
    else:
        answer = "Я не смог найти два числа для сложения."

    return MCPResponse(segment=Segment(role="assistant", content=answer))
