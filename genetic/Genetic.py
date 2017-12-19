from random import random

from math import ceil


def genetic(left, right, f, settings):
    sign = {"value": 1}

    def crossover():
        def crossover_without_mutation():
            k = settings["all_count_population"] - 1
            for i in range(0, settings["protected_from_mutation"]):
                val = (populations[i]["value"] + populations[i + 1]["value"]) / 2
                populations[k] = {"value": val, "result": f(val)}

            def inversion(value):
                value = value["value"]
                sign["value"] *= -1
                value = value + sign["value"] * (settings["epsilon"] * 10 * random())
                value = left if value < left else value
                value = right if value > right else value
                return {"value": value, "result": f(value)}

            for i in range(0, len(populations)):
                populations[i] = inversion(populations[i])

        def crossover_with_mutation():
            def micro_mutation(x):
                val = x["value"] + sign["value"] * random()
                val = left if val < left else val
                val = right if val > right else val
                return {"value": val, "result": f(val)}

            end_mutation = settings["all_count_population"] - settings["protected_from_mutation"]
            end_micro_mutation = int(ceil(end_mutation / 2))
            for i in range(0, end_micro_mutation):
                populations[i] = micro_mutation(populations[i])
            for i in range(end_micro_mutation, end_mutation):
                value = mutation()
                populations[i] = {"value": value, "result": f(value)}

        crossover_without_mutation()
        if i % settings["mutation_step"] == 0:
            crossover_with_mutation()

    mutation = lambda: random() * (right - left) + left

    def start_populations():
        values = [mutation() for _ in range(0, settings["all_count_population"])]
        return [{"value": value, "result": f(value)} for value in values]

    def time_to_stop():
        prev = result_iterations[i][0]["result"]
        curr = result_iterations[i + 1][0]["result"]
        return abs(prev - curr) < settings["epsilon"]

    f_result = lambda x: x["result"]

    result_iterations = []
    populations = start_populations()
    populations.sort(key=f_result)
    result_iterations.append(list(populations))
    for i in range(0, settings["max_iterations"]):
        crossover()
        populations.sort(key=f_result)
        result_iterations.append(list(populations))
        if time_to_stop():
            break
    return {
        "value": populations[0]["value"],
        "result": populations[0]["result"],
        "result_iterations": result_iterations,
        "it_count": len(result_iterations) - 1
    }
