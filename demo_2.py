# coding: utf-8
# Author: zhenda
rule = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}


def change_str(nums):
    pre_res, res = [], []
    if not nums:
        return res
    arr = list(nums)
    while arr:
        if not res:  # 不存在结果
            for item in rule[arr[0]]:
                res.append(item)
            arr.pop(0)

        if res:  # 存在结果
            pre_res, res = res, []
            for sub_res in pre_res:  # 旧的结果
                for item in rule[arr[0]]:  # 处理arr
                    new_res = sub_res + item
                    res.append(new_res)  # 增
            arr.pop(0)
    return res


if __name__ == '__main__':
    res = change_str('234')
    print(res)

