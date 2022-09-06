# Data required 

greeting = ["hi", "hello", "salam"]

product_status = {
        "1": "ready",
        "2": "not ready",
        "3": "shipped",
        "4": "returned",
        "5": "canceled"
        }

offers = "All offers are "\
        "displayed in our\n"\
        "website : www.shalabyphones.com"

good_bye = ["ok", "thanks", "bye"]

draw_line = "_"*34

new_line = "\n"

# Replay and print the option

options_replay = "Hi customer:\n"\
                "Please choose the number of service:\n\n"\
                "1- Shipment status\n\n"\
                "2- Offers\n\n"

wrong_option = "Sorry I can't understand you,\n"\
                "We will route this question\n"\
                "to our customers service"

# The message for getting shipment number.

shipment_n = "Please input the shipment number : "

# The message for wrong shipment number>

shipment_not_found = "Sorry we can't find this shipment number,\n"\
                    "we will route you  to our customer service\n"\
                    "Have a nice day."

# start the robot

user_start_input = input()

print(draw_line)

if user_start_input.lower() in greeting:
    print(options_replay)
    print(draw_line)
    user_choice = input("Input the number here : ")
    print(new_line)
    if user_choice == "1":
        shipment_number = input(shipment_n)
        print(new_line)
        print(draw_line)
        print(new_line)
        if shipment_number in product_status:
            print(f"Your shipment {shipment_number},\n"\
                    f"is {product_status[shipment_number]}\n"\
                    "Have a nice day.")
            print(new_line)
        else:
            print(new_line)
            print(shipment_not_found)
    elif user_choice == "2":
        print(new_line)
        print(draw_line)
        print(offers)    
    else:
        print(wrong_option)
elif user_start_input.lower() in good_bye:
    print(new_line)
    print(draw_line)
    print(new_line)
    print("Have a nice day")
else:
    print(wrong_option)

