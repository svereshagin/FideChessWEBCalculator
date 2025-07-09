import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routes.chess import router as chess_router
from routes.standart import router as root_router

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chess_router)
app.include_router(root_router)

if __name__ == "__main__":

    uvicorn.run('main:app', port=8000, reload=True)