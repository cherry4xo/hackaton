import sqlalchemy
from sqlalchemy.orm import relationship
from data.db_session import SqlAlchemyBase, create_session
from data.headhunter import HeadHunter
from sqlalchemy_serializer import SerializerMixin


class Job(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True,
                           primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=False)

    wage = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    skills = sqlalchemy.Column(sqlalchemy.Text)

    headhunter_id = sqlalchemy.Column(
        sqlalchemy.Integer, sqlalchemy.ForeignKey('headhunters.id'))
    replies = relationship("JobReply")

    def __repr__(self) -> str:
        return f'Job {self.title}'
