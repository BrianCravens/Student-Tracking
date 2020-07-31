import sqlite3

class Student():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.cohort}'


class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/home/brian/workspace/python/practice/Tracking/studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(row  [1], row[2], row[3], row[5])

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select s.Id,
                s.first_name,
                s.Last_name,
                s.slack_handle,
                s.cohort_id,
                c.name
            from students s
            join cohorts c on s.cohort_id = c.id
            order by s.cohort_id
            """)

            all_students = db_cursor.fetchall()
            print('\n***All Students***')

            for student in all_students:
                print(student)

reports = StudentExerciseReports()
reports.all_students()

class Cohort():

    def __init__(self, name):
        self.name = name
        

    def __repr__(self):
        return f'{self.name}'

class CohortsReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/home/brian/workspace/python/practice/Tracking/studentexercises.db"

    def all_cohorts(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row  [1])

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select c.id,
                c.name
                
            from cohorts c
            order by c.name
            """)

            all_cohorts = db_cursor.fetchall()
            print('\n***All Cohorts***')

            for cohort in all_cohorts:
                print(cohort)

reports = CohortsReports()
reports.all_cohorts()
class Exercise():

    def __init__(self, name, language):
        self.name = name
        self.language = language
        

    def __repr__(self):
        return f'{self.name} is written in {self.language}'

class ExercisesReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/home/brian/workspace/python/practice/Tracking/studentexercises.db"

    def all_exercises(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row  [1], row [2])

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.id,
                e.name,
                e.language
                
            from exercises e
            order by e.language
            """)

            all_exercises = db_cursor.fetchall()
            print('\n***All Exercises***')
            for exercise in all_exercises:
                print(exercise)

reports = ExercisesReports()
reports.all_exercises()
class JSExercisesReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/home/brian/workspace/python/practice/Tracking/studentexercises.db"

    def js_exercises(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row  [1], row [2])

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.id,
                e.name,
                e.language
                
            from exercises e
            where e.language = "JavaScript"
            order by e.language;
            """)
            

            js_exercises = db_cursor.fetchall()
            print('\n***JavaScript Exercises***')

            for exercise in js_exercises:
                print(exercise)

            

reports = JSExercisesReports()
reports.js_exercises()

class PYExercisesReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/home/brian/workspace/python/practice/Tracking/studentexercises.db"

    def py_exercises(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row  [1], row [2])

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select e.id,
                e.name,
                e.language
                
            from exercises e
            where e.language = "Python"
            order by e.language
            """)

            py_exercises = db_cursor.fetchall()
            print('\n***Python Exercises***')
            for exercise in py_exercises:
                print(exercise)

reports = PYExercisesReports()
reports.py_exercises()

class Instructor():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is holding down {self.cohort}'

class InstructorsReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/home/brian/workspace/python/practice/Tracking/studentexercises.db"

    def all_instructors(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor(row  [1], row[2], row[3], row[5])

            db_cursor = conn.cursor()

            db_cursor.execute("""
            select i.Id,
                i.first_name,
                i.Last_name,
                i.slack_handle,
                i.cohort_id,
                c.name
            from instructors i
            join cohorts c on i.cohort_id = c.id
            order by i.cohort_id
            """)

            all_students = db_cursor.fetchall()
            print('\n***All Instructors***')

            for student in all_students:
                print(student)

reports = InstructorsReports()
reports.all_instructors()