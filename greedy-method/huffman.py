import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def print_huffman_codes(root, code):
    if root is None:
        return
    if root.char != '-':
        print(f"{root.char}: {code}")
    print_huffman_codes(root.left, code + "0")
    print_huffman_codes(root.right, code + "1")

def huffman_coding(chars, freqs):
    heap = []
    for i in range(len(chars)):
        heapq.heappush(heap, HuffmanNode(chars[i], freqs[i]))

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        node = HuffmanNode('-', left.freq + right.freq)
        node.left = left
        node.right = right
        heapq.heappush(heap, node)

    root = heapq.heappop(heap)
    print_huffman_codes(root, "")

if __name__ == "__main__":
    chars = ['a', 'b', 'c', 'd', 'e', 'f']
    freqs = [5, 9, 12, 13, 16, 45]
    huffman_coding(chars, freqs)
