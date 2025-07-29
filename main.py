"""_Snapchat Islands_

Count the number of islands on a two dimensional grid. 1 is land: 0 is water.
Any land connected horizontally or vertically belongs to the same Island.
"""

import numpy as np
from numpy.typing import NDArray


def mark_island(map: NDArray[np.int_], point: tuple[int, int], number: int) -> None:
    height, width = map.shape

    # check whether the tuple is inside the map

    if point[0] < 0 or point[0] >= height:
        raise ValueError(f"point {point} not inside map {map}.")
    if point[1] < 0 or point[1] >= width:
        raise ValueError(f"point {point} not inside map {map}.")

    if map[point[0], point[1]] <= 0:
        return

    if map[point[0], point[1]] == 1:
        map[point[0], point[1]] = -number

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

    print(map)

    # Loop through all positions to find islands
    island_count = 0
    for (row, col), value in np.ndenumerate(map):
        if value == 1:  # Found unmarked land
            island_count += 1
            mark_island(map, (row, col), island_count)

    print(f"Found {island_count} islands")
    print("Marked map:")
    print(map)


if __name__ == "__main__":
    main()
