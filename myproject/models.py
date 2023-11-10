from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String, index=True)
    email = Column(String, index=True)
    password = Column(String)

    characters = relationship("Character", back_populates="owner")

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True, index=True)
    character_name = Column(String, index=True)
    gender = Column(String)
    race = Column(String)
    klas = Column(String)
    level = Column(Integer)
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User", back_populates="characters")
    stats = relationship("Character_stats", back_populates="characters")

class Character_stats(Base):
    __tablename__ = "characters_stats"

    id = Column(Integer, primary_key=True, index=True)
    strength = Column(Integer)
    dexterity = Column(Integer)
    constitution = Column(Integer)
    intelligence = Column(Integer)
    wisdom = Column(Integer)
    charisma = Column(Integer)
    proficiency_bonus = Column(Integer)
    walking_speed = Column(Integer)
    initiative = Column(Integer)
    armor_class = Column(Integer)
    character_id = Column(Integer, ForeignKey("characters.id"))

    characters = relationship("Character", back_populates="stats")