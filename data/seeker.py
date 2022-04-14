from requests import session
import sqlalchemy
from sqlalchemy.orm import relationship
from .db_session import SqlAlchemyBase, create_session
from sqlalchemy_serializer import SerializerMixin
from typing import List
import json


class Seeker(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'seekers'

    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True,
                           primary_key=True, autoincrement=True)
    tg_user_id = sqlalchemy.Column(sqlalchemy.Integer, unique=False)
    full_name = sqlalchemy.Column(sqlalchemy.String)
    skills = sqlalchemy.Column(sqlalchemy.JSON)
    role = sqlalchemy.Column(sqlalchemy.Boolean) # headhanter - False or seeker - True

    def repr(self):
        return f'Seeker {self.full_name}'


def get_all_seekers() -> list:
    session = create_session()
    seekers = session.query(Seeker).all()

    return seekers


def add_seeker(sess, tg_id, seekername=None, full_name=None, skills=None) -> Seeker:
    seeker = Seeker()
    seeker.tg_user_id = tg_id
    seeker.seekername = seekername
    seeker.skills = json.loads(skills)

    sess.add(seeker)
    sess.commit()

    return seeker