
num1 = list(map(int, input().split()))
num2 = list(map(int, input().split()))

num3 = []

j = 0

while True:
    try:
        num3.append(num1[j]) 
    except IndexError:
        break
    try:
        num3.append(num2[j])
    except IndexError:
        break
    j += 1

if len(num1) > len(num2):
    for i in range(j+1, len(num1)):
        num3.append(num1[i])
elif len(num1) < len(num2):
    for i in range(j+1, len(num2)):
        num3.append(num2[i])

print(num3)


