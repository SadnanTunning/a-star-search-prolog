import math, heapq, time

s_time = time.time() * 1000

movements = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, 1), (-1, -1), (1, -1)]


def manhattan(current, goal):
    return abs(int(current[0]) - int(goal[0])) + abs(int(current[1]) - int(goal[1]))


def diagonal(current, goal):
    return max(abs(int(current[0]) - int(goal[0])), abs(int(current[1]) - int(goal[1])))


def euclidean(current, goal):
    return math.sqrt(pow(int(current[0]) - int(goal[0]), 2) + pow(int(current[1]) - int(goal[1]), 2))


def print_path(maze, path, current):
    path_list = []
    while current is not None:
        path_list.append(current)
        current = path[f"{current[0]} {current[1]}"][0]
    path_list.reverse()
    print("Path: ", path_list)
    print("Path cost:", len(path_list)-1)

    end = time.time() * 1000
    print(f"Time taken (in milliseconds): {end - s_time} ")


def solve_maze(maze, start, goal):
    queue = []
    path = {
        f'{start[0]} {start[1]}': [None, 0],
    }
    current = start
    while True:
        if current == goal:
            # print("reached")
            print_path(maze, path, current)
            break #goal has been reached
        for row, col in movements: #possible moves
            new_row, new_col = current[0] + row, current[1] + col                              #new row,column based on current cell
            if path.get(f"{new_row} {new_col}") is None and 0 <= new_row < len(                #if explorable neighbour cell found
                    maze) and len(maze[0]) > new_col >= 0 == maze[new_row][new_col] == 0:      #check valid range
                current_cost = path[f"{current[0]} {current[1]}"][1]                           #check current cost
                heapq.heappush(queue, (current_cost + manhattan((new_row, new_col), goal) + 1, (new_row, new_col)))        #priority to the neighboring cell
                path[f"{new_row} {new_col}"] = [current, current_cost + 1]
        _, current = heapq.heappop(queue)                                                       #lowest estimated cost


if __name__ == '__main__':
    user_input = input("Enter the name of the text file: ")
    t_file = user_input + ".txt"
    s_time = time.time() * 1000
    with open(t_file, 'r') as file:
        Input = file.read().split('\n')
        mn = Input[0].split()
        Input.pop(0)                  #remove first line from the input list
        k = Input[1]                  #retrieves second line of the file, k=number of coordinates that have obstacles
        Input.pop(0)                  #remove second line from the input list
        start = Input[-2].split()     #splits second-to-last line of the file
        Input.pop(-2)                 #removes second-to-last line from the input list
        goal = Input[-1].split()      #splits the last line of the file
        Input.pop(-1)                 #remove last line from the input list
        maze = [[0 for _ in range(int(mn[1]))] for _ in range(int(mn[0]))]
        for i in Input:                #iteration through the remaining lines in the input list
            i = i.split()
            maze[int(i[0])][int(i[1])] = 1  #update maze grid, finding obstacles
        solve_maze(maze, (int(start[0]), int(start[1])), (int(goal[0]), int(goal[1])))


#for taking direct input from code
"""
if __name__=='__main__':
    s_time = time.time() * 1000
    with open('input1.txt', 'r') as file:
        Input = file.read().split('\n')
        mn=Input[0].split()
        Input.pop(0)
        k=Input[1]
        Input.pop(0)
        start =Input[-2].split()
        Input.pop(-2)
        goal =Input[-1].split()
        Input.pop(-1)
        maze =[[0 for _ in range(int(mn[1]))] for _ in range(int(mn[0]))]
        for i in Input:
            i=i.split()
            maze[int(i[0])][int(i[1])]=1
        solve_maze(maze,(int(start[0]),int(start[1])),(int(goal[0]),int(goal[1])))
"""


