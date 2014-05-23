# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# A longer example for a class: vectors for 3D geometry

# <markdowncell>

# Unfortunately some malicious person has mutilated the definition of class Vector, so it doesn't work any more. Please fix it!

# <codecell>

import numbers

# <codecell>

class Vector(object):
    
    def __init__(self, x, y, z):
        assert isinstance(x, numbers.Number)
        assert isinstance(y, numbers.Number)
        assert isinstance(z, numbers.Number)
        self.x = x
        self.y = y
        self.z = z
        
    def __repr__(self):
        return "Vector(%s, %s, %s)" % (repr(self.x), repr(self.y), repr(self.z))
    
    def __getitem__(self, index):
        assert 0 <= index < 3
        raise NotImplemented

    def __add__(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)
    
    def __mul__(self, other):
        assert isinstance(other, numbers.Number)
        return Vector(other*self.x, other*self.y, other*self.z)
    __rmul__ = __mul__

    def cross(self, other):
        raise NotImplemented

# <headingcell level=2>

# Creating and inspecting vectors

# <codecell>

ex = Vector(1, 0, 0)
ey = Vector(0, 1, 0)
ez = Vector(0, 0, 1)

# <codecell>

ex, ey, ez

# <codecell>

# This should fail with an AssertionError
foo = Vector('a', None, Vector)

# <codecell>

ex[0], ex[1], ex[2]

# <codecell>

# This should fail with an AssertionError
ex[3]

# <codecell>

# This should fail with an AssertionError
ex[-10]

# <headingcell level=2>

# Artithmetic on vectors

# <codecell>

ex+ey+ez

# <codecell>

ex-ey

# <codecell>

# This should fail with an AssertionError
ex+2

# <codecell>

2*ex, ex*2

# <codecell>

ex.dot(ex), ex.dot(ey), ex.dot(ez)

# <codecell>

ex.norm(), ey.norm(), ez.norm()

# <codecell>

ex.cross(ex), ex.cross(ey), ex.cross(ez)

