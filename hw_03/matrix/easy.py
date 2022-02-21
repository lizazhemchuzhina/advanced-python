class EasyMatrix:
    def __init__(self, data):
        self.rows = len(data)
        self.columns = len(data[0])
        self.data = []
        for row in data:
            if len(row) != self.columns:
                raise Exception("Incorrect dimensions")
            self.data.append(list(row))

    def __add__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise Exception("Incompatible dimensions of matrices")
        result = [list(map(sum, zip(*rows))) for rows in zip(self.data, other.data)]
        return EasyMatrix(result)

    def __mul__(self, other):
        if self.rows != other.rows or self.columns != other.columns:
            raise Exception("Incompatible dimensions of matrices")
        result = [[a * b for a, b in zip(*rows)] for rows in zip(self.data, other.data)]
        return EasyMatrix(result)

    def __matmul__(self, other):
        if self.columns != other.rows:
            raise Exception("Incompatible dimensions of matrices")
        result = [[sum(a * b for a, b in zip(A_row, B_col))
                   for B_col in zip(*other.data)]
                  for A_row in self.data]
        return EasyMatrix(result)

    def __str__(self):
        return "[" + ",\n".join(str(line) for line in self.data) + "]"
