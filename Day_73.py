# Finding The Maximum Number in a List

Number_List = [10,43,213,1,32,4,5,3,5,3,32,2,4123,543,2,354]
max = Number_List[0]
for num in Number_List:
    if max<num:
        max = num
print("Maximum Number is = ",max )



# Finding The Minimum Number in a List

Number_List = [10,43,213,1,32,4,5,3,5,3,32,2,4123,543,2,354]
min = Number_List[0]
for num in Number_List:
    if min>num:
        min = num
print("Minimum Number is = ",min )
