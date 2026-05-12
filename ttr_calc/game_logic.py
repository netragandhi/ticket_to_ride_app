from board_mapping import ROUTES, ROUTE_SCORING_TABLE
from ticket_mapping import TICKETS

def build_adj_list(route_owners):
    neighbors = {}
    for color in route_owners:
        if color not in neighbors:
            neighbors[color] = {}
        for route_name in route_owners[color]:
            city1, city2 = ROUTES[route_name]["cities"]
            if city1 not in neighbors[color]:
                neighbors[color][city1] = set()
            neighbors[color][city1].add(city2)
            if city2 not in neighbors[color]:
                neighbors[color][city2] = set()
            neighbors[color][city2].add(city1)
    print(neighbors)
    return neighbors

def dfs_ticket(graph, start, goal, visited=None):
    if visited is None:
        visited = set()

    if start == goal:
        return True

    visited.add(start)

    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            if dfs_ticket(graph, neighbor, goal, visited):
                return True

    return False

def dfs_tour_ticket(graph, ordered_cities):
    for i in range(len(ordered_cities) - 1):
        start = ordered_cities[i]
        end = ordered_cities[i + 1]

        if not dfs_ticket(graph, start, end):
            return False

    return True

def is_ticket_complete(ticket, color_graph):
    start, end = TICKETS[ticket]["cities"]
    return dfs_ticket(color_graph, start, end)

def is_tour_ticket_ordered(ticket, color_graph):
    if TICKETS[ticket]["tour_ticket"]:
        ordered_cities = TICKETS[ticket]["cities"]
        return dfs_tour_ticket(color_graph, ordered_cities)

def calculate_ticket_points(tickets, neighbors):
    points = {}
    points_reason = {}
    for color in neighbors:
        graph = neighbors[color]
        points[color] = list()
        points_reason[color] = list()
        for ticket in tickets[color]:
            if TICKETS[ticket]["tour_ticket"]:
                if is_tour_ticket_ordered(ticket, graph):
                    points[color].append(TICKETS[ticket]["points"])
                    points_reason[color].append(ticket + ", ordered")
                elif is_ticket_complete(ticket, graph):
                    points[color].append(TICKETS[ticket]["secondary_points"])
                    points_reason[color].append(ticket)
                else:
                    points[color].append(TICKETS[ticket]["penalty"])
                    points_reason[color].append(ticket + ", penalty")
            else:
                if is_ticket_complete(ticket, graph):
                    points[color].append(TICKETS[ticket]["points"])
                    points_reason[color].append(ticket)
                else:
                    points[color].append(-1 * TICKETS[ticket]["points"])
                    points_reason[color].append(ticket + ", penalty")
    
    final_ticket_points = {}
    for color in points:
        final_ticket_points[color] = sum(points[color])
    return final_ticket_points

def calculate_route_points(route_owners):
    points = {}
    points_reason = {}
    for color in route_owners:
        points[color] = list()
        points_reason[color] = list()
        for route_name in route_owners[color]:
            route_length = ROUTES[route_name]["length"]
            points_of_route = ROUTE_SCORING_TABLE[route_length]
            points[color].append(points_of_route)
            points_reason[color].append(route_name)
    
    final_route_points = {}
    for color in points:
        final_route_points[color] = sum(points[color])
    return final_route_points

def calculate_total_points(tickets, neighbors, route_owners):
    points1 = calculate_ticket_points(tickets, neighbors)
    points2 = calculate_route_points(route_owners)
    total_points = {}
    for color in points2:
        if color not in total_points:
            total_points[color] = 0
        total_points[color] += points2[color]
        if color in points1:
            total_points[color] += points1[color]
    return total_points