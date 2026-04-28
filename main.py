import json


with open ("raw_data.json", 'r') as file:
    data = json.load(file)

def get_orbit_type(altitude):
        if altitude <= 0:
            return "- Invalid altitude"
        elif altitude > 35785:
            return "- High orbit"
        elif altitude > 2000 and altitude < 35785:
            return "- Medium orbit"
        else:
            return "- Low orbit"

def get_velocity_type(velocity):
    if velocity <= 0:
        return "- Invalid velocity"
    elif velocity >= 25000:
        return "- Very high velocity"
    elif velocity >= 20000:
        return "- High velocity"
    elif velocity > 7000 and velocity < 19000:
        return "- Medium velocity"
    else:
        return "- Low velocity"

def satellite_report(satellites):
    for sat in satellites:
        name = sat["name"]
        country = sat["country"]
        altitude = sat["altitude_km"]
        velocity = sat["velocity_kmh"]

        orbit_type = get_orbit_type(altitude)
        velocity_type = get_velocity_type(velocity)

        print(f"{name} | {country} | {orbit_type} | {velocity_type}")

print()
satellite_report(data["satellites"])
print()