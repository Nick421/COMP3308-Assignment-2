import math

def knn(k, training_data, testing_data):

    # get number of attributes
    num_attributes = len(training_data[0])-1
    # array to stored neighbours
    euclieden_dist = []

    for x in range(len(training_data)):
        # for all training attributes, find euclieden distance to testing data
        distance = euclidean_distance(training_data[x],testing_data)
        euclieden_dist.append((distance,training_data[x][-1]))

    # sort the distances
    euclieden_dist.sort(key=lambda i:i[0])

    num_yes = 0;
    num_no = 0;

    for i in range(k):
        if euclieden_dist[i][1] == "yes":
            num_yes += 1
        else:
            num_no +=1
    # if there is a tie we take yes
    if num_yes >= num_no:
        return "yes"
    else:
        return "no"

def euclidean_distance(old_attribute, new_attribute):
    distance = 0;
    for i in range(len(new_attribute)):
        distance += pow((old_attribute[i]-new_attribute[i]), 2)
    return math.sqrt(distance)
