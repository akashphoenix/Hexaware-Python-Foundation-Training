from iReservationService import IReservationService
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

class ReservationService(IReservationService,SqlCommand):

    def GetReservationById(self):
        Rid = int(input("Enter ReservationID "))
        cursor = self.connection.cursor()
        cursor.execute("select * from reservation where reservationid = %s", (Rid,))
        for i in cursor:
            print(i)
        cursor.close()

    def GetReservationsByCustomerId(self,Cid):
        cursor = self.connection.cursor()
        cursor.execute("select * from reservation where customerid = %s", (Cid,))
        for i in cursor:
            print(i)
        cursor.close()


    def CreateReservation(self):
        cursor = self.connection.cursor()
        CustomerID = input("Enter Customerid ")
        VehicleID = input("Enter Vehicleid ")
        StartDate = input("Enter StartDate ")
        EndDate = input("Enter EndDate ")
        TotalCost = int(input("Enter Totalcost "))
        Status = input("Enter Status ")

        cursor.execute("insert into reservation(CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status)"
                       " values(%s,%s,%s,%s,%s,%s)",
                       (CustomerID, VehicleID, StartDate, EndDate, TotalCost, Status))
        self.connection.commit()
        cursor.close()


    def UpdateReservation(self):
        Rid = int(input("Enter ReservationID "))
        cursor = self.connection.cursor()
        cursor.execute("update reservation set totalcost = 100 where reservationid = %s", (Rid,))
        self.connection.commit()
        cursor.close()


    def CancelReservation(self):
        Rid = int(input("Enter ReservationID "))
        cursor = self.connection.cursor()
        cursor.execute("delete from reservation where reservationid = %s", (Rid,))
        self.connection.commit()
        cursor.close()
