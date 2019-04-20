import math

def knn(k, training_data, testing_data,num_attributes):

    euclieden_dist = []

    for i in training_data:
        distance = euclidean_distance(training_data,testing_data)
        euclieden_dist.append((distance,training_data[:,-1]))

    euclieden_dist.sort(key=lambda i:i[0])

    num_yes = 0;
    num_no = 0;

    for i in range(k):
        if euclieden_dist[i][1] == yes:
            num_yes++
        else:
            num_no++

    if num_yes >= num_no:
        return "yes"
    else:
        return "no"
            
def euclidean_distance(old_attribute, new_attribute, num_attributes):
    distance = 0;
    for i in range(num_attributes):
        distance += pow((old_attribute[i]-new_attribute[i]), 2)
    return math.sqrt(distance)
