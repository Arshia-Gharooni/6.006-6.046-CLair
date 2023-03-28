import java.util.*;

public class WeightedIntervalScheduling {

    static class Interval implements Comparable<Interval> {
        int start;
        int end;
        int weight;
        
        public Interval(int start, int end, int weight) {
            this.start = start;
            this.end = end;
            this.weight = weight;
        }
        
        @Override
        public int compareTo(Interval other) {
            return this.end - other.end;
        }
    }
    
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        List<Interval> intervals = new ArrayList<>();
        System.out.print("Enter the number of intervals: ");
        int n = scanner.nextInt();
        for (int i = 0; i < n; i++) {
            System.out.print("Enter the start time of interval " + (i+1) + ": ");
            int start = scanner.nextInt();
            System.out.print("Enter the end time of interval " + (i+1) + ": ");
            int end = scanner.nextInt();
            System.out.print("Enter the weight of interval " + (i+1) + ": ");
            int weight = scanner.nextInt();
            intervals.add(new Interval(start, end, weight));
        }
        int maxWeight = findMaxWeight(intervals);
        System.out.println("Maximum weight that can be obtained is: " + maxWeight);
    }
    
    public static int findMaxWeight(List<Interval> intervals) {
        Collections.sort(intervals);
        int[] maxWeight = new int[intervals.size()];
        maxWeight[0] = intervals.get(0).weight;
        for (int i = 1; i < intervals.size(); i++) {
            int weight = intervals.get(i).weight;
            int compatible = findCompatible(intervals, i);
            if (compatible != -1) {
                weight += maxWeight[compatible];
            }
            maxWeight[i] = Math.max(weight, maxWeight[i-1]);
        }
        return maxWeight[intervals.size()-1];
    }
    
    public static int findCompatible(List<Interval> intervals, int index) {
        int low = 0;
        int high = index-1;
        while (low <= high) {
            int mid = (low+high)/2;
            if (intervals.get(mid).end <= intervals.get(index).start) {
                if (intervals.get(mid+1).end <= intervals.get(index).start) {
                    low = mid+1;
                } else {
                    return mid;
                }
            } else {
                high = mid-1;
            }
        }
        return -1;
    }
}