p=[1,2,3,4,5,6]
def sum_list(p):
	result=0
	for chiffre in p:
		result=result+chiffre
	return result
print(sum_list(p))