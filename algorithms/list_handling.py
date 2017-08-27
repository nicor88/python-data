import collections

# Reverse an array
l = [{'name': 'Nicola'}, {'name': 'Anne'}]
l_reversed = list(reversed(l))

print(l)
print(l_reversed)

# Left rotation
d = [1, 2, 3, 4, 5]


def array_left_rotation(a, rotation):
    a_deque = collections.deque(a)
    left_rotation = rotation * -1
    a_deque.rotate(left_rotation)
    a_rotated = list(a_deque)
    return a_rotated

d_rotated = array_left_rotation(d, 2)
print(d)
print(d_rotated)
