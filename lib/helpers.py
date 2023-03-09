# from models import Students, Tutor

# YES = ['y', 'ye', 'yes']
# NO = ['n', 'no']

def create_student_table(students):
    print('-' * 50)
    print(f'|ID  |NAME{" " * 39}|')
    print('-' * 50)
    for student in students:
        id_spaces = 4 - len(str(student.id))
        name_spaces = 43 - len(student.name)
        print(f'|{student.id}{" " * id_spaces}|{student.name}{" " * name_spaces}|')
    print('-' * 50)

def create_tutors_table(tutors):
    print('-' * 75)
    print(f'|ID  |TUTOR NAME{" " * 24}|SPECIALTY{" " * 12}|PRICE{" " * 6}|')
    print('-' * 75)
    for tutor in tutors:
        id_spaces = 4 - len(str(tutor.id))
        name_spaces = 34 - len(tutor.name)
        specialty_spaces = 21 - len(tutor.specialty)
        rate_spaces = 10 - len(f'{tutor.rate:.2f}')
        output_string = f'|{tutor.id}{" " * id_spaces}|' + \
            f'{tutor.name}{" " * name_spaces}|' + \
            f'{tutor.specialty}{" " * specialty_spaces}|' + \
            f'${tutor.rate:.2f}{" " * rate_spaces}|'
        print(output_string)
    print('-' * 75)