import math

class VanEmdeBoasTree:
    def __init__(self, universe_size):
        self.u = universe_size
        if self.u == 2:
            self.min = None
            self.max = None
        else:
            sqrt_u = int(math.sqrt(self.u))
            self.cluster_size = int(math.ceil(self.u ** 0.5 / 2))
            self.summary = VanEmdeBoasTree(sqrt_u)
            self.cluster = [VanEmdeBoasTree(self.cluster_size) for _ in range(sqrt_u)]

    def high(self, x):
        return x // self.cluster_size

    def low(self, x):
        return x % self.cluster_size

    def index(self, i, j):
        return i * self.cluster_size + j

    def insert(self, x):
        if self.u == 2:
            if x == 0:
                self.min = 0
            elif x == 1:
                self.max = 1
        else:
            self.cluster[self.high(x)].insert(self.low(x))
            self.summary.insert(self.high(x))

    def successor(self, x):
        if self.u == 2:
            if x == 0 and self.max == 1:
                return 1
            else:
                return None
        else:
            max_low = self.cluster[self.high(x)].max
            if max_low is not None and self.low(x) < max_low:
                offset = self.cluster[self.high(x)].successor(self.low(x))
                return self.index(self.high(x), offset)
            else:
                succ_cluster = self.summary.successor(self.high(x))
                if succ_cluster is None:
                    return None
                else:
                    offset = self.cluster[succ_cluster].min
                    return self.index(succ_cluster, offset)

# Example usage:
u = 16  # Set your desired universe size
vEB_tree = VanEmdeBoasTree(u)

# Insert some elements
elements_to_insert = [2, 3, 7, 14]
for element in elements_to_insert:
    vEB_tree.insert(element)

# Test successor operation
for element in elements_to_insert:
    print(f"Successor of {element}: {vEB_tree.successor(element)}")
