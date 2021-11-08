from typing import Dict
import string
import matplotlib.pyplot as plt


def assign_coordinates(starting_position: tuple, spacing: int) -> Dict:
    """ Assigns coordinates to the points 

        Args:
            starting_position (tuple): Coordinates of point A1
            spacing (int): Spacing per step on x columns and y rows

        Returns:
            grid_coordinates (Dict): Dictionary of point names and coordinates

    """

    grid_coordinates = {}

    for letter in string.ascii_uppercase:
        y = int(starting_position[1]) + ((string.ascii_uppercase.index(letter)) * spacing)

        if letter == "I":
            break

        for i in range(1, 13):
            x = int(starting_position[0]) - (i - 1) * spacing
            point_name = letter + str(i) 
            grid_coordinates[point_name] = (x,y)
            
    print(grid_coordinates)
    return grid_coordinates


def print_location(grid: Dict, point: str):
    """ Prints the location of the requested point

        Args:
            grid (Dict): Dictionary of point names and coordinates
            point (str): Point name

        Returns: none
    """

    x, y = grid[point]

    print( str(x) + ", " + str(y))


def print_grid(grid: Dict):
    """[summary]

    Args:
        grid (Dict): [description]

    Returns:

    """
    coordinates = [(x, y) for x, y in grid[1]]
    plt.scatter(*zip(*coordinates))

    for i, name in enumerate(grid):
        plt.annotate(name, (grid[i][name], grid[i][name]))


if __name__ == "__main__":

    ## TODO errors 
    
    starting_x_pos = input("Select starting x position for A1: ")
    starting_y_pos = input("Select starting y position for A1: ")

    spacing = input("Select spacing for x and y: ")
    grid = assign_coordinates( (int(starting_x_pos), int(starting_y_pos)), int(spacing))

    print_grid(grid)

    point = input("Which point do you want to locate in this grid? ")   # show grid

    print_location(grid, point)
