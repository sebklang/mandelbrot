import sys

W = int(sys.argv[1])
H = W
maxiter = int(sys.argv[2])

image = open("image.pbm", "w")
image.write("P1 " + str(W) + " " + str(H))

for i in range(W * H):
	y = (4 / W) * (i % int(W)) - 2
	x = (4 / H) * ((i - y) / W) - 2
	c = complex(x, y)
	z, escaped = c, False
	
	for j in range(maxiter):
		z = z**2 + c
		if abs(z) > 2:
			escaped = True
			break

	if escaped:	image.write(" 1")
	else:		image.write(" 0")
