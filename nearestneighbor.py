import math
import build
import matplotlib.pyplot as plt

def find_nearest_neighbor(root, point, depth=0, best=None):   #best and depth is initialized
    if root is None:
        return best
    
    if best is None or distance(point, root.point) < distance(point, best):
        best = root.point
        
    k = len(point)
    axis = depth % k
    
    if point[axis] < root.point[axis]:
        next_branch = root.left
        opposite_branch = root.right
    else:
        next_branch = root.right
        opposite_branch = root.left
        
    best = find_nearest_neighbor(next_branch, point, depth+1, best)
    
    if opposite_branch is not None:
        if distance(point, best) > abs(root.point[axis] - point[axis]):
            best = find_nearest_neighbor(opposite_branch, point, depth+1, best)
    
    return best

def distance(p1, p2):
    return math.sqrt(sum([(p1[i] - p2[i])**2 for i in range(len(p1))]))

# example usage
def findNN(points, query_point, xlm, ylm):
    # points = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]
    root = build.build_kdtree(points)

    # query_point = (5, 5)
    nearest_neighbor = find_nearest_neighbor(root, query_point)

    print("Query point:", query_point)
    print("Nearest neighbor:", nearest_neighbor)

    # set up the plot
    plt.figure(figsize=(xlm, ylm))
    plt.xlim(0, xlm)
    plt.ylim(0, ylm)
    plt.plot(query_point[0], query_point[1], 'b*') 
    plt.text(query_point[0], query_point[1], 'Query Point', fontsize=12, color='black', ha='center', va='top')

    # visualize the k-d tree
    build.visualize_kdtree(root, 0, xlm, 0, ylm)

    # plot the points
    for point in points:
        plt.plot(point[0], point[1], 'ro')

    plt.plot(query_point[0], query_point[1], 'b*')
    plt.text(query_point[0], query_point[1], 'Query Point', fontsize=12, color='black', ha='center', va='top')
    plt.plot(nearest_neighbor[0], nearest_neighbor[1], 'cs', ms = 10)
    plt.text(nearest_neighbor[0], nearest_neighbor[1], 'Nearest Neighbor', fontsize=12, color='black', ha='center', va='top')
    plt.show() 
