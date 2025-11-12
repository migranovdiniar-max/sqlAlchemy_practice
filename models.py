from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker, Mapped, mapped_column

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


class FollowingAssociation(BaseModel):
    __tablename__ = "following_association"

    user_2_id = Column(Integer, ForeignKey("user_2.id"))
    following_id = Column(Integer, ForeignKey("user_2.id"))


class User_2(BaseModel):
    __tablename__ = 'users_2'

    username = Column(String)

    following = relationship('User', secondary="following_association", 
                             primaryjoin=("FollowingAssociation.user_2.id==User_2.id"),
                             secondaryjoin=("FollowingAssociation.following_id==User_2.id"),
                             )

    def __repr__(self):
        return f"{self.id}, {self.username}"


Base.metadata.create_all(engine)