from fastapi import FastAPI, Request, Security, APIRouter, HTTPException
from pydantic import BaseModel
from datetime import datetime as dt
from datetime import timedelta

app = FastAPI()

async def auth_header(request: Request, call_next):
    header = request.headers.get('Authorization')
    if not header.startswith("Bearer "):
        return HTTPException(401)
    print(header)

router = APIRouter(dependencies=[Security(auth_header)])

class Question(BaseModel):
    q_id: str
    question: str
    valid_until: dt
    answers: list[str]
    solved: bool


def get_user_id(request: Request) -> int:
    header = request.headers.get('Authorization')
    print(header)
    return 0

@app.get("/question")
async def get_question() -> Question:
    return Question(
        q_id="que1",
        question="asd",
        answers=["Da", "Net"],
        valid_until=dt.now() + timedelta(hours=3),
        solved=False
    )


class AnswerRequest(BaseModel):
    q_id: str
    answer: str


def validate_answer(q_id: str, answer: str) -> bool:
    return False


def register_winner(q_id: str, user_id: str) -> int:
    return 200


@app.post("/answer")
async def answer(req: AnswerRequest, request: Request):
    print(request.headers.get("Authorization"))
    if not validate_answer(req.q_id, req.answer):
        return {"correct": False, "balance": 1000, "win": 0}
    # increase balance

    win = register_winner(req.q_id, "userId")
    return {"correct": True, "balance": 1000, "win": win}
