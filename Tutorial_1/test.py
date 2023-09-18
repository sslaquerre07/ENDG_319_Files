o_list = ['/', '*']
n_list = [4, 1, 7]
result = 0
op_1 = ["*", "/"]
op_2 = ["+", "-"]

if o_list[1] in op_1:
    if o_list[1] == "*":
        result = n_list[1] * n_list[2]
    else:
        result = n_list[1] // n_list[2]  
    if o_list[0] in op_1:
        if o_list[0] == "*":
            result *= n_list[0]
        else:
            result //= n_list[0]
    else:
        if o_list[0] == "+":
            result += n_list[0]
        else:
            result -= n_list[0]
            
else:
    if o_list[0] in op_1:
        if o_list[0] == "*":
            result = n_list[0] * n_list[1]
        else:
            result = n_list[0] // n_list[1]  
        if o_list[1] in op_1:
            if o_list[1] == "*":
                result *= n_list[2]
            else:
                result //= n_list[2]
        else:
            if o_list[1] == "+":
                result += n_list[2]
            else:
                result -= n_list[2]
    else: 
        if o_list[0] == "+":
            result = n_list[0] + n_list[1]
        else:
            result = n_list[0] - n_list[1]  
        if o_list[1] in op_1:
            if o_list[1] == "*":
                result *= n_list[2]
            else:
                result //= n_list[2]
        else:
            if o_list[1] == "+":
                result += n_list[2]
            else:
                result -= n_list[2]
                
print(result)