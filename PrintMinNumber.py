import functools
def PrintMinNumber(numbers):
    if not numbers:
        return ""
    num = [str(i) for i in numbers]
    cmp2key = functools.cmp_to_key(lambda s1, s2: int(s1 + s2) - int(s2 + s1))
    num.sort(key=cmp2key)
    m = ''
    for i in num:
        m += i
    return int(m)

if __name__ == '__main__':
    a = [1,2,3,4,5]
    res = PrintMinNumber(a)
    print(res)
