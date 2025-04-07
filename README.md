# Тема 6. Домашня робота

Реалізуйте базу даних, схема якої містить:

- Таблиця студентів;
- Таблицю груп;
- Таблицю викладачів;
- Таблицю предметів із вказівкою викладача, який читає предмет;
- Таблицю, де у кожного студента є оцінки з предметів із зазначенням коли оцінку
  отримано;

В цій домашній роботі використаємо базу даних `postgres`. У командному рядку
запустіть `Docker` контейнер:

```bash
docker run --name some-postgres -p 5432:5432 -e POSTGRES_PASSWORD=mysecretpassword -d postgres
```

Замість `some-postgres` виберіть свою назву контейнера, а замість
`mysecretpassword` придумайте свій пароль для підключення до бази даних

## Технічний опис завдання

### Перший крок

Реалізуйте свої моделі **SQLAlchemy**, для таблиць:

- Таблиця студентів;
- Таблиця груп;
- Таблиця викладачів;
- Таблиця предметів із вказівкою викладача, який читає предмет;
- Таблиця де кожен студент має оцінки з предметів із зазначенням коли оцінку
  отримано;

### Другий крок

Використовуйте `alembic` для створення міграцій у базі даних.

### Третій крок

Напишіть скрипт `seed.py` та заповніть отриману базу даних випадковими даними
(~30-50 студентів, 3 групи, 5-8 предметів, 3-5 викладачів, до 20 оцінок у
кожного студента з усіх предметів). Використовуйте пакет `Faker` для наповнення.
При заповненні використовуємо механізм сесій **SQLAlchemy**.

### Четвертий крок

Зробити наступні вибірки з отриманої бази даних:

1. Знайти 5 студентів із найбільшим середнім балом з усіх предметів.
2. Знайти студента із найвищим середнім балом з певного предмета.
3. Знайти середній бал у групах з певного предмета.
4. Знайти середній бал на потоці (по всій таблиці оцінок).
5. Знайти які курси читає певний викладач.
6. Знайти список студентів у певній групі.
7. Знайти оцінки студентів у окремій групі з певного предмета.
8. Знайти середній бал, який ставить певний викладач зі своїх предметів.
9. Знайти список курсів, які відвідує певний студент.
10. Список курсів, які певному студенту читає певний викладач.

Для запитів оформити окремий файл `my_select.py`, де будуть `10` функцій від
`select_1` до `select_10`. При запитах використовуємо механізм сесій
**SQLAlchemy**.

## Додаткове завдання

Це додаткове завдання і його можна не виконувати для здачі цього домашнього
завдання.

### Перша частина

Для додаткового завдання зробіть такі запити підвищеної складності:

1. Середній бал, який певний викладач ставить певному студентові.
2. Оцінки студентів у певній групі з певного предмета на останньому занятті.

### Друга частина

Замість скрипту `seed.py` подумайте та реалізуйте повноцінну **CLI** програму
для **CRUD** операцій із базою даних. Використовуйте для цього модуль
`argparse`.

Використовуйте команду `--action` або скорочений варіант `-a` для **CRUD**
операцій. Та команду `--model` (`-m`) для вказівки над якою моделлю проводитися
операція.

Приклад:

- `-action create -m Teacher --name 'Boris Jonson'` створення вчителя
- `-action list -m Teacher` показати всіх вчителів
- `-action update -m Teacher --id 3 --name 'Andry Bezos'` оновити дані вчителя з
  `id=3`
- `-action remove -m Teacher --id 3` видалити вчителя з `id=3` Реалізуйте ці
  операції для кожної моделі.

### Приклади виконання команд у терміналі:

Створити вчителя

```bash
py main.py -a create -m Teacher -n 'Boris Jonson'
```

Створити групу

```bash
py main.py -a create -m Group -n 'AD-101'
```

## Підготовка та завантаження домашнього завдання

1. Створіть публічний репозиторій `goit-pythonweb-hw-06`.
2. Виконайте завдання та відправте його у свій репозиторій.
3. Завантажте робочі файли на свій комп’ютер та прикріпіть їх у LMS у форматі
   `zip`. Назва архіву повинна бути у форматі **ДЗ6_ПІБ**.
4. Прикріпіть посилання на репозиторій `goit-pythonweb-hw-06` та відправте на
   перевірку.

## Формат оцінювання

- Залік / Незалік

## Формат здачі

- Прикріплені файли репозиторію у форматі `zip` з назвою **ДЗ6_ПІБ**.
- Посилання на репозиторій.

> [!WARNING]
>
> 🚨 ВАЖЛИВО
>
> Перегляньте Інструкцію щодо завантаження робочого файлу з репозиторію на
> Github
> 
### Результат виконаного завдання

## 1️⃣ Create a Virtual Environment 

```bash
python -m venv venv
```

## 2️⃣ Activate the Virtual Environment  

**Windows (CMD):**  

```cmd
venv\Scripts\activate
```

## 3️⃣ Install Dependencies  

```bash
pip install -r requirements.txt
```

## 4️⃣ Running PostgreSQL via Docker

```bash
docker run --name hw-06 -p 5432:5432 -e POSTGRES_PASSWORD=password -d postgres
```

## 5️⃣ Creating an Alembic Migration

```bash
alembic revision --autogenerate -m "Initial migration"
```

## 6️⃣ Filling the database with data

```bash
python -m seeds.seed
```

## 7️⃣ Executing queries

```bash
python -m queries.my_select
```

---

## 📂 Структура проєкту

```
goit-pythonweb-hw-06-main/
├── db/
│   ├── db.py           # Підключення до бази через .env
│   └── models.py       # SQLAlchemy моделі
├── cli/
│   └── main.py         # CLI інтерфейс
├── queries/
│   └── my_select.py    # Вибірки з бази
├── seeds/
│   └── seed.py         # Наповнення тестовими даними
├── .env                # Налаштування підключення до БД
├── README.md           # Інструкція
├── requirements.txt    # Залежності
```

## 🧪 Приклади CLI команд

```bash
# 👨‍🏫 Teachers
python -m cli.main add_teacher -n "John Smith"
python -m cli.main list_teachers

# 👥 Groups
python -m cli.main add_group -n "Group A"
python -m cli.main list_groups

# 🧑‍🎓 Students
python -m cli.main add_student -n "Alice" --group_id 1
python -m cli.main list_students

# 📚 Subjects
python -m cli.main add_subject -n "Math" --teacher_id 1
python -m cli.main list_subjects

# 📝 Grades
python -m cli.main add_grade --student_id 1 --subject_id 1 --grade 5
python -m cli.main list_grades

## 🔐 .env формат

```
DATABASE_URL=postgresql://postgres:твій_пароль@localhost:5432/postgres
```
