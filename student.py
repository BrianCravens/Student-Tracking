class Student:
    def __init__(self, fname, lname, slack, cohort):
        self.first_name = fname
        self.last_name = lname
        self.slack_handle = slack
        self.cohort = cohort
        self.exercises = []

    def add_exercise(self, exercise):
        self.exercises.append(exercise)
        