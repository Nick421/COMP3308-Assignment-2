def make_folds(training_data):
    yes = []
    no = []

    for i in range(0, len(training_data)):
        if training_data[i][-1] == "yes":
            yes.append(training_data[i])
        else:
            no.append(training_data[i])

    folds = []
    for i in range(0,10):
        folds.append([])
        
    i = 0
    while len(yes) > 0:
        folds[i % 10].append(yes.pop())
        i += 1
    while len(no) > 0:
        folds[i % 10].append(no.pop())
        i += 1

    with open('pima-folds.csv', 'w', newline='') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_NONE)
        i = 1
        for fold in folds:
            wr.writerow(["fold"+str(i)])
            i = i + 1
            for row in fold:
                wr.writerow(row)

# TODO:
# Add in 10 folds strafficaction for KNN and Naive bayes
