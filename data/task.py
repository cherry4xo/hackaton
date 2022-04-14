from datetime import date
from distutils.dep_util import newer_pairwise
import sqlalchemy
from sqlalchemy.orm import relationship
from data.db_session import SqlAlchemyBase, create_session
from data.headhunter import HeadHunter
from sqlalchemy_serializer import SerializerMixin


class Task(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'tasks'

    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    payment = sqlalchemy.Column(sqlalchemy.Integer, nullable=False)
    overdue_date = sqlalchemy.Column(sqlalchemy.Date, nullable=False) 
    tags = sqlalchemy.Column(sqlalchemy.JSON)

    headhunter_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('headhunters.id'))
    replies = relationship("TaskReply")


    def __repr__(self) -> str:
        return f'Task {self.title}'


def add_task(sess, title:str, description:str, payment:int, overdue_date:date, tags:list, headhunter:HeadHunter) -> Task:
    session = create_session()
    session.expire_on_commit = True

    new_task = Task()
    new_task.title = title
    new_task.description = description
    new_task.payment = payment
    new_task.overdue_date = overdue_date
    new_task.tags = tags
    new_task.headhunter_id = headhunter.id

    sess.add(new_task)
    sess.commit()
    

    return new_task