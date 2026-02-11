# Создать программу, которая подсчитывает среднюю оценку по предмету из CSV файла с оценками студентов.
import csv



with open("studentsGrades.csv", "r") as file:
    student_stats = csv.DictReader(file)
    for Student in student_stats:
       math = int(Student["Математика"])
       phys = int(Student["Физика"])
       chem = int(Student["Химия"])
       gpa = (math+phys+chem)/3
       print(Student["Студент"]+" "+str(gpa))