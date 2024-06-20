l,lines,c_g,c_f,s_i,g_m=len,open("example.txt").readlines(),[],[],[-1,-1,-1],0
def bfs(arr,s_c,s_r,f_e='F'):
 rows,cols=l(arr),l(arr[0]);v,m,d=[['F' for _ in range(cols)] for _ in range(rows)],0,[(-1,0),(1,0),(0,-1),(0,1)];q=[(s_r,s_c,m)];v[s_r][s_c]='T'
 while q:
  row,col,m=q.pop(0)
  if f_e=='F' and arr[row][col]==1:return[[col,row],m]
  elif f_e and col==l(arr[0])-1 and row==0:return[[col,row],m]
  for dr,dc in d:
   nr,nc=row+dr,col+dc
   if 0<=nr<rows and 0<=nc<cols and v[nr][nc]=='F'and arr[nr][nc]!=4:q.append((nr,nc,m+1));v[nr][nc]='T'
for i,line in enumerate(lines):
 if "G"in line or i==l(lines)-1:
    if c_f:c_g.append(c_f);_,f_m=bfs(c_f,s_i[0],s_i[1],'T');g_m+=f_m+1;print(f"Escaped in {g_m} moves");s_i,c_g,g_m,c_f=[-1,-1,-1],[],0,[]
 if "F"in line:
  if c_f:c_g.append(c_f)
  if s_i[0]!=-1:idx,f_m=bfs(c_f,s_i[0],s_i[1]);s_i,c_f=[idx[0],idx[1],s_i[2]+1],[];g_m+=f_m+1
 if "R"in line:
  c_f.append([int(x) for x in line.split(':')[1].strip().split(' ')])
  if 3 in c_f[-1]:s_i=[c_f[-1].index(3),l(c_f)-1,l(c_g)]