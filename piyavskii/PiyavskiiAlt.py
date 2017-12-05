def piyavskii_method(left_border, right_border, f, iteration_count=100, accuracy_to=0.000001):
    def get_lipschitz_const(a, b):
        m = 10000
        return max(map(lambda pair: (f(pair[1]) - f(pair[0])) / (pair[1] - pair[0]), map(lambda i: [a + i * (b - a) / m, a + (i + 1) * (b - a) / m], range(0, m))))

    def get_point_intersection(left_point, right_point, lipschitz_const):
        func_avg = (f(left_point) - f(right_point)) / (2 * lipschitz_const)
        point_avg = (left_point + right_point) / 2
        return func_avg + point_avg

    def get_result_iteration(left_border, right_border, lipschitz_const):
        def get_minorant(left_border, right_border, lipschitz_const):
            point_intersection = get_point_intersection(left_border, right_border, lipschitz_const)
            left_distance_to_point_intersection = point_intersection - left_border
            minorant = {
                'point': left_border,
                'result_point': f(left_border),
                'distance_to_point_intersection': left_distance_to_point_intersection,
                'x_point_for_left': left_border - left_distance_to_point_intersection,
                'y_point_for_left': f(left_border) - left_distance_to_point_intersection * lipschitz_const,
                'x_point_for_right': point_intersection,
                'y_point_for_right': f(left_border) - left_distance_to_point_intersection * lipschitz_const
            }
            return minorant

        def get_majorant(left_border, right_border, lipschitz_const):
            point_intersection = get_point_intersection(left_border, right_border, lipschitz_const)
            right_distance_to_point_intersection = (right_border - point_intersection)
            majorant = {
                'point': right_border,
                'result_point': f(right_border),
                'distance_to_point_intersection': right_distance_to_point_intersection,
                'x_point_for_left': point_intersection,
                'y_point_for_left': f(right_border) - right_distance_to_point_intersection * lipschitz_const,
                'x_point_for_right': right_border + right_distance_to_point_intersection,
                'y_point_for_right': f(right_border) - right_distance_to_point_intersection * lipschitz_const
            }
            return majorant

        point_intersection = get_point_intersection(left_border, right_border, lipschitz_const)
        result_iteration = {
            'point_intersection': get_point_intersection(left_border, right_border, lipschitz_const),
            'left_area': get_point_intersection(left_border, point_intersection, lipschitz_const),
            'right_area': get_point_intersection(point_intersection, right_border, lipschitz_const),
            'lipschitz_const': lipschitz_const,
            'left': get_minorant(left_border, right_border, lipschitz_const),
            'right': get_majorant(left_border, right_border, lipschitz_const)
        }
        return result_iteration

    def is_accuracy_achieved(left_pi_x, right_pi_x, accuracy_to):
        return abs(right_pi_x - left_pi_x) < accuracy_to

    result = {
        'answer': '',
        'result_answer': '',
        'count_iteration_for_accuracy': '',
        'iterations': []
    }
    left_point = left_border
    right_point = right_border
    lipschitz_const = get_lipschitz_const(left_border, right_border)
    for i in range(0, iteration_count - 1):
        result_iteration = get_result_iteration(left_point, right_point, lipschitz_const)
        result['iterations'].append(result_iteration)
        pi_x = get_point_intersection(left_point, right_point, lipschitz_const)
        left_pi_x = get_point_intersection(left_point, pi_x, lipschitz_const)
        right_pi_x = get_point_intersection(pi_x, right_point, lipschitz_const)
        if f(left_pi_x) <= f(right_pi_x):
            right_point = pi_x
        else:
            left_point = pi_x

        if is_accuracy_achieved(left_pi_x, right_pi_x, accuracy_to):
            result['count_iteration_for_accuracy'] = i + 1
            break

    result['answer'] = get_point_intersection(left_point, right_point, lipschitz_const)
    result['result_answer'] = f(result['answer'])
    return result


def get_data_function(left_border, right_border, custom_function, iteration_count):
    step = abs(right_border - left_border) / iteration_count
    result = []
    for i in range(0, iteration_count - 1):
        x = left_border + step * (i + 1)
        obj = {
            'value': x,
            'result_function': custom_function(x)
        }
        result.append(obj)
    return result
