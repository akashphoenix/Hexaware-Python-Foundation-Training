from iVehicleService import IVehicleService
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

class VehicleService(IVehicleService,SqlCommand):
    def __init__(self,host,user,password,database):
        super().__init__(host,user,password,database)

    def GetVehicleById(self):
        Vid = int(input("Enter VehicleID "))
        cursor = self.connection.cursor()
        cursor.execute("select * from vehicle where vehicleid = %s", (Vid,))
        for i in cursor:
            print(i)
        cursor.close()


    def GetAvailableVehicles(self):
        cursor = self.connection.cursor()
        cursor.execute("select * from vehicle where Availability = 1")
        for i in cursor:
            print(i)
        cursor.close()

    def AddVehicle(self):
        cursor = self.connection.cursor()
        Model = input("Enter Model ")
        Make = input("Enter Make ")
        Year = input("Enter Year ")
        Color = input("Enter Color ")
        RegistrationNumber = input("Enter RegistrationNumber ")
        Availability = input("Enter Availability(1/0) ")
        DailyRate = input("Enter DailyRate ")

        cursor.execute("insert into vehicle (Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate)"
                       " values(%s,%s,%s,%s,%s,%s,%s)",
                       (Model, Make, Year, Color, RegistrationNumber, Availability, DailyRate))
        self.connection.commit()
        cursor.close()


    def UpdateVehicle(self):
        Vid = int(input("Enter VehicleID "))
        cursor = self.connection.cursor()
        cursor.execute("update vehicle set Availability = 1 where vehicleid = %s", (Vid,))
        self.connection.commit()
        cursor.close()


    def RemoveVehicle(self):
        Vid = int(input("Enter VehicleID "))
        cursor = self.connection.cursor()
        cursor.execute("delete from vehicle where vehicleid = %s", (Vid,))
        self.connection.commit()
        cursor.close()


# a = VehicleService("localhost","root","shree420","carconnect")
# a.connect()
# a.GetAvailableVehicles()