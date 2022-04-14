
from hashlib import new
import sqlalchemy
from sqlalchemy.orm import relationship
from data.db_session import SqlAlchemyBase, create_session
from sqlalchemy_serializer import SerializerMixin
from typing import List
from random import randint

class TestTable(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'testtableobjects'

    id = sqlalchemy.Column(sqlalchemy.Integer, unique=True, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)

    def __repr__(self):
        return f'Test Object {self.title}'

def get_all_objects() -> List[TestTable]:
    session = create_session()
    query = session.query(TestTable).filter().all()

    return query

def add_new_test_object() -> TestTable:
    session = create_session()
    new_test_object = TestTable()
    new_test_object.title = "aboba" + str(randint(1, 10))

    session.add(new_test_object)
    session.commit()

    return  new_test_object
