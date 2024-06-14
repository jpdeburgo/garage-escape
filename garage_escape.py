def bfs_find_one(array_2d, start_col, start_row, find_exit=False):
    rows, cols = len(array_2d), len(array_2d[0])
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    moves = 0
    
    # Directions for moving up, down, left, and right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = [(start_row, start_col)]
    visited[start_row][start_col] = True
    
    while queue:
        row, col = queue.pop(0)
        moves += 1
        
        if not find_exit and array_2d[row][col] == 1:
            return [[col, row], moves]
        elif find_exit and col == len(array_2d[0]) - 1 and row == len(array_2d) - 1:
            return [[col, row], moves]
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col]:
                queue.append((new_row, new_col))
                visited[new_row][new_col] = True
    
    return None

garage_escape_file = open("GarageEscape1Floor.txt")
curr_garage = []
curr_floor = []
start_index = [-1,-1,-1]
garage_moves = 0
for line in garage_escape_file:
    if "garage" in line.lower():
        start_index = [-1,-1,-1]
        curr_garage = []
    if "floor" in line.lower():
        if curr_floor:
            curr_garage.append(curr_floor)
        if start_index[0] != -1:
            one_index, floor_moves = bfs_find_one(curr_floor, start_index[0], start_index[1])
            print(f'Exit Found for floor {len(curr_garage)}')
            start_index = [one_index[0], one_index[1], start_index[2] + 1]
            garage_moves += floor_moves
        curr_floor = []
    if "row" in line.lower():
        numbers = line.split(':')[1].strip()
        row = [int(x) for x in numbers.split(' ')]
        curr_floor.append(row)
        if 3 in row:
            # col
            start_index[0] = row.index(3)
            # row
            start_index[1] = len(curr_floor) - 1
            # z index
            start_index[2] = len(curr_garage)

if curr_floor:
    curr_garage.append(curr_floor)

final_index, floor_moves = bfs_find_one(curr_floor, start_index[0], start_index[1], True)
print(f'Exit Found for floor {len(curr_garage)}')
print(f"Escaped in {garage_moves} moves")
print(start_index, garage_moves)


