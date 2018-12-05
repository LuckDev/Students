from statistics import mean
from sys import exit

def DeleteStudent(dic):
    studentNames = list(dic.keys())
    if len(studentNames):
        print(studentNames)
        aStudent = input("Which student would you like to delete?\n")
        if aStudent in studentNames:
            del dic[aStudent]
        else:
            print("Error #404: Student not found")
    else:
        print("No students in database")

def InputGrades(dic):
    studentNames = list(dic.keys())
    if len(studentNames):
        print(studentNames)
        aStudent = input("Whose grades would you like to enter?\n")
        if aStudent not in studentNames:
            print("Error #404: Student not found")
            return
        else:
            print("Input grades, each in their own line.\nType '0' when done\n")
            studentGrade = int(input())
            dic[aStudent] = []
            while studentGrade:
                try:
                    if 1 <= studentGrade <= 5:
                        dic[aStudent].append(studentGrade)
                    else:
                        print("Grades are numbers 1-5, please try again")
                    grade = int(input())
                except ValueError:
                    print("Grades are numbers 1-5, please try again")
    else:
        print("No students in database")

def CalculateAverage(dic):
    studentNames = list(dic.keys())
    if len(studentNames):
        print(studentNames)
        aStudent = input("Whose grade average would you like?\n")
        if aStudent in studentNames:
            if mean(dic[aStudent]):
                print(mean(dic[aStudent]))
            else:
                print("No grades")
        else:
            print("Error #404: Student not found")
    else:
        print("No students in database")

def InputStudent(dic):
    newStudent = input("Enter student name\n")
    if newStudent in dic:
        print("Student already in database")
    else:
        dic[newStudent] = [0]


def PrintStudents(dic):
    studentNames = list(dic.keys())
    if len(studentNames):
        for i in range(len(studentNames)):
            print(studentNames[i], '- ', end='')
            if mean(dic[studentNames[i]]):
                print(dic[studentNames[i]])
            else:
                print("no grades")
    else:
        print('No students in database')


rj = {'Mark': [1, 1, 3, 5, 3], 'John': [4, 2], 'Paul': [1, 2, 3, 3], 'Mike': [3], 'Anthony': [1, 5, 4, 4, 3, 2, 1]}
menuChoice = 0

while True:
    print("************Students************\n"
          "[1]-input students\n"
          "[2]-remove a student\n"
          "[3]-print all names and grades\n"
          "[4]-calculate a student's average\n"
          "[5]-enter a student's grades\n"
          "[6]-exit\n"
          "********************************")
    menuChoice = input()
    if menuChoice == '1':
        InputStudent(rj)
    elif menuChoice == '2':
        DeleteStudent(rj)
    elif menuChoice == '3':
        PrintStudents(rj)
    elif menuChoice == '4':
        CalculateAverage(rj)
    elif menuChoice == '5':
        InputGrades(rj)
    elif menuChoice == '6':
        exit()
    else:
        print('Error: try again')
