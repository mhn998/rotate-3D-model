from stl import mesh
import math

model = mesh.Mesh.from_file('assets/raw_039.stl')
model.rotate([0, 1, 0], math.radians(180))
model.save('output/raw_039_rotated.stl')
