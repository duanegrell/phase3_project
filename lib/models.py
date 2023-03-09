from sqlalchemy import create_engine, func, ForeignKey
from sqlalchemy import Table, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///phase3_project.db')

Base = declarative_base()

class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    email = Column(String())
    phone = Column(Integer())

    def __repr__(self):
        return f'Student(id={self.id} ' + \
            f'name = {self.name}, ' + \
            f'email = {self.email}, ' + \
            f'phone = {self.phone} ' 

class Tutors(Base):
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

class Subjects(Base):
    __tablename__ = 'subjects'

    id = Column(Integer(), primary_key = True)
    subject = Column(String())

    def __repr__(self):
        return f'Subject(id = {self.id}) ' + \
            f'subject = {self.subject} '

class TutorSessions(Base):
    __tablename__ = 'tutoring'

    id = Column(Integer(), primary_key=True)
    student_name = Column(String(), ForeignKey('students.id'))
    tutor_name = Column(String(), ForeignKey('tutors.id'))
    date = Column(DateTime())
    time = Column(DateTime())
    cost = Column(Integer())

    def __repr__(self):
        return f'TutorSessions(id={self.id}),' + \
            f'students = {self.student_name}, ' + \
            f'tutor = {self.tutor_name}, ' + \
            f'date = {self.date}, ' + \
            f'time = {self.time}, ' + \
            f'cost = {self.cost}, '

Base.metadata.create_all(engine)


