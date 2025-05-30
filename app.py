from planner.route_planner import plan_route

start = "Houston"
destination = "Austin"

route = plan_route(start, destination)
print("Planned Route:", " -> ".join(route))
