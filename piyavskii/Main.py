from math import sin
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from piyavskii.PiyavskiiAlt import get_data_function, piyavskii_method

if __name__ == '__main__':
    alpha = 2.67
    beta = 3.044
    gamma = 2.25
    a = -5
    b = 9.7
    f = lambda x: alpha * sin(beta * x) - gamma * x
    count_iterations = 180
    data_set = get_data_function(a, b, f, count_iterations)
    result = piyavskii_method(a, b, f, count_iterations)
    print(result)
    for iteration in result['iterations']:
        ax = plt.gca()
        left = iteration['left']
        right = iteration['right']
        ax.add_line(mlines.Line2D([left['point'], left['x_point_for_left']],
                                  [left['result_point'], left['y_point_for_left']], color='#a5dab2'))
        ax.add_line(mlines.Line2D([right['point'], right['x_point_for_left']],
                                  [right['result_point'], right['y_point_for_left']], color='#389e98'))
        ax.add_line(mlines.Line2D([left['point'], left['x_point_for_right']],
                                  [left['result_point'], left['y_point_for_right']], color='#a5dab2'))
        ax.add_line(mlines.Line2D([right['point'], right['x_point_for_right']],
                                  [right['result_point'], right['y_point_for_right']], color='#389e98'))

    plt.plot([data['value'] for data in data_set], [data['result_function'] for data in data_set])
    plt.show()