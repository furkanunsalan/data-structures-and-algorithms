import heapq

# Priority Queue using heapq (Min Heap)
class PriorityQueue:
    def __init__(self):
        self._queue = []

    def push(self, item):
        heapq.heappush(self._queue, item)

    def pop(self):
        return heapq.heappop(self._queue)

    def peek(self):
        return self._queue[0] if self._queue else None

# Test Priority Queue
pq = PriorityQueue()
pq.push(10)
pq.push(1)
pq.push(30)
print("Top Element:", pq.peek())
print("Popped Element:", pq.pop())
print("Top Element after pop:", pq.peek())
