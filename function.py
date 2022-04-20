print("Checking the weather for you!")
def weather_check():
  print("Looks great outside! Enjoy your trip."
)
print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")

weather_check()

# basic function program

def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit " + location)
  print("You can use the public subway system to get to " + location)

generate_trip_instructions("Grand Central Station")

# this is placing an argument inside of the function to be called by using the location variable 
# so it will auto add that text to each print statement