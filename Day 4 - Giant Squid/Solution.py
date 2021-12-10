# Day 4: Giant Squid

class BingoBoard:
    
    def __init__(self):
        self.Board = [ [0] * 5 ] * 5
        self.Bingo = False

    def setBoard(self, array):
        self.Board = array

    def markBoard(self, number):
        for x in range(0, 5):
            for y in range(0, 5):
                if self.Board[x][y] == number:
                    self.Board[x][y] = -1

    def checkForBingo(self):

        if self.Bingo:
            return True

        for x in range(0, 5):
            # Check for horizontal
            if (self.Board[x][0] == -1) and (self.Board[x][1] == -1) and (self.Board[x][2] == -1) and (self.Board[x][3] == -1) and (self.Board[x][4] == -1):
                self.Bingo = True
                return True

            # Check for vertical
            if (self.Board[0][x] == -1) and (self.Board[1][x] == -1) and (self.Board[2][x] == -1) and (self.Board[3][x] == -1) and (self.Board[4][x] == -1):
                self.Bingo = True
                return True
        
        return False

    def getSumOfUnmarkedNumbers(self):
        total = 0

        for x in range(0, 5):
            for y in range(0, 5):
                if self.Board[x][y] != -1:
                    total += self.Board[x][y]

        return total

def part1():
    
    # All Bingo Boards!
    BingoBoards = []

    # Get input
    file = open('Day 4 - Giant Squid\Input.txt', 'r').readlines()

    # Create bingo commands
    Commands = list(map(int, file[0].strip().split(',')))

    # Create bingo boards
    count = 1
    currentIndex = 0
    currentBoard = []
    for line in file[2:]:
        line = line.strip('\n').lstrip().replace('  ', ' ').split(' ')

        # Check for ['']
        if line != ['']:
            currentBoard.append(line)

        # Every 5 lines, skip a line since it is empty ['']
        if line == ['']:

            # Create bingo board with previous 5 lines
            board = BingoBoard()
            board.setBoard([[int(i) for i in currentBoard[0]],
                            [int(i) for i in currentBoard[1]],
                            [int(i) for i in currentBoard[2]],
                            [int(i) for i in currentBoard[3]],
                            [int(i) for i in currentBoard[4]]])
            
            BingoBoards.append(board)

            # Reset current board
            currentBoard = []

    # Check all boards for bingos using all commands
    for Command in Commands:

        for board in BingoBoards:
            board.markBoard(Command)

            bingo = board.checkForBingo()

            if bingo:
                # print(Command)
                # print(board.Board)
                print("Solution Part 1:", board.getSumOfUnmarkedNumbers() * Command)
                return

def part2():
    
    # All Bingo Boards!
    BingoBoards = []

    # Get input
    file = open('Day 4 - Giant Squid\Input.txt', 'r').readlines()

    # Create bingo commands
    Commands = list(map(int, file[0].strip().split(',')))

    # Create bingo boards
    count = 1
    currentIndex = 0
    currentBoard = []
    for line in file[2:]:
        line = line.strip('\n').lstrip().replace('  ', ' ').split(' ')

        # Check for ['']
        if line != ['']:
            currentBoard.append(line)

        # Every 5 lines, skip a line since it is empty ['']
        if line == ['']:

            # Create bingo board with previous 5 lines
            board = BingoBoard()
            board.setBoard([[int(i) for i in currentBoard[0]],
                            [int(i) for i in currentBoard[1]],
                            [int(i) for i in currentBoard[2]],
                            [int(i) for i in currentBoard[3]],
                            [int(i) for i in currentBoard[4]]])
            
            BingoBoards.append(board)

            # Reset current board
            currentBoard = []

    for line in file[-5:]:
        line = line.strip('\n').lstrip().replace('  ', ' ').split(' ')
        currentBoard.append(line)
    
    # Get last board on input file
    board = BingoBoard()
    board.setBoard([[int(i) for i in currentBoard[0]],
                            [int(i) for i in currentBoard[1]],
                            [int(i) for i in currentBoard[2]],
                            [int(i) for i in currentBoard[3]],
                            [int(i) for i in currentBoard[4]]])
        
    BingoBoards.append(board)

    # Check all boards for bingos using all input commands
    amountOfBoards = len(BingoBoards)
    bingoCount = 0
    winningBoards = []
    for Command in Commands:

        for board in BingoBoards:
            board.markBoard(Command)

            bingo = board.checkForBingo()
            if (bingo) and (board not in winningBoards):
                bingoCount += 1
                winningBoards.append(board)
                
                # Once the final card gets a bingo..
                if bingoCount == amountOfBoards:
                    # print(Command)
                    # print(bingoCount)
                    # print(board.Board)
                    print("Solution Part 2:", board.getSumOfUnmarkedNumbers() * Command)
                    return

# Driver
if __name__ == '__main__':
    part1()
    part2()