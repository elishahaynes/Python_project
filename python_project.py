# import random 
  
# Print instructions and rules on how to play game
# print("Winning Rules of 'Rock, Paper, Scissors' is: \n"
#     "Rock vs Paper ---> PAPER WINS! \n"
#     "Rock vs Scissors ---> ROCK WINS! \n"
#     "Paper vs Scissors ---> SCISSORS WINS! \n")













# what I'm trying to create...
# ingredients = [
#     "potatoes",
#     "broth",
#     "tofu",
# ]


# def help():
#     print("Welcome to your Meal Picker!")
#     print("""
# Enter 'Ingredients' to show the list of ingredients.
# Enter 'DONE' to quit.
# """)

# help()
# while True:
#     item = input()

#     if item == "DONE":
#         break
#     elif item == ingredients:
#         print("Here are your Ingredients:")
#         print(ingredients)
    # else:
    #     print("not working")





# what I'm trying to create VERSION 2
# Must run on python3
ingredients = [
    "potatoes",
    "broth",
    "tofu",
]


class Meals:
    def __init__(self):
        pass
    def __call__(self, x, y, z):
        print(x)
        print(y)
        print(z)


# meals = [
#     "Curry",
#     "Potato Soup",
#     "Hot & Sour Soup"
# ]


def help():
    print("Welcome to your Meal Picker!")
    print("""
Enter 'ingredients' to show the list of ingredients.
Enter 'meals' to show possible meals.
Enter 'DONE' to quit.
""")

# def meals():
#     x = "Potato Soup, Curry, and Hot & Sour Soup"
#     return x


# def name_ingredient():
#     input("Pick your first ingredient from the list! ")
#     first_ingredient = pick_first_ingredient()


# def pick_second_ingredient():
#     second_ingredient = input("Pick your second ingredient from the list! ")


help()
while True:
    item = input()

    if item == "DONE":
        break
    elif item == "meals":
        several_meals = Meals()
        several_meals("Potato Soup", "Curry", "Hot & Sour Soup")

        help()
    elif item == "ingredients":
        print("Here are your Ingredients:")
        print(", ".join(ingredients))
        first_ingredient = input("Pick an ingredient! ")
    
        # pick_first_ingredient()
        print("Your first ingredient is " + first_ingredient)
        second_ingredient = input("Pick your last ingredient! ")
        print("With your " + first_ingredient + " and " + second_ingredient + ", you should make...")
        # if first_ingredient or second_ingredient == "potatoes" + first_ingredient or second_ingredient == "tofu":
        #     final_meal = "Curry!"
        #     print(final_meal)
        # elif first_ingredient or second_ingredient == "potatoes" + first_ingredient or second_ingredient == "broth":
        #     final_meal = "Potato Soup!"
        #     print(final_meal)
        # elif first_ingredient or second_ingredient == "broth" + first_ingredient or second_ingredient == "tofu":
        #     final_meal = "Hot & Sour Soup!"
        #     print(final_meal)

        if (first_ingredient == "potatoes" or second_ingredient == "potatoes") and (first_ingredient == "tofu" or second_ingredient == "tofu"):
            final_meal = "Curry!"
            print(final_meal)
        elif (first_ingredient == "potatoes" or second_ingredient == "potatoes") and (first_ingredient == "broth" or second_ingredient == "broth"):
            final_meal = "Potato Soup!"
            print(final_meal)
        elif (first_ingredient == "broth" or second_ingredient == "broth") and (first_ingredient == "tofu" or second_ingredient == "tofu"):
            final_meal = "Hot & Sour Soup!"
            print(final_meal)

#final version if above doesn't work
        # if first_ingredient == "potatoes" and second_ingredient == "tofu":
        #     final_meal = "Curry!"
        #     print(final_meal)
        # elif first_ingredient == "potatoes" and second_ingredient == "broth":
        #     final_meal = "Potato Soup!"
        #     print(final_meal)
        # elif first_ingredient == "broth" and second_ingredient == "tofu":
        #     final_meal = "Hot & Sour Soup!"
        #     print(final_meal)
        print("...")
        help()



    # else:
    #     print("not working")




























#direct from Treehouse example
# shopping_list = []


# def show_help():
#     print("What should we pick up at the store?")
#     print("""
# Enter 'DONE' to stop adding items.
# Enter 'SHOW' to show list.
# Enter 'HELP' for this help.
# """)
    
    
# def add_to_list(item):
#     shopping_list.append(item)
#     print("Your {} was added. You now have".format(item), len(shopping_list), "items in your list.")

# def show_list():
#     print("Here's your list:")
#     for item in shopping_list:
#         print("* " + item)
    
# show_help()
# while True:
#     new_item = input("> ")
    
#     if new_item == 'DONE':
#         break
#     elif new_item == 'HELP':
#         show_help()
#         continue
#     elif new_item == 'SHOW':
#         show_list()
#         continue
        
#     add_to_list(new_item)
    
# show_list()






# intro = input("Would you like to see the list of ingredients? Y/N ")
# if intro.lower == "y":
#     print(ingredients)
# else:
#     print("Have a great day!")