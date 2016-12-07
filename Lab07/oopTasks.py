import re

class Course:

    def __init__(self, courseID, fst, snd, final):
        self.courseID = courseID
        self.fst = fst
        self.snd = snd
        self.final = final
        self.total = 0.25 * fst + 0.25 * snd + 0.50 * final

    def __str__(self):
        return self.courseID + ": (" + "{0:2.2f}".format(self.fst) + ", {0:2.2f}, ".format(self.snd) + "{0:2.2f}".format(self.final) + ") = (" + "{0:2.2f}, ".format(self.total) + self.getLetterGrade() + ")"

    def getLetterGrade(self):

        if self.total >= 90:
            return "A"
        elif self.total<90 and self.total>=80:
            return "B"
        elif self.total<80 and self.total>=70:
            return "C"
        elif self.total < 70 and self.total >= 60:
            return "D"
        else:
            return "F"

class Student:

    def __init__(self, name):
        self.name = name
        self.courses = {} # empty Dictionary

    def __str__(self):
        list_courses = list(self.courses.keys())
        list_courses.sort()

        str_out = ''
        str_out += self.name + ': '
        for val in list_courses:
            str_out += "(" + str(val) + ": " + self.courses[val].getLetterGrade() + "), "

        return str_out[0:len(str_out) - 2]

    def addCourse(self, course):
        self.courses[course.courseID] = course

    def generateTranscript(self):
        list_courses = list(self.courses.keys())
        list_courses.sort()

        str_out = ''
        str_out += self.name + '\n'

        index = 0
        while index < len(list_courses) - 1:
            str_out += str(self.courses[list_courses[index]])
            str_out += '\n'
            index += 1

        str_out += str(self.courses[list_courses[index]])

        return str_out

class School:

    def __init__(self, name):
        self.name = name
        self.students = {}

    def __str__(self):

        str_out = ''
        str_out += self.name

        no_students = len(list(self.students.keys()))

        str_out += ": " + str(no_students) + " Students" + "\n"

        sort_names = list(self.students.keys())
        sort_names.sort()

        index = 0
        while index < len(sort_names) - 1:
            str_out += sort_names[index] + '\n'
            index += 1

        str_out += sort_names[index]

        return str_out

    def loadStudentsInfo(self, filename):

        fopen = open("school_data_source.txt", "r")

        student_lines = fopen.read()
        student_lines = student_lines.split("\n\n")

        for student in student_lines:
            student_details =  student.split("\n--------------------\n")
            student_name = student_details[0]
            student = Student(student_name) # Student Object
            courses = student_details[1].split("\n")
            for course in courses:
                course_details = course.split(":")
                courseName = course_details[0].strip()
                grades = course_details[1].split(",")
                student.addCourse(Course(courseName,float(grades[0].strip()),float(grades[1].strip()),float(grades[2].strip())))

            self.students[student_name] = student

        fopen.close()

    def saveSchoolInfo(self, filename):

        with open(filename,"w") as fp:

            students_sort = list(self.students.keys())
            students_sort.sort()

            index = 0
            while index < len(students_sort)-1:
                fp.write(self.students[students_sort[index]].generateTranscript())
                fp.write('\n\n')
                index += 1

            fp.write(self.students[students_sort[index]].generateTranscript())

def main():

    # Course
    course1 = Course("ECE274",99.00, 72.00, 74.00)
    course2 = Course("ECE377", 64.00, 86.00, 79.00)
    course3 = Course("ECE474",96.00, 90.00, 67.00)
    course4 = Course("ECE678",89.00, 86.00, 79.00)

    #print(course1)

    # Student Class
    student  = Student("John Smith")
    student.addCourse(course1)
    student.addCourse(course2)
    student.addCourse(course3)
    student.addCourse(course4)

    # Student Class
    school = School("Purdue University")
    school.loadStudentsInfo("school_data_source.txt")
    school.saveSchoolInfo("sample.txt")
    print(school)

if __name__ == '__main__':
    main()