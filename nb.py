import math
import sys
import csv
from numpy import array
import numpy as np

def read_data(data_file):
    data_set = []
    with open(data_file) as data:
        data_read = csv.reader(data, delimiter = ",")
        for row in data_read:
            data_set.append(row)
    return data_set

def class_separation(data_set):
    data_map = {}
    data_map["no"] = []
    data_map["yes"] = []
    for data in data_set:
        data_map[str(data[-1])].append(data[0:-1])
    data_map_np = {}
    print(data_map)
    data_map_np["no"] = array(data_map["no"]).astype(np.float)
    data_map_np["yes"] = array(data_map["yes"]).astype(np.float)
    return data_map_np

def mean(numbers):
    return np.sum(numbers) / float(len(numbers))

def stdev(numbers):
    avg = mean(numbers)
    var = sum([pow(i - avg, 2) for i in numbers]) / float(len(numbers)-1)
    std = math.sqrt(var)
    return std

def cal_summary(class_data):
    summary = []
    for i in range(len(class_data[0])):
        avg = mean(class_data[:, i])
        std = stdev(class_data[:, i])
        summary.append((avg, std))
    return summary

def density_function(x, avg, std):
    if std == 0:
        return 1.0

    exp = math.exp(-(pow(float(x) - avg, 2))/(2 * pow(std, 2)))
    prob = (1/(std * math.sqrt(2 * math.pi))) * exp
    # print(x, mean, stdev)
    print(prob)
    return prob

def cal_prediction(summary, new_data):
    probabilities = {}
    probabilities["yes"] = float(len(summary["yes"])/(len(summary["yes"]) + len(summary["no"])))
    probabilities["no"] =  float(len(summary["no"])/(len(summary["yes"]) + len(summary["no"])))
    for i in range(len(summary["yes"])):
        probabilities["yes"] *= density_function(new_data[i], summary["yes"][i][0], summary["yes"][i][1])
    for i in range(len(summary["no"])):
        probabilities["no"] *= density_function(new_data[i], summary["no"][i][0], summary["no"][i][1])
    print(probabilities)
    if probabilities["yes"] >= probabilities["no"]:
        print("yes")
    else:
        print("no")

def nb(training_data_file, testing_data_file):
    training_data = read_data(training_data_file)
    training_map = class_separation(training_data)
    training_class_summary = {}
    training_class_summary["yes"] = cal_summary(training_map["yes"])
    training_class_summary["no"] = cal_summary(training_map["no"])

    # print(training_class_summary["yes"])
    # print(training_class_summary["no"])
    testing_data = read_data(testing_data_file)
    for input_data in testing_data:
        print(input_data)
        cal_prediction(training_class_summary, input_data)

