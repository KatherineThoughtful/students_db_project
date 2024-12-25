class QueriesStudentsDB:
    def __init__(self):
        self.ParentsEduLevel_query: str = '''INSERT INTO ParentsEduLevel (id, description) VALUES (?, ?)'''
        self.SchoolTypesQuery: str = '''INSERT INTO SchoolsStatus (id, description) VALUES (?, ?)'''
        self.FamilyRelatQuery: str = '''INSERT INTO FamilyRelationship (id, description) VALUES (?, ?)'''
        self.Parents_query: str = '''INSERT INTO Parents (id, gender, edu_level, occupation, date_of_birth, income, student_id, guardian_status) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)'''
        self.AcademicPerfomance_query: str = '''INSERT INTO AcademicPerfomances (id, date, student_id, absence_num, failures_num, study_time, 
                                    extra_classes, higher_edu_expect, final_grade) 
                                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        self.Schools_query: str = '''INSERT INTO Schools (id, address, name, number_of_students, headteacher, status) 
                            VALUES (?, ?, ?, ?, ?, ?)'''
        self.Teachers_query: str = '''INSERT INTO Teachers (id, gender, name, years_experience, school_id, date) 
                            VALUES (?, ?, ?, ?, ?, ?)'''
        self.Courses_query: str = '''INSERT INTO Courses (id, name, description, teacher_id, credits) 
                            VALUES (?, ?, ?, ?, ?)'''
        self.Dropouts_query: str = '''INSERT INTO Dropouts (id, date, reason, teacher_id) 
                            VALUES (?, ?, ?, ?)'''
        self.DropoutsRecords_query: str = '''INSERT INTO DropoutsRecords (student_id, dropout_id) 
                                VALUES (?, ?)'''
        self.Enrollments_query: str = '''INSERT INTO Enrollments (id, date) 
                            VALUES (?, ?)'''
        self.Surveys_query: str = '''INSERT INTO Surveys (id, date, description) 
                        VALUES (?, ?, ?)'''
        self.HealthStatuses_query: str = '''INSERT INTO HealthStatuses (id, date, student_id, alcohol_consumption, state_of_health) 
                                VALUES (?, ?, ?, ?, ?)'''
        self.MentalHealthStatuses_query: str = '''INSERT INTO MentalHealthStatuses (id, date, student_id, romantic_relat, family_relat_score) 
                                        VALUES (?, ?, ?, ?, ?)'''
        self.Students_query: str = '''INSERT INTO Students (id, gender, date_of_birth, address, school_id, enrollment_id, survey_id) 
                            VALUES (?, ?, ?, ?, ?, ?, ?)'''
                