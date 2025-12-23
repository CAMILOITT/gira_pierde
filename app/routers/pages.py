from pathlib import Path

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

# Inicializamos el router de FastAPI para las páginas
router = APIRouter()
# Configuramos la ruta de las plantillas Jinja2
templates_dir = Path(__file__).parent.parent / "templates"
# Inicializamos el motor de plantillas Jinja2
templates = Jinja2Templates(directory=str(templates_dir))


@router.get("/")
def home(request: Request):
  # Renderizamos la plantilla index.jinja
  return templates.TemplateResponse(
    "index.jinja",
    {
      "request": request,
    },
  )
