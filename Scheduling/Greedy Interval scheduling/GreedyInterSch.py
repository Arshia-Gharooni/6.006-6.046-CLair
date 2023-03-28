def interval_scheduling(intervals):
    """
    Finds the maximum number of non-overlapping intervals using greedy algorithm.

    :param intervals: A list of tuples representing the intervals. Each tuple contains the start and end time of the interval.
    :return: The maximum number of non-overlapping intervals.
    """
    # sort the intervals by end time in ascending order
    intervals = sorted(intervals, key=lambda x: x[1])

    # initialize the count of non-overlapping intervals and the end time of the last selected interval
    count = 0
    last_end_time = 0

    # iterate over all intervals
    for interval in intervals:
        # if the start time of the current interval is greater than or equal to the end time of the last selected interval
        if interval[0] >= last_end_time:
            # select the current interval and update the last end time
            count += 1
            last_end_time = interval[1]

    # return the count of non-overlapping intervals
    return count


#here is an example
intervals = [(1, 3), (2, 4), (3, 5), (4, 6), (5, 7)]
max_intervals = interval_scheduling(intervals)
print(f"Maximum number of non-overlapping intervals: {max_intervals}")