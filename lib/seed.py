from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Student

engine = create_engine('sqlite:///phase3_project.db')
Session = sessionmaker(bind=engine)
session = Session()

session.query(Student).delete()
session.commit()

susan = Student(name="Susan Ahmed", grade= 10, subject = "Math")
matt = Student(name= "Matthew Williams", grade = 11, subject= "N/A")
duane = Student(name="Duane Grell", grade = 12, subject="N/A")
session.add_all([susan, matt, duane])
session.commit()
