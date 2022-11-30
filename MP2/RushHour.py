
import Board as bd
import Algorithm as alg
import PuzzleGenerator as pz

if __name__ == "__main__":
    input_directory = ""

    output_directory = "Outputs/"

    outputfile = open(output_directory + "Astar.txt", 'w')

    inputFile = open(input_directory+"sample-input.txt", 'r')

    boards = []

    # Identifying the lines in the output
    for line in inputFile.readlines():
        if line[0] != '#' and line.strip() != "":
            board = bd.Board(line)
            boards.append(board)
            if line[37:].strip() != "":
                board.setfuels(line[37:])

    algorithm = alg.GreedyBestFirstSearch(boards[5])
    algorithm.search(3)
    algorithm.printSolutionsBoard()
    # for lines in algorithm.writeSolution():
    #     outputfile.write(lines)

    # solfileUCS = open(output_directory + "gbfs-h4-sol-" + str(1) + ".txt", 'w')
    # searchfileUCS = open(output_directory + "gbfs-h4-search-" + str(1) + ".txt", 'w')
    #
    # ucs = alg.GreedyBestFirstSearch(boards[0])
    # ucs.search(4)
    #
    # for lines in ucs.writeSolution():
    #     solfileUCS.write(lines + "\n")
    #
    # for lines in ucs.writeSearch():
    #     searchfileUCS.write(lines + "\n")

    # Printing all the boards one by one
    # for i in range(len(boards)):
    #     solfileUCS = open(output_directory + "ucs-sol-" + str(i+1) + ".txt", 'w')
    #     searchfileUCS = open(output_directory + "ucs-search-" + str(i+1) + ".txt", 'w')
    #
    #     ucs = alg.UniformedCostSearch(boards[i])
    #     ucs.search()
    #
    #     gbfs = alg.GreedyBestFirstSearch(boards[i])
    #
    #     astar = alg.Astar(boards[i])
    #
    #     for j in range(4):
    #
    #         solfileGBFS = open(output_directory + "gbfs-h" + str(j+1) + "-sol-" + str(i+1) + ".txt", 'w')
    #         serfileGBFS = open(output_directory + "gbfs-h" + str(j+1) + "-search-" + str(i+1) + ".txt", 'w')
    #
    #         solfileAstar = open(output_directory + "astar-h" + str(j+1) + "-sol-" + str(i+1) + ".txt", 'w')
    #         serfileAstar = open(output_directory + "astar-h" + str(j+1) + "-search-" + str(i+1) + ".txt", 'w')
    #
    #         gbfs.search(j+1)
    #         astar.search(j+1)
    #
    #         for linesGBFS in gbfs.writeSolution():
    #             solfileGBFS.write(linesGBFS + "\n")
    #         for linesGBFS in gbfs.writeSearch():
    #             serfileGBFS.write(linesGBFS + "\n")
    #
    #         for linesAstar in astar.writeSolution():
    #             solfileAstar.write(linesAstar + "\n")
    #         for linesAstar in astar.writeSearch():
    #             serfileAstar.write(linesAstar + "\n")
    #
    #
    #
    #     for lines in ucs.writeSolution():
    #         solfileUCS.write(lines + "\n")
    #
    #     for lines in ucs.writeSearch():
    #         searchfileUCS.write(lines + "\n")
    #

    # for i in range(50):
    #     puzzle = pz.puzzleGenerator()
    #     boardGen = puzzle.numVehiclesRange[8,15]
    #

    # algorithm.writeSolution()
    # puzzle = pz.puzzleGenerator()
    # puzzle.numVehiclesRange = [10,15]
    #
    # newBoard = puzzle.generateBoard()
    # newBoard.printBoard()
