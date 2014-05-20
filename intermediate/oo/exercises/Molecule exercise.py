# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=2>

# Atoms

# <codecell>

class Atom(object):

	def __init__(self, element, position): 
		self.element = element 
		self.position = position 

	def translate_by(self, vector):
		self.position += vector

	def center_of_mass(self): 
		return self.position 

	def mass(self): 
		return masses_by_element[self.element]

# <codecell>

masses_by_element = {'H': 1., 'C': 12., 'N': 14., 'O': 16.}

# <headingcell level=2>

# Molecules are groups of atoms (no bonds to keep it simple)

# <codecell>

class Molecule(object):

    def __init__(self, atom_dict):
        assert isinstance(atom_dict, dict)
        self.atoms = atom_dict 

    # this class needs to be completed

# <headingcell level=2>

# Chains are sequences of residues (which are molecules, to keep it simple)

# <codecell>

class Chain(object):
    
    pass
    # the real code needs to be written

# <headingcell level=2>

# A minimal version of the Vector class

# <codecell>

import numbers

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

    def __add__(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x+other.x, self.y+other.y, self.z+other.z)
    
    def __sub__(self, other):
        assert isinstance(other, Vector)
        return Vector(self.x-other.x, self.y-other.y, self.z-other.z)

    def __neg__(self):
        return Vector(-self.x, -self.y, -self.z)

    def __mul__(self, other):
        assert isinstance(other, numbers.Number)
        return Vector(other*self.x, other*self.y, other*self.z)
    __rmul__ = __mul__

    def __div__(self, other):
        assert isinstance(other, numbers.Number)
        return Vector(self.x/other, self.y/other, self.z/other)

# <headingcell level=2>

# A water molecule

# <codecell>

o =  Atom('O', Vector( 0.,              0.,  0.00655616814675))
h1 = Atom('H', Vector(-0.0756950327264, 0., -0.0520320595151))
h2 = Atom('H', Vector( 0.0756950327264, 0., -0.0520320595151))
water = Molecule({'O': o, 'H1': h1, 'H2': h2})

# <codecell>

water.center_of_mass()

# <codecell>

water.translate_by(Vector(0., -0.5, 0.))
water.center_of_mass()

# <codecell>

water.translate_by(-water.center_of_mass())
water.center_of_mass()

# <headingcell level=2>

# A peptide chains

# <codecell>

LYS_1 = Molecule({'N':    Atom('N', Vector( 0.3336,  1.0074,  1.0331)),
                  'CA':   Atom('C', Vector( 0.2429 , 1.0424 , 0.9199)),
                  'C':    Atom('C', Vector( 0.2415,  1.1932,  0.8954)),
                  'O':    Atom('O', Vector( 0.2390,  1.2719,  0.9904)),
                  'CB':   Atom('C', Vector( 0.1000 , 0.9944 , 0.9506)),
                  'CG':   Atom('C', Vector(-0.0038 , 1.0444 , 0.8543)),
                  'CD':   Atom('C', Vector(-0.1418 , 0.9911 , 0.8867)),
                  'CE':   Atom('C', Vector(-0.2457 , 1.0562 , 0.7967)),
                  'NZ':   Atom('N', Vector(-0.3794 , 0.9917 , 0.8074))})

VAL_2 = Molecule({'N':    Atom('N', Vector( 0.2467,  1.2329,  0.7688)),
                  'CA':   Atom('C', Vector( 0.2417,  1.3741,  0.7336)),
                  'C':    Atom('C', Vector( 0.0998,  1.3990,  0.6840)),
                  'O':    Atom('O', Vector( 0.0574,  1.3412,  0.5844)),
                  'CB':   Atom('C', Vector( 0.3462,  1.4126,  0.6256)),
                  'CG1':  Atom('C', Vector( 0.3289,  1.5600,  0.5850)),
                  'CG2':  Atom('C', Vector( 0.4873,  1.3911,  0.6799))})
                        
PHE_3 = Molecule({'N':    Atom('N', Vector( 0.0228,  1.4755,  0.7598)),
                  'CA':   Atom('C', Vector(-0.1151 , 1.5035,  0.7227)),
                  'C':    Atom('C', Vector(-0.1286,  1.6080,  0.6143)),
                  'O':    Atom('O', Vector(-0.0405,  1.6923,  0.5955)),
                  'CB':   Atom('C', Vector(-0.1933,  1.5551,  0.8437)),
                  'CG':   Atom('C', Vector(-0.2507,  1.4472,  0.9306)),
                  'CD1':  Atom('C', Vector(-0.1719,  1.3848,  1.0278)),
                  'CD2':  Atom('C', Vector(-0.3849,  1.4100,  0.9179)),
                  'CE1':  Atom('C', Vector(-0.2261,  1.2871,  1.1111)),
                  'CE2':  Atom('C', Vector(-0.4405,  1.3121,  1.0007)),
                  'CZ':   Atom('C', Vector(-0.3609,  1.2505,  1.0978))})

chain = Chain([LYS_1, VAL_2, PHE_3])

# <codecell>

chain.center_of_mass()

# <codecell>

chain.translate_by(-chain.center_of_mass())
chain.center_of_mass()

