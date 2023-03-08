# from models import Students, Tutor

YES = ['y', 'ye', 'yes']
NO = ['n', 'no']

def create_student_table(students):
    print('-' * 50)
    print(f'|ID  |NAME{" " * 39}|')
    print('-' * 50)
    for student in students:
        id_spaces = 4 - len(str(student.id))
        name_spaces = 43 - len(student.name)
        print(f'|{student.id}{" " * id_spaces}|{student.name}{" " * name_spaces}|')
    print('-' * 50)