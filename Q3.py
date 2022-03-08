"""
A structure called List that allows access to details in the syntax of a multidimensional array
"""

class List(list):
    def __init__(self, list):
        super().__init__(list)

    def __getitem__(self, item):
        if len(item) == 3 and type(item) is tuple:
            self.get_len3(item)

        elif len(item) == 2 and type(item) is tuple:
            self.get_len2(item)

        else:
            self.get_len1(item)

    def __setitem__(self, key, value):
        if len(key) == 3 and type(key) is tuple:
            self.set_len3(key, value)

        elif len(key) == 2 and type(key) is tuple:
            self.set_len2(key, value)

        else:
            self.set_len1(key, value)

    def get_len1(self, list):
        return super().__getitem__(list)

    def get_len2(self, list):
        list_pos = super().__getitem__(list[0])
        return list_pos[list[1]]

    def get_len3(self, list):
        list_pos = super().__getitem__(list[0])
        chosen_arr = list_pos[list[1]]
        return chosen_arr[list[2]]

    def set_len1(self, key, val):
        super().__setitem__(key, val)

    def set_len2(self, key, val):
        list_pos = super().__getitem__(key[0])
        list_pos[key[1]] = val

    def set_len3(self, key, val):
        list_pos = super().__getitem__(key[0])
        chosen_arr = list_pos[key[1]]
        chosen_arr[key[2]] = val
