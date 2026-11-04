import time
import msvcrt
#pixl cafe menu

menuprices = {
    "1": 20,
    "2": 30,
    "3":15,
    "4": 25,
    "5": 5,
    "6": 50,
    "7": 100,
    "8": 20,
    "9": 15,
    "10": 50,
    "11": 5,
    "12": 20,
    "13": 15,
    "14": 50,
    "15": 30,
    "16": 25
}

menunames = {
    "1": "Coffee",
    "2": "Boba",
    "3": "Apple Juice",
    "4": "Milkshake",
    "5": "Vinegar",
    "6": "Butter Beer",
    "7": "Cassie's Tears",
    "8": "Ginger Ale",
    "9":"Guava Juice",
    "10":"Pizza",
    "11":"Apple",
    "12":"Apple Pie",
    "13":"Fries",
    "14":"Burger",
    "15":"Waffles",
    "16":"Cake"
}

#active order : order_number: itemnames
customernamesanditems = {}
#time left: order no: secondsleft
customernamesandtimeleft = {}
#order timestamp: orderno:created at
order_timestamps = {}

#menu and ascii art
MENU_LEFT = [
    " WELCOME TO DA PIXL CAFE, LETS GET YOU SOMETHING TO EAT/DRINK!!!",
    "",
    "CHOOSE SOME STUFF FROM BELOW:",
    "",
    "DRINKS:",
    "",
    "",
    "      )  (              |1. COFFEE  -  20 Sand Grains",
    "     (   ) )            |2. BOBA TEA -  30 Sand Grains",
    "       ) ( (            |3. Apple Juice -  15 Sand Grains",
    "    (_______)_          |4. Milkshake -  25 Sand Grains",
    " .-'---------|          |5. Vinegar -  5 Sand Grains",
    "( C|/\\/\\/\\/\\/|          |6. Butter Beer -  50 Sand Grains",
    " '-./\\/\\/\\/\\/|          |7. Cassie's Tears - 100 Sand Grains",
    "   '_________'          |8. Ginger Ale -  10 Sand Grains",
    "    '-------'           |9. Guava Juice -  15 Sand Grains",
    "",
    "EDIBLES:",
    "",
    "                        |10. Pizza -  50 Sand Grains",
    "// \"\"--.._              |11. Apple -  5 Sand Grains",
    "||  (_)  _ \"-._         |12. Apple Pie -  20 Sand Grains",
    "||    _ (_)    '-.      |13. Fries - 15 Sand Grains",
    "||   (_)   __..-'       |14. Burger -  50 Sand Grains",
    " \\\\__..--\"\"             |15. Waffles -  30 Sand Grains",
    "                        |16. Cake -  25 Sand Grains"
]

def clear_screen():
    #clears screen
    print("\n"*1000)

def draw_screen():
    #draws welcome text, orders and status boarrd
    update_order_times()
    right_lines = [
        " Order No:    Time Left:   Ordered Items",
        " --------------------------------------------------------"
    ]
    if not customernamesanditems:
        right_lines.append("--no active orders--")
    else:
        for  order_no, items in customernamesanditems.items():
            time_left = customernamesandtimeleft.get(order_no,0)
            if time_left > 0:
                mins = time_left // 60
                secs = time_left % 60
                time_str = f"{mins:02d}:{secs:02d}"
            else:
                time_str = "ready!!"
            items_str = ", ". join(items)
            if len(items_str) > 30:
                items_str = items_str[:27] + "..."
            right_lines.append(f"#{order_no:<11} {time_str:<12} {items_str}")

    for i in range(len(MENU_LEFT)):
        left = MENU_LEFT[i].ljust(84)
        right = right_lines[i] if i < len(right_lines) else ""
        print(f"{left}|{right}")

    print("="*145)
    print("                              PIXL CAFE ORDERING CHAT (AT BOTTOM)")
    print("="*145)

def update_order_times():
    #updates order time left for active orders using elapsed times and removes finished order
    now = time.time()
    ready_to_remove = []
    for order_no, created_at in list(order_timestamps.items()):
        elapsed = int(now - created_at)
        time_left = max(0, 120 - elapsed)
        customernamesandtimeleft[order_no] = time_left
        # after order ready and 30secs pass remove it
        if elapsed >= 150:
            ready_to_remove.append(order_no)

    for order_no in ready_to_remove:
        customernamesanditems.pop(order_no, None)
        customernamesandtimeleft.pop(order_no, None)
        order_timestamps.pop(order_no, None)

#main loop

looping = True
order_counter = 0

while looping:
    clear_screen()
    draw_screen()

    print(">> press [enter] to order and [q] to quit")
    print("screen auto refreshing order queue...")

    start_wait=time.time()
    wants_to_order = False

    while time.time() - start_wait < 1:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key in (b'q', b'Q'):
                looping = False
                break
            else:
                wants_to_order = True
                break
        time.sleep(0.05)

    if not looping:
        print("\n thanks for visiting the pixl cafe buhh byeee!!!")
        break

    if not wants_to_order:
        continue

    ordering = True
    current_order_keys = []
    print("\n"+''*55)
    print("-----ordering in progress(refresh paused)")
    print("-"*55)

    while ordering:
        input_order = input("what would you like to order, type item nos seperated by spaces")
        chosen = input_order.split()

        valid_items = [item for item in chosen if item in menunames]
        invalid_items = [item for item in chosen if item not in menunames]

        if invalid_items:
            print(f"notice: item number(s) {', '.join(invalid_items)} are invalid, so skipping them")

        if valid_items:
            current_order_keys.extend(valid_items)
            current_names = [menunames[item] for item in current_order_keys]
            total_price = sum(menuprices[item] for item in current_order_keys)
            print(f"current order items: {current_names}")
            print(f"total price so far: {total_price} sand grains")

        else:
            print("no valid items are entered")

        more = input("wanna order more items(yes/no)").strip().lower()
        if more in ("no", "n"):
            ordering = False

    if current_order_keys:
        order_counter += 1
        final_items = [menunames[item] for item in current_order_keys]
        total_price = sum(menuprices[item] for item in current_order_keys)

        order_timestamps[order_counter] = time.time()
        customernamesanditems[order_counter] = final_items
        customernamesandtimeleft[order_counter] = 120 

        print(f"\nyour order number is : #{order_counter}")
        print(f"items: {final_items}")
        print(f"total paid: {total_price} sand grains")
        print(f'your order has been sent to da ktichen pls wait 2 mins')
        print("updating the board now...")
        time.sleep(2)

    else:
        print("No items ordered.")
        time.sleep(1)




