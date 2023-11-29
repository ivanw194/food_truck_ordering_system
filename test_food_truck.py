import food_truck

def combos_test():
    expected_drink = "soda"
    expected_entree = "burger"
    expected_side = "fries"
    expected_price = 7.85
    combo = food_truck.Combo(expected_drink ,expected_entree ,expected_side, expected_price)
    actual_drink = combo.drink
    assert actual_drink == expected_drink

def print_order_test():
    expected_print = "Drink:  soda, Entree:  burger, Side:  fries, Price: $ 7.85 \n Total: $ 7.85"
    order = food_truck.Combo(expected_print)
    actual_print = order.print_order
    assert actual_print == expected_print
