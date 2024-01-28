class Combo:
    __slots__ = ['drink','entree','side','price']
    def __init__ (self,drink,entree,side,price):
        self.drink = drink
        self.entree = entree
        self.side = side
        self.price = price

def helper_drink(drink):
    drink_price = {'soda': 1.95,'milk shake': 2.95,'tea': 2.15, 'water': 2.25}
    drink_code = {'s':'soda','ms':'milk shake','t':'tea','w':'water'}
    drink_name = drink_code.get(drink)
    if drink_name is None:
        return None,None
    price = drink_price.get(drink_name)
    return drink_name, price

def helper_entree(entree):
    entree_price = {'burger': 3.95,'cheese burger':4.45,'chicken fingers':4.95}
    entree_code = {'b':'burger','cb':'cheese burger','cf':'chicken fingers'}
    entree_name = entree_code.get(entree)
    if entree_name is None:
        return None,None
    price = entree_price.get(entree_name)
    return entree_name, price

def helper_side(side):
    side_price = {'fries':1.95,'waffle fries':2.95,'tater tots':2.45,'side salad':2.25}
    side_code = {'f':'fries','wf':'waffle fries','tt':'tater tots','ss':'side salad'}
    side_name = side_code.get(side)
    if side_name is None:
        return None, None
    price = side_price.get(side_name)
    return side_name, price

def combos(combo_list):
    drink = input("\nWhat would you like to drink: ")
    entree = input("What would you like for your entree: ")
    side = input("What would you like for your side: ") 
    drink_name, price_of_drink = helper_drink(drink)
    entree_name, price_of_entree = helper_entree(entree)
    side_name, price_of_side = helper_side(side)
    if drink_name is None or entree_name is None or side_name is None:
        print("Invalid Inputs. Try again!")
        return
    total_price = round(price_of_drink + price_of_entree + price_of_side,2)
    combo = Combo(drink_name ,entree_name ,side_name, total_price)
    combo_list.append(combo)

def print_order(combo_list):
    total = 0
    for combo in combo_list:
        print("Drink: ", combo.drink, end=', ')
        print("Entree: ", combo.entree, end=", ")
        print("Side: ", combo.side, end=", ")
        print("Price: $",combo.price)
        total += combo.price
    print("Total: $",total)

def print_menu():
    drink_price = {'soda': 1.95,'milk shake': 2.95,'tea': 2.15,'water': 2.25}
    drink_code = {'s':'soda','ms':'milk shake','t':'tea','w':'water'}
    entree_price = {'burger': 3.95,'cheese burger':4.45,'chicken fingers':4.95}
    entree_code = {'b':'burger','cb':'cheese burger','cf':'chicken fingers'}
    side_price = {'fries':1.95,'waffle fries':2.95,'tater tots':2.45,'side salad':2.25}
    side_code = {'f':'fries','wf':'waffle fries','tt':'tater tots','ss':'side salad'}

    print("MENU")
    print("All meals are a combo!", end="\n")
    print("Drinks: ")
    for key in drink_code:
        name = drink_code[key]
        price = drink_price[name]
        print(name+"("+key+"): " +"$"+ str(price)+" ", end = "")
    print("\nEntrees: ")
    for key in entree_code:
        name = entree_code[key]
        price = entree_price[name]
        print(name+"("+key+"): " + "$"+str(price)+" ", end = "")
    print("\nSides: ")
    for key in side_code:
        name = side_code[key]
        price = side_price[name]
        print(name+"("+key+"): " + "$"+str(price)+" ", end = "")
    print()
    print()
    print("** Please enter the drinks, sides, and entrees in the code format (ex: cs for cheese burger, s for soda, f for fries) **")

def main():
    print_menu()
    combo_list = []
    while True:
        combos(combo_list)
        other_option = input("Would you like to add another combo (Y/N): ")
        if other_option == "N":
            break
    print_order(combo_list)

if __name__=='__main__':
    main()