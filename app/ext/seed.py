import json
import os
from .database import db
from ..model import course, discipline, professor
from sqlalchemy.exc import IntegrityError, InvalidRequestError


def seed():
    exit_code = 0
    exit_code += seed_courses()
    exit_code += seed_disciplines()
    exit_code += seed_course_discipline()
    exit_code += seed_professor()
    exit_code += seed_professor_discipline()
    return 1 if exit_code > 0 else 0


def seed_courses():
    print("\nSeeding database with courses...")
    courses = read_json("courses")
    return add_seeds(courses, lambda c: course.Course(name=c.get("name")))


def seed_disciplines():
    print("\nSeeding database with disciplines...")
    disciplines = read_json("disciplines")
    return add_seeds(
        disciplines,
        lambda d: discipline.Discipline(
            discipline_code=d.get("discipline_code"), name=d.get("name")
        ),
    )


def seed_course_discipline():
    print("\nSeeding database with course_discipline...")
    course_discipline = read_json("course_discipline")
    return add_seeds(
        course_discipline,
        lambda cd: course.CourseDiscipline(
            discipline_code=cd.get("discipline_code"), id_course=cd.get("id_course")
        ),
    )


def seed_professor():
    print("\nSeeding database with professor...")
    professors = read_json("professor")
    return add_seeds(professors, lambda p: professor.Professor(name=p.get("name")))


def seed_professor_discipline():
    print("\nSeeding database with professor_discipline...")
    professor_discipline = read_json("professor_discipline")
    return add_seeds(
        professor_discipline,
        lambda pd: discipline.ProfessorDiscipline(
            discipline_code=pd.get("discipline_code"),
            id_professor=pd.get("id_professor"),
        ),
    )


def add_seeds(obj_list, modelFactory):
    try:
        for obj in obj_list:
            db.session.add(modelFactory(obj))
        db.session.commit()
        print(f"{len(obj_list)} seeds successfully added!\n\n")
        return 0
    except (IntegrityError, InvalidRequestError):
        print("Objs already in database! Cant seed!\n\n")
        return 1


def read_json(name):
    file = open(absolute_path(name), "r")
    data = json.loads(file.read())
    file.close()
    return data


def absolute_path(json_name):
    this_path = os.path.dirname(__file__)
    file_path = f"static/{json_name}.json"
    return os.path.join(this_path, file_path)
