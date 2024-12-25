import sqlite3
import pandas as pd
import numpy as np

import random

from datetime import datetime
from datetime import timedelta

from faker import Faker
fake = Faker()

import kagglehub

import warnings
warnings.filterwarnings("ignore")




path = kagglehub.dataset_download("abdullah0a/student-dropout-analysis-and-prediction-dataset")
df = pd.read_csv(path +"\\student dropout.csv")

students_db = sqlite3.connect('students.db', timeout=10)
cursor = students_db.cursor()

education_levels = {0:'No formal education',
    1:'Primary education',
    2:'Not completed Secondary education',
    3:'Completed Secondary education',
    4:'Higher education'}

school_types = {0:'Boarding school', 
                1:'Public school', 
                2:'Private school'}

family_relationship = {1:'Very weak', 
                       2:'Weak', 
                       3:'Moderate', 
                       4:'Strong', 
                       5:'Very close'}

for i,level in enumerate(education_levels.items()):
    cursor.execute("INSERT INTO ParentsEduLevel (id, description) VALUES (?, ?)", (level[0], level[1]))


for i,type in enumerate(school_types.items()):
    cursor.execute("INSERT INTO SchoolsStatus (id, description) VALUES (?, ?)", (type[0], type[1]))


for i,type in enumerate(family_relationship.items()):
    cursor.execute("INSERT INTO FamilyRelationship (id, description) VALUES (?, ?)", (type[0], type[1]))


# Работа с данными для наполнения таблицы со студентами
df = df.reset_index()
df = df.rename({'index':'id'}, axis = 1)

# Генерация адресов
new_addresses = []
for i in range(len(df)):
    new_addresses.append(fake.address())

df['address'] = pd.Series(new_addresses)

# Генерация дней рождения
df['date_of_birth'] = df['Age'].apply(lambda x: (datetime.now() - timedelta(days=x*365)).strftime('%Y-%m-%d'))

df_students = df[['id', 'Gender', 'date_of_birth', 'address']]

# for i,row in df_students.iterrows():
#     cursor.execute("INSERT INTO Students (id, gender, date_of_birth, address) VALUES (?, ?, ?, ?)", 
#                    (row['id'], row['Gender'], row['date_of_birth'], row['address']))
    

# Работа с данными для наполнения таблицы с родителями
mothers = df[['id', 'Mother_Education', 'Mother_Job', 'Guardian']]
fathers = df[['id', 'Father_Education', 'Father_Job', 'Guardian']]

fathers['Guardian'] =  fathers['Guardian'].map({'mother': 0, 'father': 1, 'other': 0})
mothers['Guardian'] =  mothers['Guardian'].map({'mother': 1, 'father': 0, 'other': 0})

mothers['Guardian'] =  mothers['Guardian'].astype(int)
fathers['Guardian'] = fathers['Guardian'].astype(int)

mothers['Gender'] = 'F'
fathers['Gender'] = 'M'

mothers = mothers.rename({'id':'student_id'}, axis = 1)
fathers = fathers.rename({'id':'student_id'}, axis = 1)

mothers.columns = ['student_id', 'education', 'job', 'guardian', 'gender']
fathers.columns = ['student_id', 'education', 'job', 'guardian', 'gender']

parents = pd.concat([mothers, fathers], ignore_index=True)

def generate_income():
    return random.randint(100.0, 10000.0)


def generate_date_in_range(start_date, end_date):
    while True:
        date_time = fake.date_time()
        if start_date <= date_time <= end_date:
            return date_time

parents['income'] = parents.apply(lambda x: generate_income(), axis=1)
parents['date_of_birth'] = parents.apply(lambda x: generate_date_in_range(datetime(1970, 1, 1), datetime(1989, 12, 31))\
                                         .strftime('%Y-%m-%d'), axis=1) 
parents = parents.reset_index()
parents = parents.rename({'index':'id'}, axis = 1)

for i,row in parents.iterrows():
    cursor.execute('''INSERT INTO Parents (id, gender, edu_level, occupation, date_of_birth, income, student_id, guardian_status) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', 
                   (row['id'], row['gender'], 
                    row['education'], row['job'],
                    row['date_of_birth'], row['income'],
                    row['student_id'], row['guardian']))
    

# Работа с данными для наполнения таблицы с данными по успеваемости студентов
academic_perfomance = df[['id','Number_of_Absences', 'Number_of_Failures', 
                          'Extra_Curricular_Activities', 'Study_Time', 
                          'Final_Grade', 'Wants_Higher_Education']]

academic_perfomance = academic_perfomance.rename({'id':'student_id'}, axis = 1)
academic_perfomance['date'] = academic_perfomance.apply(lambda x: generate_date_in_range(datetime(2023, 1, 1), datetime(2024, 12, 31))\
                                                        .strftime('%Y-%m-%d'), axis=1) 
academic_perfomance['id'] = academic_perfomance.index


for i,row in academic_perfomance.iterrows():
    cursor.execute('''INSERT INTO AcademicPerfomances (id, date, student_id, absence_num, failures_num, study_time, 
                                                        extra_classes, higher_edu_expect, final_grade) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)''', 
                   (row['id'], row['date'], 
                    row['student_id'], row['Number_of_Absences'],
                    row['Number_of_Failures'], row['Study_Time'],
                    row['Extra_Curricular_Activities'], row['Wants_Higher_Education'],
                    row['Final_Grade']))


students_db.commit()

# курсы, учителя, школы полностью синтезированные данные

subjects = [
    ["Mathematics", "Physics"], ["Chemistry", "Biology"], ["History", 'Economics'],
    "Geography", "Art", "Music", "Physical Education", ["Literature","English"], 'Computer Science'
    ]

schools = [ "Middle School", "High School", "Junior School", "School"]
school_names = [f"{fake.city()} {random.choice(schools)}" for _ in range(150)]
school_addresses = [f"{fake.address()}" for _ in range(150)]
number_of_students = [random.randint(50, 600) for _ in range(150)]
headteachers = [f"{fake.name()}" for _ in range(150)]
school_statuses = [random.choice([0,1,2]) for _ in range(150)]


female_teachers = [f"{fake.first_name_female()} {fake.last_name()}" for _ in range(150)]
male_teachers = [f"{fake.first_name_male()} {fake.last_name()}" for _ in range(150)]
years_of_experience = [random.randint(1, 30) for _ in range(300)]
date = [generate_date_in_range(datetime(2023, 1, 1), datetime(2024, 12, 31)) for _ in range(300)]

descriptions = [
        "This course introduces the fundamental concepts of the subject",
        "Students in this course will gain a comprehensive understanding of subject with practice.",
        "This fundamental course examines key themes and principles of core subject."]

schools = pd.DataFrame({'school_name':school_names, 'school_address':school_addresses, 'number_of_students':number_of_students,
              'headteacher':headteachers, 'school_status':school_statuses})

schools = schools.reset_index()
schools = schools.rename({'index':'id'}, axis = 1) 


for i,row in schools.iterrows():
    cursor.execute('''INSERT INTO Schools (id, address, name, number_of_students, headteacher, status) 
                      VALUES (?, ?, ?, ?, ?, ?)''', 
                   (row['id'], row['school_address'], 
                    row['school_name'], row['number_of_students'],
                    row['headteacher'], row['school_status'],
                    ))

teachers = pd.concat([pd.DataFrame({'name':female_teachers, 'gender':'F'}),
                      pd.DataFrame({'name':male_teachers, 'gender':'M'})], ignore_index=True)

teachers['years_experience'] = years_of_experience
teachers['date'] = [d.strftime('%Y-%m-%d') for d in date]
teachers = teachers.reset_index()
teachers = teachers.rename({'index':'id'}, axis = 1)
teachers['school_id'] = teachers.apply(lambda x: random.randint(0, 149), axis=1)


for i,row in teachers.iterrows():
    cursor.execute('''INSERT INTO Teachers (id, gender, name, years_experience, school_id, date) 
                      VALUES (?, ?, ?, ?, ?, ?)''', 
                   (row['id'], row['gender'], 
                    row['name'], row['years_experience'],
                    row['school_id'], row['date']
                    ))


courses = pd.DataFrame({'name':subjects})
courses = courses.loc[np.repeat(courses.index, 30)].reset_index(drop=True)
courses['teacher_id'] = random.sample(range(0, 300), len(courses))
courses = courses.explode('name')
courses['credits'] = courses.apply(lambda x: random.randint(1, 10), axis=1)
courses['description'] = [random.choice(descriptions) for _ in range(len(courses))]

courses['id'] = range(0, len(courses))



for i,row in courses.iterrows():
    cursor.execute('''INSERT INTO Courses (id, name, description, teacher_id, credits) 
                      VALUES (?, ?, ?, ?, ?)''', 
                   (row['id'], row['name'], 
                    row['description'], row['teacher_id'],
                    row['credits']
                    ))
    
students_db.commit()

dropout_reasons = [
    "Family responsibilities",
    "Financial difficulties",
    "Health issues",
    "Lack of interest in school",
    "Bullying",
    "Moving to a new location",
    "Mental health challenges",
    "Academic struggles"
]

dropouts = df[['id', 'Dropped_Out']]
dropouts = dropouts[dropouts['Dropped_Out'] == True]
dropouts = dropouts.rename({'id':'student_id'}, axis = 1)
dropouts['id'] = [random.randint(0, 80) for _ in range(len(dropouts))] 

dropouts_original = dropouts.copy()

dropouts = dropouts.drop_duplicates(subset = 'id')

dropouts['date'] = [generate_date_in_range(datetime(2024, 9, 1), datetime(2024, 12, 20)).strftime('%Y-%m-%d') for _ in range(len(dropouts))]
dropouts['teacher_id'] = [random.randint(0, 300) for _ in range(len(dropouts))] 
dropouts['reason'] = [random.choice(dropout_reasons) for _ in range(len(dropouts))]


for i,row in dropouts.iterrows():
    cursor.execute('''INSERT INTO Dropouts (id, date, reason, teacher_id) 
                      VALUES (?, ?, ?, ?)''', 
                   (row['id'], row['date'], 
                    row['reason'], row['teacher_id'],
                    ))
    

for i,row in dropouts_original.iterrows():
    cursor.execute('''INSERT INTO DropoutsRecords (student_id, dropout_id) 
                      VALUES (?, ?)''', 
                   (row['student_id'], row['id']
                    ))
    

enrollments = pd.DataFrame()
enrollments['id'] = [_ for _ in range(324)]
enrollments['date'] = [generate_date_in_range(datetime(2020, 8, 1), datetime(2023, 12, 20)).strftime('%Y-%m-%d') for _ in range(len(enrollments))]

for i,row in enrollments.iterrows():
    cursor.execute('''INSERT INTO Enrollments (id, date) 
                      VALUES (?, ?)''', 
                   (row['id'], row['date']
                    ))
    
syrveys = pd.DataFrame({'id':1, 'date':'2024-12-01', 
                        'description':'Survey for a comprehensive analysis of factors influencing student dropout rates in secondary education (MIT)'}, 
                        index = [0])

for i,row in syrveys.iterrows():
    cursor.execute('''INSERT INTO Surveys (id, date, description) 
                      VALUES (?, ?, ?)''', 
                   (row['id'], row['date'], row['description']
                    ))
    
health_status = df[['id', 'Weekend_Alcohol_Consumption', 'Health_Status']]

alcohol_consumption = {
    1: "No consumption",
    2: "Low",
    3: "Moderate",
    4: "Moderate-high",
    5: "High"
}

state_of_health = {
    1: "Poor",
    2: "Fair",
    3: "Average",
    4: "Good",
    5: "Excellent"
}

health_status['Alcohol_Consumption']  = health_status['Weekend_Alcohol_Consumption'].map(alcohol_consumption)
health_status['health_status']  = health_status['Health_Status'].map(state_of_health)
health_status = health_status.rename({'id':'student_id'}, axis = 1) 
health_status['id'] = [_ for _ in range(len(health_status))]
health_status['date'] = health_status.apply(lambda x: generate_date_in_range(datetime(2023, 1, 1), 
                                                                             datetime(2024, 12, 31)).strftime('%Y-%m-%d'), axis=1)

mental_health = df[['id', 'Family_Relationship', 'In_Relationship']]
mental_health = mental_health.rename({'id':'student_id'}, axis = 1) 
mental_health['id'] = [_ for _ in range(len(mental_health))]
mental_health['date'] = mental_health.apply(lambda x: generate_date_in_range(datetime(2023, 1, 1), 
                                                                             datetime(2024, 12, 31)).strftime('%Y-%m-%d'), axis=1)

for i,row in health_status.iterrows():
    cursor.execute('''INSERT INTO HealthStatuses (id, date, student_id, alcohol_consumption, state_of_health) 
                      VALUES (?, ?, ?, ?, ?)''', 
                   (row['id'], row['date'], 
                    row['student_id'], row['Alcohol_Consumption'], 
                    row['health_status']
                    ))
    
for i,row in mental_health.iterrows():
    cursor.execute('''INSERT INTO MentalHealthStatuses (id, date, student_id, romantic_relat, family_relat_score) 
                      VALUES (?, ?, ?, ?, ?)''', 
                   (row['id'], row['date'], 
                    row['student_id'], row['In_Relationship'], 
                    row['Family_Relationship']
                    ))
    
students_db.commit()

df_students = df_students.rename({'id':'student_id'}, axis = 1)
teachers = teachers.rename({'id':'teacher_id'}, axis = 1)
merged_drops_teachers = dropouts.merge(teachers, on = 'teacher_id', how = 'left')
df_students_merged = df_students.merge(merged_drops_teachers, on = 'student_id', how = 'left')
school_ids =df_students_merged[['student_id', 'school_id']]
school_ids.loc[(school_ids['school_id'].isna() == True), 'school_id'] = [random.randint(0, 149) for _ in range(len(school_ids[school_ids['school_id'].isna() == True]))]
school_ids['school_id'] = school_ids['school_id'].astype("int64")

school_ids['enrollment_id'] = [random.randint(0, 324) for _ in range(len(school_ids))]
school_ids['survey_id'] = 1

school_ids['enrollment_id'] = school_ids['enrollment_id'].astype("int64")
school_ids['survey_id'] = school_ids['survey_id'].astype("int64")

df_students_ = df_students.merge(school_ids, on = 'student_id', how = 'left')

for i,row in df_students_.iterrows():
    cursor.execute("INSERT INTO Students (id, gender, date_of_birth, address, school_id, survey_id, enrollment_id) VALUES (?, ?, ?, ?, ?, ?, ?)", 
                   (row['student_id'], row['Gender'], row['date_of_birth'], row['address'],
                    row['school_id'], row['survey_id'], row['enrollment_id']))
    
students_db.commit()
students_db.close()