class MyGroup:
    def __init__(self, name=None, surname=None, year=None):
        self.name = name
        self.surname = surname
        self.year = year

    def calculate_year(self):
        return 2025 - self.year if self.year else None

    def get_info(self):
        return [self.name, self.surname, self.year]

class ExtendedGroup(MyGroup):
    def __init__(self, name=None, surname=None, year=None, hobby=None, country=None, city=None):
        super().__init__(name, surname, year)
        self.hobby = hobby
        self.country = country
        self.city = city

    def get_info(self):
        return super().get_info() + [self.hobby, self.country, self.city]

    def get_full_description(self):
        return f"{self.name} є учасником {self.hobby} і живе в {self.city}"

    def _protected_method(self):
        return "Це захищений метод. Він для внутрішнього використання."

person = ExtendedGroup("Станіслав", "Джигарханов", 2007, "фуррі", "Україна", "Луцьку")
print(person.calculate_year())
print(person.get_info())
print(person.get_full_description())
