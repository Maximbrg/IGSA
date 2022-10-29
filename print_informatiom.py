from data.classDiagram.classDiagramLoader import loaderCD
from data.meMap.meMapLoader import loaderMeMap
from data.wikiHow.wikiHowLoader import loaderWikiHow
from data.nlpVectorLoader import vectors
import Framework.ThresholdSettings.IGSASettings as ts
from Framework.TypeSimilarities.classDiagramSimilarties import matrix_cd
from Framework.TypeSimilarities.meMapSimilarities import matrix_me
from Framework.TypeSimilarities.wikiHowSimilarties import matrix_wh

import helpFuntions as hf
import pandas as pd
import time

settings = ts.getSettings()


def load_domain(verbose=0, experiment='2'):
    if verbose == 0:
        settings[
            'exp_path'] = f'C:\\Users\\max_b\\PycharmProjects\\igsa\\data\\classDiagram\\Experiment_{experiment}\\'
        settings[
            'query path'] = f'C:\\Users\\max_b\\PycharmProjects\\igsa\\data\\classDiagram\\Experiment_{experiment}\\queries\\'
        new = loaderCD(settings['exp_path'] + 'ecore')
        maps = new.load(settings['exp_path'] + 'class_diagrams.pickle')
        settings['structure'] = matrix_cd()
        return 'Class Diagram', maps

    elif verbose == 1:
        settings['exp_path'] = f'C:\\Users\\max_b\\PycharmProjects\\igsa\\data\\meMap\\'
        settings['query path'] = 'C:\\Users\\max_b\\PycharmProjects\\igsa\\data\\meMap\\queries\\'
        new = loaderMeMap(settings['exp_path'] + 'maps')
        maps = new.load(settings['exp_path'] + 'class_diagrams.pickle')
        settings['structure'] = matrix_me()
        return 'ME-MAP', maps

    elif verbose == 2:
        settings['exp_path'] = f'C:\\Users\\max_b\\PycharmProjects\\igsa\\data\\wikiHow\\'
        settings['query path'] = 'C:\\Users\\max_b\\PycharmProjects\\igsa\\data\\wikiHow\\queries\\'
        new = loaderWikiHow(settings['exp_path'] + 'maps')
        maps = new.load(settings['exp_path'] + 'class_diagrams.pickle')
        settings['structure'] = matrix_wh()
        return 'Wiki How', maps

maps = load_domain(verbose=0, experiment='1')

vectors = vectors(0)
vectors.create_vectors(settings['exp_path'] + 'vectors.pickle')
queries, vectors = hf.load_queries(settings['query path'], vectors, levels=['multipath'], verbose=0)
settings['vectors'] = vectors.getVectors()
print(queries[4][1].vertex_info)
name = 'SmartHome.ecore'
ids = [-2, -3, -3]
for map in maps[1]:
    if name in map[1]:
        print('-----------------------')
        print(map[0].vertex_info)
        for id in ids:
            try:
                print(map[0].vertex_info[id])
            except:
                break
# def get_path(name, ids):
#     return 0