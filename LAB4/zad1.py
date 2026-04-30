import random
import numpy as np

#def tsp(cities, T, cooling_rate, max_iter):

def random_cities(n, mini=0, maxi=100):
    arr = [[random.randint(mini, maxi) for _ in range(n)] for _ in range(n)]



def tsp(cities, T, cooling_rate, max_iterations, n):
    visited = [[False for _ in range(n)] for _ in range(n)]
    current_route = []
    current_distance = []
    best_route = []   
    best_distance = []

    x = y = 0
    visited[x][y] = True
    for _ in range(max_iterations):
        neighbors = find_neighbours((visited, x, y))
        next_route = random.choice(neighbors)
        next_distance = next_route

        
        if next_distance < current_distance or random.random() < np.exp((current_distance - next_distance) / T):
            current_route, current_distance = next_route, next_distance

            if current_distance < best_distance:
                best_route, best_distance = current_route, current_distance

        T *= cooling_rate

    return best_route, best_distance



cities = random_cities(60)


def find_neighbours(visited, x, y):
    neighbours = []
    n = len(visited)
    for i in [-1, 0 ,1]:
        for j in [-1, 0, 1]:
            new_x = x + i
            new_y = y + j
            if 0 < new_x < n  and 0 < new_y < n and not visited[new_x][new_y]:
                neighbours.append((new_x, new_y))
    return neighbours

    