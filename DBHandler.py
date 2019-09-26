import getpass
import datetime
import mysql.connector as mariadb
from smig_person import Person

class DBHandler:

    NAME_MAX_CHAR = 20
    EMAIL_MAX_CHAR = 15
    ID_MAX_CHAR = 10
    EVENT_MAX_CHAR = 50

    def __init__(self):
        print("Welcome to the SMIG app v0.2")
        self.connect_db()
        self.create_tables()

    def connect_db(self):
        try:
            self.mariadb_connection = mariadb.connect(user='smig', password="jommakan_55", database='smig_1920')
            self.cursor = self.mariadb_connection.cursor()
            print("Connect success")
        except Exception as e:
            print(e)
            return None

    def get_password(self):
        try:
            p = getpass.getpass()
        except Exception as error: 
            print('ERROR', error) 
        return p

    def create_tables(self):
        # create the tables that matter
        table_person = f"CREATE TABLE IF NOT EXISTS smig_person (first_name VARCHAR({self.NAME_MAX_CHAR}), last_name VARCHAR({self.NAME_MAX_CHAR}), email VARCHAR({self.EMAIL_MAX_CHAR}) PRIMARY KEY NOT NULL, `year` VARCHAR({self.NAME_MAX_CHAR}), course VARCHAR({self.EVENT_MAX_CHAR}))"
        table_membership = f"CREATE TABLE IF NOT EXISTS smig_membership (person_email VARCHAR({self.EMAIL_MAX_CHAR}) PRIMARY KEY NOT NULL, hasPaid BOOLEAN, CONSTRAINT FOREIGN KEY (person_email) REFERENCES smig_person (email))"
        table_ID = f"CREATE TABLE IF NOT EXISTS smig_ID (person_email VARCHAR({self.EMAIL_MAX_CHAR}) PRIMARY KEY NOT NULL, `type` BOOLEAN, `number` VARCHAR({self.ID_MAX_CHAR}), CONSTRAINT FOREIGN KEY (person_email) REFERENCES smig_person (email))"
        table_event = f"CREATE TABLE IF NOT EXISTS smig_event (id INT PRIMARY KEY AUTO_INCREMENT, `name` VARCHAR({self.EVENT_MAX_CHAR}), price_non_member DECIMAL(10,2), price_member DECIMAL(10,2), `date` DATE, `time` TIME, `location` VARCHAR({self.NAME_MAX_CHAR}))"
        table_event_attendee = f"CREATE TABLE IF NOT EXISTS smig_event_attendee (event_id INT, person_email VARCHAR({self.EMAIL_MAX_CHAR}), amount_paid DECIMAL(10,2), CONSTRAINT FOREIGN KEY (person_email) REFERENCES smig_person (email), CONSTRAINT FOREIGN KEY (event_id) REFERENCES smig_event (id))"
        table_event_guest = f"CREATE TABLE IF NOT EXISTS smig_event_guest (event_id INT, guest_name VARCHAR({self.NAME_MAX_CHAR}), amount_paid DECIMAL(10,2), CONSTRAINT FOREIGN KEY (event_id) REFERENCES smig_event (id))"
        self.query(table_person)
        self.query(table_membership)
        self.query(table_ID)
        self.query(table_event)
        self.query(table_event_attendee)
        self.query(table_event_guest)

    def query(self, statement):
        try:
            self.cursor.execute(statement)
        except Exception as e:
            print(e)
            return None
        
    def exists_one(self, statement):
        try:
            self.query(statement)
            if (self.cursor.fetchone()[0] == 1):
                return True
        except Exception as e:
            print(e)
        return False

    # populate tables
    def add_person(self, person):
        # check if exists
        check_exists = f"SELECT COUNT(*) FROM smig_person WHERE email='{person.email}'"
        if not self.exists_one(check_exists):
            add_person_row = f"INSERT INTO smig_person(`first_name`, `last_name`, `email`, `year`, `course`) VALUES ('{person.first_name}', '{person.last_name}', '{person.email}', '{person.year}', '{person.course}')"
            print (add_person_row)
            self.query(add_person_row)
            self.log("add_person (OK)", person.to_string())
            self.mariadb_connection.commit()
        else:
            self.log("add_person (DUP)", person.to_string())

    def add_membership(self, person, has_paid):
        # check if exists
        check_exists = f"SELECT COUNT(*) FROM smig_person WHERE email='{person.email}'"
        if self.exists_one(check_exists):
            add_person_row = f"INSERT INTO smig_membership(`person_email`, `hasPaid`) VALUES ('{person.email}', '{'1' if has_paid else '0'}')"
            print (add_person_row)
            self.query(add_person_row)
            self.log("add_membership (OK)", f"{person.email}, {'paid' if has_paid else 'not paid'}")
            self.mariadb_connection.commit()
        else:
            self.log("add_membership (NEX)", person.to_string())

    # convert to CSV

    # convert from CSV

    # get values from tables

    # create views

    def log(self, operation, string):
        f = open(f"log{datetime.date.today()}.txt","a+")
        f.write(f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {operation}: {string}\n")

db = DBHandler()
p1 = Person("Jane", "Smith", "js20", "1", "Computer Science")
p2 = Person("John", "Sax", "js19", "2", "Physics")
db.add_person(p1)
db.add_membership(p2, True)