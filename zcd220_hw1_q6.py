class Vector:

    # 6a
    def __init__(self, *args):
        if isinstance(args[0], int):
            self.coords = [0]*args[0]
        else:
            self.coords = args[0]

    def __len__(self):
        return len(self.coords)

    def __getitem__(self, j):
        return self.coords[j]

    def __setitem__(self, j, val):
        self.coords[j] = val

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        return self.coords == other.coords

    def __ne__(self, other):
        return not (self == other)

    def __str__(self):
        return "<" + str(self.coords)[1:-1] + ">"

    def __repr__(self):
        return str(self)

    # 6b
    def __sub__(self, other):
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] - other[j]
        return result

    # 6c
    def __neg__(self):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] * -1
        return result

    # 6d, 6f
    def __mul__(self, *args):
        result = Vector(len(self))
        if isinstance(args[0], int):
            for i in range(len(self)):
                result[i] = self[i] * args[0]
            return result
        else:
            if len(self) != len(args[0]):
                raise ValueError("dimensions must agree")
        for i in range(len(self)):
            result[i] = self[i] * args[0][i]
        return sum(result)

    # 6e
    def __rmul__(self, n):
        result = Vector(len(self))
        for i in range(len(self)):
            result[i] = self[i] * n
        return result
