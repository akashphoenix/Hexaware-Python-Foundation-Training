from iAdminService import IAdminService
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

class AdminService(IAdminService,SqlCommand):
    def __init__(self,host,user,password,database):
        super().__init__(host,user,password,database)

    def GetAdminById(self,Aid):
        cursor = self.connection.cursor()
        cursor.execute("select * from Admin where adminid = %s",(Aid,))
        for i in cursor:
            print(i)
        cursor.close()

    def GetAdminByUsername(self,username):
        cursor = self.connection.cursor()
        cursor.execute("select * from Admin where username = %s", (username,))
        for i in cursor:
            print(i)
        cursor.close()


    def RegisterAdmin(self):
        cursor = self.connection.cursor()
        FirstName = input("Enter first name ")
        LastName = input("Enter last name ")
        Email = input("Enter Email ")
        PhoneNumber = int(input("Enter phonenumber "))
        Username = input("Enter username ")
        Password = input("Enter Password ")
        Role = input("Enter Role ")
        JoinDate = input("Enter joinDate ")
        cursor.execute("insert into admin(FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate)"
                       " values(%s,%s,%s,%s,%s,%s,%s,%s)",
                       (FirstName, LastName, Email, PhoneNumber, Username, Password, Role, JoinDate))
        self.connection.commit()
        cursor.close()


    def UpdateAdmin(self,Aid):
        cursor = self.connection.cursor()
        cursor.execute("update admin set role = 'SuperAdmin' where adminid = %s", (Aid,))
        self.connection.commit()
        cursor.close()

    def DeleteAdmin(self,Aid):
        cursor = self.connection.cursor()
        cursor.execute("delete from admin where adminid = %s", (Aid,))
        self.connection.commit()
        cursor.close()

if __name__ == "__main__":
    a = AdminService("localhost","root","shree420","carconnect")
    a.connect()
    # a.GetAdminById(12)
    # a.GetAdminByUsername("admin1")
    # a.RegisterAdmin()
    # a.UpdateAdmin(22)
    # a.DeleteAdmin(21)

