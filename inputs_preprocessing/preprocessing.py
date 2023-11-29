class Preprocessor:
    features = [
            'cap-shape', 'cap-surface', 'cap-color', 'bruises', 'odor', 'gill-attachment',
            'gill-spacing', 'gill-size', 'gill-color', 'stalk-shape', 'stalk-root',
            'stalk-surface-above-ring', 'stalk-surface-below-ring', 'stalk-color-above-ring',
            'stalk-color-below-ring', 'veil-color', 'ring-number', 'ring-type', 'spore-print-color',
            'population', 'habitat'
        ]
    categories = {
            'cap-shape': ['b', 'c', 'x', 'f', 'k', 's'],
            'cap-surface': ['f', 'g', 'y', 's'],
            'cap-color': ['n', 'b', 'c', 'g', 'r', 'p', 'u', 'e', 'w', 'y'],
            'bruises': ['t', 'f'],
            'odor': ['a', 'l', 'c', 'y', 'f', 'm', 'n', 'p', 's'],
            'gill-attachment': ['a', 'd', 'f', 'n'],
            'gill-spacing': ['c', 'w', 'd'],
            'gill-size': ['b', 'n'],
            'gill-color': ['k', 'n', 'b', 'h', 'g', 'r', 'o', 'p', 'u', 'e', 'w', 'y'],
            'stalk-shape': ['e', 't'],
            'stalk-root': ['b', 'c', 'u', 'e', 'z', 'r', '?'],
            'stalk-surface-above-ring': ['f', 'y', 'k', 's'],
            'stalk-surface-below-ring': ['f', 'y', 'k', 's'],
            'stalk-color-above-ring': ['n', 'b', 'c', 'g', 'o', 'p', 'e', 'w', 'y'],
            'stalk-color-below-ring': ['n', 'b', 'c', 'g', 'o', 'p', 'e', 'w', 'y'],
            'veil-color': ['n', 'o', 'w', 'y'],
            'ring-number': ['n', 'o', 't'],
            'ring-type': ['c', 'e', 'f', 'l', 'n', 'p', 's', 'z'],
            'spore-print-color': ['k', 'n', 'b', 'h', 'r', 'o', 'u', 'w', 'y'],
            'population': ['a', 'c', 'n', 's', 'v', 'y'],
            'habitat': ['g', 'l', 'm', 'p', 'u', 'w', 'd']
        }
    processed_inputs = []* 94

    def _one_hot_encode(self, user_inputs):
        processed_inputs = [0] * 94  # Ensure consistent size for all inputs

        for feature, value in zip(self.features, user_inputs):
            if value in self.categories[feature]:
                index = list(self.categories.keys()).index(feature) * len(self.categories[feature])
                category_index = self.categories[feature].index(value)
                processed_inputs[index + category_index] = 1

        return processed_inputs