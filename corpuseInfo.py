import main as cde
import numpy as np
import math

maps = cde.load_domain(verbose=1, experiment='0')
maps = maps[1]

vertex = []
counter = 0
relationship = []
#
# max_vertex = (0, 0)
# min_vertex = (0, 0)
#
# max_rel = 99999
# min_rel = 99999

for map in maps:
    if len(map[0].graph.keys()) < 2:
        continue
    vertex.append(len(map[0].graph.keys()))
    relationship.append(math.floor(len(map[0].edge_info.keys())))
    counter = counter + 1

print(f'Dataset Size: {counter}')
vertex = np.array(vertex)
relationship = np.array(relationship)
print(f'Average: {np.average(relationship)}')
print(f'Std: {np.std(relationship)}')
print(f'Max: {np.max(relationship)}')
print(f'Min: {np.min(relationship)}')
print(f'Median: {np.median(relationship)}')