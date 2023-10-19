phone_number = ''

# phone_number_queue = []

while phone_number != '0':
    phone_number = input("enter a phone number: ")

#     if phone_number.startswith("01") and len(phone_number) == 11:
#         if phone_number in phone_number_queue:
#             print("{} is already in memory".format(phone_number))
#         else:
#             phone_number_queue.append(phone_number)
#     else:
#         print("{} is not a valid phone number".format(phone_number))

# print("\n\n")

# for data in phone_number_queue:
#     if data[:3] == '017':
#         print("{} is under gp network".format(data))
#     elif data[:3] == '015':
#         print("{} is under teletalk network".format(data))
#     elif data[:3] == '019':
#         print("{} is under banglalink network".format(data))
#     elif data[:3] == '016':
#         print("{} is under airtel network".format(data))