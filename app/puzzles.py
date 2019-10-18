import numpy as np

# Index references to update array based on elements
index_ref = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 0: 'A', 1: 'B', 2: 'C', 3: 'D'}
# Symbol table toggle the symbols
symbol_table = {'<': '>', '>': '<'}


def get_index(l, obj):
    try:
        return l.index(obj)
    except ValueError:
        return None


def set_order(first, second, symbol, names_order):
    """Add elements in the priority order (method uses recursion)
    Move and insert elements in the middle of the list when required
    """
    if symbol == '<':
        first_ind = get_index(names_order, first)
        second_ind = get_index(names_order, second)
        if first_ind is None and second_ind is None:
            names_order.append(first)
            names_order.append(second)
        elif first_ind is not None and second_ind is not None and first_ind < second_ind:
            pass
        elif first_ind is None and second_ind is not None:
            names_order.insert(second_ind, first)
        elif first_ind is not None and second_ind is None:
            names_order.insert(first_ind+1, second)
    elif symbol == '>':
        set_order(first=second, second=first, symbol=symbol_table[symbol], names_order=names_order)


def puzzle_solver(d_string):
    a = np.chararray((4, 4), unicode=True)
    np.fill_diagonal(a, '=')

    conditions = d_string.splitlines()[2:]
    # List to keep the Order of elements
    names_order = list()

    # Fill the array with given conditions and set up the order for elements
    for condition in conditions:
        name, index, value = condition[0], None, None
        for ind, val in enumerate(condition[1:]):
            if val in ['<', '>']:
                set_order(name, index_ref[ind], val, names_order)
                a[index_ref[name], ind] = val
                a[ind, index_ref[name]] = symbol_table[val]
                break

    # Fill the empty indexes in array using ordered elements
    for index, x in np.ndenumerate(a):
        if not x:
            f_ind = names_order.index(index_ref[index[0]])
            s_ind = names_order.index(index_ref[index[1]])
            a[index] = '<' if f_ind < s_ind else '>'

    joined_rows = zip('ABCD', np.apply_along_axis(lambda s: '{}\n'.format(''.join(s)), axis=1, arr=a))

    return ' ABCD\n{}'.format(''.join([''.join(e) for e in joined_rows]))

