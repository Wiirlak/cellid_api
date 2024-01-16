from fastapi import FastAPI
from starlette.responses import RedirectResponse

from src.router import router

app = FastAPI()

app.include_router(router, prefix="/api/v1")


@app.get("/", include_in_schema=False)
async def redirect_doc():
    return RedirectResponse(url="/docs")
