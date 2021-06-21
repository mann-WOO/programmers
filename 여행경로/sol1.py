def get_route(routes, remain_tickets, destinations, current_city, route):
    if not remain_tickets:
        routes.append(list(route))
        return
    if destinations.get(current_city):
        for i in range(len(destinations.get(current_city))):
            city = destinations[current_city][i]
            del destinations[current_city][i]
            route.append(city)
            get_route(routes, remain_tickets - 1, destinations, city, route)
            destinations[current_city].insert(i, city)
            route.pop()
    else:
        return


def solution(tickets):
    destinations = {}
    for ticket in tickets:
        if not destinations.get(ticket[0]):
            destinations[ticket[0]] = [ticket[1]]
        else:
            destinations[ticket[0]].append(ticket[1])
    routes = []
    get_route(routes, len(tickets), destinations, 'ICN', ['ICN'])
    answer = min(routes)
    return answer


solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]])
