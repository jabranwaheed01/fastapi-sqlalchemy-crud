
from app.database.db import engine
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)

    name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    email: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True
    )


    def __repr__(self):
        return f"-------------  \nUser_id= {self.id}\nName= {self.name} \nEmail= {self.email}\n -------------"


def create_table():
    Base.metadata.create_all(engine)