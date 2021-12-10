#--- Day 1: Sonar Sweep ---
# Inputs depths from problem one into an int array "depths"

# Part 1
my_file = open("Input.txt", "r")
content_list = my_file.readlines()
depths=[]
for i in content_list:
	depths.append(int(i))

total=0
for i in range(1,len(depths)):
	if depths[i-1] < depths[i]:
		total+=1
print(total)

# Part 2
increasedCount = 0
threeMeasurementWindows = []
# content_list = [0, 1, 2, 3, 4, 5]
# sums -> [3, 6, 9, 12]
# increased -> 3

for i in range(0, len(content_list) - 2):
    # Gets current sum of three measurement window
    currentSum = int(content_list[i]) + int(content_list[i + 1]) + int(content_list[i + 2])

    # Adds current sum to list
    threeMeasurementWindows.append(currentSum)

    # Checks if new sum is greater than previous sum
    if i >= 1:
        if currentSum > threeMeasurementWindows[i-1]:
            increasedCount += 1

print(increasedCount)