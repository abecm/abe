a=[1,2,3]
b=[4,5,6]
def union(a,b):
	return a.append(b) or b.append(a)	
print(union(a,b))