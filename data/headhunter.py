from email.policy import default
import sqlalchemy
from sqlalchemy.orm import relationship
from data.db_session import SqlAlchemyBase, create_session
from sqlalchemy_serializer import SerializerMixin
from typing import List


class HeadHunter(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'headhunters'

    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, primary_key=True, autoincrement=True)
    tg_user_id = sqlalchemy.Column(sqlalchemy.Integer, unique=False)
    name = sqlalchemy.Column(sqlalchemy.String)
    field = sqlalchemy.Column(sqlalchemy.String)

    tasks = relationship("Task")

    def __repr__(self) -> str:
        return f'HeadHunter {self.name}'


def add_headhunter(sess, name:str, field:str) -> HeadHunter:
    session = create_session()
    session.expire_on_commit = True

    new_headhunter = HeadHunter()
    new_headhunter.field = field
    new_headhunter.name = name

    sess.add(new_headhunter)
    sess.commit()
    
    
    return new_headhunter