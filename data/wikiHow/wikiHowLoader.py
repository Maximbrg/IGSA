import pickle
import os
from Framework.ModelElement.wikiHow import wiki_how
import pandas as pd
import spacy
import json


class loaderWikiHow:

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
                    if '.json' in name:

                        if name not in names.keys():
                            try:
                                names[name] = 0
                                # class_diagram = UCD(yourpath+'/'+name)
                                with open(root + '/' + name, encoding="utf8") as f:
                                    data = json.load(f)

                                for json_map in data:

                                    wikiH = wiki_how(json_map)
                                    maps.append((wikiH, root + '/' + name + str(counter)))
                                    counter += 1
                                    # if counter % 10 == 0:
                                    #     print(counter)
                                    #     if counter == 15:
                                    #         print(4)
                            except:
                                print('bla')

                                continue


                        else:
                            print('1')
            # with open(path, 'wb') as handle:
            #     pickle.dump(maps, handle, protocol=pickle.HIGHEST_PROTOCOL)

            return maps
