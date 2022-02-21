import numbers
import numpy as np


class MixinWriteToFile:
    def write_to_file(self, file_name):
        with open(file_name, "w") as file:
            file.write(self.__str__())


class MixinView:
    def __str__(self):
        return "[" + "\n".join(map(str, map(list, self.value))) + "]"


class MixinVals:
    def __init__(self, value):
        self.value = np.asarray(value)

    @property
    def data(self):
        return self.value

    @data.setter
    def data(self, new_value):
        self.value = new_value


class MediumMatrix(np.lib.mixins.NDArrayOperatorsMixin, MixinView, MixinWriteToFile, MixinVals):
    _HANDLED_TYPES = (np.ndarray, numbers.Number)

    # from documentation
    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        out = kwargs.get('out', ())
        for x in inputs + out:
            if not isinstance(x, self._HANDLED_TYPES + (MediumMatrix,)):
                return NotImplemented
        inputs = tuple(x.data if isinstance(x, MediumMatrix) else x
                       for x in inputs)
        if out:
            kwargs['out'] = tuple(
                x.data if isinstance(x, MediumMatrix) else x
                for x in out)
        result = getattr(ufunc, method)(*inputs, **kwargs)

        if type(result) is tuple:
            return tuple(type(self)(x) for x in result)
        elif method == 'at':
            return None
        else:
            return type(self)(result)
