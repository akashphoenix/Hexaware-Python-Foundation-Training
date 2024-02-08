from util.DatabaseContext import DatabaseConnection

class ReportGenerator(DatabaseConnection):

    def __init__(self, host, user, password, database):
        super().__init__(host,user,password,database)

    def report(self,Rid,Vid):
        cursor = self.connection.cursor()
        cursor.execute("select * from reservation where ReservationID = %S", (Rid,))
        cursor.fetchall()
        for i in cursor:
            print(i)
        cursor.close()
        cursor = self.connection.cursor()
        cursor.execute("select * from vehicle where VehicleID = %s", (Vid,))
        cursor.fetchall()
        for i in cursor:
            print(i)
        cursor.close()

