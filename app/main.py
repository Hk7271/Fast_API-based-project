from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from app.db.session import engine, Base
from app.api.predictions import router as predictions_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Iris Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(predictions_router)