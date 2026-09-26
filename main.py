from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from automation import automate_orangehrm

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": None
        }
    )


@app.post("/", response_class=HTMLResponse)
async def run_automation(
    request: Request,
    username: str = Form(...),
    password: str = Form(...),
    first_name: str = Form(...),
    last_name: str = Form(...),
    employee_id: str = Form(...)
):

    result = automate_orangehrm(
        username,
        password,
        first_name,
        last_name,
        employee_id
    )

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": result
        }
    )