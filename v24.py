class Person:
    def __init__(self, name: str, address: str) -> None:
        self.name = name
        self.address = address
    
    def getname(self)->str:
        return self.name
    
    def getaddress(self)->str:
        return self.address
    
    def setaddress(self, new_address)->str:
        self.address = new_address

    def tostring(self)->str:
        return f"{self.name}({self.address})"
    
class Student(Person):
    def __init__(self, name: str, address: str, numcourses: int = 0, courses: list = [], grades: list = []) -> None:
        super().__init__(name, address)
        self.numcourses = numcourses
        self.courses = courses
        self.grades = grades

    def addcoursegrade(self, course: str, grade: int)->None:
        self.courses.append(course)
        self.grades.append(grade)
        
    def printgrades(self)->None:
        print("Grades: ")
        for i in self.grades:
            print(f"{i}, ", end="")
        print("")

    def getaveragegrade(self):
        return sum(grade for grade in self.grades)//len(self.grades)
    
    def tostring(self)->str:
        return f"""{Person.tostring(self)}
    Number of courses: {self.numcourses}
    Courses: {self.courses}
    Grades: {self.grades}"""

class Teacher(Person):
    def __init__(self, name: str, address: str, numcourses: int = 0, courses: list = []) -> None:
        super().__init__(name, address)
        self.numcourses = numcourses
        self.courses = courses

    def addcourse(self, new_course: str)->bool:
        if new_course in self.courses:
            return False
        else:
            self.courses.append(new_course)

    def removecourse(self, course: str)-> bool:
        if course in self.courses:
            self.courses.remove(course)
        else:
            return False
        
    def tostring(self) -> str:
        return f"""{super().tostring()}
    Number of courses: {self.numcourses}
    Courses: {self.courses}"""

student1 = Student(name="John Doe", address="123 Main St")

student1.addcoursegrade("Math", 85)
student1.addcoursegrade("Science", 90)
student1.addcoursegrade("History", 78)

student1.printgrades()

print(f"Average Grade: {student1.getaveragegrade}")

print(student1.tostring())
print("==========================================")

teacher1 = Teacher(name="Jane Smith", address="456 Elm St")

teacher1.addcourse("Math")
teacher1.addcourse("Science")
teacher1.addcourse("History")

print(teacher1.addcourse("Math"))

print(teacher1.removecourse("History"))

print(teacher1.tostring())
