from db.db import session
import argparse
from db.models import Base, Teacher, Group, Student, Subject, Grade


def create_teacher(name):
    teacher = Teacher(name=name)
    session.add(teacher)
    session.commit()
    print(f"✅ Created Teacher: {teacher.id} — {teacher.name}")


def list_teachers():
    teachers = session.query(Teacher).all()
    for t in teachers:
        print(f"{t.id}: {t.name}")


def create_group(name):
    group = Group(name=name)
    session.add(group)
    session.commit()
    print(f"✅ Created Group: {group.id} — {group.name}")


def list_groups():
    groups = session.query(Group).all()
    for g in groups:
        print(f"{g.id}: {g.name}")


def create_student(name, group_id):
    student = Student(name=name, group_id=group_id)
    session.add(student)
    session.commit()
    print(f"✅ Created Student: {student.id} — {student.name} (Group {student.group_id})")


def list_students():
    students = session.query(Student).all()
    for s in students:
        print(f"{s.id}: {s.name} (Group {s.group_id})")


def create_subject(name, teacher_id):
    subject = Subject(name=name, teacher_id=teacher_id)
    session.add(subject)
    session.commit()
    print(f"✅ Created Subject: {subject.id} — {subject.name} (Teacher {subject.teacher_id})")


def list_subjects():
    subjects = session.query(Subject).all()
    for s in subjects:
        print(f"{s.id}: {s.name} (Teacher {s.teacher_id})")


def create_grade(student_id, subject_id, grade):
    new_grade = Grade(student_id=student_id, subject_id=subject_id, grade=grade)
    session.add(new_grade)
    session.commit()
    print(f"✅ Added Grade: Student {student_id}, Subject {subject_id}, Grade {grade}")


def list_grades():
    grades = session.query(Grade).all()
    for g in grades:
        print(f"Student {g.student_id}, Subject {g.subject_id}, Grade {g.grade}")


def main():
    parser = argparse.ArgumentParser(description="🎓 CLI for School Database")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list_teachers")
    parser_add_teacher = subparsers.add_parser("add_teacher")
    parser_add_teacher.add_argument("-n", "--name", required=True)

    subparsers.add_parser("list_groups")
    parser_add_group = subparsers.add_parser("add_group")
    parser_add_group.add_argument("-n", "--name", required=True)

    subparsers.add_parser("list_students")
    parser_add_student = subparsers.add_parser("add_student")
    parser_add_student.add_argument("-n", "--name", required=True)
    parser_add_student.add_argument("--group_id", type=int, required=True)

    subparsers.add_parser("list_subjects")
    parser_add_subject = subparsers.add_parser("add_subject")
    parser_add_subject.add_argument("-n", "--name", required=True)
    parser_add_subject.add_argument("--teacher_id", type=int, required=True)

    subparsers.add_parser("list_grades")
    parser_add_grade = subparsers.add_parser("add_grade")
    parser_add_grade.add_argument("--student_id", type=int, required=True)
    parser_add_grade.add_argument("--subject_id", type=int, required=True)
    parser_add_grade.add_argument("--grade", type=int, required=True)

    args = parser.parse_args()

    match args.command:
        case "add_teacher":
            create_teacher(args.name)
        case "list_teachers":
            list_teachers()
        case "add_group":
            create_group(args.name)
        case "list_groups":
            list_groups()
        case "add_student":
            create_student(args.name, args.group_id)
        case "list_students":
            list_students()
        case "add_subject":
            create_subject(args.name, args.teacher_id)
        case "list_subjects":
            list_subjects()
        case "add_grade":
            create_grade(args.student_id, args.subject_id, args.grade)
        case "list_grades":
            list_grades()
        case _:
            print("❌ Unknown command")


if __name__ == "__main__":
    main()
