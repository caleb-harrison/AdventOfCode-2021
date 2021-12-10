#--- Day 3: Binary Diagnostic ---

# Caleb's Part 1
CalebInput = open("CalebInput.txt", "r")
CalebList = CalebInput.readlines()

# Luke's Part 1
LukeInput = open("LukeInput.txt", "r")
LukeList = LukeInput.readlines()


gamma = ""
epsilon = ""
for i in range(0,12):
	onecount = 0
	zerocount = 0
	for binary in LukeList:
		binary = binary.strip()
		if binary[i] == "1":
			onecount += 1
		else:
			zerocount += 1
	if onecount > zerocount:
		gamma += "1"
		epsilon += "0"
	elif onecount < zerocount:
		gamma += "0"
		epsilon += "1"
	elif onecount == zerocount:
		gamma += "1"
		epsilon += "0"
		
#print("Binary Gamma Rate: ",gamma)
#print("Binary Epsilon Rate: ",epsilon)
#gamma = int(gamma,2)
#epsilon = int(epsilon,2)
print("Decimal Gamma Rate: ",gamma)
#print("Decimal Epsilon Rate: ",epsilon)
#print("Decimal Gamma * Epsilon: ", gamma*epsilon)


# Luke's Part 2

# gamArr=[]
# epsArr=[]
# for i in LukeList:
# 	i = i.strip()
# 	if i[0] == gamma[0]:
# 		gamArr.append(i)
# 	else:
# 		epsArr.append(i)

# # Gamma filtering
# c=0
# i=0
# for i in range(0,11):
# 	for binary in epsArr:
# 		if binary[:i] != epsilon[:i]:
# 			epsArr.pop(c)
# 		c+=1
# 	print(epsArr)
# 	c=0

 
mc = []
lc = []
LukeList2=[]
for bin in CalebList:
    bin = bin.strip()
    LukeList2.append(bin)

oneCount = 0
zeroCount = 0
for binary in LukeList2:
    if binary[0] == "1":
        oneCount += 1
    else:
        zeroCount += 1


for binary in LukeList2:
	if binary[0] == "1" and oneCount > zeroCount:
		mc.append(binary)
	else:
		lc.append(binary)

# we have 2 arrays, one with common bit "mc"
# and one with least common bit "lc"
# print(mc)

test = ['00100',
'11110',
'10110',
'10111',
'10101',
'01111',
'00111',
'11100',
'10000',
'11001',
'00010',
'01010']

def getO(array,index):
	oneCount = 0
	zeroCount = 0
	common = ""
	newArr = []
	for binary in array:
		if binary[index] == "1":
			oneCount += 1
		else:
			zeroCount += 1	
	if zeroCount > oneCount:
		common = "0"
	elif zeroCount < oneCount:
		common = "1"
	else:
		common = "1"
		
	for binary in array:
		if binary[index] == common:
			newArr.append(binary)
	index += 1
	if len(newArr) == 1:
		print("Oxygen: ",int(newArr[0],2))
		return 0
	else:
		getO(newArr, index)

def getCO2Test(array, index):
	oneCount = 0
	zeroCount = 0
	leastcommon = ""
	newArr = []
	for binary in array:
		if binary[index] == "1":
			oneCount += 1
		else:
			zeroCount += 1
	if zeroCount > oneCount:
		leastcommon = "1"
	elif zeroCount < oneCount:
		leastcommon = "0"
	else:
		leastcommon = "0"
	for binary in array:
        
		if binary[index] == leastcommon:
			newArr.append(binary)
	index += 1
	if len(newArr) <= 1:
		#print("CO2: ",int(newArr[0],2))
		return 0
	else:
		getCO2Test(newArr, index)

def getCO2Test2(array,index):
    oneCount = 0
    zeroCount = 0
    leastcommon = ""
    newArr = []
    for binary in array:
        if binary[index] == "1":
            oneCount += 1
        else:
            zeroCount += 1	
    if zeroCount > oneCount:
        leastcommon = "1"
    elif zeroCount < oneCount:
        leastcommon = "0"
    else:
        leastcommon = "0"
    for binary in array:
        if binary[index] == leastcommon:
            newArr.append(binary)
    index += 1
    if len(newArr) <= 1:
        print("CO2: ",int(newArr[0],2))
        return 0
    else:
        getCO2Test2(newArr, index)

			
getO(mc, 1)

getCO2Test2(lc, 1)



# tried 4123182

# Caleb's Part 2
# test = ['00100',
# '11110',
# '10110',
# '10111',
# '10101',
# '01111',
# '00111',
# '11100',
# '10000',
# '11001',
# '00010',
# '01010']


# Get most common bit at index 'i'
# Cut out all numbers that bit[i] aren't equal to most common bit
# Get most common bit of new array
# Repeat..

def getMostCommonBit(array, index):
    oneCount = 0
    zeroCount = 0

    for binary in array:
        if binary[index] == '1':
            oneCount += 1
        else:
            zeroCount += 1

    if zeroCount > oneCount:
        return 0
    else:
        return 1

def clearLeastCommonBits(array, index, bit):
    length = len(array)
    newArray = []
    if length == 1:
        return array
    else:
        for binary in array:
            if length > 1:
                if int(binary[index]) == bit:
                    newArray.append(binary[index])
                    length -= 1
    
    return newArray

def testRecursive(array):
    # base case
    if len(array) == 1:
        return array
    else:
        
        # iterate over index 0 each time
        # look for most common bit at index 0 of all binary in array
        mostCommonBit = getMostCommonBit(array, 0)
        
        # cut all bits that arent equal to most common bit
        array = clearLeastCommonBits(array, 0, mostCommonBit)

        # otherwise, cut off first digit
        return testRecursive(array[1:])	

#print(testRecursive(test))

def getOxygenRating(array):
    for index in range(len(array) - 1):
        mostCommonBit = getMostCommonBit(array, index)
        array = clearLeastCommonBits(array, index, mostCommonBit)
        if len(array) == 1:
            return array[0]  

def getLeastCommonBit(array, index):
    oneCount = 0
    zeroCount = 0

    for binary in array:
        if binary[index] == '1':
            oneCount += 1
        else:
            zeroCount += 1

    if oneCount > zeroCount:
        return 1
    else:
        return 0