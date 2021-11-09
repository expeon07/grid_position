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
        # TODO break long lines
        y = int(starting_position[1]) - ((string.ascii_uppercase.index(letter)) * spacing)

        if letter == "I":
            break

        for i in range(1, 13):
            x = int(starting_position[0]) + ((i - 1) * spacing)
            point_name = letter + str(i) 
            grid_coordinates[point_name] = (x,y)
            
    # print(grid_coordinates)
    return grid_coordinates


def get_location(grid: Dict, point: str) -> tuple:
    """ Prints the location of the requested point

        Args:
            grid (Dict): Dictionary of point names and coordinates
            point (str): Point name

        Returns: 
            1 if error
    """

    x, y = grid[point]

    return (x, y)


def print_grid(grid: Dict):
    """ Displays the grid in a simple graph

    Args:
        grid (Dict): [description]

    Returns: none

    """

    # print(grid)
    coordinates = []
    for coordinate in grid.values():
        coordinates.append(coordinate)

    plt.scatter(*zip(*coordinates))

    for name in grid:
        plt.annotate(name, (grid[name][0], grid[name][1]))

    plt.show()


if __name__ == "__main__":
    
    point_err_mess = "Value should be an integer in the range [-1000, 1000]."
    starting_x_pos = None
    while (starting_x_pos == None):
        try: 
            starting_x_pos = int(input("Select starting x position for A1: "))

            if (starting_x_pos > 1000) or (starting_x_pos < -1000): 
                print(point_err_mess) 
                starting_x_pos = None

        except ValueError:
            print(point_err_mess) 
            starting_x_pos = None

    starting_y_pos = None
    while (starting_y_pos == None):
        try: 
            starting_y_pos = int(input("Select starting y position for A1: "))

            if (starting_x_pos > 1000) or (starting_x_pos < -1000): 
                print(point_err_mess) 
                starting_y_pos = None

        except ValueError:
            print(point_err_mess) 
            starting_y_pos = None

    spacing = -1
    while (spacing <= 0):
        try: 
            spacing = int(input("Select spacing for x and y: "))

        except ValueError:
            print("Spacing should be a positive integer.") 
            spacing = -1

    # Make the grid
    grid = assign_coordinates((int(starting_x_pos), int(starting_y_pos)), int(spacing))

    # Ask if user wants to show map
    show_map = input("Show map? (Y/N) ")
    if show_map == "Y":
        print_grid(grid)
    
    # Get location of a desired point
    location = (None, None)
    while (location == (None, None)):
        try: 
            point = input("Which point do you want to locate in this grid? ")
            location = get_location(grid, point)
            print(location)
        except KeyError:
            print("Please enter any point name from A1, A2, A3,..., H12.")

