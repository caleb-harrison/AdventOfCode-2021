# Get input
file = open('Day 5 - Hydrothermal Venture\Input.txt', 'r').readlines()
file = [i.strip().replace(' ','') for i in file]

# Biggest X of large input: 987
# Biggest Y of large input: 989
# Create zeros array for later use

#WIDTH, HEIGHT = 10, 10 # Example
WIDTH, HEIGHT = 988, 990 # Input
OCEAN = [[0 for x in range(WIDTH)] for y in range(HEIGHT)] 

# Get vents from input
vents = []

for vent in file:
    vent = vent.split('->')
    newVent = []
    for side in vent:
        newVent.append(tuple(map(int, side.split(','))))
    vents.append(newVent)

def prettyPrintOcean():
    for line in OCEAN:
        for point in line:
            if point == 0:
                print('.', end='')
            else:
                print(point, end='')
        print('')

def getPointsBetweenCoordinates(x1, y1, x2, y2):
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    # Reverse the list if the coordinates were reversed
    if rev:
        points.reverse()
    return points

def getAllVentLocations():
    locations = []

    for vent in vents:
        x1, y1 = vent[0]
        x2, y2 = vent[1]

        # horizontal or vertical or diagonal
        if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
            # add all points between coordinates to locations
            locations += getPointsBetweenCoordinates(x1, y1, x2, y2)

    return locations

def addAllLocationsToOcean(locations):
    for coordinate in locations:
        OCEAN[coordinate[1]][coordinate[0]] += 1

def getOverlappingLinesCount():
    count = 0

    for line in OCEAN:
        for point in line:
            if point >= 2:
                count += 1

    return count

locations = getAllVentLocations()
addAllLocationsToOcean(locations)
print(getOverlappingLinesCount())