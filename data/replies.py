import sqlalchemy
from sqlalchemy.orm import relationship
from data.db_session import SqlAlchemyBase, create_session
from data.job import Job
from data.seeker import Seeker
from data.task import Task
from sqlalchemy_serializer import SerializerMixin
from typing import List


class TaskReply(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'reply_tasks'

    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True,
                           primary_key=True, autoincrement=True)
    content = sqlalchemy.Column(sqlalchemy.Text, nullable=False)

    seeker_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('seekers.id'))
    task_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('tasks.id'))

    def __repr__(self) -> str:
        return f'TaskReply {self.content}'


class JobReply(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'reply_jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True,
                           primary_key=True, autoincrement=True)
    content = sqlalchemy.Column(sqlalchemy.Text, nullable=False)

    seeker_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('seekers.id'))
    job_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('jobs.id'))

    def __repr__(self) -> str:
        return f'JobReply {self.content}'


def add_job_reply(session, job: Job, sender: Seeker) -> JobReply:
    new_job_reply = JobReply()
    new_job_reply.job_id = job.id
    new_job_reply.seeker_id = sender.id

    session.add(new_job_reply)
    session.commit()

    return new_job_reply


def add_task_reply(sess, task: Task, content: str, sender: Seeker) -> TaskReply:
    session = create_session()
    new_task_reply = TaskReply()
    new_task_reply.task = task
    new_task_reply.content = content
    new_task_reply.seeker = sender

    sess.add(new_task_reply)
    sess.commit()

    return new_task_reply
