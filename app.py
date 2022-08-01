class Lodash:
    def __init__(self,):
        pass

    @staticmethod
    def compact(x: list) -> list:
        """
        Creates an array with all falsey values removed. The values False, None, 0 and "" are falsey.
        """
        output = []
        for obj in x:
            if obj in [False, None, 0, ""]:
                continue
            output.append(obj)
        return output

    @staticmethod
    def drop(x: list, n=1) -> list:
        """
        Creates a slice of array with n elements dropped from the beginning.
        """
        output = []
        for idx, obj in enumerate(x):
            if idx >= n:
                output.append(obj)
        return output

    @staticmethod
    def drop_right(x: list, n=1) -> list:
        """
        Creates a slice of array with n elements dropped from the end.
        """
        output = []
        x_len = len(x)
        for idx, obj in enumerate(x):
            if idx <= x_len - n - 1:
                output.append(obj)
        return output

    @staticmethod
    def find_index(x: list, predicate) -> int:
        """
        Returns the index of the found element, else -1.
        """
        if callable(predicate):
            for idx, obj in enumerate(x):
                if predicate(obj):
                    return idx
        elif isinstance(predicate, dict):
            for idx, obj in enumerate(x):
                if obj == predicate:
                    return idx
        elif isinstance(predicate, list):
            for idx, obj in enumerate(x):
                if predicate[0] in obj:
                    if obj[predicate[0]] == predicate[1]:
                        return idx
        elif isinstance(predicate, str):
            for idx, obj in enumerate(x):
                if predicate in obj:
                    if obj[predicate] == True:
                        return idx
        return -1

    @staticmethod
    def from_pairs(x: list) -> dict:
        return dict(x)

