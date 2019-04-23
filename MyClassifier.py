import sys
import csv
import numpy

from knn import knn, euclidean_distance
from nb import nb, read_data, class_separation, cal_summary, density_function, cal_prediction

def parse_file(filename):
    data = []
    with open(filename) as file:
        csv_reader = csv.reader(file, delimiter=',')
        for row in csv_reader:
            for i in range(len(row)):
                if row[i] != 'yes' and row[i] != 'no':
                    row[i] = numpy.float(row[i])
            data.append(row)
    return data

def main(argv):
    if(len(argv) != 3):
        return 1

    training_file = argv[0]
    testing_file = argv[1]
    algorithm = argv[2]

    training_data = parse_file(training_file)
    testing_data = parse_file(testing_file)

    if algorithm == 'NB':
        # do naive bayes
        nb(sys.argv[1], sys.argv[2])
    else:
        # do Knn
        k = int(algorithm.replace('NN', ''))
        # for all testing instance run knn on each of them
        for i in range(0, len(testing_data)):
            print(knn(k, training_data, testing_data[i]))

if __name__ == "__main__":
   main(sys.argv[1:])
