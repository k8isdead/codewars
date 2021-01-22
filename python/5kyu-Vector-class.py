from math import sqrt


class Vector:
  '''
  Create a Vector object that supports addition, subtraction, dot products, and norms. So, for example:
  a = Vector([1, 2, 3])
  b = Vector([3, 4, 5])
  c = Vector([5, 6, 7, 8])

  a.add(b)      # should return a new Vector([4, 6, 8])
  a.subtract(b) # should return a new Vector([-2, -2, -2])
  a.dot(b)      # should return 1*3 + 2*4 + 3*5 = 26
  a.norm()      # should return sqrt(1^2 + 2^2 + 3^2) = sqrt(14)
  a.add(c)      # raises an exception
  '''
  def __init__(self, iterable):
        self._v = tuple(x for x in iterable)

    def __str__(self):
        return str(self._v).replace(' ', '')
        
    def check(self, other):
        if not len(self._v) == len(other._v):
            raise ValueError('Vectors of different length')

    def add(self, other):
        self.check(other)
        return Vector(s + o for s, o in zip(self._v, other._v))

    def subtract(self, other):
        self.check(other)
        return Vector(s - o for s, o in zip(self._v, other._v))

    def dot(self, other):
        self.check(other)
        return sum(s * o for s, o in zip(self._v, other._v))

    def norm(self):
        return sqrt(sum(sqrt(x) for x in self._v))

    def equals(self, other):
        return self._v == other._v
