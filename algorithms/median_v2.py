def heappush(heap, item):
    """Push item onto heap, maintaining the heap invariant."""
    heap.append(item)
    _siftdown(heap, 0, len(heap)-1)


def heappop(heap):
    """Pop the smallest item off the heap, maintaining the heap invariant."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup(heap, 0)
        return returnitem
    return lastelt


def heapreplace(heap, item):
    """Pop and return the current smallest value, and add the new item.

    This is more efficient than heappop() followed by heappush(), and can be
    more appropriate when using a fixed-size heap.  Note that the value
    returned may be larger than item!  That constrains reasonable uses of
    this routine unless written as part of a conditional replacement:

        if item > heap[0]:
            item = heapreplace(heap, item)
    """
    returnitem = heap[0]    # raises appropriate IndexError if heap is empty
    heap[0] = item
    _siftup(heap, 0)
    return returnitem


def heappushpop(heap, item):
    """Fast version of a heappush followed by a heappop."""
    if heap and heap[0] < item:
        item, heap[0] = heap[0], item
        _siftup(heap, 0)
    return item


def _heappop_max(heap):
    """Maxheap version of a heappop."""
    lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
    if heap:
        returnitem = heap[0]
        heap[0] = lastelt
        _siftup_max(heap, 0)
        return returnitem
    return lastelt


def _heapreplace_max(heap, item):
    """Maxheap version of a heappop followed by a heappush."""
    returnitem = heap[0]    # raises appropriate IndexError if heap is empty
    heap[0] = item
    _siftup_max(heap, 0)
    return returnitem


def _heapify_max(x):
    """Transform list into a maxheap, in-place, in O(len(x)) time."""
    n = len(x)
    for i in reversed(range(n//2)):
        _siftup_max(x, i)

# 'heap' is a heap at all indices >= startpos, except possibly for pos.  pos
# is the index of a leaf with a possibly out-of-order value.  Restore the
# heap invariant.
def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem


def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)


def _siftdown_max(heap, startpos, pos):
    'Maxheap variant of _siftdown'
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if parent < newitem:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem


def _siftup_max(heap, pos):
    'Maxheap variant of _siftup'
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the larger child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of larger child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[rightpos] < heap[childpos]:
            childpos = rightpos
        # Move the larger child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown_max(heap, startpos, pos)


# helper object for max heap
class MaxHeapObj(object):
    def __init__(self, val): self.val = val

    def __lt__(self, other): return self.val > other.val

    def __eq__(self, other): return self.val == other.val

    def __str__(self): return str(self.val)


# heap with min on top
class MinHeap(object):
    def __init__(self): self.h = []

    def heappush(self, x): heappush(self.h, x)

    def heappop(self): return heappop(self.h)

    def __getitem__(self, i): return self.h[i]

    def __len__(self): return len(self.h)


# heap with max on top
class MaxHeap(MinHeap):
    def heappush(self, x): heappush(self.h, MaxHeapObj(x))

    def heappop(self): return heappop(self.h).val

    def __getitem__(self, i): return self.h[i].val


def add_number(number, lowers, highers):
    """
    Add a number to lowers or highers heap
    :param number: integer to add to heap
    :param lowers: heap with max on top, contain the lowers numbers
    :param highers: heap with min on top, contain the highers numbers
    :return:
    """

    # lowers[0] is the max in the lowers heap
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
    smaller_heap = highers if len(lowers) > len(highers) else lowers

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
