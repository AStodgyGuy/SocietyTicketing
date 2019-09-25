import getpass
import mysql.connector as mariadb

class DBHandler:

    NAME_MAX_CHAR = 20
    EMAIL_MAX_CHAR = 15
    ID_MAX_CHAR = 10

    def __init__(self):
        print("Welcome to the SMIG app v0.2")
        self.connect_db()
        self.create_tables()

    def connect_db(self):
        self.mariadb_connection = mariadb.connect(user='smig', password="jommakan_55", database='smig_1920')
        self.cursor = self.mariadb_connection.cursor()
        print("Connect success")

    def get_password(self):
        try:
            p = getpass.getpass()
        except Exception as error: 
            print('ERROR', error) 
        return p

    def create_tables(self):
        # create the tables that matter
        table_person = f"CREATE TABLE IF NOT EXISTS smig_person (first_name VARCHAR({self.NAME_MAX_CHAR}), last_name VARCHAR({self.NAME_MAX_CHAR}), email VARCHAR({self.EMAIL_MAX_CHAR}) PRIMARY KEY NOT NULL)"
        table_membership = f"CREATE TABLE IF NOT EXISTS smig_membership (person_email VARCHAR({self.EMAIL_MAX_CHAR}) PRIMARY KEY NOT NULL, hasPaid BOOLEAN, CONSTRAINT FOREIGN KEY (person_email) REFERENCES smig_person (email))"
        table_ID = f"CREATE TABLE IF NOT EXISTS smig_ID (person_email VARCHAR({self.EMAIL_MAX_CHAR}) PRIMARY KEY NOT NULL, `type` BOOLEAN, `number` VARCHAR({self.ID_MAX_CHAR}), CONSTRAINT FOREIGN KEY (person_email) REFERENCES smig_person (email))"
        self.query(table_person)
        self.query(table_membership)
        self.query(table_ID)

    def query(self, statement):
        try:
            self.mariadb_connection.cursor().execute(statement)
        except Exception as e:
            print(e)
            return None

    # create tables

    # populate tables

    # convert to CSV

    # get values from tables

DBHandler()