from queue import PriorityQueue

class Agent(object):
    def SearchSolution(self, state):
        return []

class AgentSnake(Agent):
    def __init__(self):
        pass

    def SearchSolution(self, state):
        start = (state.snake.HeadPosition.X, state.snake.HeadPosition.Y)
        goal = (state.FoodPosition.X, state.FoodPosition.Y)

        frontier = PriorityQueue()
        frontier.put((0, start))  # Initial priority is 0, indicating the cost so far
        came_from = {}
        cost_so_far = {}
        came_from[start] = None
        cost_so_far[start] = 0

        while not frontier.empty():
            _, current = frontier.get()  # Get the node with the lowest cost so far

            if current == goal:
                break

            for next in self.neighbors(current, state):
                new_cost = cost_so_far[current] + self.cost(current, next)  # Calculate cost based on action
                if next not in cost_so_far or new_cost < cost_so_far[next]:
                    cost_so_far[next] = new_cost
                    priority = new_cost
                    frontier.put((priority, next))  # Priority is the cost so far
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

    def cost(self, current, next):
        # Example cost function: Manhattan distance
        return abs(next[0] - current[0]) + abs(next[1] - current[1])

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

# Example usage:
# agent = AgentSnake()
# solution = agent.SearchSolution(state)
# print(solution)
