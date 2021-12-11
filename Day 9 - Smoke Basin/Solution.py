# Get input
file = open('Day 9 - Smoke Basin\Input.txt', 'r').readlines()
HEIGHTMAP = [line.strip() for line in file]
LOWPOINTS = []
# Function to check 4 surrounding points
def checkForLowPoint(point, xValue, yValue):
    #print('point:', point, 'coords:', (xValue, yValue), end=' ')

    # Get number above point
    if yValue > 0:
        top = HEIGHTMAP[yValue - 1][xValue]
        #print('top:', top, end=' ')
        if int(point) >= int(top):
            return False
    
    # Get number to left of point
    if xValue > 0:
        left = HEIGHTMAP[yValue][xValue - 1]
        #print('left:', left, end=' ')
        if int(point) >= int(left):
            return False

    # Get number to right of point
    if xValue < len(HEIGHTMAP[0]) - 1:
        right = HEIGHTMAP[yValue][xValue + 1]
        #print('right:', right, end=' ')
        if int(point) >= int(right):
            return False

    # Get number below point
    if yValue < len(HEIGHTMAP) - 1:
        bottom = HEIGHTMAP[yValue + 1][xValue]
        #print('bottom:', bottom, end=' ')
        if int(point) >= int(bottom):
            return False
    
    LOWPOINTS.append(point)
    return True

# Check each number in map and find lowpoints
yValue = 0
total = 0
for line in HEIGHTMAP:
    xValue = 0
    for point in line:
        lowPoint = checkForLowPoint(point, xValue=xValue, yValue=yValue)
        if lowPoint:
            total += int(point) + 1
        
        xValue += 1
    
    yValue += 1

print(total)