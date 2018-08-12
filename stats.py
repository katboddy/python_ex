from collections import Counter


def calculate_mean(numbers):
    s = sum(numbers)
    N = len(numbers)
    mean = s/N
    return mean

def calculate_median(numbers):
    N = len(numbers)
    numbers.sort()

    if N%2 == 0:
        m1 = N/2
        m2 = N/2 + 1
        m1 = int(m1) - 1
        m2 = int(m2) - 1
        median = (numbers[m1] + numbers[m2]) / 2
    else:
        m = N/2
        m = m - 1
        median = numbers[m]
    return median


def calculate_mode(numbers):
    c = Counter(numbers)
    numbers_freq = c.most_common()
    max_count = numbers_freq[0][1]
    modes = []
    for num in numbers_freq:
        if num[1] == max_count:
            modes.append(num[0])
    return modes


# Three different measurements of dispersion: range, variance, and standard deviation


def find_range(numbers):
    lowest = min(numbers)
    highest = max(numbers)
    r = highest - lowest
    return lowest, highest, r


def find_difference(numbers):
    mean = calculate_mean(numbers)
    diff = []
    for num in numbers:
        diff.append(num-mean)
    return diff


def calculate_variance(numbers):
    diff = find_difference(numbers)
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff / len(numbers)
    return variance


def find_standard_deviation(numbers):
    return calculate_variance(numbers) ** 0.5


def find_corr_x_y(x,y):
    n = len(x)
    prod = []
    for xi, yi in zip(x, y):
        prod.append(xi*yi)

    sum_prod_x_y = sum(prod)
    sum_x = sum(x)
    sum_y = sum(y)
    squared_sum_x = sum_x**2
    squared_sum_y = sum_y**2

    x_square = []
    for xi in x:
        x_square.append(xi**2)
    x_square_sum = sum(x_square)

    y_square = []
    for yi in y:
        y_square.append(yi**2)
    y_square_sum = sum(y_square)

    numerator = n*sum_prod_x_y - sum_x*sum_y
    denominator_term1 = n*x_square_sum - squared_sum_x
    denominator_term2 = n*y_square_sum - squared_sum_y
    denominator = (denominator_term1*denominator_term2)**0.5
    correlation = numerator / denominator

    import matplotlib.pyplot as plt
    plt.scatter(x, y)
    plt.show()

    return correlation


# list1 = [90,92,95,96,87,87,90,95,98,96]
# list2 = [85,87,86,97,96,88,89,98,98,87]
#
# if __name__ == '__main__':
#     print(find_corr_x_y(list1,list2))


