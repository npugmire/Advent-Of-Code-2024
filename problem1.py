import numpy as np

f = open('problem1.txt', 'r')
leftArray = []
rightArray = []
for line in f:
    nums = line.split()
    leftArray.append(nums[0])
    rightArray.append(nums[1])

leftArray.sort()
rightArray.sort()

leftArray = np.array(leftArray)
rightArray = np.array(rightArray)
# Part 1 #
# distance = 0
# for i in range(0, 1000):
#     difference = int(leftArray[i]) - int(rightArray[i])
#     distance += abs(difference)
# print(distance)

# Part 2
similarity = 0
for i in range(0, 1000):
    location = np.asarray(np.where(rightArray == leftArray[i]))
    count = len(location.flatten())
    if count > 0:
        similarity += (int(leftArray[i]) * count)

print(similarity)