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
