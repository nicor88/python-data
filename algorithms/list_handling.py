import collections

# Reverse an array
l = [{'name': 'Nicola'}, {'name': 'Anne'}]
l_reversed = list(reversed(l))

print(l)
print(l_reversed)

# Left rotation
d = [1, 2, 3, 4, 5]
d_deque = collections.deque(d)
# rotate left, use positive to rotate right
d_deque.rotate(2*-1)
d_rotated = list(d_deque)

print(d)
print(d_rotated)


def array_left_rotation(a, n, k):
    a_deque = collections.deque(a)
    left_rotation = n * -1
    a_deque.rotate(left_rotation)
    a_rotated = list(a_deque)
    return a_rotated