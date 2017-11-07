#!/usr/bin/python

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.

    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
from sklearn.naive_bayes import GaussianNB

### create classifier
clf = GaussianNB()

### training time
t0 = time()

### fit the classifier on the training features and labels
clf = clf.fit(features_train, labels_train)
print "Training time:", round(time()-t0, 3), "s"

### prediction time
t0 = time()

### use the trained classifier to predict labels for the test features
pred = clf.predict(features_test)
print "Prediction time:", round(time()-t0, 3), "s"

### calculate and return the accuracy on the test data
### this is slightly different than the example,
### where we just print the accuracy
### you might need to import an sklearn module
# from sklearn.metrics import accuracy_score

accuracy = clf.score(features_test, labels_test)
print "Accuracy : ", accuracy

#########################################################
