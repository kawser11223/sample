
student_array = []


def user_input_function():
    print("Options:")
    print("1. Enter Student Data")
    print("2. Display Student List")
    print("3. Check Order Number")
    print("4. Exit")
    
    option = input("Enter your choice (|1|2|3|4|): ")
    check_input_condition(option)

def check_by_order_number():
    order_num = input("please insert a order number to search: ")
    error_found = False

    for rows in student_array:
        try:
            if rows[order_num] is not None:
                print("Record found: {} - {}".format(order_num,rows[order_num]))
                user_input_function()
            else:
                check_by_order_number()
        except KeyError:
            pass
            error_found = True
    if error_found:
        print("Order number didnot found in program memory. ")
            
    print()
    user_input_function()

def take_student_data_input():
    order_number = ""
    student_name = ""

    while order_number != "exit":
        data = {}
        order_number = input("Please insert your order number: ")
        if order_number == 'exit':
            user_input_function()

        student_name = input("Please insert a student name: ")

        data[order_number] = student_name
        
        student_array.append(data)

def student_list_show():
    if len(student_array) == 0:
        print("No data found!!!")
    else:
        for row in student_array:
            print(row)
    print("")
    user_input_function()


def check_input_condition(option):
    if option == '1':
        take_student_data_input()
    elif option == '2':
        student_list_show()
    elif option == '3':
        check_by_order_number()
    else:
        return None

if __name__ == "__main__":
    user_input_function()

