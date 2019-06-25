j=input()
i=0
for a in range (len(j)):
 if(j[a].isdigit() or j[a].isalpha() or j[a]==' '):
  continue
 else:
  i+=1
print(i)  
