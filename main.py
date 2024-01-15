from fastapi import FastAPI
from starlette.responses import RedirectResponse

from src.route import router

app = FastAPI()

app.include_router(router, prefix="/api/v1")


@app.get("/")
async def redirect_doc():
    return RedirectResponse(url="/docs")
