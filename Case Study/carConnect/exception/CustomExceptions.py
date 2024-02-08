import mysql.connector


class AuthenticationException(Exception):
    pass

# def login(username,password):
#     if username == "admin1" and password == "12345":
#         print("Logged in Successfully")
#     else:
#         raise AuthenticationException
# try:
#     login("aa", "dd")
#
# except AuthenticationException:
#     print("incorrect credential")


class ReservationException(Exception):
    pass
#
# def reserve(car):


class VehicleNotFoundException(Exception):
    pass

# def Vehicle(car):
#     cars = ['Honda','Toyota','Nissan','Ford','Chevrolet']
#     if car in cars:
#         print("Reserved")
#     else:
#         raise VehicleNotFoundException
#
# try:
#     Vehicle("Honda")
# except VehicleNotFoundException:
#     print("Sorry that is reserved")



class AdminNotFoundException(Exception):
   pass
#
# def admin(username):
#     admins = ["adminOne","adminTwo","adminThree","adminFour","adminFive"]
#     if username in admins:
#         print(f"Showing details of {username}")
#     else:
#         raise AdminNotFoundException
#
# try:
#     admin("adminOne")
# except AdminNotFoundException:
#     print("This admin doesn't exist")


class InvalidInputException(Exception):
    pass
#
# def inputEmail(email):
#     if "@" in email:
#         print(f"You have entered {email}")
#     else:
#         raise InvalidInputException
# try:
#     inputEmail("Akash.kumar@gmail.com")
# except InvalidInputException:
#     print("Email is invalid")


class DatabaseConnectionException(Exception):
    pass
# def databaseConnection():
#     conn = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="shree420",
#         database="carconnect"
#     )
#     if conn:
#             cursor = conn.cursor()
#             cursor.execute("show tables")
#             for i in cursor:
#                 print(i)
#     else:
#         raise DatabaseConnectionException
#
# try:
#     databaseConnection()
# except DatabaseConnectionException:
#     print("enable to connect")




