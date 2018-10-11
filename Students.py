from statistics import mean
from sys import exit


def delete_student(dic):
    names = list(dic.keys())
    if len(names):
        print(names)
        student = input("Which student would you like to delete?\n")
        if student in names:
            del dic[student]
        else:
            print("Error #404: Student not found")
    else:
        print("No students in database")


def input_grades(dic):
    names = list(dic.keys())
    if len(names):
        print(names)
        student = input("Whose grades would you like to enter?\n")
        if student not in names:
            print("Error #404: Student not found")
            return
        else:
            print("Input grades, each in their own line.\nType '0' when done\n")
            grade = int(input())
            dic[student] = []
            while grade:
                try:
                    if 1 <= grade <= 5:
                        dic[student].append(grade)
                    else:
                        print("Grades are numbers 1-5, please try again")
                    grade = int(input())
                except ValueError:
                    print("Grades are numbers 1-5, please try again")
    else:
        print("No students in database")


def calculate_average(dic):
    names = list(dic.keys())
    if len(names):
        print(names)
        student = input("Whose grade average would you like?\n")
        if student in names:
            if mean(dic[student]):
                print(mean(dic[student]))
            else:
                print("No grades")
        else:
            print("Error #404: Student not found")
    else:
        print("No students in database")


def input_student(dic):
    new = input("Enter student name\n")
    if new in dic:
        print("Student already in database")
    else:
        dic[new] = [0]


def print_students(dic):
    names = list(dic.keys())
    if len(names):
        for i in range(len(names)):
            print(names[i], '- ', end='')
            if mean(dic[names[i]]):
                print(dic[names[i]])
            else:
                print("no grades")
    else:
        print('No students in database')


rj = {'Mark': [1, 1, 3, 5, 3], 'John': [4, 2], 'Paul': [1, 2, 3, 3], 'Mike': [3], 'Anthony': [1, 5, 4, 4, 3, 2, 1]}
menu = 0

while True:
    print("************Students************\n"
          "[1]-input students\n"
          "[2]-remove a student\n"
          "[3]-print all names and grades\n"
          "[4]-calculate a student's average\n"
          "[5]-enter a student's grades\n"
          "[6]-exit\n"
          "********************************")
    menu = input()
    if menu == '1':
        input_student(rj)
    elif menu == '2':
        delete_student(rj)
    elif menu == '3':
        print_students(rj)
    elif menu == '4':
        calculate_average(rj)
    elif menu == '5':
        input_grades(rj)
    elif menu == '6':
        exit()
    else:
        print('Error: try again')
