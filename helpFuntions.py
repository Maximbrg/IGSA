import os
import json
import time
from Framework.ModelElement.classDiagram import UCD
from Framework.ModelElement.meMap import me_map
from Framework.ModelElement.wikiHow import wiki_how
from Framework.IGSA import search_igsa
from Framework.A_star_semantic import search_a_star_semantic


def load_queries(query_path, vectors, levels=['simple', 'medium', 'complex', 'multi-path'], verbose=0):
    queries = []
    for level in levels:
        for queryName in os.listdir(query_path + level + "/"):
            key = queryName.split('.')[0]
            if verbose == 0:
                value = UCD(query_path + level + "/" + queryName)
            elif verbose == 1:
                value = me_map(query_path + level + "/" + queryName)
            elif verbose == 2:
                with open(query_path + level + "/" + queryName, encoding="utf8") as f:
                    data = json.load(f)
                value = wiki_how(data[0])
                if level == 'complex':
                    if queryName == '31.json':
                        value.update_vertex('-2', 'category', 'electronic')
                    if queryName == '32.json':
                        value.update_vertex('-2', 'Ingredient', 'peppers')
                    if queryName == '33.json':
                        value.update_vertex('-2', 'Tip', 'have insurance')
                    if queryName == '34.json':
                        value.update_vertex('-2', 'category', 'computers')
                    if queryName == '35.json':
                        value.update_vertex('-2', 'category', 'computers')

            queries.append((key, value))
            vectors.add_new_vectors(value)

    return queries, vectors


def search_ucd(maps, queries, settings, verbose=0):
    if verbose == 0:
        search = search_igsa(settings)
    if verbose == 1:
        search = search_a_star_semantic(settings)
    time_info = []
    relevant_diagrams = {}
    for query in queries:
        key = query[0]
        relevant_diagrams[key] = []
        start = time.time()
        for map in maps:

            name = map[1].split('\\')
            name = name[len(name) - 1].split('/')
            name = name[len(name) - 1]
            post = map[0]
            if len(post.graph.keys()) == 0:
                continue

            results = search.greedy_algorithm_recursive(post, query[1])

            outputs = search.read_results(results)
            if outputs:
                for output in outputs:
                    relevant_diagrams[key].append((name, output[0], output[1]))
        end = time.time()
        time_info.append(end - start)
        relevant_diagrams[key].sort(key=lambda tup: tup[2])
        relevant_diagrams[key].reverse()

    return relevant_diagrams, time_info


def evaluate(actual, predict):
    data = {'query': [], 'e-mrr': [], 'd-mrr': [], 'recall': [], 'time': []}
    avrege_MRR_domain = 0
    average_MRR_exact = 0
    average_semantic = 0
    average_semantic_count = 0.0
    recall_5 = 0

    for key in predict:
        data['query'].append(key)
        # print('++++++++++++++++++++++++++++++++')
        temp = predict[key]
        actual_result = actual.loc[actual['query'] == int(key)]  # int()
        # for vertex in queries[key].vertex_info.keys():
        #     print(queries[key].vertex_info[vertex], queries[key].vertex_type[vertex])

        counter = 0
        is_entered_name = False
        is_entered_path = False
        recall_entered = False
        for index, result in enumerate(temp):
            if index < 10:
                print(key, result)
                # target_class = maps[result[1]]
                # for item in result[0][0]:
                #     print(str(target_class.vertex_info[item]),str(target_class.vertex_type[item]))

            predicted_path = ''.join(str(e) for e in result[1])
            predicted_name = result[0]

            expected_path = actual_result['result1'].values[0].replace(',', '')
            # print(expected_path)
            expected_path_2 = actual_result['result2'].values[0].replace(',', '')
            expected_name = actual_result['domain'].values[0]

            if predicted_name == expected_name:
                # print(key + ': expected name: ', counter)
                if not is_entered_name:
                    if counter < 10:
                        recall_5 = recall_5 + 1
                        recall_entered = True
                        data['recall'].append(1)

                    avrege_MRR_domain = avrege_MRR_domain + (1 / (counter + 1))
                    data['d-mrr'].append(1 / (counter + 1))
                    is_entered_name = True
                    average_semantic += result[2]  #####
                    average_semantic_count = average_semantic_count + 1


                if predicted_path == expected_path or predicted_path == expected_path_2:
                    # print(key + ':expected path: ', counter)
                    if not is_entered_path:
                        is_entered_path = True
                        average_MRR_exact = average_MRR_exact + (1 / (counter + 1))
                        data['e-mrr'].append(1 / (counter + 1))

            counter += 1
        if not is_entered_path:
            data['e-mrr'].append(0)
        if not is_entered_name:
            data['d-mrr'].append(0)
        if not recall_entered:
            data['recall'].append(0)
    # print(len(predict))
    return average_MRR_exact / (len(predict) + 0.00001), avrege_MRR_domain / (len(
        predict) + 0.00001), average_semantic / (average_semantic_count + 0.00001), recall_5 / (len(predict) + 0.00001), data
