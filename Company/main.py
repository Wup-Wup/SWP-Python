import Human

persons = []
employee = []
group_leader = []


def add_person(gender, name, age, department):
    persons.append(Human.Person(gender,name,age,department))


def add_employee(gender, name, age, department, salary):
    employee.append(Human.Employee(gender,name,age,department, salary))


def add_group_leader(gender, name, age, department, salary):
    group_leader.append(Human.GroupLeader(gender,name,age,department, salary))


def get_all():
    return len(persons), len(employee), len(group_leader)


def get_count_departments():
    return len(Human.Department)


def get_highest_department(dep):
    count = 0
    for x in persons:
        if x.department == dep:
            count += 1
    for x in employee:
        if x.department == dep:
            count += 1
    for x in group_leader:
        if x.department == dep:
            count += 1
    return count


def male_to_female():
    maleListPerson = [x for x in persons if Human.Gender.Male == x.gender]
    maleListEmployee = [x for x in employee if Human.Gender.Male == x.gender]
    maleListGroupLeader = [x for x in group_leader if Human.Gender.Male == x.gender]

    femaleListPerson = [x for x in persons if Human.Gender.Female == x.gender]
    femaleListEmployee = [x for x in employee if Human.Gender.Female == x.gender]
    femaleListGroupLeader = [x for x in group_leader if Human.Gender.Female == x.gender]

    male = len(maleListPerson) + len(maleListEmployee) + len(maleListGroupLeader)
    female = len(femaleListPerson) + len(femaleListEmployee) + len(femaleListGroupLeader)

    return "Male in %: " + str(
        round(male / (len(persons) + len(employee) + len(group_leader)), 2) * 100) + "\nFemale in %: " + str(
        round(female / (len(persons) + len(employee) + len(group_leader)), 2) * 100)


if __name__ == "__main__":
    add_person(Human.Gender.Male, "Simon", 20, Human.Department.BioMedicine)
    add_employee(Human.Gender.Male, "Julian", 21, Human.Department.IndustrialEngineering, 2132)
    add_employee(Human.Gender.Female, "Lisa", 18, Human.Department.IndustrialEngineering, 1003)
    add_employee(Human.Gender.Male, "Luis", 23, Human.Department.BioMedicine, 2312)
    add_group_leader(Human.Gender.Male, "Okan", 18, Human.Department.IndustrialEngineering, 2032)
    print("Persons: " + str(get_all()[0]))
    print("Employees: " + str(get_all()[1]))
    print("Group leaders: " + str(get_all()[2]))
    print("Count Departments: " + str(get_count_departments()))
    for x in Human.Department:
        print(str(x) + ": " + str(get_highest_department(x)))
    print(male_to_female())
