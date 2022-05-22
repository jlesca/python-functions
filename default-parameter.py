# We can set a default parameter value.

# In this case I set as default parameter: "banana"

def myFavFruit(fruit = "banana"):
    print("My favorite fruit is: " + fruit)

# Calling the function It'll display different arguments

myFavFruit("apple")
myFavFruit("pinaple")
myFavFruit() # Here it'll take the default parameter defined "banana"
myFavFruit("peach")
