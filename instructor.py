from nssPerson import *
class Instructor(nss_person):
    def __init__(self, fname, lname, slack, cohort, speciality):
        super().__init__(fname, lname, slack, cohort)
        self.speciality = speciality
        
    def give_assignment(self, student, exercise):
        student.add_exercise(exercise)