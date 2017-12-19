from math import sin
from time import time

from genetic.Genetic import genetic

if __name__ == '__main__':
    alpha = 2.67
    beta = 3.044
    gamma = 2.25
    a = -5
    b = 9.1
    f = lambda x: alpha * sin(beta * x) - gamma * x

    settings = {
        "epsilon": 0.00001,
        "max_iterations": 1000,
        "all_count_population": 100,
        "mutation_step": 4,
        "protected_from_mutation": 15
    }
    millis = int(round(time() * 1000))
    result = genetic(a, b, f, settings)
    print("Calculated {} ms".format(int(round(time() * 1000)) - millis))
    print(result["value"])
    print(result["result"])
    print(result["it_count"])
