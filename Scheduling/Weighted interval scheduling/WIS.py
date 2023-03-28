def weighted_interval_scheduling(intervals):
    # Sort intervals by their end time
    intervals.sort(key=lambda x: x[1])
    
    # Create an array to store the maximum weight of each interval
    # where max_weight[i] represents the maximum weight of the interval
    # set that ends at i
    max_weight = [0] * len(intervals)
    
    # Initialize the first maximum weight to be the weight of the first interval
    max_weight[0] = intervals[0][2]
    
    # Calculate the maximum weight for each interval using dynamic programming
    for i in range(1, len(intervals)):
        # Find the latest non-overlapping interval j
        j = i - 1
        while j >= 0 and intervals[j][1] > intervals[i][0]:
            j -= 1
        
        # Calculate the maximum weight of the current interval
        max_weight[i] = max(intervals[i][2] + max_weight[j], max_weight[i-1])
    
    # Return the maximum weight of the last interval
    return max_weight[-1]


# Get the input from the user
n = int(input("Enter the number of intervals: "))
intervals = []
for i in range(n):
    start, end, weight = map(int, input(f"Enter the start time, end time, and weight of interval {i+1}: ").split())
    intervals.append((start, end, weight))

# Call the function to get the maximum total weight of non-overlapping intervals
max_weight = weighted_interval_scheduling(intervals)

# Print the result
print("The maximum total weight of non-overlapping intervals is:", max_weight)