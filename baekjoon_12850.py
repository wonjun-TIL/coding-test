
D = int(input())
MOD = 1000000007

graph = [[0, 1, 1, 0, 0, 0, 0, 0],
            [1, 0, 1, 1, 0, 0, 0, 0],
            [1, 1, 0, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 1, 0, 1],
            [0, 0, 0, 1, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0, 1, 0]]

def power(graph, D):
    if D == 1:
        return graph
    elif D % 2:
        return multi(power(graph, D-1), graph)
    else:
        temp = power(graph, D//2)
        return multi(temp, temp)
    
def multi(graph1, graph2):
    result = [[0 for _ in range(8)] for _ in range(8)]
    for i in range(8):
        for j in range(8):
            for k in range(8):
                result[i][j] += graph1[i][k] * graph2[k][j]
            result[i][j] %= MOD
    return result

result = power(graph, D)
print(result[0][0])
