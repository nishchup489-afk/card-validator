from fastapi import FastAPI, Form, Request, Response
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

templates = Jinja2Templates(directory=str(BASE_DIR/"templates"))

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    # Use keyword arguments to avoid signature confusion
    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

def validator_compressed(n: str) -> bool:
    n = n.replace(" ", "").replace("-", "")

    if not n.isdigit():
        return False
    
    n = [int(d) for d in str(n)[::-1]]
    total = 0

    for i, d in enumerate(n):
        total += d if i % 2 == 0 else (d * 2 - 9 if d * 2 > 9 else d * 2)
    return total % 10 == 0


@app.post("/calc", response_class=HTMLResponse)
def calc(request: Request, number: int = Form(...)):
    n = str(number)
    result = validator_compressed(n)

    # Added the missing 'name' argument here as well
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"result": result}
    )