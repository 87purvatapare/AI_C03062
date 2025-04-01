
import heapq

def jobScheduling(arr):
    n = len(arr)
    arr.sort(key=lambda x: x[1])  # Sort by deadline
    result = []
    maxHeap = []

    for i in range(n - 1, -1, -1):
        if i == 0:
            slots_available = arr[i][1]
        else:
            slots_available = arr[i][1] - arr[i - 1][1]

        heapq.heappush(maxHeap, (-arr[i][2], arr[i][1], arr[i][0]))  # Max heap (negative profit)

        while slots_available and maxHeap:
            profit, deadline, job_id = heapq.heappop(maxHeap)
            slots_available -= 1
            result.append([job_id, deadline])

    result.sort(key=lambda x: x[1])  

    print(f'\nJob Scheduling Problem:\nFollowing is the maximum profit sequence of jobs: {result}')


A = [
    ['A', 2, 100],
    ['B', 1, 19],
    ['C', 2, 27],
    ['D', 1, 25],
    ['E', 3, 15]
]

jobScheduling(A)  
