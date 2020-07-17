class Instructor:
    def __init__(self, fname, lname, slack, cohort, speciality):
        self.first_name = fname
        self.last_name = lname
        self.slack_handle = slack
        self.cohort = cohort
        self.speciality = speciality
        
    def give_assignment(self, student, exercise):
        student.add_exercise(exercise)