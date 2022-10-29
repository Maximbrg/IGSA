import pickle
import os
from Framework.ModelElement.classDiagram import UCD
import pandas as pd
import spacy


class loaderCD:

    def __init__(self, path):
        self.path = path

    def load(self, path):

        try:
            with open(path, 'rb') as handle:
                b = pickle.load(handle)
            return b

        except:
            maps = []
            names = {}
            counter = 0
            for root, dirs, files in os.walk(self.path, topdown=False):

                for name in files:
                    if '.ecore' in name:

                        if name not in names.keys():
                            try:
                                names[name] = 0
                                # class_diagram = UCD(yourpath+'/'+name)
                                class_diagram = UCD(root + '/' + name)
                                maps.append((class_diagram, root + '/' + name))
                                counter += 1
                                if counter % 10 == 0:
                                    print(counter)
                                    if counter == 15:
                                        print(4)
                            except:
                                print('bla')

                                continue


                        else:
                            print('1')
            with open(path, 'wb') as handle:
                pickle.dump(maps, handle, protocol=pickle.HIGHEST_PROTOCOL)

            return maps