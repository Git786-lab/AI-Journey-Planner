import random

def plan_route(start, destination):
    print(f"Planning route from {start} to {destination}...")

    # Simulate AI logic by picking random waypoints
    waypoints = ["Central Park", "City Mall", "Tech Hub", "Museum District", "Lake View"]
    route = [start]
    route += random.sample(waypoints, k=2)  # Pick 2 random stops
    route.append(destination)

    return route
