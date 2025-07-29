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
        ValueError: number is not positive
    """
    row, col = point
    height, width = map.shape

    # Validate number parameter
    if number < 1:
        raise ValueError(f"number {number} must be a positive integer.")

    # Base case: out of bounds, water, or already visited
    if row < 0 or row >= height or col < 0 or col >= width or map[row, col] <= 0:
        return

    # Mark this land cell as visited
    map[row, col] = -number

    # Recursively explore all 4 directions
    mark_island(map, (row - 1, col), number)  # up
    mark_island(map, (row + 1, col), number)  # down
    mark_island(map, (row, col - 1), number)  # left
    mark_island(map, (row, col + 1), number)  # right


def count_islands(map: NDArray[np.int_]) -> int:
    """Count the number of islands in a 2D grid.

    Args:
        map: 2D array where 1 represents land and 0 represents water

    Returns:
        Number of islands found

    Raises:
        ValueError: If map is not 2D or contains invalid values
    """
    if map.ndim != 2:
        raise ValueError("Map must be a 2D array")

    if not np.all((map == 0) | (map == 1)):
        raise ValueError("Map must contain only 0s (water) and 1s (land)")

    # Make a copy to avoid modifying the original
    working_map = map.copy()

    island_count = 0
    for (row, col), value in np.ndenumerate(working_map):
        if value == 1:  # Found unmarked land
            island_count += 1
            mark_island(working_map, (row, col), island_count)

    return island_count


def main():
    """Demonstrate island counting with a sample grid."""
    print("Hello from snapchat-islands!")

    sample_map = np.array(
        [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [0, 1, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1],
        ]
    )

    print("Original map:")
    print(sample_map)

    island_count = count_islands(sample_map)

    print(f"\nFound {island_count} islands")

    return island_count


if __name__ == "__main__":
    main()
