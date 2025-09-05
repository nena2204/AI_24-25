from searching_framework import *
# from utils import *
# from uninformed_search import *
# from informed_search import * 


class Boxes(Problem):
    def __init__(self, initial, n, boxes):
        # state = ((x, y), frozenset(remaining_boxes))
        self.n = n
        self.blocked = set(boxes)          # ne stapnuvame nikofas
        super().__init__(initial)

    
    def _in_bounds(self, p):
        x, y = p
        return 0 <= x < self.n and 0 <= y < self.n

    @staticmethod
    def _adjacent(p, b):
        
        return p != b and abs(p[0] - b[0]) <= 1 and abs(p[1] - b[1]) <= 1

    def _drop_balls(self, pos, remaining):
        
        rem = frozenset(remaining)
        return frozenset(b for b in rem if not self._adjacent(pos, b))

    
    def actions(self, state):
        return list(self.successor(state).keys())

    def result(self, state, action):
        return self.successor(state)[action]

    def goal_test(self, state):
        pos, rem = state
        rem = self._drop_balls(pos, rem)
        return len(rem) == 0

    def successor(self, state):
        (x, y), rem = state
        
        rem = self._drop_balls((x, y), rem)

        succ = {}

        up = (x, y + 1)
        if self._in_bounds(up) and up not in self.blocked:
            succ["Gore"] = (up, self._drop_balls(up, rem))

        right = (x + 1, y)
        if self._in_bounds(right) and right not in self.blocked:
            succ["Desno"] = (right, self._drop_balls(right, rem))

        return succ


if __name__ == '__main__':
    n = int(input().strip())
    man_pos = (0, 0)

    num_boxes = int(input().strip())
    boxes = []
    for _ in range(num_boxes):
        boxes.append(tuple(map(int, input().strip().split(','))))

    
    initial_state = (man_pos, frozenset(boxes))
    problem = Boxes(initial_state, n, boxes)

    sol = breadth_first_graph_search(problem)
    if sol is None:
        print("No Solution!")
    else:
        print(sol.solution())   
