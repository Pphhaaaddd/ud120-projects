#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "r") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list)
labels, features = targetFeatureSplit(data)



### your code goes here

from sklearn import tree
from sklearn.model_selection import train_test_split

features_train , features_test, labels_train, labels_test = train_test_split(features,labels,test_size = 0.3, random_state=42)

clf = tree.DecisionTreeClassifier()
clf = clf.fit(features_train,labels_train)

print "Accuracy: " , clf.score(features_test,labels_test)

#get number of POIs in test set
print  "Number of POIs in test set: " , labels_test.count(1.0)

#get total number of people
print "Total number of people in test set: " , len(labels_test)

#print both true and prediction
print labels_test
pred = clf.predict(features_test)
print pred

i=0
tp =0
fp =0
fn =0
tn =0
for a in labels_test:
    if(pred[i] == a and a == 1.):
        tp += 1
    elif(pred[i] == a and a == 0.):
        tn += 1
    elif(a == 0. and pred[i] == 1.):
        fp += 1
    else:
        fn += 1
    i += 1
print "Number of True Positives: ", tp
print "Number of False Positive: ", fp
print "Number of False Negetive: ", fn
print "Number of True Negetive: ", tn

from sklearn.metrics import precision_score
print "Precision score: " , precision_score(labels_test,pred)
