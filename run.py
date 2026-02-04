from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.routes import router

app = FastAPI(title="AcademicTask Manager")

# Archivos estáticos (CSS, JS)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Rutas
app.include_router(router)
