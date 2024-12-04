import re
f = open("problem3.txt", "r")

numsList = re.findall("mul\(\d{0,3},\d{0,3}\)", f.read())
p1 = 0
p2 = 0
for i in numsList:
    number = i.strip("mul()")
    number = number.replace(",", " ")
    nums = list(map(int, number.split(" ")))
    p1 += (nums[0] * nums[1])
print(p1)

skipFlag = False

f = open("problem3.txt", "r")
string = re.findall("mul\(\d{0,3},\d{0,3}\)|do\(\)|don't\(\)", f.read())
for i in string:
    if i == "do()":
        skipFlag = False
    elif i == "don't()":
        skipFlag = True
    else:
        if skipFlag == False:
            number = i.strip("mul()")
            number = number.replace(",", " ")
            nums = list(map(int, number.split(" ")))
            p2 += (nums[0] * nums[1])
print(p2)