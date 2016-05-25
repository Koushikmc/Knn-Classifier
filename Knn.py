#-----------------------------------------------------------------------------------------------------------------------
#   Author  :Koushik Modayur Chandramouleeswaran
#   ModuleName  : Knn.py
#   Descriprion : K nearest neighbour classification algorithm implementation
#   Date    : 09/19/2015
#-----------------------------------------------------------------------------------------------------------------------
import _csv as csv
import math
import operator


training_data = []                      #Global list for storing training data
def load_train_data(file_name):
    # Function to read the input file and store it in a list
    try:
        train = open(file_name)
        data = csv.reader(train)
        for rec in data:
            temp_list = []
            for cols in rec:
                if rec.index(cols) != len(rec)-1:
                    temp_list.append(float(cols))
                else:
                    temp_list.append(cols)

            training_data.append(temp_list)

        print ("training data loaded")
    except IOError:
        print ("File not available. Please check the filename")
        exit()



def calcdist(train,test):
    #Function to calculate the cartesion/euclidean distance between the training and test records
    distance_set = []
    for rec in train:
        if len(rec[0:len(rec)-1]) != len(test):
            print("Dimensions of test and train do not match")
            break
        else:
            dist = 0
            for i in range(0,len(test)):
                dist += (test[i]-rec[i])**2

        print ("Distance between the test point and training data " +str(train.index(rec)+1)+ " " +str(round(math.sqrt(dist),3)))

        distance_set.append(round(math.sqrt(dist),3))


    return distance_set

def find_neighbours(dist,numofneighbors):
    # Function to find the nearest specified k neighbours and determine the class using majority voting

    topelemets_list = sorted(range(len(dist)),key=lambda x:dist[x])
    neighbours = topelemets_list[:numofneighbors]

    class_dict = {}
    for n in neighbours:
        if training_data[n][-1] in class_dict:
            class_dict[training_data[n][-1]] +=1
        else:
            class_dict.update({training_data[n][-1]:1})

    output_class = sorted(class_dict.items(), key=operator.itemgetter(1),reverse = True)[0][0]
    print (output_class)

if __name__ == "__main__":
    print ("Place the input dataset csv file in the same directory of the python module ")
    file_name = input("Enter the name of the training dataset csv file :")
    load_train_data(file_name)
    test = [float(x) for x in (raw_input("Enter the values separated by ',': " ).split(","))]
    k=int(raw_input("Enter the number of neighbours to consider :"))
    distance = calcdist(training_data,test)
    find_neighbours(distance,k)







