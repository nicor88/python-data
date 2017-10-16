import queue as Q


class ReversePriorityQueue(Q.PriorityQueue):
    def put(self, number):
        newtup = (-1 * number, number)
        Q.PriorityQueue.put(self, newtup)

    def get(self):
        tup = Q.PriorityQueue.get(self)
        return tup[1]
