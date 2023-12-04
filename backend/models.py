from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
 
class Movier(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    tmdb_id= Column(String)
    title=Column(String)
    #user_id
    is_active = Column(Boolean, default=True)
    

class Favorito_movie(Base):
    __tablename__ = "favoritos_movies"
    tmdb_id = Column(String, primary_key=True, index=True)
    user_id = Column(String)
    title=Column(String)
    # is_active = Column(Boolean, default=True)
    # user = relationship(User="user", back_populates="favorite_movies")r

class Artistas(Base):
    __tablename__= "artistas"
    tmdb_id = Column (String, primary_key = True, index = True)
    name = Column(String)
    rank = Column(String)
    user_id = Column(String)
