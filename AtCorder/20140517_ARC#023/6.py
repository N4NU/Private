import math
days=raw_input()
diary=map(int,raw_input().split())
fl=0
count=0
losedays=0
for i in diary:
	if(i==-1 and fl==0):
		fl=1
		count=count+1
		start=pres
	elif(i==-1 and fl==1):
		count=count+1
	elif(fl==1):
		sum=1
		total=i-start+1
		if(total<count):
			count=total
		while count>0:
			if(count==1):
				sum=sum+total
			else:
				sum=sum*total
				count=count-1
		losedays=losedays+sum
		fl=0
		count
	else:
		pres=i
print losedays%1000000007
raw_input()

