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
    """
    """
    conversion = float(meter) * 3.28
    return round(conversion, 2)

def degrees_to_radians(degrees):
    """
    """
    conversion = degrees * math.pi / 180

    return round(conversion, 2)

def get_vessel_dimensions():
    length = input("Enter the vessel length (in meter): ")
    width = input("Enter the vessel width (in meter): ")

    return meter_to_feet(length), meter_to_feet(width)

def get_valid_coordinate(val_name, min_float, max_float):
    coordinate = float(input("What is your " + val_name + " ?"))

    while not (coordinate < max_float and coordinate > min_float):
        print("invalid", val_name)
        coordinate = float(input("What is your " + val_name + " ?"))

    return coordinate

def get_gps_location():
    get_valid_coordinate("latitude", MIN_LAT, MAX_LAT)
    get_valid_coordinate("longitude", MIN_LONG, MAX_LONG)

def distance_two_points(lat_1, long_1, lat_2, long_2):
    new_lat_1 = degrees_to_radians(lat_1)
    new_long_1 = degrees_to_radians(long_1)
    new_lat_2 = degrees_to_radians(lat_2)
    new_long_2 = degrees_to_radians(long_2)

    delta_lat = new_lat_2 - new_lat_1
    delta_long = new_long_2 - new_long_1

    a = math.sin(delta_lat/2) ** 2 + math.cos(new_lat_1) * math.cos(new_lat_2) * \
        math.sin(delta_long/2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    final_distance= EARTH_RADIUS * c

    return round(final_distance, 2)

def check_safety(lat, long):
    if distance_two_points(lat, long, 25, -71) <= 400:
        print("Error: Restricted zone!")
    elif (lat <= 41 and lat >=40) and (long <=-70 and lat >=-71):
        print("Warning: Hazardous area! Navigate with caution.")
    else:
        print("Safe navigation.")

def get_max_capacity(length, width):
    if length <= 26:
        max_num_adult = length * width / 15
    else:
        max_num_adult = length * width / 15 + (length - 26) * 3
    
    return int(max_num_adult)

def passengers_on_boat(length, width, passenger_num):
    if get_max_capacity(length, width) < passenger_num:
        return False
    else:
        if (get_max_capacity(length, width) % 4) == 0:
            return True
        else:
            return False

def update_coordinate(position, min_float, max_float):
    random.seed(123)
    num = random.random() * 20 - 10
    new_position = position + num

    while not (new_position > min_float and new_position < max_float):
        num = random.random() * 20 - 10
        new_position = position + num
    
    return round(new_position, 2)

def wave_hit_vessel(lat, long):
    new_lat = update_coordinate(lat, MIN_LAT, MAX_LAT)
    new_long = update_coordinate(long, MIN_LONG, MAX_LONG)

    check_safety(new_lat, new_long)
    return new_lat, new_long

def vessel_menu():
    print("Welcome to the boat menu!")
    lat = float(input("What is your latitude ?"))
    long = float(input("What is your longtitude ?"))
    print("Your current position is at latitude", lat, "and longitude", long)
    length = meter_to_feet(float(input("Enter the vessel length (in meter): ")))
    width = meter_to_feet(float(input("Enter the vessel width (in meter): ")))
    print("Your boat measures", length, "feet by", width, "feet")
    message = "Please select an option below: \n\
1. Check the safety of your boat\n\
2. Check the maximum number of people that can fit on the boat\n\
3. Update the position of your boat\n\
4. Exit boat menu\n\
Your selection: "
    choice = int(input(message))

    while not choice == 4:
        if choice == 1:
            check_safety(lat, long)
        elif choice == 2:
            passenger_num = int(input("How many adults go on the boat? "))
            if passengers_on_boat(length, width, passenger_num):
                print("Your boat can hold", passenger_num, "adults")
            else:
                print("Your boat cannot hold", passenger_num, "adults")
        elif choice == 3:
            [new_lat, new_long] = wave_hit_vessel(lat, long)
            print("Your new position is latitude of", new_lat, "and longitude of", new_long)
        choice = int(input(message))
    print("End of boat menu.")

vessel_menu()