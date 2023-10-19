import ast
def check_by_order_number(order_number):
    file_data = open('store_data.txt')


    for data in file_data:
        abc = data.strip().split("\n")[0].split(" -> ")
        if len(abc) > 1:
            each_list = ast.literal_eval(abc[1])
            for list_item in each_list:
                list_to_dict = dict(list_item)
                try:
                    print("Record found: {} - {}".format(order_number,list_to_dict[str(order_number)]))
                except:
                    pass

    file_data.close()