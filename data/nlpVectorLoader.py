import pickle
import spacy
import pandas as pd


class vectors:

    def __init__(self, maps=0):
        self.vec = None
        self.maps = maps
        self.nlp = spacy.load('en_core_web_lg')

    def create_vectors(self, path, verbose=0):

        if self.maps == 0:
            with open(path, 'rb') as handle:
                b = pickle.load(handle)
            self.vec = b
        else:

            i = 0
            data = {'entity_1': [], 'entity_2': []}
            for map in self.maps[1]:

                for edges in map[0].edge_info:
                    name_1 = map[0].vertex_info[edges[0]]
                    name_2 = map[0].vertex_info[edges[1]]

                    data['entity_1'].append(name_1)
                    data['entity_2'].append(name_2)

            df = pd.DataFrame(data)

            entites_calculate = set()
            for row in df.iterrows():
                name_1 = row[1]['entity_1']
                name_2 = row[1]['entity_2']

                entites_calculate.add(name_1)
                entites_calculate.add(name_2)
            i = 0
            vectors = {}
            for entity in entites_calculate:
                print(i)
                i = i + 1
                token = self.nlp(str(entity))
                vectors[entity] = token

            with open(path, 'wb') as handle:
                pickle.dump(vectors, handle, protocol=pickle.HIGHEST_PROTOCOL)

            self.vec = vectors

    def add_new_vectors(self, map):

        entities_calculate = set()

        for edges in map.edge_info:
            name_1 = map.vertex_info[edges[0]]
            name_2 = map.vertex_info[edges[1]]

            entities_calculate.add(name_1)
            entities_calculate.add(name_2)

        for entity in entities_calculate:
            token = self.nlp(str(entity))
            self.vec[entity] = token

    def getVectors(self):
        return self.vec
