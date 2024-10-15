from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import pdfs

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


ORIGINS = ["http://localhost:3000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(pdfs.router, prefix="/pdfs", tags=["pdfs"])
