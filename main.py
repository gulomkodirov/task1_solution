import sys
import pandas as pd
import numpy as np
import datetime


class MyClass:
    def __repr__(self):
        return 'MyClass'


def print_vars():
    local_var = sys._getframe(1).f_locals
    for var in local_var:
        print('{}: {}'.format(var, local_var[var].__class__.__module__ == 'builtins'))


def foo():
    a = 1
    b = MyClass()
    c = [1, 2, 3]
    d = pd.DataFrame(data={'col1': [1, 2], 'col2': [3, 4]})
    print_vars()


def check_print_vars():
    none_ = None
    int_ = 1
    float_ = 1.1
    bool_ = False
    str_ = 'str'
    list_ = list([1, 2, 5])
    set_ = {1, 2, 4}
    tuple_ = 1, 2, 5
    dict_ = {'a': 1, 'b': 2}
    np_array = np.array([1, 2, 3])
    dt = datetime.datetime(2007, 12, 6, 16, 29, 43, 79043)
    print_vars()


if __name__ == '__main__':
    foo()
