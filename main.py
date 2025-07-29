"""_Snapchat Islands_

Count the number of islands on a two dimensional grid. 1 is land: 0 is water.
Any land connected horizontally or vertically belongs to the same Island.
"""

import numpy as np
from numpy.typing import NDArray


def mark_island(matrix: NDArray[np.int_], point: tuple[int, int], number: int) -> None:
    """Mark all patches of land constituting an island

    Args:
        matrix (NDArray[np.int_]): The array representing land = 1 and water = 0
        point (tuple[int, int]): point of departure for exploring an island.
        number (int): positive integer representing the first, second or third Island that has been detected.

    Raises:
        ValueError: number is not positive
    """
    row, col = point
    height, width = matrix.shape

    # Validate number parameter
    if number < 1:
        raise ValueError(f"number {number} must be a positive integer.")

    # Base case: out of bounds, water, or already visited
    if row < 0 or row >= height or col < 0 or col >= width or matrix[row, col] <= 0:
        return

    # Mark this land cell as visited
    matrix[row, col] = -number

    # Recursively explore all 4 directions
    mark_island(matrix, (row - 1, col), number)  # up
    mark_island(matrix, (row + 1, col), number)  # down
    mark_island(matrix, (row, col - 1), number)  # left
    mark_island(matrix, (row, col + 1), number)  # right


def count_islands(matrix: NDArray[np.int_]) -> tuple[int, NDArray[np.int_]]:
    """Count the number of islands in a 2D grid.

    Args:
        matrix: 2D array where 1 represents land and 0 represents water

    Returns:
        Number of islands found

    Raises:
        ValueError: If matrix is not 2D or contains invalid values
    """
    if matrix.ndim != 2:
        raise ValueError("matrix must be a 2D array")

    if not np.all((matrix == 0) | (matrix == 1)):
        raise ValueError("matrix must contain only 0s (water) and 1s (land)")

    # Make a copy to avoid modifying the original
    working_matrix = matrix.copy()

    island_count = 0
    for (row, col), value in np.ndenumerate(working_matrix):
        if value == 1:  # Found unmarked land
            island_count += 1
            mark_island(working_matrix, (row, col), island_count)

    return island_count, working_matrix


def main():
    """Demonstrate island counting with a sample grid."""
    print("Hello from snapchat-islands!")

    sample_matrix = np.array(
        [
            [1, 1, 0, 0, 0],
            [1, 1, 0, 0, 1],
            [0, 1, 0, 1, 1],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1],
        ]
    )

    print("Original matrix:")
    print(sample_matrix)

    island_count, working_matrix = count_islands(sample_matrix)
    
    print("Labeled matrix:")
    print(working_matrix)
    print(f"\nFound {island_count} islands")

    return island_count, working_matrix


if __name__ == "__main__":
    main()
