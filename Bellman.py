def maximize_by(investment_table, score_function):
    if len(investment_table) == 0:
        return -1, [], -1
    f = [lambda x: (investment_table[0][x], [x], score_function(x, investment_table[0][x]))]
    f += map(lambda i: lambda x: maximize(i, f, investment_table, score_function, x), range(1, len(investment_table)))
    return max(map(f[-1], range(0, len(investment_table[0]))), key=lambda res: res[2])


def maximize(i, f, investment_table, score_function, x):
    return max(map(lambda u: generate_result(i, x, f, investment_table, score_function, u), range(0, x + 1)),
               key=lambda res: res[2])


def generate_result(i, x, f, investment_table, score_function, u):
    res = f[i - 1](x - u)
    return investment_table[i][u] + res[0], res[1] + [u], score_function(x, investment_table[i][u] + res[0])


def main():
    investment_table = [
        [40, 90, 395, 440, 620, 850, 1000, 1080],
        [30, 110, 385, 470, 740, 800, 1120, 1150],
        [35, 95, 270, 630, 700, 920, 980, 1040]
    ]
    maximize_ratio = lambda investment, result: -1 if investment == 0 else result / investment
    # maximize_result = lambda investment, result: result
    print(maximize_by(investment_table, maximize_ratio))


if __name__ == '__main__':
    main()
