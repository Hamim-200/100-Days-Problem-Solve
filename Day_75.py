# Converting a list into a string
list = ["P","Y","T","H","O","N"]
converted_string = "".join(list)
print(converted_string)
print(type(converted_string))

#Adding Two List Elements Together
lst1 = [1,2,3]
lst2 = [4,5,6]

main_list = []
for i in range(0,len(lst1)):
    main_list.append(lst1[i] + lst2[i])
print(main_list)

