from hw_03.matrix.easy import EasyMatrix


class MixinHash:
    def __hash__(self):
        return sum([sum(row) for row in self.data])


class HardMatrix(EasyMatrix, MixinHash):
    _matmul_hashes = {}

    def __matmul__(self, other):
        key = (self.__hash__(), other.__hash__())
        if key in self._matmul_hashes:
            return self._matmul_hashes[key]
        matmul = HardMatrix(super().__matmul__(other).data)
        self._matmul_hashes[key] = matmul
        return matmul
