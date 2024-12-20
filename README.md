### Проект по созданию базы данных по тематике академического и социального бэкграунда учащихся. 

**Цель проекта**: создать базу с помощью исходных и синтезированных данных, связанных с академическим и социальным бэкграундом учеников, которая бы содержала основу для формирования прогнозов относительно вероятности отчисления из школы.

При реализации проекта использован [датасет с Kaggle](https://www.kaggle.com/datasets/abdullah0a/student-dropout-analysis-and-prediction-dataset), содержащий данные социологических опросов. Датасет включает в себя демографическую информацию об учащихся, их академическую успеваемость, сведения о семье и внеклассной занятости. Помимо датасета были дополнительно сгенерированы данные, которые предлагают отсутствующую в изначальном варианте информацию об учителях и расширяют уже существующие характеристики школ и учебных курсов.

Репозиторий содержит следующие файлы:
- `students_create_db.py` - скрипт с DDL командами (создание базы данных и таблиц);
- `students_insert_to_db.py` - скрипт с DML командами (наполнение базы на основе исходных и синтезированных данных);
- `students.db` - файл с базой данных;
- `students_db_loader.ipynb` - ноутбук для отладки кода и применения DML команд (повторяет скрипт с DML командами);
- `students_db_sqlite_scheme.svg` - визуализация схемы БД.

База данных создана на основе SQLite.

Библиотеки, использованные в ходе работы над проектом: sqlite3, faker (синтез данных).

[Концептальная схема базы данных по студентам](https://drive.google.com/file/d/1up-pHYgRnpuUeZ46K-X7zxkanIEcnq3-/view?usp=sharing) 
