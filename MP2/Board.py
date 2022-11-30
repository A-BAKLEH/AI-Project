import Cars as car


class Board:
    def __init__(self, string):
        # First pass - create an empty 6x6 board with just dots on it
        self._lambda = 5
        self.string = string
        self.board = [[0 for x in range(6)] for y in range(6)]
        self.cars = []
        self.isWon = False
        self.isSolvable = True
        self.listOfMoves = []
        c = 0

        # Replace all the dots in this empty 6x6 board with the respective letters from the input file
        for i in range(6):
            for j in range(6):
                self.board[i][j] = string[c]
                c = c + 1

        # Identify all the cars on the board and group them into a list
        for alphabet in letters:
            aCount = []

            index_i = 0
            for i in self.board:
                index_j = 0
                for j in i:
                    if j is alphabet:
                        aCount.append([index_i, index_j])
                    index_j = index_j + 1
                index_i = index_i + 1

            if len(aCount) > 0:
                test = aCount[:]
                self.cars.append(car.Car(alphabet, 100, cells=test))
                test = []

    def printBoard(self):
        for i in self.board:
            for j in i:
                print(j, end='  ')
            print()

        for c in self.cars:
            c.printCarInfo()

    def exploreMoves(self):
        self.listOfMoves = []
        aCar = None
        cars = self.cars
        for car in cars:
            if(car.name == 'A'):

                aCar = car

            if car.fuel <= 0:
                pass
                #print(car.name + " Car Has No Fuel")

            else:

                if car.orientation == "Horizontal":

                    if car.cell_list[0][1] != 0 and self.board[car.cell_list[0][0]][car.cell_list[0][1] - 1] == '.':

                        #print(car.name + " Can Move Left")
                        freeSpacesLeft = self.getnumberOfFreeSpaces(car.orientation, car.cell_list[0], "Left")
                        for x in range(freeSpacesLeft):
                            if car.fuel >= x:
                                self.listOfMoves.append([car.name, "Left", x+1, car.fuel])
                    else:
                        pass
                        #print(car.name + " Can't Move Left")

                    if car.cell_list[len(car.cell_list) - 1][1] != 5 and self.board[car.cell_list[0][0]][
                        car.cell_list[len(car.cell_list) - 1][1] + 1] == '.':

                        #print(car.name + " Can Move Right")

                        freeSpacesRight = self.getnumberOfFreeSpaces(car.orientation, car.cell_list[-1], "Right")
                        for x in range(freeSpacesRight):
                            if car.fuel >= x:
                                self.listOfMoves.append([car.name, "Right", x+1, car.fuel])
                    else:
                        pass
                        #print(car.name + " Can't Move Right")

                elif car.orientation == "Vertical":

                    if car.cell_list[0][0] != 0 and self.board[car.cell_list[0][0] - 1][car.cell_list[0][1]] == '.':

                        #print(car.name + " Can Move Up")
                        freeSpacesUp = self.getnumberOfFreeSpaces(car.orientation, car.cell_list[0], "Up")
                        for x in range(freeSpacesUp):
                            if car.fuel >= x:
                                self.listOfMoves.append([car.name, "Up", x+1, car.fuel])

                    else:
                        pass
                        #print(car.name + " Can't Move Up")

                    if car.cell_list[len(car.cell_list) - 1][0] != 5 and \
                            self.board[car.cell_list[len(car.cell_list) - 1][0] + 1][car.cell_list[0][1]] == '.':

                        #print(car.name + " Can Move Down")

                        freeSpacesDown = self.getnumberOfFreeSpaces(car.orientation, car.cell_list[-1], "Down")
                        for x in range(freeSpacesDown):
                            if car.fuel >= x:
                                self.listOfMoves.append([car.name, "Down", x+1, car.fuel])

                    else:
                        pass
                        #print(car.name + " Can't Move Down")

                else:

                    pass
        if(aCar.cell_list[len(aCar.cell_list)-1][1] != 5 and len(self.listOfMoves) == 0):

            #print("Board has no solution")
            self.isSolvable = False

        #print(self.listOfMoves)
        return self.listOfMoves

    def checkWin(self):
        aCar = None
        for car in self.cars:
            if(car.name == 'A'):
                aCar = car

        if(aCar.cell_list[len(aCar.cell_list)-1][1] == 5):
            self.isWon = True
            print("Game Won")
        else:
            print("Puzzle still not completed")
        return self.isWon

    #My contract is that the user is supposed to know the correct number of moves; otherwise, I will fail
    def moveCar(self, carName, move, noOfCells:int):

        cars = self.cars
        theCar = None
        for car in cars:
            if car.name == carName:
                theCar = car

        if move == "Up":
            for move in self.listOfMoves:
                if move[0] == theCar.name and move[1] == "Up" and move[2] == noOfCells:
                    for x in range(noOfCells):
                        self.board[theCar.cell_list[len(theCar.cell_list) - 1][0] - x][theCar.cell_list[0][1]] = '.'

                    for cell in theCar.cell_list:
                            cell[0] = cell[0] - noOfCells
                            self.board[cell[0]][cell[1]] = carName

                    for car in self.cars:
                        if car.name == carName:
                            car.cell_list = theCar.cell_list
                            car.fuel = car.fuel - noOfCells
            return self

        elif move == "Down":
            for move in self.listOfMoves:
                if move[0] == theCar.name and move[1] == "Down" and move[2] == noOfCells:

                    for x in range(noOfCells):
                        self.board[theCar.cell_list[0][0] + x][theCar.cell_list[0][1]] = '.'
                    #print(theCar.cell_list)
                    for cell in theCar.cell_list:
                        cell[0] = cell[0] + noOfCells
                        #print(cell)
                        self.board[cell[0]][cell[1]] = carName
                    for car in self.cars:
                        if car.name == carName:
                            car.cell_list = theCar.cell_list
                            car.fuel = car.fuel - noOfCells
            return self

        elif move == "Left":

            for move in self.listOfMoves:
                if move[0] == theCar.name and move[1] == "Left" and move[2] == noOfCells:

                    for x in range(noOfCells):
                        self.board[theCar.cell_list[0][0]][theCar.cell_list[len(theCar.cell_list) - 1][1] - x] = '.'

                    for cell in theCar.cell_list:
                        cell[1] = cell[1] - noOfCells
                        self.board[cell[0]][cell[1]] = carName

                    for car in self.cars:
                        if car.name == carName:
                            car.cell_list = theCar.cell_list
                            car.fuel = car.fuel - noOfCells
            return self

        elif move == "Right":

            for move in self.listOfMoves:
                if move[0] == theCar.name and move[1] == "Right" and move[2] == noOfCells:
                    for x in range(noOfCells):
                        self.board[theCar.cell_list[0][0]][theCar.cell_list[0][1] + x] = '.'

                    for cell in theCar.cell_list:
                        cell[1] = cell[1] + noOfCells
                        self.board[cell[0]][cell[1]] = carName

                    for car in self.cars:
                        if car.name == carName:
                            car.cell_list = theCar.cell_list
                            car.fuel = car.fuel - noOfCells
            return self

        else:

            print("invalid move")
        self.removecar()

    def setfuels(self,string):
        for alphabet in letters:
            for char in string:
                if char is alphabet:
                    for car in self.cars:
                        if car.name == alphabet:
                            car.fuel = int(string[string.index(char)+ 1])



    def getblockedpositions(self):
        h = 0
        i = 0
        j = 0
        for car in self.cars:
            if car.name == "A":
                i = car.cell_list[len(car.cell_list)-1][0]
                j = car.cell_list[len(car.cell_list)-1][1] + 1
        while j < 6:
            if self.board[i][j] != ".":
                h = h + 1
                j = j + 1
            else:
                j = j + 1

        #print(h)
        return h

    def getNumberOfblockedvehicles(self):
        return len(self.getblockingvehicles())

    # def getNumberOfblockedvehicles(self):
    #     h = 0
    #     i = 0
    #     j = 0
    #     for car in self.cars:
    #         if car.name == "A":
    #             i = car.cell_list[len(car.cell_list)-1][0]
    #             j = car.cell_list[len(car.cell_list)-1][1] + 1
    #     while j < 6:
    #         if self.board[i][j] != "." and self.board[i][j] != self.board[i][j - 1]:
    #             h = h + 1
    #             j = j + 1
    #         else:
    #             j = j + 1

    #     print(h)
    #     return h

    # Remove the Car out of the board once reach 3f (exit)
    def removecar(self):
        if self.board[2][5] != ".":
            char = self.board[2][5]
            for c in self.cars:
                if c.name == char and not c.name == 'A':
                    if c.orientation == "Horizontal":
                        for cell in c.cell_list:
                            i = cell[0]
                            j = cell[1]
                            self.board[i][j] = "."
                        self.cars.remove(c)
                        #print(c.name,"Was Removed!")



#Horizontal Distance to exit
    def heuresticThree(self):
        return self._lambda * self.getNumberOfblockedvehicles()

#Horizontal Distance to exit
    def heuresticFour(self):
         for car in self.cars:
            if car.name == "A":
                return 6 - car.cell_list[-1][-1] - 1

#returns a list of all horizontally blocking cars
    def getblockingvehicles(self):
        blockingvehicles = []
        i = 0
        j = 0
        for car in self.cars:
            if car.name == "A":
                i = car.cell_list[len(car.cell_list)-1][0]
                j = car.cell_list[len(car.cell_list)-1][1] + 1
        while j < 6:
            if self.board[i][j] != "." and self.board[i][j] != self.board[i][j - 1]:
                blockingvehicles.append(self.board[i][j])
            j = j + 1

        return blockingvehicles



#returns the number of free spaces after the car
    def getnumberOfFreeSpaces(self, orientation:str, point:tuple, direction:str):
        i = point[0] #row
        j = point[1] #column
        freeSpaces = 0
        if orientation == "Horizontal":
            if direction == "Right":
                for k in range(j + 1, 6):
                    if k < 6 and self.board[i][k] == ".":
                        freeSpaces += 1
                    else: return freeSpaces
            else:
                #Watch out for out of boundary
                for k in range(j - 1 , -1, -1):
                    if k > -1 and self.board[i][k] == ".":
                        freeSpaces += 1
                    else: return freeSpaces
        else:
            if direction == "Up":
                #Watch out for out of boundary
                for k in range(i - 1, -1, -1):
                    if k > -1 and self.board[k][j] == ".":
                        freeSpaces += 1
                    else: return freeSpaces
            else:
                for k in range(i + 1, 6):
                    if k < 6 and self.board[k][j] == ".":
                        freeSpaces += 1
                    else: return freeSpaces
        return freeSpaces


    def returnstring(self):
        str = ""

        for board in self.board:
            for i in board:
                str += i

        return str

    def returnboardconfig(self):
        str_board = ""
        for i in self.board:
            for j in i:
                str_board += (str(j) + "  ")
            str_board += "\n"

        str_board += "\n\n"
        return str_board



letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']