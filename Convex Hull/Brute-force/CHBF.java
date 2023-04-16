import java.util.*;

public class ConvexHull {
    public static void main(String[] args) {
        // Example set of points
        int[][] points = {{0, 0}, {1, 1}, {2, 2}, {2, 0}, {3, 3}, {4, 4}, {4, 0}};

        // Find the convex hull
        List<int[]> hull = bruteForceConvexHull(points);

        // Print the convex hull
        System.out.println("Convex Hull:");
        for (int[] point : hull) {
            System.out.println(Arrays.toString(point));
        }
    }

    public static List<int[]> bruteForceConvexHull(int[][] points) {
        // Initialize the convex hull as an empty list
        List<int[]> hull = new ArrayList<>();

        // Check each pair of points to see if it makes up an edge of the convex hull
        for (int i = 0; i < points.length; i++) {
            for (int j = i + 1; j < points.length; j++) {
                int[] p1 = points[i];
                int[] p2 = points[j];

                // Find the equation of the line between p1 and p2: y = mx + b
                double m = (p2[1] - p1[1]) / (double) (p2[0] - p1[0]);
                double b = p1[1] - m * p1[0];

                // Check if all other points are on one side of the line
                boolean onOneSide = true;
                for (int[] p : points) {
                    if (p == p1 || p == p2) {
                        continue;
                    }
                    double y = m * p[0] + b;
                    if (p[1] < y) {
                        onOneSide = false;
                        break;
                    }
                }

                // If all other points are on one side of the line, add it to the convex hull
                if (onOneSide) {
                    if (!hull.contains(p1)) {
                        hull.add(p1);
                    }
                    if (!hull.contains(p2)) {
                        hull.add(p2);
                    }
                }
            }
        }

        return hull;
    }
}