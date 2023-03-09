from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Students, Tutors, Subjects, TutorSessions
from faker import Faker
from random import random, randint, choice as rc


engine = create_engine('sqlite:///phase3_project.db')
Session = sessionmaker(bind=engine)
session = Session()

# fake = Faker()
# subject_list = ["Math", "Science", "Literature", "History"]

# def student_name():
#     session.query(Students).delete()
#     session.commit()

#     print("Fetching our scholars...")
#     students = [Students(
#         name = fake.name(),
#         grade = randint(9, 12),
#         subject = random.choice(subject_list)
#     ) for i in range(20)]

#     session.add_all(students)
#     session.commit()

#     return students

# def tutor_name():
#     session.query(Tutors).delete()
#     session.commit()

#     print("Let's find you a tutor...")
#     tutors = [Tutors(
#         name = fake.name(),
#         specialty = random.choice(subject_list),
#         rate = randint(100, 300), 
#     ) for i in range(15)]

#     session.add_all(tutors)
#     session.commit()

#     return tutors

# def make_schedule(student_name, tutor_name):
#     session.query(TutorSessions).delete()
#     session.commit()

#     print("Time to Learn!")
    




#     if __name__ == '__main__':
#         session.query()

session.query(Students).delete()
session.commit()

susan = Students(name="Susan A", grade= 10, subject = "Math")
matt = Students(name= "Matthew W", grade = 11, subject= "Science")
duane = Students(name="Duane G", grade = 12, subject="History")
bob = Students(name = "Bob R", grade = 9, subject = "English")
tom = Students (name = "Tom E", grade = 9, subject = "History")
jessica = Students(name= "Jessica T", grade = 10, subject="Science")
frank = Students(name = "Franklin L", grade = 11, subject = "Math")
troy = Students(name = "Troy B", grade = 12, subject = "History")
carl = Students(name = "Carl R", grade = 9, subject= "English")
anthony = Students(name = "Anthony P", grade = 10, subject = "Math")

session.add_all([susan, matt, duane, bob, tom, jessica, frank, troy, carl, anthony])
session.commit()

session.query(Tutors).delete()
session.commit()

eleanor = Tutors(name = "Eleanor", specialty = "Math", rate = 250)
tyler = Tutors(name = "Tyler", specialty = "Science", rate = 250)
gehrig = Tutors(name = "Gehrig", specialty = "History", rate = 200)
amanda = Tutors(name = "Amanda", specialty = "Math", rate = 175)
mike = Tutors(name = "Michael", specialty = "Science", rate= 150)


session.add_all([eleanor, tyler, gehrig, amanda, mike])
session.commit()

session.query(Subjects).delete()
session.commit()

math = Subjects(subject = "Math")
science = Subjects(subject = "Science")
history = Subjects(subject = "History")
english = Subjects(subject = "English")

session.add_all([math, science, history, english])
session.commit()

