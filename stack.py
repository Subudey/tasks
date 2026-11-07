class Stack:
    def __init__(self):
        self._data = []

    def push(self, item):
        if self._data:
            cur_min = min(self._data[-1][1], item)

        else:
            cur_min = item

        self._data.append((item, cur_min))

    def pop(self):
        self._data.pop()

    def top(self):
        return  self._data[-1][0]

    def get_min(self):
        return self._data[-1][1]