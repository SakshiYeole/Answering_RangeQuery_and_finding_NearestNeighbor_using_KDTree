import matplotlib.pyplot as plt

#define node in the tree
class Node:
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right                                      

#build k-d tree
def build_kdtree(points, depth=0):
    if not points:
        return None
    
    k = len(points[0])
    axis = depth % k
    
    points = sorted(points, key=lambda point: point[axis])          #lambda-> to define an anonymous function 
    median_idx = len(points) // 2
    median = points[median_idx]
    
    left_points = points[:median_idx]
    right_points = points[median_idx+1:]
    
    return Node(median,
                left=build_kdtree(left_points, depth+1),
                right=build_kdtree(right_points, depth+1))

# visualize the plotted points
def visualize_kdtree(node, xmin, xmax, ymin, ymax, depth=0):
    if node is None:
        return
    
    k = len(node.point)
    axis = depth % k
    
    if axis == 0:
        plt.plot([node.point[0], node.point[0]], [ymin, ymax], color='black')
        visualize_kdtree(node.left, xmin, node.point[0], ymin, ymax, depth+1)
        visualize_kdtree(node.right, node.point[0], xmax, ymin, ymax, depth+1)
    else:
        plt.plot([xmin, xmax], [node.point[1], node.point[1]], color='black')
        visualize_kdtree(node.left, xmin, xmax, ymin, node.point[1], depth+1)
        visualize_kdtree(node.right, xmin, xmax, node.point[1], ymax, depth+1)

# # Testing
# # example usage
# points = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]
# root = build_kdtree(points)

# # set up the plot
# plt.figure(figsize=(8, 8))
# plt.xlim(0, 10)
# plt.ylim(0, 10)

# # visualize the k-d tree
# visualize_kdtree(root, 0, 10, 0, 10)

# # plot the points
# for point in points:
#     plt.plot(point[0], point[1], 'ro')

# #plt.plot(5, 5, 'b*')
# plt.show()
