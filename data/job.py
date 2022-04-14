import sqlalchemy
from sqlalchemy.orm import relationship
from data.db_session import SqlAlchemyBase, create_session
from data.headhunter import HeadHunter
from sqlalchemy_serializer import SerializerMixin


class Job(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'jobs'

    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    requirements = sqlalchemy.Column(sqlalchemy.Text)

    wage = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    is_alltime = sqlalchemy.Column(sqlalchemy.Boolean, default=True) # постоянная занятость / подработка и т д  
    skills = sqlalchemy.Column(sqlalchemy.JSON)

    headhunter_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey('headhunters.id'))
    replies = relationship("JobReply")

    def __repr__(self) -> str:
        return f'Job {self.title}'


def add_job(title:str, description:str, requirements:str, skills:list, wage:int, is_alltime:bool, headhunter:HeadHunter) -> Job:
    session = create_session()
    session.expire_on_commit = True

    new_job = Job()
    new_job.title = title
    new_job.description = description
    new_job.requirements = requirements
    new_job.skills = skills
    new_job.wage = wage
    new_job.is_alltime = is_alltime
    new_job.headhunter_id = headhunter.id

    session.add(new_job)
    session.commit()
    

    return new_job