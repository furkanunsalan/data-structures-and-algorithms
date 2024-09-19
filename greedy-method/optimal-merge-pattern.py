import heapq

def min_computation(files):
    heapq.heapify(files)
    total_computation = 0

    while len(files) > 1:
        first = heapq.heappop(files)
        second = heapq.heappop(files)
        merge_cost = first + second
        total_computation += merge_cost
        heapq.heappush(files, merge_cost)

    return total_computation

if __name__ == "__main__":
    files = [40, 30, 20, 10]
    print("Minimum computation cost:", min_computation(files))
