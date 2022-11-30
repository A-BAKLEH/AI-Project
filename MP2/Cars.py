class Car:
    def __init__(self, name, fuel, cells=None, orientation=None):
        self.name = name
        self.fuel = fuel
        self.cell_list = []
        self.orientation = None
        if cells is None:
            cells = []
            orientation = None
        else:
            for i in cells:
                self.cell_list.append(i)

            if self.cell_list[0][0] == self.cell_list[1][0]:
                self.orientation = "Horizontal"
            else:
                self.orientation = "Vertical"

    def printCarInfo(self):
        print("Name: " + self.name, ", Fuel: ", self.fuel, ", Cells: ", self.cell_list, " Orientation : ", self.orientation)

    def carOrientation(self):
        if self.cell_list[0][0] == self.cell_list[1][0]:
            print("Horizontal")
            self.orientation = "Horizontal"
        else:
            print("Vertical")
            self.orientation = "Vertical"







