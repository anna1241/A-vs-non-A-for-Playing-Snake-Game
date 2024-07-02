from queue import PriorityQueue

class Agent(object):
    def SearchSolution(self, state):
        return []

class AgentSnake(Agent):
    def _init_(self):
        pass

    def heuristic(self, a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    def SearchSolution(self, state):
        start = (state.snake.HeadPosition.X, state.snake.HeadPosition.Y)
        goal = (state.FoodPosition.X, state.FoodPosition.Y)

        frontier = PriorityQueue()
        frontier.put(start, 0)
        came_from = {}
        came_from[start] = None

        while not frontier.empty():
            current = frontier.get()

            if current == goal:
                break

            for next in self.neighbors(current, state):
                if next not in came_from:
                    frontier.put(next, self.heuristic(goal, next))
                    came_from[next] = current

        path = []
        current = goal
        while current != start:
            path.append(current)
            current = came_from[current]
        path.append(start)
        path.reverse()

        plan = []
        for i in range(1, len(path)):
            dx = path[i][0] - path[i-1][0]
            dy = path[i][1] - path[i-1][1]
            if dx == 1:
                plan.append(3)  # Right
            elif dx == -1:
                plan.append(9)  # Left
            elif dy == 1:
                plan.append(6)  # Down
            elif dy == -1:
                plan.append(0)  # Up

        return plan

    def neighbors(self, pos, state):
        x, y = pos
        neighbors = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if nx >= 0 and ny >= 0 and nx < state.maze.WIDTH and ny < state.maze.HEIGHT and state.maze.MAP[ny][nx] != -1 and (nx, ny) not in state.snake.Body:
                neighbors.append((nx, ny))
        return neighbors

def showAgent():
    print("A Snake Solver By MB")
