#list datas tructure
my_list = ["totyota","bmw","tata","ford","mercedes","audi"]
my_list.append("mazda")

print(my_list)
print(my_list[0])
my_list[1] = "fiat"   #mutable
print(f"{my_list[1]} is manufactured in Bayerische, Germany")

#tuple datastructure
my_tuple = ("banana","apples","grapes","pears","kiwi","orange")
print(f"i like eating {my_tuple[3]}")
print(my_tuple)

#set datastructure
my_set = {"law","medicine","architecture","survey","economy","sociology"}
print(my_set)

#dictionary data structure
my_dict = {"name":"Kaku","Age":18,"Gender":"Prefer not to say"}
print(my_dict)
print(my_dict["Age"])
print(my_dict["Gender"])
print(f"My name is {my_dict[0]}, I'm {my_dict[1]}. For my gender,I{my_dict[3]}")