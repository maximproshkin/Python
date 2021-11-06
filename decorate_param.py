"""Написать декоратор с параметром, который будет показывать сколько раз отдавать кешируемый результат.
Если данный счетчик обнуляется, то выполняем функцию и вновь кешируем ее результат."""


def decorate(arg):
    def memoize_func(f):
        memo = dict()
        memo_counter = dict()

        def wrapper(*args):
            if args in memo and memo_counter[args] == arg:
                memo.pop(args)
                memo_counter.pop(args)
                pass
            elif args in memo:
                memo_counter[args] += 1
                pass

            print(f'Run with args={args}, memo={memo}')
            if args not in memo:
                memo_counter[args] = 0
                memo[args] = f(*args)
            return memo[args]
        return wrapper
    return memoize_func


count = 2  # счетчик


@decorate(count)
def func(a, b):
    print(f'    Run func({a}, {b})')
    return a ** b


print(func(3, 5), '\n')
print(func(3, 5), '\n')
print(func(3, 5), '\n')
print(func(3, 5), '\n')
print(func(3, 4), '\n')
print(func(3, 5), '\n')
print(func(3, 5), '\n')
print(func(3, 5), '\n')
