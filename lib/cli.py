#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Students
from helpers import (create_student_table) 

engine = create_engine('sqlite:///db/phase3_project.db')
session = sessionmaker(bind=engine)()


if __name__ == '__main__':
    #Intro: welcome to the CLI
    print('''
    
    Hi, Welcome to the tutoring scheduler. We're here to help! Please select your student ID.
    ''')
    print('''
    IDs and Names Listed Below:
    
    ''')
    student = session.query(Students)
    
    create_student_table(student)