import mysql.connector

class DatabaseConnection:
    def __init__(self,host,user,password,database):
        self.host = host
        self.user = user
        self.password= password
        self.database = database
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host = self.host,
                user = self.user,
                password = self.password,
                database = self.database
            )
            print(f"Connected to {self.database} database")
        except:
            print("Error connecting to database")

    def executeQuery(self,query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        for i in result:
            print(i)

    def disconnect(self):
        try:
            if self.connection:
                self.connection.close()
            print("Disconnected")
        except:
            print("Error disconnecting")


if __name__ == "__main__":
    b = DatabaseConnection("localhost","root","shree420","baklol")
    b.connect()
    b.disconnect()