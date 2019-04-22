import math

def knn(k, training_data, testing_data):

    num_attributes = len(training_data[0])-1
    euclidean_dist = []
    results = []

    for i in range(len(testing_data)):
        for x in range(len(training_data)):
            temp_attributes = []
            for y in range(0,num_attributes+1):
                temp_attributes.append(training_data[x][y])

            distance = euclidean_distance(temp_attributes,testing_data[i])
            euclidean_dist.append((distance,temp_attributes[-1]))

        euclidean_dist.sort(key=lambda i:i[0])

        num_yes = 0;
        num_no = 0;

        for i in range(k):
            if euclidean_dist[i][1] == "yes":
                num_yes += 1
            else:
                num_no +=1
        # if there is a tie
        if num_yes >= num_no:
            results.append("yes")
        else:
            results.append("no")

    return results

def euclidean_distance(old_attribute, new_attribute):
    distance = 0;
    for i in range(len(new_attribute)):
        distance += pow((old_attribute[i]-new_attribute[i]), 2)
    return math.sqrt(distance)
