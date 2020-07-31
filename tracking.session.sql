DELETE FROM student_exercises;
DELETE FROM exercises;
DELETE FROM instructors;
DELETE FROM students;
DELETE FROM cohorts;

DROP TABLE IF EXISTS cohorts;
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS instructors;
DROP TABLE IF EXISTS exercises;
DROP TABLE IF EXISTS student_exercises;

CREATE TABLE cohorts (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL UNIQUE
);

CREATE TABLE students (
    "id" Integer NOT NULL PRIMARY KEY AUTOINCREMENT,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "slack_handle" TEXT NOT NULL,
    "cohort_id" INTEGER,
    FOREIGN KEY("cohort_id") REFERENCES "cohorts"("id")
);

CREATE TABLE instructors (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "first_name" TEXT NOT NULL,
    "last_name" TEXT NOT NULL,
    "slack_handle" TEXT NOT NULL,
    "cohort_id" INTEGER,
    "speciality" TEXT NOT NULL,
    FOREIGN KEY("cohort_id") REFERENCES "cohorts"("id")
);

CREATE TABLE exercises (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "name" TEXT NOT NULL,
    "language" TEXT NOT NULL

);

CREATE TABLE student_exercises (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "exercise_id" INTEGER,
    "student_id" INTEGER,
    FOREIGN KEY ("exercise_id") REFERENCES "exercises"("id"),
    FOREIGN KEY ("student_id") REFERENCES "students"("id")
    

);


INSERT INTO cohorts (name)
VALUES ("Cohort 40");
INSERT INTO cohorts (name)
VALUES ("Cohort 41");
INSERT INTO cohorts (name)
VALUES ("Cohort 42");

INSERT INTO exercises (name, language)
VALUES ("Kennel", "JavaScript");
INSERT INTO exercises (name, language)
VALUES ("Planets", "Python");
INSERT INTO exercises (name, language)
VALUES ("Coins to Cash", "Python");
INSERT INTO exercises (name, language)
VALUES ("student exercise", "sql");
INSERT INTO exercises (name, language)
VALUES ("Cash to Coins", "Python");

INSERT INTO instructors (first_name, last_name, slack_handle, cohort_id, speciality)
VALUES ("Joe", "Shepherd", "joes", 1, "JavaScript");
INSERT INTO instructors (first_name, last_name, slack_handle, cohort_id, speciality)
VALUES ("Bryan", "Nilsen", "bryfive", 2, "JavaScript");
INSERT INTO instructors (first_name, last_name, slack_handle, cohort_id, speciality)
VALUES ("Maddie", "Pepper", "maddiep", 3, "JavaScript");

INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
VALUES ("Brian", "Cravens", "bcravens", 1);
INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
VALUES ("Ricky", "Bobby", "rbobby", 2);
INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
VALUES ("Joe", "Dirt", "jdirt", 3);
INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
VALUES ("Joe", "Montana", "jmontana", 1);
INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
VALUES ("Ricky", "Rick", "rrick", 2);
INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
VALUES ("Milk", "Man", "mman", 3);
INSERT INTO students (first_name, last_name, slack_handle, cohort_id)
VALUES ("Matt", "Daddy", "mdaddy", 1);

INSERT INTO student_exercises (exercise_id, student_id )
VALUES (1, 1);
INSERT INTO student_exercises (exercise_id, student_id )
VALUES (1, 4);
INSERT INTO student_exercises (exercise_id, student_id )
VALUES (2, 3);
INSERT INTO student_exercises (exercise_id, student_id )
VALUES (2, 2);
INSERT INTO student_exercises (exercise_id, student_id )
VALUES (3, 1);
INSERT INTO student_exercises (exercise_id, student_id )
VALUES (3, 3);
INSERT INTO student_exercises (exercise_id, student_id )
VALUES (4, 2);
INSERT INTO student_exercises (exercise_id, student_id )
VALUES (4, 1);
INSERT INTO student_exercises (exercise_id, student_id )
VALUES (5, 3);
INSERT INTO student_exercises (exercise_id, student_id )
VALUES (5, 5);
INSERT INTO student_exercises (exercise_id, student_id )
VALUES (6, 5);
INSERT INTO student_exercises (exercise_id, student_id )
VALUES (6, 1);
INSERT INTO student_exercises (exercise_id, student_id )
VALUES (7, 4);
INSERT INTO student_exercises (exercise_id, student_id )
VALUES (7, 3);

SELECT s.first_name, s.last_name, i.last_name as instructor, cohorts.name, ex.name as exercise
FROM students s 
JOIN cohorts on cohorts.id = s.cohort_id
JOIN student_exercises
ON s.id = student_exercises.student_id
JOIN exercises ex
ON student_exercises.exercise_id = ex.id
JOIN instructors i
ON i.cohort_id = cohorts.id
ORDER BY s.last_name