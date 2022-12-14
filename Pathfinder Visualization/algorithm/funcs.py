import math
import heapq

def initialize_costs(size, start):
    costs = [[math.inf] * size for i in range(size)]
    x, y = start
    costs[x][y] = 0
    return costs

def find_neighbors(node, visited_nodes, size, obstacles):
    row, col = node
    max_row, max_col = size
    succ_states = []
    # horizontal and vertical
    if row > 0:
        succ_states += [(row - 1, col)]
    if col > 0:
        succ_states += [(row, col - 1)]
    if row < max_row - 1:
        succ_states += [(row + 1, col)]
    if col < max_col - 1:
        succ_states += [(row, col + 1)]
    # aslope
    if row > 0 and col > 0 and not ((row, col - 1) in obstacles and (row - 1, col) in obstacles):
        succ_states += [(row - 1, col - 1)]
    if row > 0 and col < max_col - 1 and not ((row, col + 1) in obstacles and (row - 1, col) in obstacles):
        succ_states += [(row - 1, col + 1)]
    if row < max_row - 1 and col > 0 and not ((row, col - 1) in obstacles and (row + 1, col) in obstacles):
        succ_states += [(row + 1, col - 1)]
    if row < max_row - 1 and col < max_col - 1 and not ((row + 1, col) in obstacles and (row, col + 1) in obstacles):
        succ_states += [(row + 1, col + 1)]

    return [s for s in succ_states if s not in visited_nodes if s not in obstacles]

def distance_heuristic(node, goal):
    x, y = node
    u, v = goal
    return math.sqrt(abs(x - u)**2 + abs(y - v)**2)

def get_distance_from_start(node, costs):
    return costs[node[0]][node[1]]


        