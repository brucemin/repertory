#求1！+2！+3！+4！+5！的和
s = 1
z = 0
for i in range(1,6):
    s = s*i
    z = z + s
print(z)