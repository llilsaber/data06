buy = []
for _ in range(5):
    print("i want: ", end='')
    buy.append(input())
print(buy)

wish = list()
print('입력: ', end='')
wish2 = input()
wish = wish2.split(',')
for x in wish:
    print('I wnat', x)