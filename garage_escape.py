def bfs_find_one(array_2d, start):
    rows, cols = len(array_2d), len(array_2d[0])
    start_row, start_col = start
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    
    # Directions for moving up, down, left, and right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    queue = [(start_row, start_col)]
    visited[start_row][start_col] = True
    
    while queue:
        row, col = queue.pop(0)
        
        if array_2d[row][col] == 1:
            return (row, col)
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            
            if 0 <= new_row < rows and 0 <= new_col < cols and not visited[new_row][new_col]:
                queue.append((new_row, new_col))
                visited[new_row][new_col] = True
    
    return None

garage_escape_file = open("GarageEscape-1.txt")
curr_garage = []
curr_floor = []
start_index = [-1,-1,-1]
curr_moves = 0
for line in garage_escape_file:
    if "garage" in line.lower():
        start_index = [-1,-1,-1]
        curr_garage = []
    if "floor" in line.lower():
        curr_garage.append(curr_floor)
        curr_floor = []
    if "row" in line.lower():
        numbers = line.split(':')[1].strip()
        row = [int(x) for x in numbers.split(' ')]
        if 3 in row:
            start_index[0] = row.index(3)
            start_index[1] = len(curr_floor)
            start_index[2] = len(curr_garage)
            start_index = bfs_find_one(curr_garage, (start_index[0], start_index[1]))
        curr_floor.append(row)

print(curr_garage[start_index[2]][start_index[1]][start_index[0]], len(curr_garage))
print(start_index)


