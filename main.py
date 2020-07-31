from cohort import *
from exercise import *
from instructor import *
from student import *
from reports import *

## Add Exercises ##
kennel = Exercise("Kennel", "JavaScript")
planets = Exercise("Planets", "Python")
random_numbers = Exercise("Random Numbers", "Python")
solar_system = Exercise("Solar System", "JavaScript")
coins_to_cash = Exercise("Coins To Cash", "Python")

## Add Cohorts ##
c40 = Cohort("C-40")
c38 = Cohort("C-38")
c39 = Cohort("C-39")
c35 = Cohort("C-35")
c23 = Cohort("C-23")

## Add Students ## 
brian = Student("Brian", "Cravens", "bcravens", "c40")
derick = Student("Derick", "Cravens", "dcravens", "c35")
connor = Student("Connor", "Wagner", "cwagner", "c39")
summer = Student("Summer", "Wagner", "swagner", "c38")
spyke = Student("Spyke", "Cravens", "scravens", "c23")

## Add Instructors ##
joe_shepherd = Instructor("Joe", "Shepherd", "joes", "c40", "JavaScript")
bryan_nilsen = Instructor("Bryan", "Nilsen", "bnilsen", "c39", "JavaScript")
steve_brownlee = Instructor("Steve", "Brownlee", "sbrownlee", "c38", "Python")


joe_shepherd.give_assignment(brian, kennel)
joe_shepherd.give_assignment(connor, kennel)
joe_shepherd.give_assignment(spyke, kennel)
joe_shepherd.give_assignment(derick, kennel)
bryan_nilsen.give_assignment(brian, planets)
bryan_nilsen.give_assignment(derick, planets)
bryan_nilsen.give_assignment(connor, planets)
bryan_nilsen.give_assignment(spyke, planets)
bryan_nilsen.give_assignment(summer, planets)

students = list()
students.extend([brian, derick, summer, connor, spyke])

exercises = list()
exercises.extend([kennel, planets, random_numbers, solar_system, coins_to_cash])

def student_assignments():
    for student in students:
        student_assignments = []
        print(f'******{student.first_name} is currently assigned:******')
        for exercise in student.exercises:
            student_assignments.append(exercise.name)
            print('')
            print(f'{exercise.name}')
            print('')

student_assignments()

reports.all_students()
