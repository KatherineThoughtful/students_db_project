**Здесь можно создать описание нашего проекта**

Использован [датасет с Kaggle](https://www.kaggle.com/datasets/abdullah0a/student-dropout-analysis-and-prediction-dataset) c опросными данными

Репозиторий содержит следующие файлы:
- `students_create_db.py` - скрипт с DDL командами (создание базы данных и таблиц);
- `students_insert_to_db.py` - скрипт с DML командами (наполнение базы на основе исходных и синтезированных данных);
- `students.db` - файл с базой данных;
- `students_db_loader.ipynb` - ноутбук для отладки применения DML команд, повторяет скрипт с DML командами;
- `students_db_sqlite_scheme.svg` - визуализация схемы БД.

База создана на основе SQLite.

Библиотеки, использованные в ходе работы над проектом: sqlite3, faker

[Концептальная схема базы данных по студентам](https://drive.google.com/file/d/1up-pHYgRnpuUeZ46K-X7zxkanIEcnq3-/view?usp=sharing) 
