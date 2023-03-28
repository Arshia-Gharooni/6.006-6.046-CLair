import java.util.*;

public class IntervalSchedulingProblem {

    public static void main(String[] args) {
        // Get input intervals from user
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the number of intervals: ");
        int n = scanner.nextInt();
        int[][] intervals = new int[n][2];
        System.out.println("Enter the start and end times for each interval:");
        for (int i = 0; i < n; i++) {
            System.out.print("Interval " + (i + 1) + ": ");
            intervals[i][0] = scanner.nextInt();
            intervals[i][1] = scanner.nextInt();
        }
        
        int maxIntervals = findMaxIntervals(intervals);
        System.out.println("Maximum number of intervals that can be scheduled: " + maxIntervals);
    }

    public static int findMaxIntervals(int[][] intervals) {
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[1], b[1])); // sort by end time
        int count = 0;
        int endTime = -1;
        for (int[] interval : intervals) {
            if (interval[0] >= endTime) {
                count++;
                endTime = interval[1];
            }
        }
        return count;
    }
}