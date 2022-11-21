import sqlite3

def get_connection():
    connection = sqlite3.connect('teatchers.db')
    return connection

def close_connection(connection):
    if connection:
        connection.close()

def create_table():
  try:
    connection = get_connection()
    cursor = connection.cursor()
    create_query = """CREATE TABLE Students
    (
    Student_Id INTEGER NOT NULL PRIMARY KEY,
    Student_Name TEXT NOT NULL,
    School_Id INTEGER NOT NULL
    );
    """
    cursor.execute(create_query)
    connection.commit()
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в создании таблицы ", error)

def insert_students():
  try:
    connection = get_connection()
    cursor = connection.cursor()
    insert_query = """INSERT INTO Students (Student_Id, Student_Name, School_Id)
    VALUES
    ('201', 'Иван', '1'),
    ('202', 'Петр', '2'),
    ('203', 'Анастасия', '3'),
    ('204', 'Игорь', '4');
    """
    cursor.execute(insert_query)
    connection.commit()
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в наполнении базы ", error)

def get_student_detail(Student_Id):
  try:
    connection = get_connection()
    cursor = connection.cursor()
    join_query = """SELECT * FROM Students JOIN School ON Students.School_Id=School.School_Id 
    WHERE Student_Id = ?;"""
    cursor.execute(join_query,(Student_Id,))
    records = cursor.fetchall()
    print ("Информация о студенте с названием школы по ID студента")
    for row in records:
        print ("ID студента：", row[0])
        print ("Имя студента：", row[1])
        print ("ID школы：", row[2])
        print ("Название школы：", row[4])
    close_connection(connection)
  except (Exception, sqlite3.Error) as error:
    print ("Ошибка в итоговом выводе", error)

# create_table()
# insert_students()
get_student_detail(202)