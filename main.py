import nearestneighbor
import rangequery

def main():
    while(True):
        print(" 1. Nearest Neighbor\n 2. Range Query\n 3. Close")
        choice = int(input("Enter Choice: "))

        points = [(2,3), (5,4), (9,6), (4,7), (8,1), (7,2)]
        query_point = (5, 5)
        xlm, ylm = 10, 10
        xmin, xmax = 2, 6
        ymin, ymax = 4, 7
        if choice == 1:
            nearestneighbor.findNN(points, query_point, xlm, ylm)
        elif choice == 2:
            rangequery.rangeQ(points, xlm, ylm, xmin, xmax, ymin, ymax)
        elif choice == 3:
            break
        else:
            print("Invalid Choice.")

        print("-------------------------")
        print()
        
if __name__ == "__main__":
    main()


