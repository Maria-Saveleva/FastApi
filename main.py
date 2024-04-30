from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_item(request: Request, side_1: str = '', side_2: str = ''):
    answer = 0
    try:
        side_1 = float(side_1)
        side_2 = float(side_2)
        answer = (side_1 + side_2) / 2
    except ValueError:
        pass

    return templates.TemplateResponse(
        request=request, name="index.html", context={"side_1": side_1, "side_2": side_2, "answer": answer}
    )