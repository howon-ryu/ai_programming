import pickle
class Person:
    def __init__(self):
        self.name = input("이름을 입력하세요 : ")
        self.sex =input("성별을 입력하세요 : ")
        self.age =input("나이를 입력하세요 : ")
    def set_name(self):
        self.name = input("이름을 입력하세요 : ")
        self.print_info()
    def set_sex(self):
        self.sex = input("성별을 입력하세요 : ")
        self.print_info()
    def set_age(self):
        self.age = input("나이를 입력하세요 : ")
        self.print_info()
    def print_info(self):
        print("현재 저장된 이름, 성별, 나이를 출력합니다 ")
        print (self.name)
        print (self.age)
        print (self.sex)



class Student(Person):
    def __init__(self):
        self.name = input("이름을 입력하세요 : ")
        self.sex = input("성별을 입력하세요 : ")
        self.age = input("나이를 입력하세요 : ")
        self.id = input("id를 입력하세요 : ")
        self.course = input("course를 입력하세요 : ")
        self.print_info()
    def set_id(self):
        self.id = input("id를 입력하세요 : ")
        self.print_info()
    def set_course(self):
        self.course = input("course를 입력하세요 : ")
        self.print_info()
    def print_info(self):
        print("현재 저장된 이름, 성별, 나이, id, course 를 출력합니다 ")
        print (self.name)
        print (self.age)
        print (self.sex)
        print (self.id)
        print (self.course)

class Teacher(Person):
    def __init__(self):
        self.name = input("이름을 입력하세요 : ")
        self.sex = input("성별을 입력하세요 : ")
        self.age = input("나이를 입력하세요 : ")
        self.sal = input("sal를 입력하세요 : ")
        self.degree = input("degree를 입력하세요 : ")
        self.print_info()
    def set_sal(self):
        self.sal = input("sal를 입력하세요 : ")
        self.print_info()
    def set_degree(self):
        self.degree = input("degree를 입력하세요 : ")
        self.print_info()
    def print_info(self):
        print("현재 저장된 이름, 성별, 나이, id, course 를 출력합니다 ")
        print (self.name)
        print (self.age)
        print (self.sex)
        print (self.sal)
        print (self.degree)

print("person 시작")
a = Person()
a.print_info()
a.set_name()
a.set_sex()
a.set_age()
print("student 시작")
b = Student()
b.set_id()
c = Student()
c.set_course()
print("teacher 시작")
d = Teacher()
d.set_sal()
e = Teacher()
e.set_degree()


with open('class.bin','wb')as file:
    pickle.dump(a,file)
    pickle.dump(b,file)
    pickle.dump(c,file)
    pickle.dump(d,file)
    pickle.dump(e,file)


with open('class.bin','rb')as file:
    a = pickle.load(file)
    b = pickle.load(file)
    c = pickle.load(file)
    d = pickle.load(file)
    e = pickle.load(file)
    print("person 시작")

    a.print_info()
    a.set_name()
    a.set_sex()
    a.set_age()
    print("student 시작")

    b.set_id()

    c.set_course()
    print("teacher 시작")

    d.set_sal()
    e.set_degree()