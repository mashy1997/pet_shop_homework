# WRITE YOUR FUNCTIONS HERE

def get_pet_shop_name(name):
    return (name["name"])

def get_total_cash(total_monies):
    return(total_monies["admin"]["total_cash"])

# def add_or_remove_cash(amount, add_money):
#    amount["admin"]["total_cash"] += add_money

def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount
    return pet_shop["admin"]["total_cash"]

def get_pets_sold(sold):
    return(sold["admin"]["pets_sold"])

def increase_pets_sold(pet_shop, extra_pet):
    pet_shop["admin"]["pets_sold"] += extra_pet 

# def get_stock_count(stock):
#     count = 0
#     for element in stock:
#         if isinstance(element, dict):
#             count += 1

#         return count

def get_stock_count(stock):
    return len(stock["pets"])


def get_pets_by_breed(pets_list, breed_name):
    matching_pets = []
    for pet in pets_list["pets"]:
        if pet["breed"] == breed_name:
            matching_pets.append(pet)
    return matching_pets


