from datetime import datetime
import package_to_check_by_order_num

student_array = []


def store_student_data(data):
    cleaned_data = str(datetime.now()) + " -> " + str(data)
    with open('store_data.txt','a') as store_file_data:
        store_file_data.write("\n"+cleaned_data)

def read_data_from_store_file():
    file_data = open('store_data.txt')
    print("===============\n")

    print(file_data.read())

    print("\n===============")

    file_data.close()

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

    package_to_check_by_order_num.check_by_order_number(order_num)

            
    print()
    user_input_function()

def take_student_data_input():
    order_number = ""
    student_name = ""

    while order_number != "exit":
        data = {}
        order_number = input("Please insert your order number: ")
        if order_number == 'exit':
            store_student_data(student_array)
            user_input_function()

        student_name = input("Please insert a student name: ")

        data[order_number] = student_name
        
        student_array.append(data)

    
    


def student_list_show():
  
    read_data_from_store_file()
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