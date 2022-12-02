
import Board as bd
import Algorithm as alg
import PuzzleGenerator as pz
import xlsxwriter

if __name__ == "__main__":
    input_directory = ""

    output_directory = "Outputs/"

    inputFile = open(input_directory+"sample-input.txt", 'r')

    boards = []

    # Identifying the lines in the output
    for line in inputFile.readlines():
        if line[0] != '#' and line.strip() != "":
            board = bd.Board(line)
            boards.append(board)
            if line[37:].strip() != "":
                board.setfuels(line[37:])

    for i in range(len(boards)):
        solfileUCS = open(output_directory + "ucs-sol-" + str(i+1) + ".txt", 'w')
        searchfileUCS = open(output_directory + "ucs-search-" + str(i+1) + ".txt", 'w')

        ucs = alg.UniformedCostSearch(boards[i])
        ucs.search()

        gbfs = alg.GreedyBestFirstSearch(boards[i])

        astar = alg.Astar(boards[i])

        for j in range(4):

            solfileGBFS = open(output_directory + "gbfs-h" + str(j+1) + "-sol-" + str(i+1) + ".txt", 'w')
            serfileGBFS = open(output_directory + "gbfs-h" + str(j+1) + "-search-" + str(i+1) + ".txt", 'w')

            solfileAstar = open(output_directory + "astar-h" + str(j+1) + "-sol-" + str(i+1) + ".txt", 'w')
            serfileAstar = open(output_directory + "astar-h" + str(j+1) + "-search-" + str(i+1) + ".txt", 'w')

            gbfs.search(j+1)
            astar.search(j+1)

            for linesGBFS in gbfs.writeSolution():
                solfileGBFS.write(linesGBFS + "\n")
            for linesGBFS in gbfs.writeSearch():
                serfileGBFS.write(linesGBFS + "\n")

            for linesAstar in astar.writeSolution():
                solfileAstar.write(linesAstar + "\n")
            for linesAstar in astar.writeSearch():
                serfileAstar.write(linesAstar + "\n")



        for lines in ucs.writeSolution():
            solfileUCS.write(lines + "\n")

        for lines in ucs.writeSearch():
            searchfileUCS.write(lines + "\n")


    databook = xlsxwriter.Workbook('Outputs/Datasheet.xlsx')
    datasheet = databook.add_worksheet()

    datasheet.write('A1','Puzzle Number')
    datasheet.write('B1','Algorithm')
    datasheet.write('C1','Heuristic')
    datasheet.write('D1','Solution Length')
    datasheet.write('E1','SearchPath Length')
    datasheet.write('F1','Execution Time')

    row = 1

    for i in range(50):
        puzzle = pz.puzzleGenerator()
        puzzle.numVehiclesRange = [8,12]
        boardGen = puzzle.generateBoard()

        ucsSolver = alg.UniformedCostSearch(boardGen)
        ucsSolver.search()

        datasheet.write(row,0,i+1)
        datasheet.write(row,1,"UCS")
        datasheet.write(row,2,"N/A")
        datasheet.write(row,3,int(ucsSolver.solutionPathLength()))
        datasheet.write(row,4,ucsSolver.spathlength)
        datasheet.write(row,5,ucsSolver.runtime)
        row += 1

        for j in range(4):
            gbfsSolver = alg.GreedyBestFirstSearch(boardGen)

            gbfsSolver.search(j+1)

            datasheet.write(row, 0, i + 1)
            datasheet.write(row, 1, "GBFS")
            datasheet.write(row, 2, j+1)
            datasheet.write(row, 3, int(gbfsSolver.solutionPathLength()))
            datasheet.write(row, 4, gbfsSolver.spathlength)
            datasheet.write(row, 5, gbfsSolver.runtime)

            row += 1
        for j in range(4):
            aStarSolver = alg.Astar(boardGen)
            aStarSolver.search(j+1)

            datasheet.write(row, 0, i + 1)
            datasheet.write(row, 1, "A*")
            datasheet.write(row, 2, j+1)
            datasheet.write(row, 3, int(aStarSolver.solutionPathLength()))
            datasheet.write(row, 4, aStarSolver.spathlength)
            datasheet.write(row, 5, aStarSolver.runtime)
            row +=1

    databook.close()

