KATZ_DELI = []
OTHER_DELI = ["Logan", "Avi", "Spencer"]


def line(local_deli):
    katz_deli = local_deli
    
    if not katz_deli:
        print("The line is currently empty.") 
    else:
        num = [f'{line_no[0]}. {line_no[1]}' for line_no in enumerate(katz_deli, 1)]
        message =  f'The line is currently: {" ".join(num)}'
        print(message)  

def take_a_number(list,name):
    deli_line = list
    deli_line.append(name)
    customers = [
        f'Welcome, {num[1]}. You are number {num[0]} in line.' for num in enumerate(deli_line, 1) if num[1] == name ]
    print(''.join(customers))
    pass

def now_serving(list):
    new_list = list
    if not new_list:
        print("There is nobody waiting to be served!")
    else:
        print(f'Currently serving {new_list[0]}.')
        new_list.remove(new_list[0])







