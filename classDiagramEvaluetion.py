from data.classDiagram.classDiagramLoader import loaderCD
from data.meMap.meMapLoader import loaderMeMap
from data.wikiHow.wikiHowLoader import loaderWikiHow
from data.nlpVectorLoader import vectors as vec
import Framework.ThresholdSettings.IGSASettings as ts
from Framework.TypeSimilarities.classDiagramSimilarties import matrix_cd
from Framework.TypeSimilarities.meMapSimilarities import matrix_me
from Framework.TypeSimilarities.wikiHowSimilarties import matrix_wh

import helpFuntions as hf
import pandas as pd

settings = ts.getSettings()


def load_domain(verbose=0, experiment='2'):
    if verbose == 0:
        settings[
            'exp_path'] = f'{settings["path"]}data\\classDiagram\\Experiment_{experiment}\\'
        settings[
            'query path'] = f'{settings["path"]}data\\classDiagram\\Experiment_{experiment}\\queries\\'
        new = loaderCD(settings['exp_path'] + 'ecore')
        maps = new.load(settings['exp_path'] + 'class_diagrams.pickle')
        settings['structure'] = matrix_cd()
        return 'Class Diagram', maps

    elif verbose == 1:
        settings['exp_path'] = f'{settings["path"]}data\\meMap\\'
        settings['query path'] = f'{settings["path"]}data\\meMap\\queries\\'
        new = loaderMeMap(settings['exp_path'] + 'maps')
        maps = new.load(settings['exp_path'] + 'class_diagrams.pickle')
        settings['structure'] = matrix_me()
        return 'ME-MAP', maps

    elif verbose == 2:
        settings['exp_path'] = f'{settings["path"]}data\\wikiHow\\'
        settings['query path'] = f'{settings["path"]}data\\wikiHow\\queries\\'
        new = loaderWikiHow(settings['exp_path'] + 'maps')
        maps = new.load(settings['exp_path'] + 'class_diagrams.pickle')
        settings['structure'] = matrix_wh()
        return 'Wiki How', maps


# Load the queries

def run_experiment(maps, vectors, levels=['medium'], domain=0, verbose=0):
    print('Domain: ', maps[0])
    maps = maps[1]
    evaluation = pd.read_csv(settings['exp_path'] + 'evaluation.csv')
    if verbose == 0:
        print('Algorithm: IGSA algorithm')
    else:
        print('Algorithm: A* semantic algorithm')
    for level in levels:
        print('----------------')
        queries, vectors = hf.load_queries(settings['query path'], vectors, levels=[level], verbose=domain)
        settings['vectors'] = vectors.getVectors()
        relevant_diagrams, time_q = hf.search_ucd(maps, queries, settings, verbose=verbose)
        avg_exact, avg_domain, avg_semantic, recall, info = hf.evaluate(evaluation, relevant_diagrams)
        print(f'Complexity level is: {level}')
        print(f'Exact MRR: {avg_exact}')
        print(f'Domain MRR: {avg_domain}')
        print(f'Recall@10: {recall}')
        print(f'Average time: {(sum(time_q)) / len(queries)}')
        print(f'Semantic: {avg_semantic}')
        print('')
        info['time'] = time_q
        return level, avg_exact, avg_domain, recall, (sum(time_q)) / len(queries), avg_semantic, info


def run():
    maps = load_domain(verbose=settings['domain'], experiment='1')
    # Load Semantic vectors
    if not settings['domain']:
        vectors = vec(0)
        vectors.create_vectors(settings['exp_path'] + 'vectors.pickle')
    else:
        vectors = vec(maps)
        vectors.create_vectors(settings['exp_path'] + 'vectors.pickle')

    _, _, _, _, _, _, _ = \
        run_experiment(maps, vectors, levels=['multipath'], domain=settings['domain'], verbose=settings['algorithm'])


if __name__ == '__main__':
    run()
