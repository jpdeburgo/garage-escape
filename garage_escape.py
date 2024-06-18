def bfs_find_one(array_2d,start_col,start_row,find_exit=False):
 rows,cols=len(array_2d),len(array_2d[0])
 visited=[[False for _ in range(cols)]for _ in range(rows)]
 directions=[(-1,0),(1,0),(0,-1),(0,1)]
 queue=[((start_row,start_col),0)]
 visited[start_row][start_col]=True
 while queue:
  (row,col),moves=queue.pop(0)
  if not find_exit and array_2d[row][col]==1:return[[col,row],moves]
  elif find_exit and col==cols-1 and row==rows-1:return[[col,row],moves]
  for dr,dc in directions:
   new_row,new_col=row+dr,col+dc
   if 0<=new_row<rows and 0<=new_col<cols and not visited[new_row][new_col] and array_2d[new_row][new_col]!=4:
    queue.append(((new_row,new_col),moves+1))
    visited[new_row][new_col]=True
 return None
file,c_g,c_f,s_i,g_m=open("example.txt"),[],[],[-1,-1,-1],0
lines=file.readlines()
for i,line in enumerate(lines):
 if "garage" in line.lower() or i==len(lines)-1:
  if c_f:
   c_g.append(c_f)
   final_index,floor_moves=bfs_find_one(c_f,s_i[0],s_i[1],True)
   g_m+=floor_moves+1
   print(f"Escaped in {g_m} moves")
  s_i,c_g,g_m,c_f=[-1,-1,-1],[],0,[]
 if "floor" in line.lower():
  if c_f:c_g.append(c_f)
  if s_i[0]!=-1:
   g_m+=1
   one_index,floor_moves=bfs_find_one(c_f,s_i[0],s_i[1])
   s_i=[one_index[0],one_index[1],s_i[2]+1]
   g_m+=floor_moves
  c_f=[]
 if "row" in line.lower():
  row=[int(x)for x in line.split(':')[1].strip().split()]
  c_f.append(row)
  if 3 in row:s_i=[row.index(3),len(c_f)-1,len(c_g)]
