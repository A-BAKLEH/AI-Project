<h2> List of students working on the project:</h2>

| Full Names    |  Github Usernames | StudentID |
| ------------- | ------------- | ------------- |
| Athanas Bakleh    |[@A-BAKLEH](https://github.com/A-BAKLEH)| 40093110 |
| Omar Mahmoud   |[@OmarHesham123](https://github.com/OmarHesham123)| 40158127 |
| Mohammad Aamir Parekh   |[@Ap2603](https://github.com/Ap2603)| 40136289 |

<h2> URL to the repository (private):</h2>
https://github.com/A-BAKLEH/COMP472Project  

https://github.com/OmarHesham123/COMP472Project

<h2> How to run </h2>
1.) Open the main file, "RushHour.py"
In this file you can either generate a text file with puzzles, or provide your own input file
Once you run it, the search and solution files for these puzzles will be generated using all 3 search algorithms and all 4 heuristics.
These search and solution files will be written to the output folder

2.) The Board.py file contains all our game rules(moveCar,exploreMoves etc.), as well as the data structure for the board.
Each board is a 6x6 grid with cars on it, these cars being stored in a list
Each board also has a list of possible moves each car can make.
The Board class also contains the implementations for all 4 of our heuristics

3.) The Car.py file contains the data structure for each of our cars.
Each car has a list of cells it covers, a fuel value and an orientation

4.) The Algorithm.py file contains the implementations of all 3 of our search algorithms, as well as the writeSearch and writeSolution function for each.
This file also contains the node data structure, which has a boardstate,parent and cost. We use this data structure to store our various states and calculate the solutions based on their cost.

5.) The PuzzleGenerator.py file generates a text file containing the various puzzles we can test our algorithm on, and takes a minimum and maximum number of vehicles to populate the puzzle with.
