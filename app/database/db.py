from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URl = "sqlite:///sqlite.db"

engine = create_engine (DATABASE_URl , echo= True)

SessionLocal = sessionmaker(bind= engine , expire_on_commit=False)