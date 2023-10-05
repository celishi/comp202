# 1. Please complete the following:
#   Your First name and Last Name: Celia Shi
#   Your Student ID: 261175554
import math
import random

MIN_LAT = -90
MAX_LAT = 90
MIN_LONG = -180
MAX_LONG = 180
EARTH_RADIUS = 6371

METER_TO_FEET_CST = 3.28
HALF_CIRCLE_DEG = 180
LENGTH_SNALL_VESSEL = 26

#coordinates and constant for the restricted zones
LAT_RES_ZONE = 25
LONG_RES_ZONE = -71
MIN_DISTANCE = 400

#coordinates for hazardous zone
LAT_MIN = 40
LAT_MAX = 40
LONG_MIN = -71
LONG_MAX = -70

#menu constant
CHECK_SAFETY = 1
CHECK_MAX_CAPACITY = 2
UPDATE_POSITION = 3
EXIT_MENU = 4

def meter_to_feet(meter):
    """ (num) -> float
    Return the conversion from meter to feet

    >>> meter_to_feet(1.83)
    6.0
    >>> meter_to_feet(5)
    16.4
    >>> meter_to_feet(6)
    19.68
    """
    conversion = float(meter) * METER_TO_FEET_CST
    return round(conversion, 2)

def degrees_to_radians(degrees):
    """ (num) -> float
    Return the conversion from degrees to radians

    >>> degrees_to_radians(35)
    0.61
    >>> degrees_to_radians(90)
    1.57
    >>> degrees_to_radians(180)
    3.14
    """
    conversion = degrees * math.pi / HALF_CIRCLE_DEG
    return round(conversion, 2)

def get_vessel_dimensions():
    """ () -> float, float
    Asks for the length and width of the vessel and 
    returns the conversion from meter to feet

    >>> get_vessel_dimensions()
    Enter the vessel length (in meter): 10
    Enter the vessel width (in meter): 6
    (32.8, 19.68)
    >>> get_vessel_dimensions()
    Enter the vessel length (in meter): 5
    Enter the vessel width (in meter): 3
    (16.4, 9.84)
    >>> get_vessel_dimensions()
    Enter the vessel length (in meter): 7
    Enter the vessel width (in meter): 42
    (22.96, 137.76)  
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
    >>> get_valid_coordinate("x-coordinate", -75, 75)
    What is your x-coordinate ?80
    Invalid x-coordinate
    What is your x-coordinate ?65
    65.0
    >>> get_valid_coordinate("y-coordinate", -75, 75)
    What is your y-coordinate ?-43.6
    -43.6  
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

    >>> get_gps_location()
    What is your latitude ?45.51
    What is your longitude ?-73.56
    (45.51, -73.56)
    >>> get_gps_location()
    What is your latitude ?46
    What is your longitude ?987
    Invalid longitude
    What is your longitude ?34
    (46.0, 34.0)
    >>> get_gps_location()
    What is your latitude ?55
    What is your longitude ?26.4
    (55.0, 26.4)
    """
    lat = get_valid_coordinate("latitude", MIN_LAT, MAX_LAT)
    long = get_valid_coordinate("longitude", MIN_LONG, MAX_LONG)

    return float(lat), float(long)

def distance_two_points(lat1, long1, lat2, long2):
    """ (float, float, float, float) -> float
    Returns the distance between 2 points 

    >>> distance_two_points(45, -74, 19, -99)
    3739.5
    >>> distance_two_points(33, 90, 30, -75)
    12831.65
    >>> distance_two_points(25, -55, 45, 67)
    10232.26
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

    if distance_two_points(lat, long, LAT_RES_ZONE, LONG_RES_ZONE) <= MIN_DISTANCE:
        print("Error: Restricted zone!")
    elif (lat <= LAT_MAX and lat >= LAT_MIN) and (long <= LONG_MAX and lat >= LONG_MIN):
        print("Warning: Hazardous area! Navigate with caution.")
    else:
        print("Safe navigation.")

def get_max_capacity(length, width):
    """ (float, float) -> int
    Returns the maximum number of adults on the boat depending on its size

    >>> get_max_capacity(18, 6)
    7
    >>> get_max_capacity(16, 6)
    6
    >>> get_max_capacity(32, 8)
    35
    """
    if length <= LENGTH_SNALL_VESSEL:
        max_num_adult = length * width / 15
    else:
        max_num_adult = length * width / 15 + (length - LENGTH_SNALL_VESSEL) * 3
    
    return int(max_num_adult)

def passengers_on_boat(length, width, passenger_num):
    """ (num, num, num) -> Boolean
    Returns a boolean that indicates is the boat can hold that number of people
    and if it can be divided equally

    >>> passengers_on_boat(18, 6, 6)
    False
    >>> passengers_on_boat(20, 10, 8)
    True
    >>> passengers_on_boat(23, 10, 10)
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
    >>> update_coordinate(13, 0, 20)
    10.32
    >>> update_coordinate(8, 5, 17)
    7.66
    """
    random.seed(123)
    num = random.random() * 20 - 10 # to get a random value between (-10, 10)
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
    >>> wave_hit_vessel(47, -9)
    Safe navigation.
    (51.41, -14.39)
    >>> wave_hit_vessel(35, -62)
    Safe navigation.
    (29.76, -52.06)
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

    while not selection == EXIT_MENU:
        if selection == CHECK_SAFETY:
            check_safety(lat, long)
        elif selection == CHECK_MAX_CAPACITY:
            passenger_num = int(input("How many adults go on the boat? "))
            if passengers_on_boat(length, width, passenger_num):
                print("Your boat can hold", passenger_num, "adults")
            else:
                print("Your boat cannot hold", passenger_num, "adults")
        elif selection == UPDATE_POSITION:
            [lat, long] = wave_hit_vessel(lat, long)
            print("Your new position is latitude of", lat, "and longitude of", long)
        selection = menu_message()
    print("End of boat menu.")