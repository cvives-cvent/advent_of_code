#part 1
'''with open("input_2.txt","r") as f:
    lines = f.readlines()
    map_dict = {"X":"A", "Y":"B", "Z":"C"}
    point_dict = {"X":1,"Y":2, "Z":3}
    curr_score = 0
    for line in lines:
        op1, op2 = line.strip().split()

        if op1==map_dict[op2]:
            curr_score+=3
            curr_score+=point_dict[op2]
        elif op1=="A" and map_dict[op2]=="B":
            curr_score += 6
            curr_score += point_dict[op2]
        elif op1=="B" and map_dict[op2]=="C":
            curr_score += 6
            curr_score += point_dict[op2]
        elif op1=="C" and map_dict[op2]=="A":
            curr_score += 6
            curr_score += point_dict[op2]
        else:
            curr_score += point_dict[op2]
    print(curr_score)'''

#part 2
with open("input_2.txt","r") as f:
    lines = f.readlines()
    win_dict = {"A":"B", "B":"C", "C":"A"}
    lose_dict = {"A":"C","B":"A", "C":"B"}
    point_dict = {"A":1,"B":2, "C":3}
    curr_score = 0
    for line in lines:
        op1, op2 = line.strip().split()
        #win
        if op2=="Z":
            curr_score += 6
            curr_score += point_dict[win_dict[op1]]
        #draw
        elif op2=="Y":
            curr_score += 3
            curr_score += point_dict[op1]
        else:
            curr_score += point_dict[lose_dict[op1]]
    print(curr_score)