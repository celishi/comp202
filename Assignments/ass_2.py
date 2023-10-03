# 1. Please complete the following:
#   Your First name and Last Name: Celia Shi
#   Your Student ID: 
import math
import random

MIN_LAT = -90
MAX_LAT = 90
MIN_LONG = -180
MAX_LONG = 180
EARTH_RADIUS = 6371

def meter_to_feet(meter):
    """ (num) -> float
    Return the conversion from meter to feet

    >>> meter_to_feet(1.83)
    6.0
    """
    conversion = float(meter) * 3.28
    return round(conversion, 2)

def degrees_to_radians(degrees):
    """ (num) -> float
    Return the conversion from degrees to radians

    >>> degrees_to_radians(35)
    0.61
    """
    conversion = degrees * math.pi / 180
    return round(conversion, 2)

def get_vessel_dimensions():
    """ () -> float, float
    Asks for the length and width of the vessel and 
    returns the conversion from meter to feet

    >>> get_vessel_dimensions()
    Enter the vessel length (in meter): 10
    Enter the vessel width (in meter): 6
    (32.8, 19.68)
    """
    length = input("Enter the vessel length (in meter): ")
    width = input("Enter the vessel width (in meter): ")

    return meter_to_feet(length), meter_to_feet(width)

def get_valid_coordinate(val_name, min_float, max_float):
    """(string, float, float) -> num
    Returns a valid coordinate

    >>> get_valid_coordinate("latitude", -90, 90)
    What is your latitude ?-100
    Invalid latitude
    What is your latitude ?-87.6
    -87.6
    """
    coordinate = float(input("What is your " + val_name + " ?"))

    while not (coordinate < max_float and coordinate > min_float):
        print("Invalid", val_name)
        coordinate = float(input("What is your " + val_name + " ?"))

    return coordinate

def get_gps_location():
    """ () -> float, float
    Calls get_valid_coordinate function to get the latitude and longitude
    Returns two floats for the coordinates

    >>>get_gps_location()
    What is your latitude ?45.51
    What is your longitude ?-73.56
    (45.51, -73.56)
    """
    lat = get_valid_coordinate("latitude", MIN_LAT, MAX_LAT)
    long = get_valid_coordinate("longitude", MIN_LONG, MAX_LONG)

    return float(lat), float(long)

def distance_two_points(lat1, long1, lat2, long2):
    """ (float, float, float, float) -> float
    Returns the distance between 2 points 

    >>> distance_two_points(45, -74, 19, -99)
    3739.5
    """
    new_lat1, new_long1 = degrees_to_radians(lat1), degrees_to_radians(long1)
    new_lat2, new_long2 = degrees_to_radians(lat2), degrees_to_radians(long2)

    delta_lat = new_lat2 - new_lat1
    delta_long = new_long2 - new_long1

    a = math.sin(delta_lat/2) ** 2 + math.cos(new_lat1) * math.cos(new_lat2) * \
        math.sin(delta_long/2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    final_distance= EARTH_RADIUS * c

    return round(final_distance, 2)

def check_safety(lat, long):
    """ (float, float) -> 
    Void function that checks if the ship is found in the safe zone

    >>> check_safety(21.8, -72.3)
    Error: Restricted zone!
    >>> check_safety(40.36, -70.3)
    Warning: Hazardous area! Navigate with caution
    >>> check_safety(45.36, -70.3)
    Safe navigation.
    """
    if distance_two_points(lat, long, 25, -71) <= 400:
        print("Error: Restricted zone!")
    elif (lat <= 41 and lat >=40) and (long <=-70 and lat >=-71):
        print("Warning: Hazardous area! Navigate with caution.")
    else:
        print("Safe navigation.")

def get_max_capacity(length, width):
    """ (float, float) -> int
    Returns the maximum number of adults on the boat depending on its size

    >>> get_max_capacity(18, 6)
    7
    """
    if length <= 26:
        max_num_adult = length * width / 15
    else:
        max_num_adult = length * width / 15 + (length - 26) * 3
    
    return int(max_num_adult)

def passengers_on_boat(length, width, passenger_num):
    """ (num, num, num) -> Boolean
    Returns a boolean that indicates is the boat can hold that number of people
    and if it can be divided equally

    >>> passengers_on_boat(18, 6, 6)
    False
    """
    max_capacity = get_max_capacity(length, width)

    if (max_capacity >= passenger_num) and ((passenger_num % 4) == 0):
        return True
    else:
        return False

def update_coordinate(position, min_float, max_float):
    """ (float, float, float) -> float
    Returns the new coordinates of the boat by adding 
    a random value between (-10,10)

    >>> update_coordinate(15, 0, 40)
    6.05
    """
    random.seed(123)
    num = random.random() * 20 - 10
    new_position = position + num

    while not (new_position > min_float and new_position < max_float):
        num = random.random() * 20 - 10
        new_position = position + num
    
    return round(new_position, 2)

def wave_hit_vessel(lat, long):
    """ (float, float) -> float, float
    Returns updated coordinate if they are valid by checking if they are
    within the allowed values and if the new location is safe

    >>> wave_hit_vessel(45, -73)
    Safe navigation.
    (36.05, -81.95)
    """
    new_lat = update_coordinate(lat, MIN_LAT, MAX_LAT)
    new_long = update_coordinate(long, MIN_LONG, MAX_LONG)

    check_safety(new_lat, new_long)
    return new_lat, new_long

def menu_message():
    """ () -> int
    Function that displays the menu text and asks an input from the user
    which it then returns
    """
    print("Please select an option below: ")
    print("1. Check the safety of your boat")
    print("2. Check the maximum number of people that can fit on the boat")
    print("3. Update the position of your boat")
    print("4. Exit boat menu")
    choice = int(input("Your selection: "))

    return choice

def vessel_menu():
    """ () ->
    Void function that runs the menu and allows user to check the safety
    of the boat, if the boat can hold the number of passengers and 
    update the position of the boat
    """
    print("Welcome to the boat menu!")
    [lat, long] = get_gps_location()
    print("Your current position is at latitude", lat, "and longitude", long)
    [length, width] = get_vessel_dimensions()
    print("Your boat measures", length, "feet by", width, "feet")
    selection = menu_message()

    while not selection == 4:
        if selection == 1:
            check_safety(lat, long)
        elif selection == 2:
            passenger_num = int(input("How many adults go on the boat? "))
            if passengers_on_boat(length, width, passenger_num):
                print("Your boat can hold", passenger_num, "adults")
            else:
                print("Your boat cannot hold", passenger_num, "adults")
        elif selection == 3:
            [lat, long] = wave_hit_vessel(lat, long)
            # lat = new_lat
            # long = new_long
            print("Your new position is latitude of", lat, "and longitude of", long)
        selection = menu_message()
    print("End of boat menu.")