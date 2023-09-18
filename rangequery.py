import build
import matplotlib.pyplot as plt

def range_query(node, xmin, xmax, ymin, ymax, result=[], depth=0):
    if node is None:
        return
    
    k = len(node.point)
    axis = depth % k
    
    if xmin <= node.point[0] <= xmax and ymin <= node.point[1] <= ymax:
        result.append(node.point)
    
    if axis == 0:
        if xmin <= node.point[0]:
            range_query(node.left, xmin, xmax, ymin, ymax, result, depth+1)
        if xmax >= node.point[0]:
            range_query(node.right, xmin, xmax, ymin, ymax, result, depth+1)
    else:
        if ymin <= node.point[1]:
            range_query(node.left, xmin, xmax, ymin, ymax, result, depth+1)
        if ymax >= node.point[1]:
            range_query(node.right, xmin, xmax, ymin, ymax, result, depth+1)

# example usage

def rangeQ(points, xlm, ylm, xmin, xmax, ymin, ymax):
    # points = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]
    root = build.build_kdtree(points)

    # perform range query
    # xmin, xmax = 4, 6
    # ymin, ymax = 0, 10
    result = []
    range_query(root, xmin, xmax, ymin, ymax, result)

    # set up the plot
    plt.figure(figsize=(xlm, ylm))
    plt.xlim(0, xlm)
    plt.ylim(0, ylm)

    # visualize the k-d tree
    build.visualize_kdtree(root, 0, xlm, 0, ylm)

    # plot the points
    for point in points:
        # print(point)
        plt.plot(point[0], point[1], 'ro')

    # print the points within the range
    print("Points within the range:")
    for point in result:
        print(point)
        plt.plot(point[0], point[1], 'bs', ms = 10)
        plt.text(point[0], point[1], 'Rangepoint', fontsize=12, color='black', ha='center', va='top')

    plt.show()
