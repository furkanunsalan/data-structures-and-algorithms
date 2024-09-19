class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def get_max_value(capacity, items):
    items.sort(key=lambda x: x.value / x.weight, reverse=True)
    total_value = 0

    for item in items:
        if capacity - item.weight >= 0:
            capacity -= item.weight
            total_value += item.value
        else:
            total_value += (item.value / item.weight) * capacity
            break

    return total_value

if __name__ == "__main__":
    items = [Item(10, 60), Item(20, 100), Item(30, 120)]
    capacity = 50
    print("Maximum value we can obtain =", get_max_value(capacity, items))
