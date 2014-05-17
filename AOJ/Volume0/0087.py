import sys
for line in sys.stdin.readlines():
	stack=[]
	for foo in line.strip().split():
		if foo=="+":
			foo=stack.pop()+stack.pop()
		elif foo=="-":
			foo=-(stack.pop()-stack.pop())
		elif foo=="*":
			foo=stack.pop()*stack.pop()
		elif foo=="/":
			foo=1.0/stack.pop()*stack.pop()
		stack.append(float(foo))
	print "{:.6f}".format(stack[0]+0)