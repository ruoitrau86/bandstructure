import numpy as np
from .lattice import Lattice


class HoneycombLattice(Lattice):
    def initialize(self):
        l1 = np.array([np.sqrt(3), 1])/2
        l2 = np.array([np.sqrt(3), -1])/2

        b1 = np.array([0, 0])
        b2 = np.array([np.sqrt(3), 0])/3

        a = np.linalg.norm(b2)

        self.addLatticevector(l1/a)
        self.addLatticevector(l2/a)
        self.addBasisvector(b1/a)
        self.addBasisvector(b2/a)
