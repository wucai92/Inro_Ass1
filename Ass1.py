majigs_list = ['object_1', 'object_2', 'object_3', 'object_4', 'object_5']

majigs_list.append('thingy')
majigs_list.append('whatsit')

print(majigs_list)

majigs_list.remove('object_2')

print(majigs_list)

def confirm_quan():
    quan = int(input('How many would you like to buy?'))
    print('you have ordered', quan, 'items, thank you!')
    return quan

# confirm_quan()

def cal_sum():
    quan = int(input('How many would you like to buy?'))
    price = 10
    print('you have ordered', quan, 'items, the total cost will be $', quan*price, ', thank you!')
    return quan * price

price = cal_sum()
print(price)

majigs_storage = [10,3,13,11,0,4]

with open ('inventory.txt','w') as myFile:
    for i in range(len(majigs_list)):
        myFile.write(majigs_list[i] + ': ' + str(majigs_storage[i])+'\n')

with open ('inventory.txt','r') as myFile:
    data = myFile.read()
print(data)

def check_inventory(file):
    with open(file, 'r') as myFile:
        for line in myFile:
            line = line.strip()
            storage = int(line.split(": ")[1])
            if storage < 5 and storage != 0:
                print(line + ' LOW!')
            elif storage == 0:
                print(line + ' OUT!')

check_inventory('inventory.txt')

filename = 'staff_list.txt'
def create_staff_list(txt):
    name = input('please enter the name: ')
    with open(txt, 'w') as myFile:
        while name != 'DONE':
            myFile.write(name + '\n')
            name = input('please enter the next name: ')
    with open(txt, 'r') as myFile:
        data = myFile.read()
        print(data)

create_staff_list(filename)

with open(filename, 'r') as myFile:
    data = myFile.read()
    print(data)

items = [['magic','10','0'], ['hero','15','0'], ['prince','12','0'], ['monster','8','0'], ['thingy','18','0']]



def get_totalprice(list):
    ask_items = input('Which item do you want to buy?enter no if you do not want to buy')
    for i in range (len(list)):
        if list[i][0] == ask_items:
            list[i][2] = list[i][1] * int(input('how many would you want to buy?'))

        if ask_items == 'magic':
            prices[0] = ask_quantity * 20


        elif ask_items == 'hero':
            prices[1] = ask_quantity * 12
            aget_totalprice()

        elif ask_items == 'prince':
            prices[2] = ask_quantity * 13
            get_totalprice()
        elif ask_items == 'monster':
            prices[3] = ask_quantity * 15
            get_totalprice()

        elif ask_items == 'thingy':
            prices[4] = ask_quantity * 25
            get_totalprice()

        elif ask_items == 'whatlist':
            price[5] = ask_quantity * 10
            get_totalprice()

    return sum(prices)


print(get_totalprice())