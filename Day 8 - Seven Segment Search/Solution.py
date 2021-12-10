# Get input
file = open('Day 8 - Seven Segment Search\LargeExample.txt', 'r').readlines()
file = [i.strip().split(' | ') for i in file]

# Create segments/commands
SEGMENTS = []
for line in file:
    segments = line[0].split(' ')
    commands = line[1].split(' ')
    SEGMENTS.append((segments, commands))

'''
SEGMENTS contains tuples (pairs) with a list of segments
at index 0 and a list of commands at index 1
'''

print(SEGMENTS)