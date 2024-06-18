def bfs(array_2d,start_col,start_row,find_exit=False):
 rows,cols=len(array_2d),len(array_2d[0]) 
 v=[[False for _ in range(cols)] for _ in range(rows)]
 m=0
 d=[(-1,0),(1,0),(0,-1),(0,1)]
 q=[(start_row,start_col,m)]
 v[start_row][start_col]=True
 while q:
  row,col,m=q.pop(0)
  if not find_exit and array_2d[row][col]==1:return [[col,row],m]
  elif find_exit and col==len(array_2d[0])-1 and row==0:return [[col,row],m]
  for dr,dc in d:
   new_row,new_col=row + dr,col + dc
   if 0<=new_row<rows and 0<=new_col<cols and not v[new_row][new_col] and array_2d[new_row][new_col]!=4:
    q.append((new_row,new_col,m+1))
    v[new_row][new_col]=True
file,c_g,c_f,s_i,g_m=open("example.txt"),[],[],[-1,-1,-1],0
lines=file.readlines()
for i,line in enumerate(lines):
 if "G" in line or i==len(lines)-1:
    if c_f:
     c_g.append(c_f)
     _,f_m=bfs(c_f,s_i[0],s_i[1],True)
     g_m+=f_m+1
     print(f"Escaped in {g_m} moves")
    s_i,c_g,g_m,c_f=[-1,-1,-1],[],0,[]
 if "F" in line:
  if c_f:
   c_g.append(c_f)
  if s_i[0] != -1: 
   one_index,f_m=bfs(c_f,s_i[0],s_i[1])
   s_i,c_f=[one_index[0],one_index[1],s_i[2] + 1],[]
   g_m+=f_m+1
 if "R" in line:
  nums=line.split(':')[1].strip()
  row=[int(x) for x in nums.split(' ')]
  c_f.append(row)
  if 3 in row:
   s_i[0],s_i[1],s_i[2]=row.index(3),len(c_f)-1,len(c_g)