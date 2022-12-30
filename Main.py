file = open('Actual_Input.txt', 'r')
lines = file.read()
print(lines)
calorie_list = []
#lines = int(float(lines))
for line in lines:
  if line.strip() == "":
    #calorie_list.append(sum)
    print(calorie_list)
