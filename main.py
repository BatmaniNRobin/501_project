#############################################################
# author: Mohammad Malik
# course: VCU CMSC Fall 2020 - 501_Advanced_Algorithms
# date: 11/22/2020
# Professor: Dr. Thang Dinh
#############################################################

# Inspiration for code
####################################################################
# https://codereview.stackexchange.com/questions/203319/greedy-graph-coloring-in-python/203328
####################################################################


import sys
import collections


# colors the map to solve sudoku
def welsh_powell(graph, mapOfColors):

    #sort the values in descending order and color the map accordingly (most neighbors ... least neighbors)
    vertices = sorted(graph, key=lambda x: len(graph[x]), reverse=True)

    for vertex in vertices:
        # check to see if node has been visited or not, if it has not then color the graph
        if mapOfColors[vertex - 1] == 0:
            directions = set(mapOfColors.get(node - 1) for node in graph[vertex])
            mapOfColors[vertex - 1] = next(color for color in range(1, len(graph) + 1) if color not in directions)
    
    return mapOfColors

# main function
def main():
    # read input and parse it into nodes and edges via spacing delimiter
    numNodes, numEdges = list(map(int, input().strip().split(" ")))
    edges = [tuple(map(int, input().strip.split(" "))) for index in range(numEdges)]
    colors = list(map(int, input().strip.split(" ")))

    graph = defaultdict(list)

    for edge in edges:
        source = edge[0]
        dest = edge[1]

        graph[source].append(dest)
        graph[dest].append(source)
    
    mapOfColors = {}
    for i, color in enumerate(colors):
        mapOfColors[i] = color

    # call the graph coloring function to color the graphs and solve the sudoku
    retval = welsh_powell(graph, mapOfColors)

    # get max value of colors for starting
    old_colors = 0

    if 0 not in set(colors):
        old_colors = len(set(colors))
    else:
        old_colors = len(set(colors)) - 1

    # new max value of colors
    new_colors = len(set(retval.values()))
    
    # assuming colors start from 1 to max-color, this is the additional colors
    additional_colors = new_colors - old_colors
    
    print(additional_colors)

    for value in solution.values():
        print(value)
        print(" ")


if __name__ == "__main__":
    main()
