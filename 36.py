st=input()
a=b=c=0
for i in range(0,len(st)):
	if st[i].isalpha():
		a=a+1
if st[i].isnumeric():
	b=b+1
else:
	c=c+1
print(c)
