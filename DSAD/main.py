from Graph import Graph
from Stack import MyStack

# Create Stack => stack = MyStack()
# Functions of Stack => push(int), pop(), top(), is_empty() 


def dfs_traversal_helper(g, source, visited):
    result = ""
    # Stack Implemented since we can't import stack.
    stack = MyStack()
    stack.push(source)
    visited[source] = True
    # Traverse while stack is not empty
    while not stack.is_empty() :
        # Pop and add it to the result
        current_node = stack.pop()
        result += str(current_node)
        # Get adjacent vertices to the current_node from the array,
        # and if they are not already visited then push them in the stack
        temp = g.array[current_node].head_node
        while temp is not None:
            if not visited[temp.data]:
                stack.push(temp.data)
                # Visit the node
                visited[temp.data] = True
            temp = temp.next_element
    return result, visited  

def dfs_traversal(g, source):
    result = ""
    num_of_vertices = g.vertices
    if num_of_vertices == 0:
        return result
    # A list to hold the history of visited nodes
    visited = []
    for i in range(num_of_vertices):
        visited.append(False)
    # Start from source
    result, visited = dfs_traversal_helper(g, source, visited)
    # visit remaining nodes
    for i in range(num_of_vertices):
        if not visited[i]:
            result_new, visited = dfs_traversal_helper(g, i, visited)
            result += result_new
    return result


if __name__ == "__main__":
    stack = MyStack()
    graph = Graph(5)
    graph.add_edge(0,1)
    graph.add_edge(0,2)
    graph.add_edge(1,3)
    graph.add_edge(1,4)
    result = dfs_traversal(graph, 0)
    print(result)
    for i in result:
        stack.push(i)
    stack.printStack()
    # Create a reversed graph
    gr = graph.getTranspose()

    visited =[False]*(5)
