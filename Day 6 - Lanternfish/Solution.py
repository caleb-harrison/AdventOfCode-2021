# Get input
file = open('Day 6 - Lanternfish\Input.txt', 'r').read().split(',')

# Global fish array
FISH = [int(i) for i in file]

def addDay():
    for i in range(len(FISH)):
        # Add 8 to the end and reset current fish to 6
        if FISH[i] == 0:
            FISH.append(8)
            FISH[i] = 6
        else:
            FISH[i] -= 1

def addDays(numberOfDays):
    for i in range(numberOfDays):
        addDay()
        print("Day", i+1)

def optimalAddDays(days):
    tracker = [FISH.count(i) for i in range(9)]
    for day in range(days):
        tracker[(day + 7) % 9] += tracker[day % 9]
    return sum(tracker)