from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from db import get_db
import models
import schema

app = FastAPI()

origins = ["http://localhost:3000/", "https://localhost:3000/"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependencies
@app.get("/players", response_model=list[schema.Player])
def get_all_players(db: Session = Depends(get_db)):
    results: list[tuple[models.Element, models.Team, models.ElementType]] = (
        db.query(models.Element, models.Team, models.ElementType)
        .join(models.Team)
        .join(models.ElementType)
        .all()
    )
    return results
