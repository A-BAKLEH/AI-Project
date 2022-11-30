import itertools
import random
import Cars as car
import Board as bd

class puzzleGenerator:

    def __int__(self,minVehicles,maxVehicles):

        self.numVehiclesRange = [minVehicles, maxVehicles]

    def generateBoard(self):

        numOfVehicles = random.randint(self.numVehiclesRange[0], self.numVehiclesRange[1])
        boardInstance = [['.','.','.','.','.','.'],['.','.','.','.','.','.'],['.','.','.','.','.','.'],
                         ['.','.','.','.','.','.'],['.','.','.','.','.','.'],['.','.','.','.','.','.']]

        vehicles = []

        column = random.randint(0, 3)
        row = 2

        ambulance = car.Car(name='A', fuel=random.randint(0,100), cells=[[row,column],[row,column+1]])
        vehicles.append(ambulance)

        for i in range(numOfVehicles-1):

            randomVehicle = self.getRandomVehicle(letters[i])
            attempts = 0

            while True:

                alreadyExists = False

                for vehicle in vehicles:
                    for cellv in vehicle.cell_list:
                        for cellz in randomVehicle.cell_list:
                            if cellv == cellz:
                                alreadyExists = True
                                break
                if alreadyExists:
                    randomVehicle = self.getRandomVehicle(letters[i])
                    attempts += 1
                else:
                    break
                if attempts > 400:
                    return self.generateBoard()
            vehicles.append(randomVehicle)

        for boardVehicle in vehicles:
            for cells in boardVehicle.cell_list:
                boardInstance[cells[0]][cells[1]] = boardVehicle.name


        boardStr = "".join(itertools.chain(*boardInstance))
        print(boardStr)
        newPuzzleObject = bd.Board(boardStr)

        for boardCar in newPuzzleObject.cars:
            for carsVroom in vehicles:
                if boardCar.name == carsVroom.name:
                    boardCar.fuel = int(carsVroom.fuel)

        return newPuzzleObject

    def onBoundaries(self,x,y,size):

        if (x < 0 or x > 5 or y < 0 or y > 5):
            return False
        if(x+size > 6 or y+size > 6):
            return False
        return True

    def getRandomVehicle(self,carName):

        randomSize = random.randint(2,3)

        carCells = []

        row = random.randint(0, 5)
        column = random.randint(0, 5)
        randOrientation = random.randint(0,1)
        randFuel = random.randint(0,100)

        while not self.onBoundaries(row,column,randomSize):

            row = random.randint(0, 5)
            column = random.randint(0, 5)
            randOrientation = random.randint(0,1)
            randomSize = random.randint(2,3)

        if(randOrientation == 1):

            for horz in range(randomSize):
                carCells.append([row,horz+column])

            randCar = car.Car(name=carName, fuel=randFuel,cells=carCells)
            return randCar
        else:

            for vert in range(randomSize):
                carCells.append([vert+row,column])

            randCar = car.Car(name=carName, fuel=randFuel, cells=carCells)
            return randCar



letters = ['B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T','U','V']