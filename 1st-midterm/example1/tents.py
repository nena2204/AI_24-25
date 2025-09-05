import bisect
from constraint import *

GRID_SIZE = 6

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def tents_not_adjacent(*positions):
    for i in range(len(positions)):
        x1, y1 = positions[i]
        for j in range(i + 1, len(positions)):
            x2, y2 = positions[j]
            if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
                return False
    return True



if __name__ == '__main__':
    tents_and_trees = Problem(BacktrackingSolver())
    num_trees = int(input())
    trees = list()

    for _ in range(num_trees):
        trees.append(tuple(map(int, input().split(" "))))


    #mozni mesta za tents
    for i, (x, y) in enumerate(trees):
        possible_tent_positions = []
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE and (nx, ny) not in trees:
                possible_tent_positions.append((nx, ny))

        tents_and_trees.addVariable(f"tent_{i}", possible_tent_positions)

    # print(trees)
    tents_and_trees.addVariable("trees", trees)


    tents_and_trees.addConstraint(tents_not_adjacent, [f"tent_{i}" for i in range(num_trees)])

    # print(tents_and_trees.getSolution())

    solution = tents_and_trees.getSolution()
    if solution:
        print([solution[f"tent_{i}"] for i in range(num_trees)])
    else:
        print("No solution found.")
