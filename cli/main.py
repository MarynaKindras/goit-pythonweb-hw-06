from db.db import session
import argparse
from models import Base, Teacher, Group, Student, Subject



def create_teacher(name):
    teacher = Teacher(name=name)
    session.add(teacher)
    session.commit()
    print(f"✅ Created Teacher: {teacher.id} — {teacher.name}")


def list_teachers():
    teachers = session.query(Teacher).all()
    for t in teachers:
        print(f"{t.id}: {t.name}")


def update_teacher(id, name):
    teacher = session.query(Teacher).get(id)
    if teacher:
        teacher.name = name
        session.commit()
        print(f"✏️ Updated Teacher {id} to '{name}'")
    else:
        print("⚠️ Teacher not found")


def remove_teacher(id):
    teacher = session.query(Teacher).get(id)
    if teacher:
        session.delete(teacher)
        session.commit()
        print(f"🗑 Removed Teacher {id}")
    else:
        print("⚠️ Teacher not found")


def create_group(name):
    group = Group(name=name)
    session.add(group)
    session.commit()
    print(f"✅ Created Group: {group.id} — {group.name}")


def list_groups():
    groups = session.query(Group).all()
    for g in groups:
        print(f"{g.id}: {g.name}")


def update_group(id, name):
    group = session.query(Group).get(id)
    if group:
        group.name = name
        session.commit()
        print(f"✏️ Updated Group {id} to '{name}'")
    else:
        print("⚠️ Group not found")


def remove_group(id):
    group = session.query(Group).get(id)
    if group:
        session.delete(group)
        session.commit()
        print(f"🗑 Removed Group {id}")
    else:
        print("⚠️ Group not found")


def main():
    parser = argparse.ArgumentParser(description="📚 University Database CLI")
    parser.add_argument("-a", "--action", choices=[
                        "create", "list", "update", "remove"], required=True, help="CRUD action")
    parser.add_argument(
        "-m", "--model", choices=["Teacher", "Group"], required=True, help="Model to act on")

    parser.add_argument("--id", type=int, help="ID for update or delete")
    parser.add_argument("-n", "--name", help="Name for create/update")

    args = parser.parse_args()

    if args.model == "Teacher":
        if args.action == "create":
            create_teacher(args.name)
        elif args.action == "list":
            list_teachers()
        elif args.action == "update":
            update_teacher(args.id, args.name)
        elif args.action == "remove":
            remove_teacher(args.id)

    elif args.model == "Group":
        if args.action == "create":
            create_group(args.name)
        elif args.action == "list":
            list_groups()
        elif args.action == "update":
            update_group(args.id, args.name)
        elif args.action == "remove":
            remove_group(args.id)


if __name__ == "__main__":
    main()

def create_student(name, group_id):
    student = Student(name=name, group_id=group_id)
    session.add(student)
    session.commit()

def list_students():
    return session.query(Student).all()

def create_subject(name, teacher_id):
    subject = Subject(name=name, teacher_id=teacher_id)
    session.add(subject)
    session.commit()

def list_subjects():
    return session.query(Subject).all()

def create_grade(student_id, subject_id, grade):
    new_grade = Grade(student_id=student_id, subject_id=subject_id, grade=grade)
    session.add(new_grade)
    session.commit()

def list_grades():
    return session.query(Grade).all()


def main():
    parser = argparse.ArgumentParser(description="CLI for School Database")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("list_teachers")
    parser_add_teacher = subparsers.add_parser("add_teacher")
    parser_add_teacher.add_argument("name")

    subparsers.add_parser("list_groups")
    parser_add_group = subparsers.add_parser("add_group")
    parser_add_group.add_argument("name")

    subparsers.add_parser("list_students")
    parser_add_student = subparsers.add_parser("add_student")
    parser_add_student.add_argument("name")
    parser_add_student.add_argument("group_id", type=int)

    subparsers.add_parser("list_subjects")
    parser_add_subject = subparsers.add_parser("add_subject")
    parser_add_subject.add_argument("name")
    parser_add_subject.add_argument("teacher_id", type=int)

    subparsers.add_parser("list_grades")
    parser_add_grade = subparsers.add_parser("add_grade")
    parser_add_grade.add_argument("student_id", type=int)
    parser_add_grade.add_argument("subject_id", type=int)
    parser_add_grade.add_argument("grade", type=int)

    args = parser.parse_args()

    if args.command == "add_teacher":
        create_teacher(args.name)
    elif args.command == "list_teachers":
        for t in session.query(Teacher).all():
            print(t.name)
    elif args.command == "add_group":
        create_group(args.name)
    elif args.command == "list_groups":
        for g in session.query(Group).all():
            print(g.name)
    elif args.command == "add_student":
        create_student(args.name, args.group_id)
    elif args.command == "list_students":
        for s in list_students():
            print(f"{s.name} (Group {s.group_id})")
    elif args.command == "add_subject":
        create_subject(args.name, args.teacher_id)
    elif args.command == "list_subjects":
        for s in list_subjects():
            print(f"{s.name} (Teacher {s.teacher_id})")
    elif args.command == "add_grade":
        create_grade(args.student_id, args.subject_id, args.grade)
    elif args.command == "list_grades":
        for g in list_grades():
            print(f"Student {g.student_id}, Subject {g.subject_id}, Grade {g.grade}")

if __name__ == "__main__":
    main()
