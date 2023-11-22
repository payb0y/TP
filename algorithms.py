class Algorithms:
    def __init__(self):
        self._algorithms = {}

    def dfs(self, start, target):
        # Initialize the queue with the start position
        stack = [start]
        visited = set()
        path = []

        while stack:
            position = stack.pop()
            if position not in visited:
                visited.add(position)
                path.append(position)
                if position == target:
                    break


    def bfs(self, start, target):
        # Initialize the queue with the start position
        stack = [start]
        visited = set()
        path = []

        while stack:
            position = stack.pop(0)
            if position not in visited:
                visited.add(position)
                path.append(position)
                if position == target:
                    break

    def logic():
        pass