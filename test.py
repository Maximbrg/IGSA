# import classDiagramEvaluetion as cde
# import networkx as nx
# import numpy as np
# import math
#
# from collections import defaultdict




# maps = cde.load_domain(experiment='1')
# maps = maps[1]
#
# similarity_type_matrix = {}
#
# dict_info_2 = {'Class': [],
#               'Abstract': [],
#               'Interface': []
#               }
#
# dict_info = { 'Class': {},
#               'Abstract': {},
#               'Interface': {}
#
# }
# print('a')
# classes_info = ['Class', 'Abstract', 'Interface']
# i = 0
# for vertex_a in classes_info:
#     for vertex_b in classes_info:
#         dict_info[vertex_a][vertex_b] = 999
#
# for map in maps:
#     name = map[1].split('/')[len(map[1].split('/'))-1]
#     map = map[0]
#
#     dict_info = {'Class': {},
#                  'Abstract': {},
#                  'Interface': {}
#
#                  }
#
#     for vertex_a in classes_info:
#         for vertex_b in classes_info:
#             dict_info[vertex_a][vertex_b] = 999
#     print(i)
#     if i == 69:
#         print('d')
#     i = i + 1
#     G = nx.Graph()
#     dict_info_2 = {'Class': [],
#                    'Abstract': [],
#                    'Interface': []
#                    }
#     edges = []
#     for node_a in map.graph.keys():
#         dict_info_2[map.vertex_type[node_a]].append(node_a)
#         for node_b in map.graph[node_a]:
#             G.add_edge(node_a, node_b)
#
#     # print(nx.shortest_path(G, source=-1, target=-2))
#     # G
#
#
#     for type_a in classes_info:
#         for type_b in classes_info:
#             if type_b == type_a:
#                 dict_info[type_a][type_b] = 0
#             else:
#                 min = dict_info[type_a][type_b]
#                 for vertex_a in dict_info_2[type_a]:
#                     for vertex_b in dict_info_2[type_b]:
#                         try:
#                             path_length = len(nx.shortest_path(G, source=-1, target=-2)) - 1
#                             if path_length < min:
#                                 min = path_length
#                                 dict_info[type_a][type_b] = path_length
#                         except:
#                             continue
#
#
#     # print(BFS_SP(graph, -1, -2))
#     max_min = 0
#     for type_a in dict_info.keys():
#         for type_b in dict_info[type_a].keys():
#             if dict_info[type_a][type_b] == 999:
#                 continue
#             elif dict_info[type_a][type_b] > max_min:
#                 max_min = dict_info[type_a][type_b]
#
#     for type_a in dict_info.keys():
#         for type_b in dict_info[type_a].keys():
#             if dict_info[type_a][type_b] == 999:
#                 dict_info[type_a][type_b] = 0
#             elif dict_info[type_a][type_b] == 0:
#                 dict_info[type_a][type_b] = 1
#             else:
#                 dict_info[type_a][type_b] = 1 - (dict_info[type_a][type_b]/max_min)
#     similarity_type_matrix[name] = dict_info
#
#
#
# from collections import defaultdict
#
# i = 0
# dict_map = {}
#
#
# # Function to build the graph
# def build_graph(edges):
#     'UsiXML-task.ecore' = {dict: 3}
#     {'Class': {'Class': 1, 'Abstract': 0.0, 'Interface': 0}, 'Abstract': {'Class': 0.0, 'Abstract': 1, 'Interface': 0},
#      'Interface': {'Class': 0, 'Abstract': 0, 'Interface': 1}}  # edges = [
#     #     ["A", "B"], ["A", "E"],
#     #     ["A", "C"], ["B", "D"],
#     #     ["B", "E"], ["C", "F"],
#     #     ["C", "G"], ["D", "E"]
#     # ]
#     graph = defaultdict(list)
#
#     # Loop to iterate over every
#     # edge of the graph
#     for edge in edges:
#         a, b = edge[0], edge[1]
#
#         # Creating the graph
#         # as adjacency list
#         graph[a].append(b)
#         graph[b].append(a)
#     return graph
#
#
#
# # graph = build_graph()
# #
# print(dict_info)


import json

with open('data/wikiHow/maps/wikiHow0.json', encoding="utf8") as f:
    data = json.load(f)

MainTask = data[0]['MainTask']
Steps = data[0]['Steps']
Categories = data[0]['Categories']
print()