class Person:

    def __init__(self, first_name, last_name, email, year, course):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.year = year
        self.course = course

    def to_string(self):
        return f"{self.first_name}, {self.last_name}, {self.email}, {self.year}, {self.course}"
        