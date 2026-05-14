student_grade={ }

#adding new student
def add_student(name,grade):
    student_grade[name] = grade
    #[priti]=100
    print(f'Added {name} with a {grade}')
    #Added priti with 100

# upadating student data
def update_student(name,grade):
    if name in student_grade:
        student_grade[name]=grade
        #priti=200 get updated
        print(f'{name} with marks are updated')
    else:
        print(f'{name} is not found')


#deletind a student
def delete_student(name):
    if name in student_grade:
        del student_grade[name]
        print(f'{name} has been successfully deleted')
    else:
        print(f'{name} is not found')

#veiw all student
def display_all_student():
    if student_grade:
        for name , grade in student_grade.items():
            print(f'{name}:{grade}')
    else:
        print(f'no student found/added')

def main():
    while True:
        print("\n Student Grade Management System:")
        print("1.Add student")
        print("2.Update a student")
        print("3.Delete student")
        print("4.View student")
        print("5.exit")
         
        choice=int(input("enter your choice:"))
        if choice==1:
            name=input("enter the name of the student:")
            grade=int(input("enter the grade of the student:"))
            add_student(name,grade)
        elif choice==2:
            name=input("enter the name of the student:")
            grade=int(input("enter the grade of the student:"))
            update_student(name,grade)
        elif choice==3: 
            name=input("enter the name of the student:")
            delete_student(name)
        elif choice==4: 
            display_all_student()
        elif choice==5:   
            print("closing the program")
            break
        else:
            print('invalid input')
main()
    
