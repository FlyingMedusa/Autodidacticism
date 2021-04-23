

class Hogwarts:

    def __init__(self):
        print("Welcome to Hogwarts!")
    
    def read_motto(self):
        print("Draco dormiens nunquam titillandus")


class Gryffindor(Hogwarts):

    def __init__(self, name, last, age, pet):
        self.name = name
        self.last = last
        self.age = age
        self.pet = pet
        self.__status = "1st year student" # private
    
    def read_motto(self):
        print("\n*****")
        super().__init__()
        print("Our motto:")
        super().read_motto()
        print("Gryffindor:\nTheir daring, nerve and chivalry set Gryffindors apart\n*****")

    def muggle_email(self):
        return "{}_{}@legitmuggle.com".format(self.name.lower(), self.last.lower())

    def show_status(self):
        print("Student: {} {}\nCurrent year: {}".format(self.last, self.name, self.__status))
    
    def graduate(self, year):
        self.__status = "{} year student".format(year)


student_01 = Gryffindor('Harry', 'Potter', 13, 'owl')
student_02 = Gryffindor('Ron', 'Weasley', 13, 'rat')
student_03 = Gryffindor('Hermiona', 'Granger', 13, 'cat')

print('Student: {} {}'.format(student_02.name.capitalize(), student_02.last.capitalize()))

print('{}'.format(student_01.muggle_email()))
print('{}'.format(Gryffindor.muggle_email(student_01)))

student_01.read_motto()

student_03.__status = "2nd year student"
student_03.show_status()  #not gonna work - private atribute
student_03.graduate("2nd")
student_03.show_status()