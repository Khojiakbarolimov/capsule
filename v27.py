class Developer:
    def __init__(self, surname: str, position: str, salary: int) -> None:
        self.surname = surname
        self.position = position
        self.salary = salary

class Softwareengineer(Developer):
    def __init__(self, surname: str, position: str, salary: int, bonus: int, department: str) -> None:
        super().__init__(surname, position, salary)
        self.bonus = bonus
        self.department = department

    def getdepartment(self)->str:
        return self.department
    
    def getsalary(self)->int:
        return self.salary
    
    def getbonus(self)->int:
        return self.bonus
    
lst = [
    Softwareengineer("Anvar", "Junior", 500, 100, "1-bo'lim"),
    Softwareengineer("Asror", "Middle", 1500, 500, "2-bo'lim"),
    Softwareengineer("Kamola", "Senior", 2500, 100, "3-bo'lim"),
    Softwareengineer("Vali", "Junior", 500, -100, "1-bo'lim"),
    Softwareengineer("Davron", "Middle", 1500, 100, "2-bo'lim"),
    Softwareengineer("Bahodir", "Senior", 2500, 100, "3-bo'lim"),
    Softwareengineer("Farrrux", "Junior", 500, 100, "1-bo'lim"),
    Softwareengineer("Jamila", "Middle", 1500, 200, "2-bo'lim"),
    Softwareengineer("Jasur", "Senior", 2500, 500, "3-bo'lim"),
    Softwareengineer("Komila", "Junior", 500, -100, "1-bo'lim")
]

dct = dict()

for i in lst:
    if i.getdepartment in dct:
        dct[i.getdepartment()] += (i.getsalary() + i.getbonus())
    else:
        dct[i.getdepartment()] = (i.getsalary() + i.getbonus())

for key, val in dct.items():
    print(key, val)