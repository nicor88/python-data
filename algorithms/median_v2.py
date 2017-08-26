import heapq


# helper object for max heap
class MaxHeapObj(object):
    def __init__(self, val): self.val = val

    def __lt__(self, other): return self.val > other.val

    def __eq__(self, other): return self.val == other.val

    def __str__(self): return str(self.val)


# heap with min on top
class MinHeap(object):
    def __init__(self): self.h = []

    def heappush(self, x): heapq.heappush(self.h, x)

    def heappop(self): return heapq.heappop(self.h)

    def __getitem__(self, i): return self.h[i]

    def __len__(self): return len(self.h)


# heap with max on top
class MaxHeap(MinHeap):
    def heappush(self, x): heapq.heappush(self.h, MaxHeapObj(x))

    def heappop(self): return heapq.heappop(self.h).val

    def __getitem__(self, i): return self.h[i].val


def add_number(number, lowers, highers):
    """
    Add a number to lowers or highers heap
    :param number: integer to add to heap
    :param lowers: heap with max on top, contain the lowers numbers
    :param highers: heap with min on top, contain the highers numbers
    :return:
    """
    if len(lowers) == 0 or number < lowers[0]:
        lowers.heappush(number)
    else:
        highers.heappush(number)


def rebalance(lowers, highers):
    """
    Give 2 heaps, it will return the heaps with same length
    :param lowers:
    :param highers:
    :return:
    """
    bigger_heap = lowers if len(lowers) > len(highers) else highers
    smaller_heap = lowers if len(lowers) < len(highers) else highers

    if len(bigger_heap) - len(smaller_heap) >= 2:
        smaller_heap.heappush(bigger_heap.heappop())


def get_median(lowers, highers):
    bigger_heap = lowers if len(lowers) > len(highers) else highers
    smaller_heap = highers if len(lowers) > len(highers) else lowers

    if len(bigger_heap) == len(smaller_heap):
        # print('Sum {}'.format(bigger_heap[0] + smaller_heap[0]))
        return (bigger_heap[0] + smaller_heap[0]) / 2
    else:
        return float(bigger_heap[0])


n = 10
a = []

# in lowers max is on top lowers[0] return the max
lowers = MaxHeap()

# in highers max is on top lowers[0] return the max
highers = MinHeap()

for a_i in range(n):
    # a_t = randint(0, 9000)
    a_t = a_i + 1
    add_number(a_t, lowers, highers)
    rebalance(lowers, highers)
    print(get_median(lowers, highers))
