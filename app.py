from sqlalchemy.orm import sessionmaker, Mapped, mapped_column
from models import Student, User_3, engine, Address_2, Node, Course
import random
from sqlalchemy import or_, and_, not_, func

Session = sessionmaker(bind=engine)
session = Session()

# --------------------------------------------------------------------------------------------------------------------
# user1 = User(name='John Doe', age=52)
# user2 = User(name='Jane Smith', age=34)

# # Creating addresses
# address1 = Address(
#     city='New York', state='NY', zip_code='10001'
# )
# address2 = Address(
#     city='Los Angeles', state='CA', zip_code='90001'
# )
# address3 = Address(
#     city='Chicago', state='IL', zip_code='60601'
# )

# user1.addresses.extend([address1, address2])
# user2.addresses.append(address3)

# session.add(user1)
# session.add(user2)
# session.commit()

# print(user1.addresses)
# print(user2.addresses)
# print(f"{address1.user = }")
# --------------------------------------------------------------------------------------------------------------------



# users = session.query(User.age, func.count(User.id)).group_by(User.age).all()

# users = session.query(User).filter(User.age > 24).filter(User.age < 50).all()

# users_tuple = (
#     session.query(User.age, User.name, func.count(User.id))
#     .filter(User.age > 24)
#     .order_by(User.age)
#     .filter(User.age < 50)
#     .group_by(User.age)
#     .all()
# )

# for user in users_tuple:
#     print(user)

# only_iron_man = False
# group_by_age = True

# users = session.query(User)

# if only_iron_man:
#     users = users.filter(User.name == "Iron man")

# if group_by_age:
#     users = users.group_by(User.age)

# users = users.all()

# for user in users:
#     print(user.age, user.name)
# --------------------------------------------------------------------------------------------------------------------


# new_user = User_3(name='John Doe')
# new_address = Address_2(email='johndoe@gmail.com', user=new_user)
# session.add(new_user)
# session.add(new_address)

# session.commit()
# --------------------------------------------------------------------


# node1 = Node(value=1)
# node2 = Node(value=2)
# node3 = Node(value=3)

# node1.next_node = node2
# node2.next_node = node3
# node3.next_node = node1

# session.add_all([node1, node2, node3])
# session.commit()

# print(node1)
# print(node2)
# print(node3)
# --------------------------------------------------------------------------------------------

# maths = Course(title="Maths")
# physics = Course(title="Physics")
# bill = Student(name="Bill", courses=[maths, physics])
# rob = Student(name="Rob", courses=[maths])

# session.add_all([maths, physics, bill, rob])
# session.commit()
# --------------------------------------------------------------------------------------------


# rob = session.query(Student).filter_by(name='Rob').first()
# courses = [Course.title for Course in rob.courses]
# print(courses)
# --------------------------------------------------------------------------------------------
