import sqlite3


conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()


cursor.execute('''CREATE TABLE IF NOT EXISTS countries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL
                )''')

# Добавление записей в таблицу countries
countries_data = [
    ('USA',),
    ('UK',),
    ('France',)
]
cursor.executemany("INSERT INTO countries (title) VALUES (?)", countries_data)

# Создание таблицы cities
cursor.execute('''CREATE TABLE IF NOT EXISTS cities (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    area REAL DEFAULT 0,
                    country_id INTEGER,
                    FOREIGN KEY (country_id) REFERENCES countries(id)
                )''')

# Добавление записей в таблицу cities
cities_data = [
    ('New York', 468.9, 1),
    ('London', 1572, 2),
    ('Paris', 105.4, 3),
    ('Los Angeles', 1302, 1),
    ('Manchester', 115.6, 2),
    ('Lyon', 47.9, 3),
    ('San Francisco', 600.6, 1)
]
cursor.executemany("INSERT INTO cities (title, area, country_id) VALUES (?, ?, ?)", cities_data)

# Создание таблицы students
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    last_name TEXT NOT NULL,
                    city_id INTEGER,
                    FOREIGN KEY (city_id) REFERENCES cities(id)
                )''')

# Добавление записей в таблицу students
students_data = [
    ('John', 'Doe', 1),
    ('Jane', 'Smith', 2),
    ('Alice', 'Johnson', 3),
    ('Bob', 'Brown', 4),
    ('Emma', 'Davis', 5),
    ('Michael', 'Wilson', 6),
    ('Olivia', 'Martinez', 7),
    ('William', 'Anderson', 1),
    ('Sophia', 'Taylor', 2),
    ('James', 'Lee', 3),
    ('Emily', 'Jackson', 4),
    ('Alexander', 'Harris', 5),
    ('Charlotte', 'White', 6),
    ('Daniel', 'Clark', 7),
    ('Ava', 'Thomas', 1)
]
cursor.executemany("INSERT INTO students (first_name, last_name, city_id) VALUES (?, ?, ?)", students_data)

conn.commit()
conn.close()

def display_students_by_city(city_id):
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    cursor.execute('''SELECT students.first_name, students.last_name, countries.title, cities.title, cities.area
                      FROM students
                      INNER JOIN cities ON students.city_id = cities.id
                      INNER JOIN countries ON cities.country_id = countries.id
                      WHERE cities.id = ?''', (city_id,))
    students = cursor.fetchall()

    if students:
        print("Имя\tФамилия\tСтрана\tГород проживания\tПлощадь города")
        for student in students:
            print("\t".join(map(str, student)))
    else:
        print("Нет учеников в выбранном городе.")

    conn.close()

def main():
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()

    cursor.execute("SELECT id, title FROM cities")
    cities = cursor.fetchall()

    print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")
    for city in cities:
        print(f"{city[0]}: {city[1]}")

    city_id = int(input("Введите id города: "))
    if city_id == 0:
        print("Выход из программы.")
    elif city_id not in [city[0] for city in cities]:
        print("Некорректный id города.")
    else:
        display_students_by_city(city_id)

if __name__ == "__main__":
    main()
