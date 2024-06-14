def hello():
    print('Greetings coder!')

def pack(item_one, item_two, item_three):
    pack = [item_one, item_two, item_three]
    return pack

def eat_lunch(lunch_list):
    if not lunch_list:
        print("My lunchbox is empty!")
    else:
        for i, item in enumerate(lunch_list):
            if i == 0:
                print(f"First I eat {item}")
            else:
                print(f"Next I eat {item}")

hello()
print(pack("pillow", "snacks", "clothes"))
eat_lunch(["strawberries", "cheese", "crackers"])
