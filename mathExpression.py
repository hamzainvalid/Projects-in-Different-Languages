x = 0
y = 0
z = 0
for i in range(1,100,+1):
    x = i
    for j in range(1,100,+1):
        y = j
        for k in range(1,100,+1):
            z = k
            if (x + y + z == 12) and (2*x - y == 12) and (3*y + z == 14):
                print(x, y, z)