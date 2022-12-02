#part 1
'''with open("input_1.txt","r") as f:
    x = f.readlines()
    curr_sum = 0
    calories = []
    for cal in x:
        cal = cal.strip()
        if cal =="":
            calories.append(curr_sum)
            curr_sum = 0

        else:
            curr_sum += int(cal)
    print(sorted(calories)[-1])'''

#part 2
with open("input_1.txt","r") as f:
    x = f.readlines()
    curr_sum = 0
    calories = []
    for cal in x:
        cal = cal.strip()
        if cal =="":
            calories.append(curr_sum)
            curr_sum = 0

        else:
            curr_sum += int(cal)
    print(sum(sorted(calories)[-3:]))