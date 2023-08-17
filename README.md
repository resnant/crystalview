# crystalview

The original code is written by @lan496 and taken from here:
https://gist.github.com/lan496/3f60b6474750a6fd2b4237e820fbfea4


## Usage

```python
from crystalview.plot import plot3d
from pymatgen.core import Structure, Lattice
import numpy as np

# rutile structure taken from mp-2657
a = 4.653
c = 2.969
x_4f = 0.3046

lattice = Lattice.from_parameters(a, a, c, 90, 90, 90)
species = ["Ti", "Ti", "O", "O", "O", "O"]
frac_coords = np.array([
    [0, 0, 0],                      # Ti(2a)
    [0.5, 0.5, 0.5],                # Ti(2a)
    [x_4f, x_4f, 0],                # O(4f)
    [1 - x_4f, 1 - x_4f, 0],        # O(4f)
    [0.5 - x_4f, 0.5 + x_4f, 0.5],  # O(4f)
    [0.5 + x_4f, 0.5 - x_4f, 0.5],  # O(4f)
])
structure = Structure(lattice, species, frac_coords)

plot3d(structure, spacefill=True)
```