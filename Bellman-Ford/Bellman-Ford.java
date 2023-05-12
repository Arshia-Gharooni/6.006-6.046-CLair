import java.util.*;

public class BellmanFord {
    public static void main(String[] args) {
        // Example usage:
        int[][] edges = {{0, 1, 4}, {0, 2, 5}, {1, 2, -2}, {1, 3, 6}, {2, 3, 1}};
        List<List<int[]>> adj = buildAdjacencyList(4, edges);
        int[] dist = bellmanFord(adj, 0);
        System.out.println(Arrays.toString(dist)); // [0, 4, 2, 3]
    }

    public static List<List<int[]>> buildAdjacencyList(int n, int[][] edges) {
        List<List<int[]>> adj = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] edge : edges) {
            int u = edge[0], v = edge[1], w = edge[2];
            adj.get(u).add(new int[]{v, w});
        }
        return adj;
    }

    public static int[] bellmanFord(List<List<int[]>> adj, int s) {
        int n = adj.size();
        double[] dist = new double[n];
        Arrays.fill(dist, Double.POSITIVE_INFINITY);
        int[] parent = new int[n];
        Arrays.fill(parent, -1);
        dist[s] = 0;

        for (int k = 0; k < n - 1; k++) {
            for (int u = 0; u < n; u++) {
                for (int[] edge : adj.get(u)) {
                    int v = edge[0], w = edge[1];
                    if (dist[u] + w < dist[v]) {
                        dist[v] = dist[u] + w;
                        parent[v] = u;
                    }
                }
            }
        }

        for (int u = 0; u < n; u++) {
            for (int[] edge : adj.get(u)) {
                int v = edge[0], w = edge[1];
                if (dist[u] + w < dist[v]) {
                    throw new RuntimeException("Negative cycle detected!");
                }
            }
        }

        return parent;
    }
}