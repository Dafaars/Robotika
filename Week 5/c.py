import numpy as np

def cell_decomposition(grid, start, goal):
    # Daftar jalur yang ditempuh
    path = []
    current = start
    
    while current != goal:
        path.append(current)
        # Gerakan sederhana ke arah tujuan
        if current[0] < goal[0] and grid[current[0] + 1][current[1]] == 0:
            current = (current[0] + 1, current[1])
        elif current[1] < goal[1] and grid[current[0]][current[1] + 1] == 0:
            current = (current[0], current[1] + 1)
        elif current[0] > goal[0] and grid[current[0] - 1][current[1]] == 0:
            current = (current[0] - 1, current[1])
        elif current[1] > goal[1] and grid[current[0]][current[1] - 1] == 0:
            current = (current[0], current[1] - 1)
        else:
            print("Tidak ada jalur bebas rintangan yang tersedia.")
            return None
    
    path.append(goal)
    return path

# Contoh grid (0 = cell bebas, 1 = rintangan)
grid = [
    [0, 0, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

# Penggunaan metode Cell Decomposition
start, goal = (0, 0), (4, 4)
path = cell_decomposition(grid, start, goal)
print(f"Jalur Cell Decomposition: {path}")
