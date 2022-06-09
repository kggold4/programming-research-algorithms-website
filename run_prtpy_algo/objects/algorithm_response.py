import itertools
import json

algorithm_descriptions = {"kk": "Karmarkar-karp", "ckk": "Complete Karmarkar-Karp",
                          "rnp": "Recursive Number Partitioning", "irnp": "Improved Recursive Number Partitioning"}


class AlgorithmResponse:
    def __init__(self, name: str, bins: list[list[int]], sums: list[int], error: str = ''):
        self.name = name
        self.description = algorithm_descriptions[name]
        self.bins = bins
        self.sums = sums
        self.length = len(self.bins)
        self.diff_sum = calculate_diff(bins)
        self.error = error

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)


def get_algorithms_choices():
    result = []
    for key, value in algorithm_descriptions.items():
        result.append((key, value))
    return result


def calculate_diff(items: list[int]):
    different_sum = 0
    for combination in itertools.combinations(items, 2):
        if len(combination[0]) == 0 or len(combination[1]) == 0:
            break
        else:
            different_sum += abs(sum(combination[0]) - sum(combination[1]))
    return different_sum
