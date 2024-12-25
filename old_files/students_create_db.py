import sqlite3

students_db = sqlite3.connect('students.db')

cursor = students_db.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
    id INTEGER PRIMARY KEY,
    gender TEXT,
    date_of_birth TEXT,
    address TEXT,
    school_id INTEGER,
    survey_id INTEGER,    
    enrollment_id INTEGER,
    FOREIGN KEY (school_id) REFERENCES Schools (id) ON DELETE SET NULL,
    FOREIGN KEY (enrollment_id) REFERENCES Enrollments (id) ON DELETE SET NULL,
    FOREIGN KEY (survey_id) REFERENCES Surveys (id) ON DELETE SET NULL
                           
) 
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Parents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    gender TEXT,
    edu_level INTEGER,
    occupation TEXT,
    date_of_birth TEXT,
    income REAL,
    student_id INTEGER,
    guardian_status INTEGER,
    FOREIGN KEY (student_id) REFERENCES Students (id) ON DELETE SET NULL,
    FOREIGN KEY (edu_level) REFERENCES ParentsEduLevel (id) ON DELETE SET NULL
               
) 
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS ParentsEduLevel (
    id INTEGER PRIMARY KEY,
    description TEXT            
) 
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Schools (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    address TEXT,
    name TEXT,
    number_of_students INTEGER,
    headteacher TEXT,
    status INTEGER,
    FOREIGN KEY (status) REFERENCES SchoolStatus (id) ON DELETE SET NULL          
) 
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS SchoolsStatus (
    id INTEGER PRIMARY KEY,
    description TEXT            
) 
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Teachers (
    id INTEGER PRIMARY KEY,
    gender TEXT,
    name TEXT,
    years_experience INTEGER,
    school_id INTEGER,
    date TEXT,
    FOREIGN KEY (school_id) REFERENCES Schools (id) ON DELETE SET NULL          
) 
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Courses (
    id INTEGER PRIMARY KEY,
    name TEXT,
    description TEXT,
    teacher_id INTEGER,
    credits INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES Teachers (id) ON DELETE SET NULL          
) 
''')


cursor.execute('''CREATE TABLE IF NOT EXISTS Dropouts (
    id INTEGER PRIMARY KEY,
    date TEXT,
    reason TEXT,
    teacher_id INTEGER,
    FOREIGN KEY (teacher_id) REFERENCES Teachers (id) ON DELETE SET NULL          
) 
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS DropoutsRecords (
    student_id INTEGER,
    dropout_id INTEGER,
    FOREIGN KEY (student_id) REFERENCES Students (id) ON DELETE SET NULL
    FOREIGN KEY (dropout_id) REFERENCES Dropouts (id) ON DELETE SET NULL  
    PRIMARY KEY (student_id, dropout_id)        
) 
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS AcademicPerfomances (
    id INTEGER PRIMARY KEY,
    date TEXT,
    student_id INTEGER,
    absence_num INTEGER,
    failures_num INTEGER,
    study_time REAL,
    extra_classes TEXT,
    higher_edu_expect TEXT,
    final_grade REAL,
    FOREIGN KEY (student_id) REFERENCES Students (id) ON DELETE SET NULL          
) 
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS HealthStatuses (
    id INTEGER PRIMARY KEY,
    date TEXT,
    student_id INTEGER,
    alcohol_consumption TEXT,
    state_of_health TEXT,
    FOREIGN KEY (student_id) REFERENCES Students (id) ON DELETE SET NULL          
) 
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS MentalHealthStatuses (
    id INTEGER PRIMARY KEY,
    date TEXT,
    student_id INTEGER,
    romantic_relat TEXT,
    family_relat_score INTEGER,
    FOREIGN KEY (family_relat_score) REFERENCES FamilyRelationship (id) ON DELETE SET NULL,
    FOREIGN KEY (student_id) REFERENCES Students (id) ON DELETE SET NULL          
) 
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS FamilyRelationship (
    id INTEGER PRIMARY KEY,
    description TEXT        
) 
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Surveys (
    id INTEGER,
    date TEXT,
    description TEXT        
) 
''')

cursor.execute('''CREATE TABLE IF NOT EXISTS Enrollments (
    id INTEGER,
    date TEXT       
) 
''')

students_db.commit()

students_db.close()