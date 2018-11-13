numberOfRows = int(input())
qaly = 0.0

while numberOfRows > 0:
  line = input().split()
  qaly += (float(line[0]) * float(line[1]))
  numberOfRows -= 1

print(qaly)