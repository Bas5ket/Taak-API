from pydantic import BaseModel

class UserCreate(BaseModel):
    user_name: str
    email: str
    password: str

class CharacterCreate(BaseModel):
    character_name: str
    gender: str
    race: str
    klas: str
    level: int
    owner_id: int

class CharacterStatsCreate(BaseModel):
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int
    proficiency_bonus: int
    walking_speed: int
    initiative: int
    armor_class: int
    character_id: int

class UserResponse(BaseModel):
    id: int
    user_name: str
    email: str

class CharacterResponse(BaseModel):
    id: int
    character_name: str
    gender: str
    race: str
    klas: str
    level: int
    owner_id: int

class CharacterStatsResponse(BaseModel):
    id: int
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int
    proficiency_bonus: int
    walking_speed: int
    initiative: int
    armor_class: int
    character_id: int

class UserDelete(BaseModel):
    id: int
    user_name: str
    email: str
    password: str


class CharacterDelete(BaseModel):
    id: int
    character_name: str
    gender: str
    race: str
    klas: str
    level: int
    owner_id: int

class CharacterStatsDelete(BaseModel):
    id: int
    strength: int
    dexterity: int
    constitution: int
    intelligence: int
    wisdom: int
    charisma: int
    proficiency_bonus: int
    walking_speed: int
    initiative: int
    armor_class: int
    character_id: int
