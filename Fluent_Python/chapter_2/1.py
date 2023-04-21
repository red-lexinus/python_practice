def fixed(o) -> bool:
    try:
        hash(o)
    except TypeError:
        return False
    return True


def fun_1() -> None:
    data = tuple(
        ((i * 5, (i - 1) * 5) for i in range(1, 5))
    )
    if fixed(data):
        for values in data:
            print('%i %i' % values)
        for _, value in data:
            print(f'?? - 5 = {value}')
    else:
        print('Error')


def fun_2():
    return [[43]]


def fun_3():
    [[num_1]] = fun_2()
    [(num_2,)] = fun_2()
    [(num_3)] = fun_2()
    print(num_1, num_2, num_3)


def fun_4(message: str or list):
    if type(message) == str:
        message = message.split()
    match message:
        case ['test', num]:
            print(f'Это тест №{num}')
        case ['test', *args]:
            res = ''
            if args:
                res = ' '.join(args)
            print(f'Просто тестик- {res}')
        case ['finish', time, distance]:
            print(f'Вы пробежали {distance} за {time}')
        case _:
            raise 'Не та команда'


if __name__ == '__main__':
    fun_1()
    fun_2()
    fun_3()
    fun_4('test 4')
