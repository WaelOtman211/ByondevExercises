import heapq

def dijkstra(graph, start):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances
def BuildGraph(grid,n,m):
    hash1={}
    hash2={}
    for i in range(0, n):
        for j in range(0, m):
            hash2={}
            if(grid[i][j]==0):
                if i+1<n:
                    if grid[i+1][j]==0:
                        hash2[(i+1,j)] = 1;
                if(j+1<m):
                   
                    if grid[i][ j+1]==0:
                        hash2[(i,j+1)] = 1;
                if(i-1 > n):
                    if grid[i-1][ j]==0:
                        hash2[(i-1,j)] = 1;
                if(j-1 > m):
                    if grid[i][j-1]==0:
                        hash2[(i,j-1)] = 1;
                hash1[(i,j)]=hash2
    return hash1        


def main():
    n=3
    m=3
    k=6
    target=(2,2)
    start=(0,0)
    grid = [[0, 0, 0],
            [1, 1, 0],
            [0, 0, 0]]
    if target[0] >m or target[1] >n  :
       print("Out Of Range")
    elif grid[start[0]][start[1]]==1:
        print("you can't start from this point")    
    elif grid[target[0]][target[1]]==1:
        print("you can't reach to this point")
    else:   
        print(BuildGraph(grid,n,m))
        if (dijkstra(BuildGraph(grid, n, m),start)[target]<=k):
            print("True")
        else:    
            print("False")
if __name__ == "__main__":
    main()


