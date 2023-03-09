#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Students, Tutors
from helpers import (create_student_table, create_tutors_table) 

engine = create_engine('sqlite:///phase3_project.db')
session = sessionmaker(bind=engine)()


if __name__ == '__main__':
    #Intro: welcome to the CLI
    print('''
    
    Hi, Welcome to the tutoring scheduler. We're here to help! Please select your student ID.
    ''')
    print('''
    IDs and Names Listed Below:
    
    ''')
    students = session.query(Students)
    create_student_table(students)

    # Student picks the ID from the list
    selected_student = None
    while not selected_student:
        selected_student_id = input('Please enter your student ID: ')
        selected_student = session.query(Students).filter(Students.id == selected_student_id).one_or_none()
    
    # Display a list of subjects to be tutored in
    print(f'''
    
    Hi {selected_student.name}, please select the tutor that you would like to meet with

    Tutors, Specialties and Rates are Listed Below:
    
    ''')

    tutors = session.query(Tutors)
    create_tutors_table(tutors)

    # Student picks a tutor
    selected_tutor = None
    while not selected_tutor:
        selected_tutor_id = input('Please enter the ID of the tutor you would like to work with: ')
        selected_tutor = session.query(Tutors).filter(Tutors.id == selected_tutor_id).one_or_none()

    # Display the selected Tutors - Choice
    print(f'''
    
    Hi {selected_student.name}, you have selected {selected_tutor.name} who specializes in {selected_tutor.specialty}.

    Your tutor's hourly rate is: ${selected_tutor.rate:.2f}
    
    How many hours would you like to work on {selected_tutor.specialty} with {selected_tutor.name}?
    
    ''')

    # Student picks the numberof hours
    
    selected_hours = None
    while not selected_hours:
        selected_hours = input(f'Please enter the amount of hours you would like to work with {selected_tutor.name}: ')
    
    total_cost = selected_hours * selected_tutor.rate

    print(f'''
    
    Hi {selected_student.name},
    
    You have selected to work {selected_tutor.name} who specializes in {selected_tutor.specialty} for {selected_hours} hours.
    
    Total Cost: ${total_cost}
    
    ''')