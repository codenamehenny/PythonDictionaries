# 1. Real-World Python Dictionary Applications
#Task 1: Restaurant Menu Update You are given an initial structure of a restaurant menu stored in a nested dictionary. 
# Your task is to update this menu based on given instructions

restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

# - Add a new category called "Beverages" with at least two items.
restaurant_menu.update({"Beverages": {"Water": 1.99, "Fruit Juice": 2.99}})

#- Update the price of "Steak" to 17.99.
restaurant_menu["Main Course"].update({"Steak":17.99})

#- Remove "Bruschetta" from "Starters". 
restaurant_menu["Starters"].pop("Bruschetta")

#organized menu
for course, course_item in restaurant_menu.items():
    print(f"{course}:")
    for item, price in course_item.items():
        print(f"-{item}: {price}")


#print(restaurant_menu)
