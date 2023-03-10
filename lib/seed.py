from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Students, Tutors, Subjects, TutorSessions
from faker import Faker
from random import randint
import random

if __name__ == '__main__':
    engine = create_engine('sqlite:///phase3_project.db')
    Session = sessionmaker(bind=engine)
    session = Session()

fake = Faker()
subject_list = ["Python", "HTML", "CSS", "SQL", "JavaScript", "Flask"]
rand_subject = random.choice(subject_list)
students = []

session.query(Students).delete()
session.commit()

for i in range(35):
    student = Students(
        name = f"{fake.first_name()} {fake.last_name()}",
        email = fake.email(),
        phone = random.randint(1000000000, 9999999999)
    )

    session.add(student)
    session.commit()

    students.append(student)

session.query(Subjects).delete()
session.commit()

py = Subjects(subject = "Python")
html = Subjects (subject = "HTML")
css= Subjects (subject = "CSS")
sql= Subjects(subject = "SQL")
js = Subjects(subject = "JavaScript")
fl= Subjects(subject = "Flask")

session.add_all([py, html, css, sql, js, fl])
session.commit()


tutors = []

session.query(Tutors).delete()
session.commit()

for i in range(20):
    tutor = Tutors(
        name = f"{fake.first_name()}",
        specialty = random.choice(subject_list),
        rate = randint(100, 300)
    )
    session.add(tutor)
    session.commit()

    tutors.append(Tutors)




# *****MANUAL DATA*****

# session.query(Students).delete()
# session.commit()

# susan = Students(name="Susan A", grade= 10, subject = "Math")
# matt = Students(name= "Matthew W", grade = 11, subject= "Science")
# duane = Students(name="Duane G", grade = 12, subject="History")
# bob = Students(name = "Bob R", grade = 9, subject = "English")
# tom = Students (name = "Tom E", grade = 9, subject = "History")
# jessica = Students(name= "Jessica T", grade = 10, subject="Science")
# frank = Students(name = "Franklin L", grade = 11, subject = "Math")
# troy = Students(name = "Troy B", grade = 12, subject = "History")
# carl = Students(name = "Carl R", grade = 9, subject= "English")
# anthony = Students(name = "Anthony P", grade = 10, subject = "Math")

# session.add_all([susan, matt, duane, bob, tom, jessica, frank, troy, carl, anthony])
# session.commit()

# session.query(Tutors).delete()
# session.commit()

# eleanor = Tutors(name = "Eleanor", specialty = "Math", rate = 250)
# tyler = Tutors(name = "Tyler", specialty = "Science", rate = 250)
# gehrig = Tutors(name = "Gehrig", specialty = "History", rate = 200)
# amanda = Tutors(name = "Amanda", specialty = "Math", rate = 175)
# mike = Tutors(name = "Michael", specialty = "Science", rate= 150)


# session.add_all([eleanor, tyler, gehrig, amanda, mike])
# session.commit()

# session.query(Subjects).delete()
# session.commit()

# math = Subjects(subject = "Math")
# science = Subjects(subject = "Science")
# history = Subjects(subject = "History")
# english = Subjects(subject = "English")

# session.add_all([math, science, history, english])
# session.commit()

