class matrix_wh:

    def __init__(self):
        self.Similarity_matrix_edge = {'non': {}}
        self.Similarity_matrix_edge['non']['non'] = 1

        self.Similarity_matrix_class = {'MainTask': {}, 'Steps': {}, 'step': {}, 'Categories': {}, 'category': {},
                                        'Ingredients': {}, 'Ingredient': {}, 'Requirements': {}, 'Requirement': {}
                                        , 'Tips': {}, 'Tip': {}}

        self.Similarity_matrix_class['MainTask']['MainTask'] = 1
        self.Similarity_matrix_class['MainTask']['Steps'] = 0
        self.Similarity_matrix_class['MainTask']['step'] = 0.5
        self.Similarity_matrix_class['MainTask']['Categories'] = 0
        self.Similarity_matrix_class['MainTask']['category'] = 0.5
        self.Similarity_matrix_class['MainTask']['Ingredients'] = 0
        self.Similarity_matrix_class['MainTask']['Ingredient'] = 0.5
        self.Similarity_matrix_class['MainTask']['Requirements'] = 0
        self.Similarity_matrix_class['MainTask']['Requirement'] = 0.5
        self.Similarity_matrix_class['MainTask']['Tips'] = 0
        self.Similarity_matrix_class['MainTask']['Tip'] = 0.5

        self.Similarity_matrix_class['Steps']['MainTask'] = 0
        self.Similarity_matrix_class['Steps']['Steps'] = 1
        self.Similarity_matrix_class['Steps']['step'] = 0
        self.Similarity_matrix_class['Steps']['Categories'] = 0.5
        self.Similarity_matrix_class['Steps']['category'] = 0
        self.Similarity_matrix_class['Steps']['Ingredients'] = 0.5
        self.Similarity_matrix_class['Steps']['Ingredient'] = 0
        self.Similarity_matrix_class['Steps']['Requirements'] = 0.5
        self.Similarity_matrix_class['Steps']['Requirement'] = 0
        self.Similarity_matrix_class['Steps']['Tips'] = 0.5
        self.Similarity_matrix_class['Steps']['Tip'] = 0

        self.Similarity_matrix_class['step']['MainTask'] = 0.5
        self.Similarity_matrix_class['step']['Steps'] = 0
        self.Similarity_matrix_class['step']['step'] = 1
        self.Similarity_matrix_class['step']['Categories'] = 0
        self.Similarity_matrix_class['step']['category'] = 0.5
        self.Similarity_matrix_class['step']['Ingredients'] = 0
        self.Similarity_matrix_class['step']['Ingredient'] = 0.5
        self.Similarity_matrix_class['step']['Requirements'] = 0
        self.Similarity_matrix_class['step']['Requirement'] = 0.5
        self.Similarity_matrix_class['step']['Tips'] = 0
        self.Similarity_matrix_class['step']['Tip'] = 0.5

        self.Similarity_matrix_class['Categories']['MainTask'] = 0
        self.Similarity_matrix_class['Categories']['Steps'] = 0.5
        self.Similarity_matrix_class['Categories']['step'] = 0
        self.Similarity_matrix_class['Categories']['Categories'] = 1
        self.Similarity_matrix_class['Categories']['category'] = 0
        self.Similarity_matrix_class['Categories']['Ingredients'] = 0.5
        self.Similarity_matrix_class['Categories']['Ingredient'] = 0
        self.Similarity_matrix_class['Categories']['Requirements'] = 0.5
        self.Similarity_matrix_class['Categories']['Requirement'] = 0
        self.Similarity_matrix_class['Categories']['Tips'] = 0.5
        self.Similarity_matrix_class['Categories']['Tip'] = 0

        self.Similarity_matrix_class['category']['MainTask'] = 0.5
        self.Similarity_matrix_class['category']['Steps'] = 0
        self.Similarity_matrix_class['category']['step'] = 0.5
        self.Similarity_matrix_class['category']['Categories'] = 0
        self.Similarity_matrix_class['category']['category'] = 1
        self.Similarity_matrix_class['category']['Ingredients'] = 0
        self.Similarity_matrix_class['category']['Ingredient'] = 0.5
        self.Similarity_matrix_class['category']['Requirements'] = 0
        self.Similarity_matrix_class['category']['Requirement'] = 0.5
        self.Similarity_matrix_class['category']['Tips'] = 0
        self.Similarity_matrix_class['category']['Tip'] = 0.5

        self.Similarity_matrix_class['Ingredients']['MainTask'] = 0
        self.Similarity_matrix_class['Ingredients']['Steps'] = 0.5
        self.Similarity_matrix_class['Ingredients']['step'] = 0
        self.Similarity_matrix_class['Ingredients']['Categories'] = 0.5
        self.Similarity_matrix_class['Ingredients']['category'] = 0
        self.Similarity_matrix_class['Ingredients']['Ingredients'] = 1
        self.Similarity_matrix_class['Ingredients']['Ingredient'] = 0
        self.Similarity_matrix_class['Ingredients']['Requirements'] = 0.5
        self.Similarity_matrix_class['Ingredients']['Requirement'] = 0
        self.Similarity_matrix_class['Ingredients']['Tips'] = 0.5
        self.Similarity_matrix_class['Ingredients']['Tip'] = 0

        self.Similarity_matrix_class['Ingredient']['MainTask'] = 0.5
        self.Similarity_matrix_class['Ingredient']['Steps'] = 0
        self.Similarity_matrix_class['Ingredient']['step'] = 0.5
        self.Similarity_matrix_class['Ingredient']['Categories'] = 0
        self.Similarity_matrix_class['Ingredient']['category'] = 0.5
        self.Similarity_matrix_class['Ingredient']['Ingredients'] = 0
        self.Similarity_matrix_class['Ingredient']['Ingredient'] = 1
        self.Similarity_matrix_class['Ingredient']['Requirements'] = 0
        self.Similarity_matrix_class['Ingredient']['Requirement'] = 0.5
        self.Similarity_matrix_class['Ingredient']['Tips'] = 0
        self.Similarity_matrix_class['Ingredient']['Tip'] = 0.5

        self.Similarity_matrix_class['Requirements']['MainTask'] = 0
        self.Similarity_matrix_class['Requirements']['Steps'] = 0.5
        self.Similarity_matrix_class['Requirements']['step'] = 0
        self.Similarity_matrix_class['Requirements']['Categories'] = 0.5
        self.Similarity_matrix_class['Requirements']['category'] = 0
        self.Similarity_matrix_class['Requirements']['Ingredients'] = 0.5
        self.Similarity_matrix_class['Requirements']['Ingredient'] = 0
        self.Similarity_matrix_class['Requirements']['Requirements'] = 1
        self.Similarity_matrix_class['Requirements']['Requirement'] = 0
        self.Similarity_matrix_class['Requirements']['Tips'] = 0.5
        self.Similarity_matrix_class['Requirements']['Tip'] = 0

        self.Similarity_matrix_class['Requirement']['MainTask'] = 0.5
        self.Similarity_matrix_class['Requirement']['Steps'] = 0
        self.Similarity_matrix_class['Requirement']['step'] = 0.5
        self.Similarity_matrix_class['Requirement']['Categories'] = 0
        self.Similarity_matrix_class['Requirement']['category'] = 0.5
        self.Similarity_matrix_class['Requirement']['Ingredients'] = 0
        self.Similarity_matrix_class['Requirement']['Ingredient'] = 0.5
        self.Similarity_matrix_class['Requirement']['Requirements'] = 0
        self.Similarity_matrix_class['Requirement']['Requirement'] = 1
        self.Similarity_matrix_class['Requirement']['Tips'] = 0
        self.Similarity_matrix_class['Requirement']['Tip'] = 0.5

        self.Similarity_matrix_class['Tips']['MainTask'] = 0
        self.Similarity_matrix_class['Tips']['Steps'] = 0.5
        self.Similarity_matrix_class['Tips']['step'] = 0
        self.Similarity_matrix_class['Tips']['Categories'] = 0.5
        self.Similarity_matrix_class['Tips']['category'] = 0
        self.Similarity_matrix_class['Tips']['Ingredients'] = 0.5
        self.Similarity_matrix_class['Tips']['Ingredient'] = 0
        self.Similarity_matrix_class['Tips']['Requirements'] = 0.5
        self.Similarity_matrix_class['Tips']['Requirement'] = 0
        self.Similarity_matrix_class['Tips']['Tips'] = 1
        self.Similarity_matrix_class['Tips']['Tip'] = 0

        self.Similarity_matrix_class['Tip']['MainTask'] = 0.5
        self.Similarity_matrix_class['Tip']['Steps'] = 0
        self.Similarity_matrix_class['Tip']['step'] = 0.5
        self.Similarity_matrix_class['Tip']['Categories'] = 0
        self.Similarity_matrix_class['Tip']['category'] = 0.5
        self.Similarity_matrix_class['Tip']['Ingredients'] = 0
        self.Similarity_matrix_class['Tip']['Ingredient'] = 0.5
        self.Similarity_matrix_class['Tip']['Requirements'] = 0
        self.Similarity_matrix_class['Tip']['Requirement'] = 0.5
        self.Similarity_matrix_class['Tip']['Tips'] = 0
        self.Similarity_matrix_class['Tip']['Tip'] = 1



    def edge_matrix(self):
        return self.Similarity_matrix_edge

    def class_matrix(self):
        return self.Similarity_matrix_class