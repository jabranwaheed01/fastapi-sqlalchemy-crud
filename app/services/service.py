from app.models.models import User
from app.database.db import SessionLocal
from sqlalchemy import select

def create_user (name:str,email:str):
    with SessionLocal() as session:
        user = User(name= name , email= email )
        session.add(user)
        session.commit()

  #---- Sindle USER Data --------
  

def get_single_user(user_id:int):
    with SessionLocal() as session:
        user  = session.get(User, user_id)
        return user

#------- GET ALL USERS------

def get_all_user():
    with SessionLocal() as session:
        stmt = select(User)
        users = session.scalars(stmt).all()
        return users

#-------- UPDATE USER EMAIL

def update_user_email(user_id: int , new_email:str):
    with SessionLocal () as session:
        user= session.get(User , user_id)
        if user:
            user.email = new_email
            session.commit()
        return user


# -------- DELETE USER ID -------


def delete_user_id(user_id: int):
    with SessionLocal () as session :
        user = session.get(User , user_id)
        if user:
            session.delete(user)
            session.commit()