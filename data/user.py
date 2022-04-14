
from hashlib import new
from venv import create
import sqlalchemy
from sqlalchemy.orm import relationship
from data.db_session import SqlAlchemyBase, create_session
from sqlalchemy_serializer import SerializerMixin
from typing import List
import db_session
import json

class User(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, primary_key=True, autoincrement=True)
    tg_user_id = sqlalchemy.Column(sqlalchemy.Integer, unique=True)
    username = sqlalchemy.Column(sqlalchemy.String)
    first_name = sqlalchemy.Column(sqlalchemy.String)
    second_name = sqlalchemy.Column(sqlalchemy.String)
    full_name = sqlalchemy.Column(sqlalchemy.String)
    skills =  sqlalchemy.Column(sqlalchemy.JSON)
    role = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        return f'New user {self.title}'

def get_user_by_tg_id(tg_id: str) -> User:
    tg_id = int(tg_id)
    session = db_session.create_session()
    user = session.query(User).filter(User.tg_id == tg_id).first()
    return user if user else False

def get_all_users() -> list:
    session = db_session.create_session()
    users = session.query(User).all()

    return users

def create_user(tg_id, username=None, first_name=None, second_name=None, full_name=None, skills=None) -> User:
    user = User()
    user.tg_user_id = tg_id
    user.username = username
    user.first_name = first_name
    user.second_name = second_name
    user.full_name = full_name
    user.skills = json.loads(skills)
    
    session = db_session.create_session()
    session.add(user)
    session.commit()

    return get_user_by_tg_id(tg_id)