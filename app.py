from planner.route_planner import plan_route

if __name__ == "__main__":
    route = plan_route("Houston", "Austin")
    print("Planned Route:", " -> ".join(route))
