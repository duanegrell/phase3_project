from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student, Tutor


engine = create_engine('sqlite:///phase3_project.db')
Session = sessionmaker(bind=engine)
session = Session()

session.query(Student).delete()
session.commit()

susan = Student(name="Susan Ahmed", grade= 10, subject = "Math")
matt = Student(name= "Matthew Williams", grade = 11, subject= "Science")
duane = Student(name="Duane Grell", grade = 12, subject="History")
session.add_all([susan, matt, duane])
session.commit()

session.query(Tutor).delete()
session.commit()

eleanor = Tutor(name = "Eleanor", specialty = "Math", rate = 200)
tyler = Tutor(name = "Tyler", specialty = "Science", rate = 250)
gehrig = Tutor(name = "Gehrig", specialty = "History", rate = 150)


session.add_all([eleanor, tyler, gehrig])
session.commit()
