import math
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
    length = input("Enter the vessel length (in meter) : ")
    width = input("Enter the vessel width (in meter) : ")

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
    print()