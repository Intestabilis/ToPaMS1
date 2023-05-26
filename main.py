import math

from matplotlib import pyplot as plt


def polygonHistogram(array):
    a, bins, c = plt.hist(array, bins=7, histtype='step')
    l = list(bins)
    l.insert(0, 0)
    l.insert(len(bins) + 1, bins[len(bins) - 1])
    mid = []
    for i in range(len(l) - 1):
        ele = (l[i] + l[i + 1]) / 2
        mid.append(ele)
    array = list(a)
    array.insert(0, 0)
    array.insert(len(a) + 1, 0)
    plt.plot(mid, array, 'ro--')
    plt.xlabel("Intervals")
    plt.ylabel("Frequency")
    plt.title("Polygon and Histogram")
    plt.show()


def average(array):
    length = len(array)

    array_sum = sum(array)
    result = array_sum / length
    print("Average: " + str(round(result, 2)))


def median(array):
    length = len(array)
    array.sort()

    if length % 2 == 0:
        first = array[length // 2]
        second = array[length // 2 - 1]
        result = (first + second) / 2
    else:
        result = array[length // 2]
    print("Median: " + str(result))


def mode(array):
    array.sort()

    counts = []

    for number in array:
        counts.append(array.count(number))

    dictionary = dict(zip(array, counts))
    modes = {number for (number, quantity) in dictionary.items() if quantity == max(counts)}
    print("Mode(s):" + str(modes))


def variance(array):
    average = sum(array) / len(array)
    variance = sum((x - average) ** 2 for x in array) / len(array)
    square = math.sqrt(variance)
    print("Sample variance: " + str(round(variance, 2)))
    print("Root-mean-square deviation: " + str(round(square, 2)))


def boxPlot(array):
    plt.boxplot(array, showmeans=True, labels=['Data'])
    plt.title('Box plot')
    plt.show()


def paretoChart(array):
    counts = []
    for number in array:
        counts.append(array.count(number))
    frequency_dict = dict(zip(array, counts))

    sorted_dict = sorted(frequency_dict.items(), key=lambda f: f[1], reverse=True)

    quantity = len(array)
    cumulative_sum = 0
    percentages = []
    for value, frequency in sorted_dict:
        cumulative_sum += frequency
        percent = (cumulative_sum / quantity) * 100
        percentages.append(percent)

    # chart
    fig, ax1 = plt.subplots()

    ax1.bar(range(len(sorted_dict)), [f[1] for f in sorted_dict], color='grey')
    ax1.set_xticks(range(len(sorted_dict)))
    ax1.set_xticklabels([str(n[0]) for n in sorted_dict])
    ax1.set_ylabel('Frequency')

    ax2 = ax1.twinx()
    ax2.plot(range(len(sorted_dict)), percentages, '-mo')
    ax2.set_ylim([0, 100])
    ax2.set_ylabel('Cumulative Percentage')
    plt.title('Pareto')
    plt.show()


def pieChart(array):
    counts = []
    for number in array:
        counts.append(array.count(number))
    frequency_dict = dict(zip(array, counts))

    sorted_dict = sorted(frequency_dict.items(), key=lambda f: f[1], reverse=True)

    numbers, frequencies = zip(*sorted_dict)

    plt.pie(frequencies, labels=numbers)
    plt.title('Pie chart')
    plt.show()


samples = [5, 9, 10, 7, 4, 8, 2, 4, 5, 6, 5, 9, 8, 5, 12, 5, 9, 8, 8, 6, 5, 9, 6, 4, 6, 7, 4, 10, 8, 11, 6, 7, 7, 8, 7,
           5, 10, 8, 4, 5, 8, 3, 8, 5, 10, 7, 5, 7, 8, 5, 5, 5, 7, 3, 6, 9, 4, 8, 6, 6, 9, 9, 5, 9, 5, 6, 7, 7, 8, 8, 7,
           8, 10, 6, 9, 6, 5, 7, 7, 5, 6, 4, 8, 10, 8, 9, 6, 5, 8, 8, 5, 9, 9, 9, 7, 8, 5, 5, 5, 6, 7, 6, 5, 9, 6, 5, 7,
           5, 8, 4, 8, 10, 4, 6, 3, 7, 3, 7, 9, 6, 6, 4]

polygonHistogram(samples)

average(samples)
print()
median(samples)
print()
mode(samples)
print()
variance(samples)

boxPlot(samples)
paretoChart(samples)
pieChart(samples)
