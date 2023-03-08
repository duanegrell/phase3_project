from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Tutor
from faker import Faker
from random import random, randint


engine = create_engine('sqlite:///phase3_project.db')
Session = sessionmaker(bind=engine)
session = Session()

fake = Faker()
subject_list = ["Math", "Science", "Literature", "History"]

def student_name():
    session.query(Student).delete()
    session.commit()

    print("Fetching our scholars...")
    students = [Student(
        name = fake.name(),
        grade = randint(9, 12),
        subject = random.choice(subject_list)
    ) for i in range(20)]

    session.add_all(student_name)
    session.commit()

    return students

def tutor_name():
    session.query(Tutor).delete()
    session.commit()

    print("Let's find you a tutor...")
    tutors = [Tutor(
        name = fake.name(),
        specialty = random.choice(subject_list),
        rate = randint(100, 300), 
    ) for i in range(15)]

    session.add_all(tutors)
    session.commit()

    return tutors




    if __name__ == '__main__':
        session.query()

# session.query(Student).delete()
# session.commit()

# susan = Student(name="Susan Ahmed", grade= 10, subject = "Math")
# matt = Student(name= "Matthew Williams", grade = 11, subject= "Science")
# duane = Student(name="Duane Grell", grade = 12, subject="History")
# session.add_all([susan, matt, duane])
# session.commit()

# session.query(Tutor).delete()
# session.commit()

# eleanor = Tutor(name = "Eleanor", specialty = "Math", rate = 200)
# tyler = Tutor(name = "Tyler", specialty = "Science", rate = 250)
# gehrig = Tutor(name = "Gehrig", specialty = "History", rate = 150)


# session.add_all([eleanor, tyler, gehrig])
# session.commit()
