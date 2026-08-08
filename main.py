from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# Configuración de plantillas Jinja2
templates = Jinja2Templates(directory="templates")

# Lista de tareas temporal
tareas = []

@app.get("/", response_class=HTMLResponse)
def inicio(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"tareas": tareas}
    )

@app.post("/agregar", response_class=HTMLResponse)
def agregar_tarea(request: Request, titulo: str = Form(...)):
    nueva_tarea = {
        "id": len(tareas) + 1,
        "titulo": titulo
    }
    tareas.append(nueva_tarea)
    
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"tareas": tareas}
    )