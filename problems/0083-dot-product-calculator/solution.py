import numpy as np

def calculate_dot_product(vec1, vec2):
	n = len(vec1)
	ans = []
	for i in range(n):
		ans.append(vec1[i] * vec2[i])
	
	return sum(ans)