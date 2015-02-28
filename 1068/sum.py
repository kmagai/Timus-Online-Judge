x = int(input())

sum = 0
if x > 1:
    while x >= 1:
        sum += x
        x -= 1
else:
    while x <= -2:
        sum += x
        x += 1

print(sum)
