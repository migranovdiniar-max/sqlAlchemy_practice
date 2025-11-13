from sqlalchemy import Table, Text, create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, Mapped, mapped_column
from datetime import datetime

db_url = "sqlite:///database.db"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    __allow_unmapped__ = True

    id = Column(Integer, primary_key=True)


class Address(BaseModel):
    __tablename__ = "addresses"

    city = Column(String)
    state = Column(String)
    zip_code = Column(Integer)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")

    def __repr__(self):
        return f"{self.id}, {self.city}"
    

class User(BaseModel):
    __tablename__ = 'users'

    name = Column(String)
    age = Column(Integer)
    addresses: Mapped[list["Address"]] = relationship()


# --------------------------------------------------------------------------------------------------------------------
# class FollowingAssociation(BaseModel):
#     __tablename__ = "following_association"

#     user_2_id = Column(Integer, ForeignKey("user_2.id"))
#     following_id = Column(Integer, ForeignKey("user_2.id"))


# class User_2(BaseModel):
#     __tablename__ = 'users_2'

#     username = Column(String)

#     following = relationship('User', secondary="following_association", 
#                              primaryjoin=("FollowingAssociation.user_2.id==User_2.id"),
#                              secondaryjoin=("FollowingAssociation.following_id==User_2.id"),
#                              )

#     def __repr__(self):
#         return f"{self.id}, {self.username}"
# --------------------------------------------------------------------------------------------------------------------

class User_3(BaseModel):
    __tablename__ = "users_3"

    name = Column(String)
    address = relationship("Address_2", back_populates="user", uselist=False)


class Address_2(BaseModel):
    __tablename__ = "addresses_2"

    email = Column(String, unique=True)
    user_id = Column(Integer, ForeignKey("users_3.id"))
    user = relationship("User_3", back_populates="address")


class NodeAssociation(BaseModel):
    __tablename__ = 'node_association'

    current_node_id = Column(Integer, ForeignKey('nodes.id'))
    next_node_id = Column(Integer, ForeignKey("nodes.id"))

class Node(BaseModel):
    __tablename__ = 'nodes'

    value = Column(Integer, nullable=False)
    node_id = Column(Integer, ForeignKey("nodes.id"))
    next_node = relationship(
        "Node",
        secondary='node_association',
        primaryjoin="NodeAssociation.current_node_id==Node.id",
        secondaryjoin="NodeAssociation.next_node_id==Node.id",
        uselist=False,
    )

    def __repr__(self):
        return f"{self.value}, {self.next_node}"


class Student(BaseModel):
    __tablename__ = 'students'

    name = Column(String)
    courses = relationship("Course", secondary="student_course", back_populates="students")


#Association Table
# student_course_link = Table("stundent_course", Base.metadata, 
#                             Column("student_id", Integer, ForeignKey("students_id")),
#                             Column("course_id", Integer, ForeignKey("courses.id")))
class StundentCourse(BaseModel):
    __tablename__ = 'student_course'

    student_id = Column('student_id', Integer, ForeignKey('students.id'))
    course_id = Column("course_id", Integer, ForeignKey("courses.id"))


class Course(BaseModel):
    __tablename__ = 'courses'

    title = Column(String)
    students = relationship("Student", secondary="student_course", back_populates="courses")


class Appointment(BaseModel):
    __tablename__ = 'appointments'

    doctor_id = Column(Integer, ForeignKey('doctors.id'))
    patient_id = Column(Integer, ForeignKey("patients.id"))
    appointment_date = Column(DateTime, default=datetime.utcnow)
    notes = Column(String)

    doctor = relationship("Doctor", backref="appointments")
    patient = relationship("Patient", backref="appointments")


class Doctor(BaseModel):
    __tablename__ = 'doctors'

    name = Column(String)
    specialty = Column(String)


class Patient(BaseModel):
    __tablename__ = "patients"

    name = Column(String)
    dob = Column(DateTime)


class User_4(BaseModel):
    __tablename__ = 'users_4'

    name = Column(String)
    posts = relationship("Post", lazy="select", backref="user_4")

    def __repr__(self):
        return f"{self.name}"
    

class Post(BaseModel):
    __tablename__ = "posts"

    content = Column(Text)
    user_id = Column(Integer, ForeignKey("users_4.id"))

    def __repr__(self):
        return f"{self.id}"
    

Base.metadata.create_all(engine)