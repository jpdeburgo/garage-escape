def print_path(previous, start, end):
    print(f"Starting at {start[0]}, {start[1]}")
    path = []
    row, col = end
    while (row, col) is not None and (row, col) != start:
        path.append((row, col))
        row, col = previous[row][col]
    path.reverse()
    print(f"Path taken:{path}, total moves: {len(path)}")
    return path