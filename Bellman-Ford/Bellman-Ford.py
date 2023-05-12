def bellman_ford(Adj, w, s):
    
    infinity = float('inf') 
    d = [infinity for _ in Adj] 
    parent = [None for _ in Adj] 
    d[s], parent[s] = 0, s 
    
    V = len(Adj) 
    for k in range(V - 1): 
        for u in range(V): 
            for v, weight in Adj[u]: 
                if d[u] + weight < d[v]: 
                    d[v] = d[u] + weight
                    parent[v] = u
    
    for u in range(V): 
        for v, weight in Adj[u]: 
            if d[u] + weight < d[v]: 
                raise Exception('Ack! There is a negative weight cycle!')
    return d, parent