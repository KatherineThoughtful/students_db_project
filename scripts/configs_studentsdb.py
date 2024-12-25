import datetime

class ConfigsStudentsDB():
    def __init__(self):
        self.parents_birthday_start: datetime.datetime = datetime.datetime(1970, 1, 1)
        self.parents_birthday_end: datetime.datetime  = datetime.datetime(1989, 12, 31)
        self.academic_perf_date_start: datetime.datetime  = datetime.datetime(2023, 1, 1)
        self.academic_perf_date_end: datetime.datetime  = datetime.datetime(2024, 12, 31)
        self.status_date_start: datetime.datetime  = datetime.datetime(2023, 1, 1)
        self.status_date_end: datetime.datetime  = datetime.datetime(2024, 12, 31)
        self.enrollment_start_date: datetime.datetime  = datetime.datetime(2020, 8, 1)
        self.enrollment_end_date: datetime.datetime  = datetime.datetime(2023, 12, 20)
        self.dropout_start_date: datetime.datetime  = datetime.datetime(2024, 9, 1)
        self.dropout_end_date: datetime.datetime  = datetime.datetime(2024, 12, 20)
        self.teachers_info_start_date: datetime.datetime  = datetime.datetime(2023, 1, 1)
        self.teachers_info_end_date: datetime.datetime  = datetime.datetime(2024, 12, 31)
        self.students_to_dropout: int = 80
        self.teachers_num: int = 300
        self.num_teachers_one_gender:int = 150
        self.courses_num: int = 30
        self.schools_ids: int = 149
        self.max_year_of_exp: int = 30
        self.students_num_min: int = 50
        self.students_num_max: int = 600
        self.schools_num: int = 150


