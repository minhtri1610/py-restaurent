import uvicorn
from fastapi import FastAPI, Query
from pydantic import Required
from api import api_router
# from .api import config

app = FastAPI()

app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
