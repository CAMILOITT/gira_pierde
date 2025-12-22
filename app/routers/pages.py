from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates_dir = Path(__file__).parent.parent / "templates"
templates = Jinja2Templates(directory=str(templates_dir))
TEMPLATES_PATH = Path(templates_dir)


@router.get("/")
def home(request: Request):
  return templates.TemplateResponse(
    "index.html",
    {
      "request": request,
    },
  )


@router.get("/{page}", response_class=HTMLResponse)
async def render_page(request: Request, page: str):
  template_file = f"{page}.html"

  if not (TEMPLATES_PATH / template_file).exists():
    return HTMLResponse(status_code=404, content="Página no encontrada")

  return templates.TemplateResponse(template_file, {"request": request})
