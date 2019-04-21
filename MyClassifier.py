import sys
import csv
import numpy

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
    else:
        k = int(algorithm.replace('NN', ''))

        results = knn(k,training_data,testing_data)

    for result in results:
        print(result)

if __name__ == "__main__":
   main(sys.argv[1:])
