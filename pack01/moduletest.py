num1 = int(input('number1 >> '))
num2 = int(input('number2 >> '))
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 % num2)
print(num1 // num2)

in1 = input('input1 >> ')
in2 = int(input('input2 >> '))
print(in1, 'is', in2, 'years old')
if (in2 > 100):
    print('old!!')
else:
    print("young!!")

hobby = 'run'
time = 10
print(hobby, 'is', time, 'time')
if (hobby == 'run' and time >= 10):
    print('today', hobby, 'is clear')
elif (hobby == 'run' or time < 10):
    print('everybody hobby start!!')