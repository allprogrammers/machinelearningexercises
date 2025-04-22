import numpy as np
from typing import List, Tuple, Dict

def read_file(filename: str) -> Tuple[int, List[Tuple[int, int]]]:
    """Reads the file and returns the room size and list of lightspot coordinates."""
    with open(filename, 'r') as file:
        lines = file.readlines()
        N = int(lines[0].strip())
        lightspots = [tuple(map(int, line.strip().split())) for line in lines[1:]]
    return N, lightspots

def compute_light_matrix_list(N: int, lightspots: List[Tuple[int, int]]) -> List[List[float]]:
    """Computes the light intensity matrix using a list of lists."""
    room = [[0.0 for _ in range(N)] for _ in range(N)]
    intensity_pattern = [
        [0.2, 0.2, 0.2, 0.2, 0.2],
        [0.2, 0.5, 0.5, 0.5, 0.2],
        [0.2, 0.5, 1.0, 0.5, 0.2],
        [0.2, 0.5, 0.5, 0.5, 0.2],
        [0.2, 0.2, 0.2, 0.2, 0.2],
    ]

    for x, y in lightspots:
        for i in range(-2, 3):
            for j in range(-2, 3):
                nx, ny = x + i, y + j
                if 0 <= nx < N and 0 <= ny < N:
                    room[nx][ny] += intensity_pattern[i + 2][j + 2]
    return room

def compute_light_matrix_dict(N: int, lightspots: List[Tuple[int, int]]) -> Dict[Tuple[int, int], float]:
    """Computes the light intensity matrix using a dictionary of keys."""
    room = {(i, j): 0.0 for i in range(N) for j in range(N)}
    intensity_pattern = [
        [0.2, 0.2, 0.2, 0.2, 0.2],
        [0.2, 0.5, 0.5, 0.5, 0.2],
        [0.2, 0.5, 1.0, 0.5, 0.2],
        [0.2, 0.5, 0.5, 0.5, 0.2],
        [0.2, 0.2, 0.2, 0.2, 0.2],
    ]

    for x, y in lightspots:
        for i in range(-2, 3):
            for j in range(-2, 3):
                nx, ny = x + i, y + j
                if 0 <= nx < N and 0 <= ny < N:
                    room[(nx, ny)] += intensity_pattern[i + 2][j + 2]
    return room

def compute_light_matrix_numpy(N: int, lightspots: List[Tuple[int, int]]) -> np.ndarray:
    """Computes the light intensity matrix using a 2D NumPy array."""
    room = np.zeros((N, N), dtype=float)

    for x, y in lightspots:
        for i in range(-2, 3):
            for j in range(-2, 3):
                nx, ny = x + i, y + j
                if 0 <= nx < N and 0 <= ny < N:
                    room[nx, ny] += 0.2 if abs(i)>1 or abs(j)>1 else (0.5 if abs(i)==1 or abs(j)==1 else 1.0)
    return room

def print_matrix_list(matrix: List[List[float]]) -> None:
    """Prints the light intensity matrix (list of lists)."""
    for row in matrix:
        print(" ".join(f"{value:.1f}" for value in row))

def print_matrix_dict(matrix: Dict[Tuple[int, int], float], N: int) -> None:
    """Prints the light intensity matrix (dictionary of keys)."""
    for i in range(N):
        row = [matrix[(i, j)] for j in range(N)]
        print(" ".join(f"{value:.1f}" for value in row))

def print_matrix_numpy(matrix: np.ndarray) -> None:
    """Prints the light intensity matrix (NumPy array)."""
    for row in matrix:
        print(" ".join(f"{value:.1f}" for value in row))

def main() -> None:
    filename = "spotlight.txt"
    N, lightspots = read_file(filename)

    # Using list of lists
    print("Using list of lists:")
    light_matrix_list = compute_light_matrix_list(N, lightspots)
    print_matrix_list(light_matrix_list)

    print("\nUsing dictionary of keys:")
    # Using dictionary of keys
    light_matrix_dict = compute_light_matrix_dict(N, lightspots)
    print_matrix_dict(light_matrix_dict, N)

    print("\nUsing NumPy array:")
    # Using NumPy array
    light_matrix_numpy = compute_light_matrix_numpy(N, lightspots)
    print_matrix_numpy(light_matrix_numpy)

if __name__ == "__main__":
    main()