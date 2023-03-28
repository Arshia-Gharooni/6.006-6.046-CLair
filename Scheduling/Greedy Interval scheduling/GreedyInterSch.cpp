#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

struct Interval {
    int start;
    int end;
};

bool cmp(Interval a, Interval b) {
    return a.end < b.end;
}

int main() {
    int n;
    cout << "Enter the number of intervals: ";
    cin >> n;

    vector<Interval> intervals(n);
    cout << "Enter the start and end time of each interval:\n";
    for (int i = 0; i < n; i++) {
        cin >> intervals[i].start >> intervals[i].end;
    }

    sort(intervals.begin(), intervals.end(), cmp);

    int count = 1;
    int prev_end = intervals[0].end;

    for (int i = 1; i < n; i++) {
        if (intervals[i].start >= prev_end) {
            count++;
            prev_end = intervals[i].end;
        }
    }

    cout << "Maximum number of intervals that can be scheduled: " << count << endl;

    return 0;
}