from iCustomerService import ICustomerService
import mysql.connector
from util.sqlconnection import SqlConnection

class SqlCommand(SqlConnection):
    def __init__(self,host,user,password,database):
        super().__init__(host,user,password,database)

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
             )
            print("connected")
        except:
            print("could not connect to database")

    def executeQuery(self,query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        for i in cursor:
            print(i)
        cursor.close()

    def updateCustomer(self,query,value):
        cursor = self.connection.cursor()
        cursor.execute(query,value)
        self.connection.commit()
        cursor.close()

    def addingRow(self,query,value):
         cursor = self.connection.cursor()
         cursor.execute(query,value)
         self.connection.commit()
         cursor.close()

    def updateVehicle(self,query,value):
        cursor = self.connection.cursor()
        cursor.execute(query,value)
        self.connection.commit()
        cursor.close()

    def getAvailableVehicle(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from courses where courseid = 103")
        for i in cursor:
            print(i)
        cursor.close()

    def getVehicle(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from courses")
        for i in cursor:
            print(i)
        cursor.close()

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Disconnected")



class CustomerService(ICustomerService,SqlCommand):
    def __init__(self,host,user,password,database):
        super().__init__(host,user,password,database)

    def GetCustomerById(self):
        Cid = int(input("Enter CustomerID "))
        cursor = self.connection.cursor()
        cursor.execute("select * from customer where customerid = %s", (Cid,))
        for i in cursor:
            print(i)
        cursor.close()

    def GetCustomerByUsername(self,username):
        cursor = self.connection.cursor()
        cursor.execute("select * from customer where username = %s", (username,))
        for i in cursor:
            print(i)
        cursor.close()

    def RegisterCustomer(self):
        cursor = self.connection.cursor()
        FirstName = input("Enter first name ")
        LastName = input("Enter last name ")
        Email = input("Enter Email ")
        PhoneNumber = int(input("Enter phonenumber "))
        Username = input("Enter username ")
        Password = input("Enter Password ")
        RegistrationDate = input("Enter registrationDate ")

        cursor.execute("insert into customer(FirstName, LastName, Email, PhoneNumber, Username, Password,RegistrationDate)"
                       " values(%s,%s,%s,%s,%s,%s,%s)",
                       (FirstName, LastName, Email, PhoneNumber, Username, Password,RegistrationDate))
        self.connection.commit()
        cursor.close()

    def UpdateCustomer(self):
        Cid = int(input("Enter CustomerID "))
        cursor = self.connection.cursor()
        cursor.execute("update customer set phonenumber = '1234567893' where customerid = %s", (Cid,))
        self.connection.commit()
        cursor.close()

    def DeleteCustomer(self):
        Cid = int(input("Enter CustomerID "))
        cursor = self.connection.cursor()
        cursor.execute("delete from customer where customerid = %s", (Cid,))
        self.connection.commit()
        cursor.close()


if __name__ == "__main__":
    a = CustomerService("localhost","root","shree420","carconnect")
    a.connect()
    a.GetCustomerById(1)