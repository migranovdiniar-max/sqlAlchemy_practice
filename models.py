from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

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
    user_id = Column(ForeignKey("users.id"))
    user = relationship("User", back_populates="addresses")

    def __repr__(self):
        return f"{self.id}, {self.city}"
    

class User(BaseModel):
    __tablename__ = 'users'

    name = Column(String)
    age = Column(Integer)
    addresses = relationship(Address)


Base.metadata.create_all(engine)