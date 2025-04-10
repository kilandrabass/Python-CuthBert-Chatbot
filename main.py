"""
    Name:
    Collaborators: 
    COSC-010
    Cuthbert Assignment

    Code adapted from an original program created by Alphie
    In this program, Cuthbert - a "baker bot" - has 
    a conversation with the user. Cuthbert asks the user for 
    information and then does some impressive calculations.

"""

# By importing time library, the program can have pauses (in this case, to simulate "thinking")
# We can also set a float variable, delay, to set how long each pause will be
#     - Set delay to 0.0 for testing or speed runs
#     - Set delay to larger numbers for dramatic effect. (2.0 = 2 seconds)
import time	
delay = 1.0
foodList = ["muffin", "cookie", "scone", "cake"]
priceList = [2.5, 2.0, 3.0, 25.0]
calorieList = [510, 390, 460, 6500]

print("Hi, I'm Cuthbert the Baker Bot!")

# Each time we want a pause, the program can use the time.sleep() method
time.sleep(delay)		
userName = input("What's your name? ")

time.sleep(delay)
eatOrNot = input("Hi, " + userName + "! Would you like to eat something? ")
if eatOrNot.lower() == "yes":

  """
  For Part 1...
  """

  time.sleep(delay)		
  foodChoice = input("Okay, what would you like to eat? Options are a muffin, cookie, scone, or cake. ") 

  time.sleep(delay)		
  if foodChoice == foodList[0] or foodChoice == foodList[1] or   foodChoice == foodList[2] or foodChoice == foodList[3]:
    print("Great news, " + userName + "! We have a " + foodChoice + " for you!")
    print("Its costs $" + str(priceList[0]) + " and has " +                str(calorieList[0]) + " calories.")
  else:
    print("Sorry, " + userName + " - we do not have any " + foodChoice + " for you today.")
elif eatOrNot.lower() == "no":
  print("Okay, have a nice day!")
  
"""
    For Part 2...
"""
time.sleep(delay)
inflatedPrices = priceList.copy()
inflationRate = float(input(userName + ", what is the inflation rate? Please enter a decimal. "))
inflated_Prices = [price * (1 + inflationRate) for price in priceList]
print("Bad news. While we've been talking, inflation has made all the prices higher.")

inflatedPricesTotal = sum(inflated_Prices)
originalPricesTotal = sum(priceList)
round(inflatedPricesTotal, 2)
round(originalPricesTotal, 2)
print("If you ate one of each item, your total would now be", inflatedPricesTotal, "dollars.")
print("In the past, your total would have been", originalPricesTotal )


"""
    For Part 3...
"""
time.sleep(delay)
newFoodOrNot = input("Would you like to add anything to the menu? ")
if newFoodOrNot.lower() == "yes":
  #Add in new menu item, new price, & new calories to respective list
  newFood = input("Enter the name of the new food: ")
  newPrice = float(input("Enter the price of " + newFood + ": "))
  newCalories = int(input("Enter the calories of " + newFood + ": "))

  foodList.append(newFood)
  priceList.append(newPrice)
  calorieList.append(newCalories)
  #Number of food items on menu
  numItems = len(foodList)

  print("The new item", newFood, "has been added to the menu!")
  print("Food List:", foodList)
  print("Price List:", priceList)
  print("Calorie List:", calorieList)

else:
  print("Okay, let me know if you change your mind!")
  numItems = len(foodList)

print("We currently have", numItems, "items on our menu.")
totalPrices = sum(inflated_Prices)
totalCalories = sum(calorieList)
round(totalPrices, 2)
time.sleep(delay)
print("If you ate one of each item, it would cost", totalPrices, "dollars and be", totalCalories, "calories.")

removeFoodOrNot = input("Would you like to remove anything from the menu? ")
if removeFoodOrNot.lower() == "yes":
  #Remove food item from menu
  removeFood = input("Enter the name of the food you would like to remove: ")
  if removeFood in foodList: #Check if food item is in list
    index = foodList.index(removeFood)  # Find the index of the food item
    foodList.remove(removeFood)  # Remove the food item from the list
    priceList.pop(index)  # Remove the corresponding price
    calorieList.pop(index)  # Remove the corresponding calorie
    numItems = len(foodList) #Updated number of food items on menu
    # After removing an item from priceList
    inflatedPrices = [price * (1 + inflationRate) for price in priceList] #Updated Inflation Prices when item is removed
    
    print("The item", removeFood, "has been removed from the menu!")
    print("Food List:", foodList)
    print("Price List:", priceList)
    print("Calorie List:", calorieList)
    print("We currently have", numItems, "items on our menu.")

    #Recalculate total prices and calories
    totalPrices = sum(inflatedPrices)
    totalCalories = sum(calorieList)

    round(totalPrices, 2)
    
    time.sleep(delay)
    print("If you ate one of each item, it would cost", totalPrices, "dollars and be", totalCalories, "calories.")
  else:
    print("Sorry, we do not have", removeFood, "on the menu.")
time.sleep(delay)
print("Bon appetit!")


