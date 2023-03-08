from sqlalchemy import create_engine, func
from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///phase3_project.db')

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    grade = Column(Integer())
    subject = Column(String())

    def __repr__(self):
        return f'Student(id={self.id} ' + \
            f'name = {self.name}, ' + \
            f'grade = {self.grade}' + \
            f'subject = {self.subject})'

class Tutor(Base):
    __tablename__ = 'tutors'

    id = Column(Integer(), primary_key= True)
    name = Column(String())
    specialty = Column(String())
    rate = Column(Integer())

    def __repr__(self):
        return f'Tutor(id={self.id}), ' + \
            f'name = {self.name}, ' + \
            f'specialty = {self.specialty} ' + \
            f'rate = {self.rate} '