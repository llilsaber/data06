from pack01.human import *

class Student(Person):
    def study(self):
        print('study')

    def __str__(self):
        return self.name + ' ' + str(self.age)

class Worker(Person):
    company = ''

    def __init__(self, company):
        self.company = company

    def work(self):
        print('work')

    def __str__(self):
        return self.name + ' ' + str(self.age) + ' ' + self.company

if __name__ == '__main__':
    stu = Student()
    stu.name = 'hong'
    stu.age = 10
    stu.study()
    print(stu)

    wo = Worker('nc')
    wo.name = 'back'
    wo.age = 15
    wo.work()
    print(wo)