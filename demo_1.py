# coding: utf-8
# Author: zhenda

# 深度合并dict

# def merge_dict(source_dict, update_dict) -> dict
# 例子：
source_dict = {
    'key0': 'a',
    'key1': 'b',
    'key2': {
        'inner_key0': 'c',
        'inner_key1': 'd'

    },
    'key3': [1, 2, 3]
}
update_dict = {
    'key1': 'x',
    'key2': {
        'inner_key0': 'y'
    },
    'key3': [4, 5, 6],
    'key8': 666
}

# result = merge_dict(source_dict, update_dict)
result = {
    'key0': 'a',
    'key1': 'x',  # overridden by update_dict
    'key2': {
        'inner_key0': 'y',  # overridden by update_dict
        'inner_key1': 'd'
    },
    'key3': [4, 5, 6],
    'key8': 666
}


def merge_dict(source_dict, update_dict) -> dict:
    for key, val in update_dict.items():  #
        if key in source_dict:
            if isinstance(source_dict[key], dict) and isinstance(update_dict[key], dict):
                source_dict[key] = merge_dict(source_dict[key], update_dict[key])
        source_dict[key] = val
    return source_dict


if __name__ == '__main__':
    res = merge_dict(source_dict['key2'], update_dict['key2'])
    res2 = merge_dict(source_dict, update_dict)
    print(res)
    print(res2)



