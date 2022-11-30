import copy
import itertools
import pickle
from queue import PriorityQueue
import timeit
import time

#import ujson
class move:
    def __init__(self,move,fuel,board,fuelList):
        self.move  = move
        self.fuel = fuel
        self.board = board
        self.fuelList = fuelList

class Node:
    def __init__(self, parent, board, cost, Move=None):

        self.parentNode = parent
        self.boardState = board
        self.stateCost = cost
        self.g = 0
        self.h = 0
        self.move = Move

    def __lt__(self, other):
        return self.stateCost < other.stateCost

    def getSolutionPath(self):

        solutionPath = []

        while self.parentNode != None:
            solutionPath.append(self.boardState)
            self = self.parentNode
        solutionPath.append(self.boardState)
        return solutionPath

    def tracePath(self):
        solPath = []

        while self.parentNode != None:
            solPath.append(self)
            self = self.parentNode
        solPath.append(self)
        return solPath


class Algorithm:

    def __init__(self, board):
        self.visited = PriorityQueue()
        self.closed = []
        self.solutions = []
        self.numOfSolution = 0
        self.board = board
        self.searchpath = []
        self.runtime = 0
        self.spathlength = 0
        self.solutionPath = []


class UniformedCostSearch(Algorithm):


    def search(self):
        expandednodes = 0
        starttime = time.time()
        initialNode = Node(board=self.board,parent=None,cost=0)
        self.visited.put([initialNode.stateCost,initialNode])

        while not self.visited.empty() and self.numOfSolution != 1:

            self.closed.append(self.visited.queue[0][1])
            expandednodes = len(self.closed)

            boardToExplore = self.visited.queue[0][1].boardState

            if boardToExplore.checkWin() != True:


                for moves in boardToExplore.exploreMoves():
                    stateBoard = pickle.loads(pickle.dumps(boardToExplore, -1))
                    stateBoard.moveCar(moves[0],moves[1],moves[2])
                    nodeVisited = False
                    for vals in self.closed:
                        if vals.boardState.board == stateBoard.board:
                            nodeVisited = True
                    for node in self.visited.queue:
                        if node[1].boardState.board == stateBoard.board:
                            nodeVisited = True
                    if not nodeVisited:
                        nodeToAppend = Node(board=stateBoard, parent=self.visited.queue[0][1],cost=  self.costFunction(self.visited.queue[0][0]), Move = moves)
                        self.visited.put([nodeToAppend.stateCost,nodeToAppend])
            else:
                self.solutions.append(self.visited.queue[0][1].getSolutionPath())
                self.solutionPath.append(self.visited.queue[0][1].tracePath())
                self.numOfSolution += 1
                self.spathlength = expandednodes
                print("expanded nodes: ", expandednodes)
                endtime = time.time()
                self.runtime = endtime - starttime
            self.searchpath.append(self.visited.get())

        if self.numOfSolution == 0 and self.visited.empty():
            print("No Solution")

    def printSolutionsBoard(self):
        for solution in self.solutions:
            for board in solution:
                board.printBoard()
            print("--------------------------------------------------------------------")
    def printSolutions(self):

        for solution in self.solutions:
            for board in solution:
                print("".join(itertools.chain(*board.board)))
            print("--------------------------------------------------------------------")

    # function F = G(x) + 0
    def costFunction(self, cost):

        return cost + 1


    def writeSearch(self):
        Strings = []
        text = "--------------------------------------------------------------------"
        initialboard = self.searchpath[0][1]
        text += "".join(itertools.chain(*initialboard.boardState.board))
        if self.numOfSolution == 0:

            Strings.append("No Solution")
            return Strings
        else:

            for solution in self.searchpath:
                string = "" + str(solution[1].stateCost) + " " + str(solution[1].stateCost) + " " + "0" + " " + solution[1].boardState.returnstring()
                Strings.append(string)
                # print(solution[1].stateCost,solution[1].stateCost,solution[1].h, end = "")
                # print("".join(itertools.chain(*solution[1].boardState.board)))

        return Strings


    def writeSolution(self):
        Strings = []

        if self.numOfSolution == 0:

            Strings.append("No Solution")
            return Strings
        else:

            temp = self.solutions[len(self.solutions) - 1][len(self.solutions[0]) - 1].returnstring()
            string1 = "Inital Board Configuration: " + temp + "\n"
            Strings.append(string1)
            temp2 = self.solutions[len(self.solutions) - 1][len(self.solutions[0]) - 1].returnboardconfig() + "\n"
            Strings.append(temp2)
            fuelline = "Car Fuel Available: "
            board = self.solutions[len(self.solutions) - 1][len(self.solutions[0]) - 1]
            for car in board.cars:
                fuelline += car.name + ":" + str(car.fuel) + " "
            Strings.append(fuelline)

            timetaken = "Runtime: " + str(round(self.runtime,3)) + " seconds." + "\n"
            Strings.append(timetaken)

            searchpathlength = "Search path length: " + str(self.spathlength) + " states." + "\n"
            Strings.append(searchpathlength)

            solpathlength = "Solution Path Length: " + str(len(self.solutions[0])-1) + " moves." + "\n"
            Strings.append(solpathlength)

            solpath = "Solution Path: " + self.getsolmoves()
            Strings.append(solpath)

            sol = self.getboardline()
            Strings.append(sol)

            fuelline2 = "Car Fuel Remaining: "
            finalboard = self.solutions[0][0]
            for car in finalboard.cars:
                fuelline2 += car.name + ":" + str(car.fuel) + " "

            Strings.append(fuelline2)

            finalbline = self.solutions[0][0].returnboardconfig() + "\n"
            Strings.append(finalbline)

        return Strings


    def getsolmoves(self):
        line = ""
        for node in reversed(self.solutionPath):
            for nodes in reversed(node):
                if nodes.move is not None:
                    line += nodes.move[0]
                    line += " " + str(nodes.move[1])
                    line += " " + str(nodes.move[2])
                    line += "; "
        return line

    def getboardline(self):
        line = ""
        for node in reversed(self.solutionPath):
            for nodes in reversed(node):
                if nodes.move is not None:
                    line += nodes.move[0]
                    line += " " + str(nodes.move[1])
                    line += " " + str(nodes.move[2])
                    line += "\t\t"

                    for row in nodes.boardState.board:
                        for cell in row:
                            line += str(cell)

                line += "\n"

        return line

class GreedyBestFirstSearch(Algorithm):
    def __init__(self, board):
        super().__init__(board)
        #self.moves = None

    def search(self, heur: int):
        expandednodes = 0
        starttime = time.time()
        initialNode = Node(board=self.board,parent=None,cost=0)
        self.visited.put([initialNode.stateCost,initialNode])

        while not self.visited.empty() or self.numOfSolution != 1:

            self.closed.append(self.visited.queue[0][1])
            expandednodes = len(self.closed)

            boardToExplore = self.visited.queue[0][1].boardState

            if boardToExplore.checkWin() != True:

                for moves in boardToExplore.exploreMoves():
                    stateBoard = pickle.loads(pickle.dumps(boardToExplore, -1))
                    stateBoard.moveCar(moves[0],moves[1],moves[2])
                    nodeVisited = False

                    for vals in self.closed:
                        if vals.boardState.board == stateBoard.board:
                            nodeVisited = True

                    for node in self.visited.queue:
                        if node[1].boardState.board == stateBoard.board:
                            nodeVisited = True

                    if not nodeVisited:
                        nodeToAppend = Node(board=stateBoard, parent=self.visited.queue[0][1],
                                                cost=self.costFunction(boardToExplore, hselection=heur), Move=moves)
                        self.visited.put([nodeToAppend.stateCost, nodeToAppend])
            else:
                self.solutions.append(self.visited.queue[0][1].getSolutionPath())
                self.solutionPath.append(self.visited.queue[0][1].tracePath())
                self.numOfSolution += 1
                self.spathlength = expandednodes
                print("expanded nodes: ", expandednodes)
                endtime = time.time()
                self.runtime = endtime - starttime
                break

            self.searchpath.append(self.visited.get())

        if self.numOfSolution == 0 and self.visited.empty():
            print("No Solution")


    def printSolutionsBoard(self):
        for solution in self.solutions:
            for board in solution:
                board.printBoard()
            print()

    def printSolutions(self):

        for solution in self.solutions:
            for board in solution:
                print("".join(itertools.chain(*board.board)))
            print("--------------------------------------------------------------------")


    def writeSearch(self):
        Strings = []
        text = "--------------------------------------------------------------------"
        initialboard = self.searchpath[0][1]
        text += "".join(itertools.chain(*initialboard.boardState.board))
        if self.numOfSolution == 0:

            Strings.append("No Solution")
            return Strings
        else:

            for solution in self.searchpath:
                string = "" + str(solution[1].stateCost) + " " + str(solution[1].stateCost) + " " + "0" + " " + solution[1].boardState.returnstring()
                Strings.append(string)
                # print(solution[1].stateCost,solution[1].stateCost,solution[1].h, end = "")
                # print("".join(itertools.chain(*solution[1].boardState.board)))

        return Strings


    def writeSolution(self):
        Strings = []

        if self.numOfSolution == 0:

            Strings.append("No Solution")
            return Strings
        else:

            temp = self.solutions[len(self.solutions) - 1][len(self.solutions[0]) - 1].returnstring()
            string1 = "Inital Board Configuration: " + temp + "\n"
            Strings.append(string1)
            temp2 = self.solutions[len(self.solutions) - 1][len(self.solutions[0]) - 1].returnboardconfig() + "\n"
            Strings.append(temp2)
            fuelline = "Car Fuel Available: "
            board = self.solutions[len(self.solutions) - 1][len(self.solutions[0]) - 1]
            for car in board.cars:
                fuelline += car.name + ":" + str(car.fuel) + " "
            Strings.append(fuelline)

            timetaken = "Runtime: " + str(round(self.runtime,3)) + " seconds." + "\n"
            Strings.append(timetaken)

            searchpathlength = "Search path length: " + str(self.spathlength) + " states." + "\n"
            Strings.append(searchpathlength)

            solpathlength = "Solution Path Length: " + str(len(self.solutions[0])-1) + " moves." + "\n"
            Strings.append(solpathlength)

            solpath = "Solution Path: " + self.getsolmoves()
            Strings.append(solpath)

            sol = self.getboardline()
            Strings.append(sol)

            fuelline2 = "Car Fuel Remaining: "
            finalboard = self.solutions[0][0]
            for car in finalboard.cars:
                fuelline2 += car.name + ":" + str(car.fuel) + " "

            Strings.append(fuelline2)

            finalbline = self.solutions[0][0].returnboardconfig() + "\n"
            Strings.append(finalbline)

        return Strings


    def getsolmoves(self):
        line = ""
        for node in reversed(self.solutionPath):
            for nodes in reversed(node):
                if nodes.move is not None:
                    line += nodes.move[0]
                    line += " " + str(nodes.move[1])
                    line += " " + str(nodes.move[2])
                    line += "; "
        return line

    def getboardline(self):
        line = ""
        for node in reversed(self.solutionPath):
            for nodes in reversed(node):
                if nodes.move is not None:
                    line += nodes.move[0]
                    line += " " + str(nodes.move[1])
                    line += " " + str(nodes.move[2])
                    line += "\t\t"

                    for row in nodes.boardState.board:
                        for cell in row:
                            line += str(cell)

                line += "\n"

        return line

    def writeSearch(self):
        text = "--------------------------------------------------------------------"
        Strings = []
        initialboard = self.searchpath[0][1]
        text += "".join(itertools.chain(*initialboard.boardState.board))
        if self.numOfSolution == 0:

            Strings.append("No Solution")
            return Strings
        else:
            for solution in self.searchpath:
                string = "" + str(solution[1].stateCost) + " " + "0" + " " + str(solution[1].stateCost) + " " + solution[1].boardState.returnstring()
                Strings.append(string)
        return Strings


    # function F = 0 + H(x)
    def costFunction(self, board, hselection):
        #print(move)
        if hselection == 1:
            return board.getNumberOfblockedvehicles()
        elif hselection == 2:
            return board.getblockedpositions()
        elif hselection == 3:
            return board.heuresticThree()
        elif hselection == 4:
           return board.heuresticFour()
    def returnh(self,board,i):
        if i == 1:
            h = board.getNumberOfblockedvehicles()
        elif i == 2:
            h = board.getblockedpositions()
        elif i == 3:
            h = board.heuresticThree()
        elif i == 4:
            h = board.heuresticFour()
        print(h)
        return h
class Astar(Algorithm):
    def search(self, h: int):
        expandednodes = 0
        starttime = time.time()
        if h > 4 or h <= 0:
            return "Error in heuristic val, try again!"

        initialNode = Node(board=self.board, parent=None, cost=0)
        self.visited.put([initialNode.stateCost, initialNode])

        while not self.visited.empty() and self.numOfSolution != 1:

            self.closed.append(self.visited.queue[0][1])
            expandednodes = len(self.closed)

            boardToExplore = self.visited.queue[0][1].boardState

            if boardToExplore.checkWin() != True:

                for moves in boardToExplore.exploreMoves():
                    stateBoard = pickle.loads(pickle.dumps(boardToExplore, -1))
                    stateBoard.moveCar(moves[0], moves[1], moves[2])
                    nodeVisited = False

                    for vals in self.closed:
                        if vals.boardState.board == stateBoard.board:
                            nodeVisited = True

                    for node in self.visited.queue:
                        if node[1].boardState.board == stateBoard.board:
                            nodeVisited = True
                    if not nodeVisited:
                        nodeToAppend = Node(board=stateBoard, parent=self.visited.queue[0][1], cost=self.costFunction(self.visited.queue[0][0], boardToExplore,  h),
                                            Move= moves)
                        nodeToAppend.g = self.returng(self.visited.queue[0][0])
                        nodeToAppend.h = self.returnh(nodeToAppend.boardState,h)
                        self.visited.put([nodeToAppend.stateCost, nodeToAppend])
            else:
                self.solutions.append(self.visited.queue[0][1].getSolutionPath())
                self.solutionPath.append(self.visited.queue[0][1].tracePath())
                print(self.solutionPath)
                print(list(reversed(self.solutionPath)))
                self.numOfSolution += 1
                self.spathlength = expandednodes
                print("Nodes Expanded: ", expandednodes)
                endtime = time.time()
                self.runtime = endtime - starttime
            self.searchpath.append(self.visited.get())



        if self.numOfSolution == 0 and self.visited.empty():
            print("No Solution")

    def printSolutionsBoard(self):
        for solution in self.solutions:
            for board in solution:
                board.printBoard()
            print("--------------------------------------------------------------------")

    def printSolutions(self):

        for solution in self.solutions:
            for board in solution:
                print("".join(itertools.chain(*board.board)))
            print("--------------------------------------------------------------------")
            # Used to determine which cars moved every turn

        def determineMoves(self):
            for solution in self.solutions:
                for i in range(len(solution) - 1, -1, -1):
                    board = solution[i]
                    x = 0
                    if i >= 1:
                        self.oldCars = solution[i - 1].cars
                        fuelList = []
                        for car in board.cars:
                            if (self.oldCars[x].fuel != car.fuel):
                                fuelList.append(self.oldCars[x].name + str(self.oldCars[x].fuel))
                                mv = move(car.determineMove(self.oldCars[x]), self.oldCars[x].fuel,
                                          "".join(itertools.chain(*board.board)), fuelList)
                                self.moves.append(mv)
                            x = x + 1

    def writeSolution(self):
        Strings = []
        if self.numOfSolution == 0:

            Strings.append("No Solution")
            return Strings
        else:

            temp = self.solutions[len(self.solutions) - 1][len(self.solutions[0]) - 1].returnstring()
            string1 = "Inital Board Configuration: " + temp + "\n"
            Strings.append(string1)
            temp2 = self.solutions[len(self.solutions) - 1][len(self.solutions[0]) - 1].returnboardconfig() + "\n"
            Strings.append(temp2)
            fuelline = "Car Fuel Available: "
            board = self.solutions[len(self.solutions) - 1][len(self.solutions[0]) - 1]
            for car in board.cars:
                fuelline += car.name + ":" + str(car.fuel) + " "
            Strings.append(fuelline)

            timetaken = "Runtime: " + str(self.runtime) + " seconds."
            Strings.append(timetaken)

            searchpathlength = "Search path length: " + str(self.spathlength) + " states." + "\n"
            Strings.append(searchpathlength)

            solpathlength = "Solution Path Length: " + str(len(self.solutions[0])-1) + " moves." + "\n"
            Strings.append(solpathlength)

            solpath = "Solution Path: " + self.getsolmoves() + "\n"
            Strings.append(solpath)


            sol = self.getboardline()
            Strings.append(sol)

            fuelline2 = "Car Fuel Remaining: "
            finalboard = self.solutions[0][0]
            for car in finalboard.cars:
                fuelline2 += car.name + ":" + str(car.fuel) + " "

            Strings.append(fuelline2)

            finalbline = self.solutions[0][0].returnboardconfig() + "\n"
            Strings.append(finalbline)

        return Strings


        # function F = G(x) + H(x)

    def costFunction(self,cost, board, i):
        if i == 1:
            h = board.getNumberOfblockedvehicles()
        elif i == 2:
            h = board.getblockedpositions()
        elif i == 3:
            h = board.heuresticThree()
        elif i == 4:
            h = board.heuresticFour()

        g = cost + 1
        f = g + h
        return f
        pass

    def returng(self,cost):
        g = cost + 1
        return g

    def returnh(self,board,i):
        if i == 1:
            h = board.getNumberOfblockedvehicles()
        elif i == 2:
            h = board.getblockedpositions()
        elif i == 3:
            h = board.heuresticThree()
        elif i == 4:
            h = board.heuresticFour()
        return h


    def writeSearch(self):
        Strings = []
        text = "--------------------------------------------------------------------"
        initialboard = self.searchpath[0][1]
        text += "".join(itertools.chain(*initialboard.boardState.board))
        if self.numOfSolution == 0:

            Strings.append("No Solution")
            return Strings
        else:

            for solution in self.searchpath:
                string = "" + str(solution[1].stateCost) + " " + str(solution[1].g) + " " + str(solution[1].h) + " " + solution[1].boardState.returnstring()
                Strings.append(string)
                # print(solution[1].stateCost,solution[1].g,solution[1].h, end = "")
                # print("".join(itertools.chain(*solution[1].boardState.board)))

        return Strings

    def getsolmoves(self):
        line = ""
        for node in reversed(self.solutionPath):
            for nodes in reversed(node):
                if nodes.move is not None:
                    line += nodes.move[0]
                    line += " " + str(nodes.move[1])
                    line += " " + str(nodes.move[2])
                    line += "; "
        return line

    def getboardline(self):
        line = ""
        for node in reversed(self.solutionPath):
            print(node)
            for nodes in reversed(node):
                if nodes.move is not None:
                    line += nodes.move[0]
                    line += " " + str(nodes.move[1])
                    line += " " + str(nodes.move[2])
                    line += "\t\t"

                    for row in nodes.boardState.board:
                        for cell in row:
                            line += str(cell)

                line += "\n"

        return line


    def getboardline2(self):
        line = ""

        for i in range(len(self.solutionPath[0])-1):
            for nodes in self.solutionPath[0]:
                if nodes.move is not None:
                    line += nodes.move[0]
                    line += " " + str(nodes.move[1])
                    line += " " + str(nodes.move[2])
                    line += "\t\t"

                    for row in nodes.boardState.board:
                        for cell in row:
                            line += str(cell)

                line += "\n"

            return line

