class Lodash:
    def __init__(self,):
        pass
    
    ##### LIST METHODS
    @staticmethod
    def compact(x: list) -> list:
        """
        Creates an list with all falsey values removed. The values False, None, 0 and "" are falsey.
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
        Creates a slice of list with n elements dropped from the beginning.
        """
        output = []
        for idx, obj in enumerate(x):
            if idx >= n:
                output.append(obj)
        return output

    @staticmethod
    def drop_right(x: list, n=1) -> list:
        """
        Creates a slice of list with n elements dropped from the end.
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
        """
        This method returns an object composed from key-value pairs.
        """
        return dict(x)

    @staticmethod
    def head(x: list):
        """
        Returns the first element of list.
        """
        if len(x) > 0:
            return x[0] 

    @staticmethod
    def initial(x: list) -> list:
        """
        Gets all but the last element of list.
        """
        output = []
        x_len = len(x)
        if x_len == 0:
            return output
        for idx in range(0, x_len-1):
            output.append(x[idx])            
        return output

    @staticmethod
    def join(x: list, y: str) -> str:
        """
        Returns the joined string.
        """
        output = ""
        x_len = len(x)
        for idx, obj in enumerate(x):
            if idx < x_len - 1:
                output += f"{obj}{y}"
            else:
                output += f"{obj}"
        return output

    @staticmethod
    def last(x: list):
        """
        Returns the last element of list.
        """
        if len(x) > 0:
            return x[-1] 

    ##### LANG METHODS
    @staticmethod
    def gte(value, other):
        """
        Returns true if value is greater than or equal to other, else false.
        """
        return value >= other

    @staticmethod
    def gt(value, other):
        """
        Returns true if value is greater than other, else false.
        """
        return value > other
