height=[0]*3
for i in range(10):
	tmp1=input()
	for j in range(3):
		if tmp1>height[j]:
			tmp2=height[j]
			height[j]=tmp1
			tmp1=tmp2
for i in range(3):
	print height[i]