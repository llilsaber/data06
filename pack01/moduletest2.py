for a in range(20):
    print(a)

for b in range(1, 101, 1):
    print(b)

for c in range(0, 201, 1):
    print(c)

for d in range(1, 101, 2):
    print(d)

for e in range(100, 501, 5):
    print(e)

sum1 = 0
for f in range(100, 501, 10):
    sum1 = sum1 + f
print(sum1)

sum2 = 1
for g in range(3, 201, 8):
    sum2 = sum2 * g
print(sum2)

food = ['potato', 'sweet potato', 'onion']
for h1 in food:
    print(h1, 'good!')
for h2 in food:
    print(h2, 'good!', end='')
print()

food2 = "potato sweepotato onion soup noodle ramen"
food2_list = food2.split()
for i in food2_list:
    if (i != 'onion' and i != 'noodle'):
        print(i, 'UMA! ', end='')