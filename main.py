"""_Snapchat Islands_

Count the number of islands on a two dimensional grid. 1 is land: 0 is water.
Any land connected horizontally or vertically belongs to the same Island.
"""

import numpy as np
from numpy.typing import NDArray


def mark_island(map: NDArray[np.int_], point: tuple[int, int], number: int) -> None:
    """Mark all patches of land constituting an island

    Args:
        map (NDArray[np.int_]): The array representing land = 1 and water = 0
        point (tuple[int, int]): point of departure for exploring an island.
        number (int): positive integer representing the first, second or third Island that has been detected.

    Raises:
        ValueError: tuple does not represent point inside the map.
    """
    height, width = map.shape

    # check whether the tuple is inside the map

    if point[0] < 0 or point[0] >= height:
        raise ValueError(f"point {point} not inside map {map}.")
    if point[1] < 0 or point[1] >= width:
        raise ValueError(f"point {point} not inside map {map}.")
    if number < 1:
        raise ValueError(f"number {number} must be a positive integer.")

    # If the point represents water then do not look for connected islands.
    if map[point[0], point[1]] <= 0:
        return

    # Mark patches of land with a negative number, in order to indicate that the Island
    # has been visited before and the patch does not represent a new Island.
    if map[point[0], point[1]] == 1:
        map[point[0], point[1]] = -number

    # Search for patches of land in the neighborhood of the marked patch.
    # Check point one row up
    if point[0] - 1 >= 0 and map[point[0] - 1, point[1]] == 1:
        new_point = (point[0] - 1, point[1])
        mark_island(map, new_point, number)

    # Check point one row down

    if point[0] + 1 < height and map[point[0] + 1, point[1]] == 1:
        new_point = (point[0] + 1, point[1])
        mark_island(map, new_point, number)

    # Check point to the left
    if point[1] - 1 >= 0 and map[point[0], point[1] - 1] == 1:
        new_point = (point[0], point[1] - 1)
        mark_island(map, new_point, number)

    # Check point to the right
    if point[1] + 1 < width and map[point[0], point[1] + 1] == 1:
        new_point = (point[0], point[1] + 1)
        mark_island(map, new_point, number)


def main():
    print("Hello from snapchat-islands!")

    map = np.array(
        [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [0, 1, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1],
        ]
    )

    # Loop through all positions to find islands
    island_count = 0
    for (row, col), value in np.ndenumerate(map):
        if value == 1:  # Found unmarked land
            island_count += 1
            mark_island(map, (row, col), island_count)

    print(f"Found {island_count} islands")
    print("Marked map:")
    print(map)
    
    return island_count


if __name__ == "__main__":
    main()
