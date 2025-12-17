import random
from pathlib import Path
from typing import Dict, List

from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates_dir = Path(__file__).parent.parent / "templates"
templates = Jinja2Templates(directory=str(templates_dir))

# In-memory storage for retos (replace with DB if needed)
_challenges: List[Dict] = [
  {"id": 1, "title": "Primer reto", "description": "Descripción del primer reto."},
  {"id": 2, "title": "Reto de ejemplo", "description": "Otro reto para probar."},
]


@router.get("/")
def home(request: Request):
  random_challenge = random.choice(_challenges) if _challenges else None
  return templates.TemplateResponse(
    "index.html",
    {
      "request": request,
      "challenges": _challenges,
      "random_challenge": random_challenge,
    },
  )
