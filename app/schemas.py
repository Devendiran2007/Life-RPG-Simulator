from pydantic import BaseModel

class UserCreate(BaseModel):
    username : str
    email : str
    password : str

class UserResponse(BaseModel):
    id : int
    username : str
    email : str


class UserLogin(BaseModel):
    username : str
    password : str
 
class QuestCreate(BaseModel):
    title : str
    description : str
    difficulty : int
    xp_reward : int
    coin_reward : int   

class QuestResponse(BaseModel):
    id : int
    title : str
    description : str
    difficulty : int
    xp_reward : int
    coin_reward : int   

class QuestUpdate(BaseModel):
    title : str
    description : str
    difficulty : int
    xp_reward : int
    coin_reward : int      

class QuestDelete(BaseModel):
    id : int