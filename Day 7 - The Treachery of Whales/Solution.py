# Get input
file = open('Day 7 - The Treachery of Whales\Input.txt', 'r').read().split(',')

# Global crab array
CRABS = [int(i) for i in file]

# Create hash map for difference between all elements
OUTCOMES = {}
leastFuel = -1
leastFuelCrab = -1
for startingCrab in CRABS:
    
    # Go to each crab from startingCrab
    if startingCrab not in OUTCOMES:
        OUTCOMES[startingCrab] = 0
        for destinationCrab in CRABS:
            steps = abs(startingCrab - destinationCrab)
            fuel = 0
            for i in range(1, steps + 1):
                fuel += i

            OUTCOMES[startingCrab] += fuel

    # Check if this crab has the least fuel
    if leastFuel == -1:
        leastFuel = OUTCOMES[startingCrab]
        leastFuelCrab = startingCrab
    elif leastFuel > OUTCOMES[startingCrab]:
        leastFuel = OUTCOMES[startingCrab]
        leastFuelCrab = startingCrab

print(leastFuelCrab)
print(leastFuel)