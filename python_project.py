# Welcome to your "Meal Picker"!
# Must run on python3 in console!

# Feature Item: List that is populated with several values and retrieved throughout program
ingredients = [     
    "potatoes",
    "broth",
    "tofu",
]


# Feature Item: Class that is created to hold meals
class Meals:        
    def __init__(self):
        pass
    def __call__(self, x, y, z):
        print(x)
        print(y)
        print(z)


# Main function used to run application
def help():
    print("Welcome to your Meal Picker!")
    print("""
Enter 'ingredients' to show the list of ingredients.
Enter 'meals' to show possible meals.
Enter 'DONE' to quit.
""")


# Start of the "master loop" application (Feature Item)
help()
while True:
    item = input()

    if item == "DONE":
        break
    elif item == "meals":
        several_meals = Meals()  # Feature Item(cont. from above): Object created from class and populated with data
        several_meals("Potato Soup", "Curry", "Hot & Sour Soup")
        help()
    elif item == "ingredients":
        print("Here are your Ingredients:")
        print(", ".join(ingredients))   # Feature Item(cont. from above): Retrieved ingredients from list
        first_ingredient = input("Pick an ingredient! ")
        print("Your first ingredient is " + first_ingredient)
        second_ingredient = input("Pick your last ingredient! ")
        print("With your " + first_ingredient + " and " + second_ingredient + ", you should make...")

# If statement that decides the meal based on ingredients
        if (first_ingredient == "potatoes" or second_ingredient == "potatoes") and (first_ingredient == "tofu" or second_ingredient == "tofu"):
            final_meal = "Curry!"
            print(final_meal)
        elif (first_ingredient == "potatoes" or second_ingredient == "potatoes") and (first_ingredient == "broth" or second_ingredient == "broth"):
            final_meal = "Potato Soup!"
            print(final_meal)
        elif (first_ingredient == "broth" or second_ingredient == "broth") and (first_ingredient == "tofu" or second_ingredient == "tofu"):
            final_meal = "Hot & Sour Soup!"
            print(final_meal)
        
        print("...")
        help()