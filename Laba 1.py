class MyGroup:
    def student(self, name=None, surname=None, year=None):
        self.name = name
        self.surname = surname
        self.year = year

    def calculate_year(self):
        return 2025 - self.year if self.year else None

    def get_name_list(self):
        return [self.name, self.surname, self.year]

person = MyGroup()
person.student("Станіслав", "Джигарханов",2007)
print(person.calculate_year())
print(person.get_name_list())