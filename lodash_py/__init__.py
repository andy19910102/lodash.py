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

    @staticmethod
    def pull(x: list, *argv):
        """
        Removes all given values from list.
        """
        output = []
        for obj in x:
            if obj not in argv:
                output.append(obj)
        return output

    @staticmethod
    def pull_all(x: list, y: list):
        """
        Removes all given values from list.
        """
        output = []
        for obj in x:
            if obj not in y:
                output.append(obj)
        return output

    @staticmethod
    def pull_at(x: list, y:list) -> list:
        """
        Removes elements from list corresponding to indexes and returns a list of removed elements.
        """
        output = []
        copied_x = x.copy()
        x.clear()
        for idx, obj in enumerate(copied_x):
            if idx in y:
                output.append(obj)
            else:
                x.append(obj)
        return output
    
    @staticmethod
    def tail(x: list) -> list:
        """
        Gets all but the first element of list.
        """
        if len(x) <= 1:
            return []
        return x[1:]

    @staticmethod
    def take(x: list, n=1) -> list:
        """
        Creates a slice of list with n elements taken from the beginning.
        """
        output = []
        i = 0
        for obj in x:
            i += 1
            if i > n:
                break
            output.append(obj)
        return output

    @staticmethod
    def uniq(x: list) -> list:
        """
        Creates a duplicate-free version of an list.
        """
        return list(set(x))

    @staticmethod
    def xor(x: list, y:list) -> list:
        """
        Creates an list of unique values that is the symmetric difference of the given list. 
        The order of result values is determined by the order they occur in the list.
        """
        x, y = set(x), set(y)
        return list(x ^ y) 


    ##### LANG METHODS
    @staticmethod
    def cast_list(x=None) -> list:
        """
        Casts value as an list
        """
        if x is None:
            return []
        return [x]

    @staticmethod
    def conforms_to(dict_input: dict, source:dict) -> bool:
        """
        Checks if dict_input conforms to source by invoking the predicate properties of source with the corresponding property values of dict_input.
        """
        key = list(source.keys())[0]
        check_method = source[key]
        if key in dict_input:
            return check_method(dict_input[key])
        return False

    @staticmethod
    def gt(value, other):
        """
        Returns true if value is greater than other, else false.
        """
        return value > other
    
    @staticmethod
    def gte(value, other):
        """
        Returns true if value is greater than or equal to other, else false.
        """
        return value >= other

    @staticmethod
    def is_list(x) -> bool:
        """
        Checks if value is classified as a List.
        """
        return isinstance(x, list)

    ##### MATH METHODS
    @staticmethod
    def add(augend, addend):
        """
        Adds two numbers.
        """
        return augend + addend

    @staticmethod
    def divide(dividend, divisor):
        """
        Divide two numbers.
        """
        return dividend / divisor

    @staticmethod
    def max(x: list):
        """
        Computes the maximum value of list.
        """
        output = x[0]
        for obj in x:
            if obj > output:
                output = obj
        return output

    @staticmethod
    def min(x: list):
        """
        Computes the minimum value of list.
        """
        output = x[0]
        for obj in x:
            if obj < output:
                output = obj
        return output


