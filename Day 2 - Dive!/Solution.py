#--- Day 2: Dive! ---

# Caleb's Part 1
CalebInput = open("CalebInput.txt", "r")
CalebList = CalebInput.readlines()

horizontalPosition = 0
depth = 0

for command in CalebList:
    # Removes new line character from end of line
    command = command.strip()
    
    if command[0] == "f":
        # Forward
        horizontalPosition += int(command[-1])
    elif command[0] == "u":
        # Up
        depth -= int(command[-1])
    else:
        # Down
        depth += int(command[-1])

# Prints product of depth and horizontal position
print("Caleb's Part 1:", depth * horizontalPosition)

# Luke's Part 1
LukeInput = open("LukeInput.txt", "r")
LukeList = LukeInput.readlines()

x=0
y=0

for i in LukeList:
	i = i.strip()
	new = i.split(" ")
	if new[0] == "forward":
		x += int(new[1]) 
	elif new[0] == "down":
		y+=int(new[1])
	elif new[0] == "up":
		y-=int(new[1])
print("Luke's Part 2: ",x*y)

#####################################################

# Caleb's Part 2
horizontalPosition = 0
depth = 0
aim = 0

for command in CalebList:
    # Removes new line character from end of line
    command = command.strip()
    
    if command[0] == "f":
        # Forward
        horizontalPosition += int(command[-1])
        depth += aim * int(command[-1])
    elif command[0] == "u":
        # Up
        aim -= int(command[-1])
    else:
        # Down
        aim += int(command[-1])

print("Caleb's Part 2:", depth * horizontalPosition)

# Luke's Part 1
LukeInput = open("LukeInput.txt", "r")
LukeList = LukeInput.readlines()

x=0
y=0
aim=0
for i in LukeList:
	i = i.strip()
	new = i.split(" ")
	if new[0] == "forward":
		x+=int(new[1])
		y+=aim*int(new[1])
	elif new[0] == "down":
		aim+=int(new[1])
	elif new[0] == "up":
		aim-=int(new[1])

print("Luke's Part 2: ",x*y)

"""
forward 5 adds 5 to your horizontal position, a total of 5. Because your aim is 0, your depth does not change.
down 5 adds 5 to your aim, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13. Because your aim is 5, your depth increases by 8*5=40.
up 3 decreases your aim by 3, resulting in a value of 2.
down 8 adds 8 to your aim, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15. Because your aim is 10, your depth increases by 2*10=20 to a total of 60.
"""

