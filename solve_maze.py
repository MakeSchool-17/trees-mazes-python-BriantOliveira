import maze
import generate_maze
import sys
import random


# Solve maze using Pre-Order DFS algorithm, terminate with solution
def solve_dfs(m):
    # TODO: Implement solve_dfs
    stack = []
    cell = 0
    visited_cells = 0

    while cell < m.total_cells -1:
        neighbors = m.cell_neighbors(cell)
        print(neighbors)
        if len(neighbors) > 0:
            neighbors_index = random.randint(0, len(neighbors) - 1)
            new_cell = neighbors[neighbors_index][0]
            compass_index = neighbors[neighbors_index][1]
            m.visit_cell(cell, new_cell, compass_index)
            stack.append(cell)
            cell = new_cell
            visited_cells += 1

        else:
            backtrack_cell = m.backtrack(cell)
            cell = stack.pop()
        m.refresh_maze_view()
    m.state = 'idle'



# Solve maze using BFS algorithm, terminate with solution
def solve_bfs(m):
    # TODO: Implement solve_bfs
    queue = Queue()
    cell = 0
    in_direction = 0b0000
    visited_cells = 0
    queue.enqueue(cell, in_direction)
    print(queue)
    while (cell != m.total_cells - 1) and not (queue.isEmpty()):
        cell, in_direction = queue.dequeue
        visit = bfs_visit_cell(cell)
        visited_cells += 1
        m.refresh_maze_view()

        unvisited_neighbors = m.cell_neighbors(cell)
        for neighbor in neighbors:
            queue.enqueue(neighbor)
    m.reconstruct_solution(cell)

    m.state = 'idle'


def print_solution_array(m):
    solution = m.solution_array()
    print('Solution ({} steps): {}'.format(len(solution), solution))


def main(solver='dfs'):
    current_maze = maze.Maze('create')
    generate_maze.create_dfs(current_maze)
    if solver == 'dfs':
        solve_dfs(current_maze)
    elif solver == 'bfs':
        solve_bfs(current_maze)
    while 1:
        maze.check_for_exit()
    return

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        main()
