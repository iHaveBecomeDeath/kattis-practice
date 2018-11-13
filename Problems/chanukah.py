
for i in range(0, int(input())):
  in_data = input().split()
  days = [x for x in range(int(in_data[1])+1)]
  print(in_data[0] + ' ' + str(sum(days) + int(in_data[1])))
