class Day:
    stu = None
    time = None
    place = None

    def __init__(self, stu, time, place):
        self.stu = stu
        self.time = time
        self.place = place

    def study(self):
        #print(self.stu, 'study is', self.time, 'hours')
        return self.stu + ' study is ' + str(self.time) + ' hours'

    def where(self):
        #print(self.place, 'in there', self.stu, 'study')
        return self.place + ' in there ' + self.stu + ' study'

    def __str__(self):
        return 'day의 속성값들 : ' + str(self.stu) + ',' + str(self.time) + ',' + str(self.place)

if __name__ == '__main__':
    day1 = Day('python', 10, 'Gangnam')
    print(day1.study())
    print(day1.where())

    day2 = Day('java', 11, 'Shinchon')
    day3 = Day('db', 12, 'Jongro')