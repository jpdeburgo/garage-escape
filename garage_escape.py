from print_path import print_path
def bfs_find_one(array_2d, start_col, start_row, find_exit=False):
    rows, cols = len(array_2d), len(array_2d[0]) 
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    previous = [[None for _ in range(cols)] for _ in range(rows)]  # To store the path
    moves = 0
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = [((start_row, start_col), moves)]
    visited[start_row][start_col] = True
    while queue:
        (row, col), moves = queue.pop(0)
        if not find_exit and array_2d[row][col] == 1: 
            print_path(previous, (start_row, start_col), (row, col))
            return [[col, row], moves]
        elif find_exit and col == len(array_2d[0]) - 1 and row == 0:
            print_path(previous, (start_row, start_col), (row, col))
            return [[col, row], moves]
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col] and array_2d[new_row][new_col] != 4:
                queue.append(((new_row, new_col), moves + 1))
                visited[new_row][new_col] = True
                previous[new_row][new_col] = (row, col)
    return None
garage_escape_file = open("randall-tramia-cases.txt")
curr_garage = []
curr_floor = []
start_index = [-1,-1,-1]
garage_moves = 0
lines = garage_escape_file.readlines()
for i, line in enumerate(lines):
    if "garage" in line.lower() or i == len(lines) - 1:
        if curr_floor:
            curr_garage.append(curr_floor)
            final_index, floor_moves = bfs_find_one(curr_floor, start_index[0], start_index[1], True)
            garage_moves+=floor_moves+1
            print(f"Escaped in {garage_moves} moves")
        start_index = [-1,-1,-1]
        curr_garage = []
        garage_moves = 0
        curr_floor = []
    if "floor" in line.lower():
        if curr_floor:
            curr_garage.append(curr_floor)
        if start_index[0] != -1: 
            garage_moves+=1
            one_index, floor_moves = bfs_find_one(curr_floor, start_index[0], start_index[1])
            start_index = [one_index[0], one_index[1], start_index[2] + 1]
            garage_moves+=floor_moves
        curr_floor = []
    if "row" in line.lower():
        numbers = line.split(':')[1].strip()
        row = [int(x) for x in numbers.split(' ')]
        curr_floor.append(row)
        if 3 in row:
            start_index[0] = row.index(3)
            start_index[1] = len(curr_floor) - 1
            start_index[2] = len(curr_garage)