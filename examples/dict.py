import random
# d = [1, 2, 3, 4, 5, 6, 21, 23, 24, 52]
# l = len(d)-1
# print(d)
# for x in range(int(len(d)/2)):
#     temp = d[x]
#     d[x] = d[l-x]
#     d[l-x] = temp
#     print(d, 'x')


class board:
    def __init__(self, count):
        self.board = []
        self.agentPosition = []
        self.numDirection = 4
        self.createBoard(count)
        self.populateBoard()

    def createBoard(self, count):
        # only supports square grids
        for row in range(count):
            self.board.append([])
            for column in range(count):
                self.board[row].append(0)

    def populateBoard(self):
        for x in self.board:
            for y in x:
                y = random.randint(0, 1)

    def addAgent(self, row, column):
        self.agentPosition = [row, column]
        self.board[row][column] = 1

    def updateAgent(self, row, column):
        self.board[self.agentPosition[0]][self.agentPosition[1]] = 0
        self.agentPosition = [row, column]
        self.board[row][column] = 1


class agent:
    def __init__(self, maxEnergy, movCapacity, vision):
        self.energy = maxEnergy
        self.movementCapacity = movCapacity
        self.vision = vision

    def update(self, grid):
        # create visal space
        row = grid.agentPosition[0]
        column = grid.agentPosition[1]
        top = grid.board[row-self.vision][column]
        bottom = grid.board[row+self.vision][column]
        right = grid.board[row][column+self.vision]
        left = grid.board[row][column-self.vision]
        vision = [top, bottom, right, left]

        # for x in board.
        pass


count = 5
grid = board(5)
player = agent(100, 1, 1)

# while player.energy > 0:
#     player.update(grid)
print(grid.board)

for x in grid.board:
    print(x)
