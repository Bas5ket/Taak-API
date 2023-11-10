from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud
import database
import models
import schemas

app = FastAPI()

models.Base.metadata.create_all(bind=database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/users/", response_model=schemas.UserResponse)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.post("/characters/", response_model=schemas.CharacterResponse)
def create_character(character: schemas.CharacterCreate, db: Session = Depends(get_db)):
    return crud.create_character(db=db, character=character)

@app.post("/characters_stats/", response_model=schemas.CharacterStatsResponse)
def create_character(character: schemas.CharacterStatsCreate, db: Session = Depends(get_db)):
    return crud.create_character_stats(db=db, character=character)

@app.get("/users/{user_id}", response_model=schemas.UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/by_name/{user_name}", response_model=schemas.UserResponse)
def read_user_by_name(user_name: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_name(db=db, user_name=user_name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/users/by_email/{email}", response_model=schemas.UserResponse)
def read_user_by_email(email: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db=db, email=email)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.get("/characters/{character_id}", response_model=schemas.CharacterResponse)
def read_character(character_id: int, db: Session = Depends(get_db)):
    db_character = crud.get_character(db=db, character_id=character_id)
    if db_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_character

@app.get("/characters/by_name/{character_name}", response_model=schemas.CharacterResponse)
def read_character_by_name(character_name: str, db: Session = Depends(get_db)):
    db_character = crud.get_character_by_name(db=db, character_name=character_name)
    if db_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_character

@app.get("/characters_stats/{character_stats_id}", response_model=schemas.CharacterStatsResponse)
def read_character(character_stats_id: int, db: Session = Depends(get_db)):
    db_character_stats = crud.get_character_stats(db=db, character_stats_id=character_stats_id)
    if db_character_stats is None:
        raise HTTPException(status_code=404, detail="stats not found")
    return db_character_stats

@app.delete("/users/{user_id}", response_model=schemas.UserDelete)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.delete_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.delete("/characters/{character_id}", response_model=schemas.CharacterDelete)
def delete_character(character_id: int, db: Session = Depends(get_db)):
    db_character = crud.delete_character(db=db, character_id=character_id)
    if db_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return db_character

@app.delete("/characters_stats/{character_stats_id}", response_model=schemas.CharacterStatsDelete)
def delete_character_stats(character_stats_id: int, db: Session = Depends(get_db)):
    db_character_stats = crud.delete_character_stats(db=db, character_stats_id=character_stats_id)
    if db_character_stats is None:
        raise HTTPException(status_code=404, detail="stats not found")
    return db_character_stats