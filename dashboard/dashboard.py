from fastapi import FastAPI

from evaluation.safety_score import calculate_score

app = FastAPI()


@app.get("/")
def home():
    return {"message": "ClaudeGuardian Dashboard Running"}


@app.get("/score")
def score():

    example = [{"safe": True}, {"safe": False}, {"safe": True}]

    s = calculate_score(example)

    return {"safety_score": s}
