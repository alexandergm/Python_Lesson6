list1 = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

lenght: int = len(list1)
store_id = id(list1)
for i in range(lenght):
    entity = list1.pop(0)
    if  entity.isdigit():
        list1.append(F'"{int(entity):02d}"')
    elif entity[0] == "+" and entity[1].isdigit():
        list1.append(F'"+{int(entity):02d}"')
    else:
        list1.append(entity)
print(' '.join(list1))
