from nssPerson import *

class Student(nss_person):
    def __init__(self, fname, lname, slack, cohort):
        super().__init__(fname, lname, slack, cohort)
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)
        