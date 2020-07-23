def max_num(num1:int,num2:int)->int:
    max = num1 if num1 > num2 else num2
    return max
#print(help(max_num))
result= max_num(12,23)
print(result)