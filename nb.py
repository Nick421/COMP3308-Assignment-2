import math
import sys
import csv
from numpy import array
import numpy as np


def mean(numbers):
    return np.sum(numbers) / float(len(numbers))

def stdev(numbers):
    if len(numbers) < 2:
        return 0
    avg = mean(numbers)
    var = sum([pow(i - avg, 2) for i in numbers]) / float(len(numbers)-1)
    std = math.sqrt(var)
    return std

def class_divide(data_set):
    class_divided = {}
    class_divided["yes"] = []
    class_divided["no"] = []
    for row in data_set:
        class_divided[row[-1]].append(row[0:-1])
    class_divided["yes"] = array(class_divided["yes"])
    class_divided["no"] = array(class_divided["no"])
    # print(class_divided)
    return class_divided

def class_mean_std(class_divided):
    class_mean_std_set = {}
    class_mean_std_set["yes"] = []
    class_mean_std_set["no"] = []
    for i in range(len(class_divided["yes"][0])):
        class_mean_std_set["yes"].append((mean(class_divided["yes"][:, i]),stdev(class_divided["yes"][:, i])))
    for i in range(len(class_divided["no"][0])):
        class_mean_std_set["no"].append((mean(class_divided["no"][:, i]),stdev(class_divided["no"][:, i])))
    return class_mean_std_set


def density_function(x, avg, std):
    if std == 0:
        # print(1)
        return 1
    exp = math.exp(-(pow(x - avg, 2))/(2 * pow(std, 2)))
    prob = (1/(std * math.sqrt(2 * math.pi))) * exp
    # print(prob)
    return prob

def calculate_prob(summary_train_set, input_data, py, pn):
    # print(summary_train_set)
    probabilities = {}
    
    probabilities["yes"] = py
    probabilities["no"] =  pn
    for i in range(len(summary_train_set["yes"])):
        probabilities["yes"] *= density_function(input_data[i], summary_train_set["yes"][i][0], summary_train_set["yes"][i][1])
    for i in range(len(summary_train_set["no"])):
        probabilities["no"] *= density_function(input_data[i], summary_train_set["no"][i][0], summary_train_set["no"][i][1])
    # print(probabilities)
    if probabilities["yes"] >= probabilities["no"]:
        print("yes")
        return
    print("no")

def nb(train_set, test_set):
    train_divided = class_divide(train_set)
    py = len(train_divided["yes"]) / (len(train_divided["yes"]) + len(train_divided["no"]))
    pn = len(train_divided["no"]) / (len(train_divided["yes"]) + len(train_divided["no"]))
    summary_train_set = class_mean_std(train_divided)
    # print(summary_train_set["yes"])
    for row in test_set:
        calculate_prob(summary_train_set, row, py, pn)

