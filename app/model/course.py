from ..ext.database import db

COURSE_DISCIPLINE = db.Table(
    "course_discipline",
    db.Column(
        "discipline_code",
        db.String(80),
        db.ForeignKey("discipline.discipline_code"),
        nullable=False,
        primary_key=True,
    ),
    db.Column(
        "id_course",
        db.Integer,
        db.ForeignKey("course.id_course"),
        nullable=False,
        primary_key=True,
    ),
)


class Course(db.Model):
    __tablename__ = "course"

    id_course = db.Column(db.Integer, nullable=False, primary_key=True)
    name = db.Column(db.String(255), nullable=False, unique=True)
    disciplines = db.relationship(
        "Discipline", secondary="course_discipline", lazy="dynamic"
    )
