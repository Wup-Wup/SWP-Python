from enum import Enum


class Gender(Enum):
    Male = 0
    Female = 1


class Department(Enum):
    BioMedicine = 0
    IndustrialEngineering = 1


class Person():
    def __init__(self, gender, name, age, department):
        self.gender = gender
        self.name = name
        self.age = age
        self.department = department


class Employee(Person):
    def __init__(self, gender, name, age, department, salary):
        super().__init__(gender, name, age, department)
        self.salary= salary


class GroupLeader(Employee):
    def __init__(self, gender, name, age, department, salary):
        super().__init__(gender, name, age, department, salary)
