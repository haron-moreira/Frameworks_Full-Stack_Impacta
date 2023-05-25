import mysql.connector

class Connection:

    def __init__(self) :
        self.host = 'localhost'
        self.user = 'root'
        self.password = 'root'
        self.database = 'cadastro'


    def open_connection(self):
        conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
        )
        return conn