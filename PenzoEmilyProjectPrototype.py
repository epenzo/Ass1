def loadFile(filename):
    resultList = []
    infile = open(filename, 'r')
    i = 1 # index of file line #
    n = 0 # number of students read
    for line in infile:
        line = line.strip()
        if (i > 1 and len(line) > 0):
            fields = line.split('\t')
            resultList.append(fields)
            n += 1
        i += 1
    infile.close()
    print(resultList)
    return resultList
# def loadFile(file):
#     first_line= file.readline()
#     #print(first_line)
#     first_line= first_line.rstrip("\n")
#     first_line= first_line.split("\t")
#     #print(first_line)
#     student_list=[]
#     for line in file:
#         #print(line)
#         line= line.rstrip("\n")
#         line= line.split("\t")
#         #print(line)
#         student_list.append(line)     
#     #file.rstrip("\n")
#     return student_list   
   

def mainMenu():
    print("\nPlease choose:")
    print("0) Quit")
    print("1) Display All")
    print("2) Display by Grad Year")
    print("3) Display Surname")
    choice = input("==> ")
    try:
        ichoice = int(choice)
    except:
        ichoice = -1
    return ichoice


def gradMenu():
    choice = input("Enter grad year of interest ==> ")
    return choice
def surname_fx():
    choice = input("Enter your last name ==> ")
    return choice

def displayStudent(student):
    print(student[0], student[1], student[2], student[3], student[4], student[5], sep='\t')

def displayAll():
    for student in students:
        displayStudent(student)
    print(len(students), "student records displayed")


def displayGradYear(argyear):
    count = 0 
    for student in students:
        thisyear = student[3] 
        if thisyear == argyear:
            displayStudent(student)
            count += 1
    if count == 0:
        print("No students found for grad year", argyear)
    else:
        print(count, "student records displayed")
def displaysurname(lastname):
    count = 0 
    for student in students:
        if student[2].lower()== lastname.lower():
            displayStudent(student)
            count += 1
    if count == 0:
        print("No students found for lastname", lastname)
    else:
        print(count, "student records displayed")

print("Welcome to SQT")
infilename = "students.txt"
try:
    students = loadFile(infilename) 
   
except:
    print("input file not found")
    exit(1)


mainChoice = mainMenu() 
while (mainChoice != 0): 
    if mainChoice == -1:
        print("Unknown choice")
    elif mainChoice == 1: 
        displayAll()
    elif mainChoice == 2: 
        gradYear = gradMenu()
        displayGradYear(gradYear)
    elif mainChoice ==3:
        lastname= surname_fx()
        displaysurname(lastname)
    else:
        print("Unknown choice")
    mainChoice = mainMenu() 

print("Thanks for using SQT.")
