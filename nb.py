import math
import sys
import csv

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
        data_map[str(data[-1])].append(data)
    return data_map

def cal_summary(class_data):
    summary = []
    for i in range(len(class_data[0])):
        if i  == len(class_data[0]) - 1:
                break
        mean = 0
        stdev = 0
        for data in class_data:
            mean += float(data[i])
        mean = mean / len(class_data)
        for data in class_data:
            stdev += pow(float(data[i]) - mean, 2)
        if len(class_data) > 1:
            stdev = stdev/(len(class_data) - 1)
            stdev = math.sqrt(stdev)
        else:
            stdev = 0
        summary.append((mean, stdev))
    return summary

def density_function(x, mean, stdev):
    if stdev == 0:
        return 1
    exp = math.exp(-(pow(float(x) - mean, 2))/(2 * pow(stdev, 2)))
    return (1/(stdev * math.sqrt(2 * math.pi))) * exp

def cal_prediction(summary, new_data):
    probabilities = {}
    probabilities["yes"] = float(len(summary["yes"])/(len(summary["yes"]) + len(summary["no"])))
    probabilities["no"] =  float(len(summary["no"])/(len(summary["yes"]) + len(summary["no"])))
    for i in range(len(summary["yes"])):
        probabilities["yes"] *= density_function(new_data[i], summary["yes"][i][0], summary["yes"][i][1])
    for i in range(len(summary["no"])):
        probabilities["no"] *= density_function(new_data[i], summary["no"][i][0], summary["no"][i][1])
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
        cal_prediction(training_class_summary, input_data)

if __name__ == "__main__":
    if sys.argv[3] == "NB":
        nb(sys.argv[1], sys.argv[2])
    else: 
        print("REEEEEEEEEEEEEEEEEEEEEEE")
