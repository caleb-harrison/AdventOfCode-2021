# Get input
# file = open('Day 8 - Seven Segment Search\Input.txt', 'r').readlines()
# file = [i.strip().split(' | ') for i in file]

# # Create segments/commands
# SEGMENTS = []
# for line in file:
#     segments = line[0].split(' ')
#     commands = line[1].split(' ')
#     SEGMENTS.append((segments, commands))

# '''
# SEGMENTS contains tuples (pairs) with a list of segments
# at index 0 and a list of commands at index 1
# '''

# # Check output values
# count = 0
# for line in SEGMENTS:
#     output = ''
#     commands = line[1]
#     for command in commands:
#         command = sorted(command)
#         length = len(command)
#         if length == 2: # Found 1
#             count += 1
#             output += '1'
#         elif length == 3: # Found 7
#             count += 1
#             output += '7'
#         elif length == 4: # Found 4
#             count += 1
#             output += '4'
#         elif length == 7: # Found 8
#             count += 1
#             output += '8'
#         elif length == 6: # Found 6, 9
#             # Compare command to various segments
#             if command == 'bcdefg': # Found 6
#                 count += 1
#                 output += '6'
#             elif command == 'abcdef': # Found 9
#                 count += 1
#                 output += '9'
#         elif length == 5: # Found 2, 3, 5
#             # Compare command to various segments
#             if command == 'acdfg': # Found 2
#                 count += 1
#                 output += '2'
#             elif command == 'abcdf': # Found 3
#                 count += 1
#                 output += '3'
#             elif command == 'bcdef': # Found 5
#                count += 1
#                output += '5'

def check_sub_char(sub: list, sup: list) -> bool:
    return all(x in sup for x in sub)


def char_sub(x: list, y: list) -> list:
    temp = y[:]
    for a in x:
        if a in temp:
            temp.remove(a)
    return temp


def char_add(x: list, y: list) -> list:
    temp = y[:]
    for a in x:
        if a not in temp:
            temp.append(a)
    return sorted(temp)


unique = [x.split('|')[0].rstrip('\n') for x in open('Day 8 - Seven Segment Search\Input.txt', 'r').readlines()]
output = [x.split('|')[1].rstrip('\n') for x in open('Day 8 - Seven Segment Search\Input.txt', 'r').readlines()]

result = 0

for i in range(len(unique)):
    encoded = [sorted(x) for x in unique[i].split()]
    decoded = [""]*10
    sorted_output = [sorted(x) for x in output[i].split()]
    # solve simple values
    for x in encoded:
        if len(x) == 2:
            decoded[1] = x
        elif len(x) == 3:
            decoded[7] = x
        elif len(x) == 4:
            decoded[4] = x
        elif len(x) == 7:
            decoded[8] = x
    for x in encoded:
        if len(x) == 5:
            if check_sub_char(decoded[1], x):
                decoded[3] = x
            elif check_sub_char(char_sub(decoded[1], decoded[4]), x):
                decoded[5] = x
            else:
                decoded[2] = x
    decoded[6] = char_add(char_sub(decoded[1], decoded[8]), decoded[5])
    decoded[9] = char_add(decoded[1], decoded[5])
    for x in encoded:
        if x not in decoded:
            decoded[0] = x
    value = ""
    for x in sorted_output:
        value += str(decoded.index(x))
    result += int(value)

print(result)