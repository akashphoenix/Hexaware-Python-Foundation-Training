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

    def executeQuery(self,query,value):
        cursor = self.connection.cursor()
        cursor.execute(query,value)
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

if __name__ == "__main__" :

    a = SqlCommand("localhost","root","shree420","carconnect")
    a.connect()
    # a.updateCustomer("update courses set coursename = %s where courseid = %s",("Economy",103))
    # a.addingRow("insert into courses(courseid,coursename,credits) values (%s,%s,%s)",(108,"thermodynamics",5))
    # a.getVehicle()
    # a.executeQuery("select username,password from customer where customerid = 1")
    a.disconnect()
