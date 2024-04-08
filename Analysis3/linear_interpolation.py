from colors import bcolors


def linearInterpolation(table_points, point):
    flag = 1
    for i in range(len(table_points) - 1):
        if table_points[i][0] <= point <= table_points[i + 1][0]:
            x1, x2, y1, y2 = table_points[i][0], table_points[i + 1][0], table_points[i][1], table_points[i + 1][1]
            result = (((y1 - y2) / (x1 - x2)) * point) + ((y2 * x1) - (y1 * x2)) / (x1 - x2)
            print(bcolors.OKGREEN, "\nThe approximation (interpolation) of the point ", point, " is: ",bcolors.ENDC, round(result, 4))
            flag = 0
    if flag:
        if point > table_points[len(table_points) - 1][0]:
            x1 = table_points[len(table_points) - 1][0]
            x2 = table_points[len(table_points) - 2][0]
            y1 = table_points[len(table_points) - 1][1]
            y2 = table_points[len(table_points) - 2][1]
            m = (y1 - y2) / (x1 - x2)
            result = y1 + m * (point - x1)
        else:
            x1 = table_points[0][0]
            x2 = table_points[1][0]
            y1 = table_points[0][1]
            y2 = table_points[1][1]
            m = (y1 - y2) / (x1 - x2)
            result = y1 + m * (point - x1)
        print(bcolors.OKGREEN, "\nThe approximation (extrapolation) of the point ", point, " is: ", bcolors.ENDC,
              round(result, 4))



if __name__ == '__main__':

    table_points = [(1, 0), (2, 0.8415), (3, 0.9093), (4, 0.1411), (5, -0.7568), (6, -0.9589), (7, -0.2794)]
    x = 3.7
    print(bcolors.OKBLUE, "----------------- Interpolation & Extrapolation Methods -----------------\n", bcolors.ENDC)
    print(bcolors.OKBLUE, "Table Points: ", bcolors.ENDC, table_points)
    print(bcolors.OKBLUE, "Finding an approximation to the point: ", bcolors.ENDC, x)
    linearInterpolation(table_points, x)
    print(bcolors.OKBLUE, "\n---------------------------------------------------------------------------\n", bcolors.ENDC)


