#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################

### your code here!  name your classifier object clf if you want the
### visualization code (prettyPicture) to show you the decision boundary

from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn import tree
from sklearn.ensemble import RandomForestRegressor
from sklearn import neighbors
from sklearn.ensemble import AdaBoostClassifier

#clf = GaussianNB()
#clf = SVC(kernel='rbf', gamma = 50)
#clf = tree.DecisionTreeClassifier(min_samples_split=40)
#clf = RandomForestRegressor(n_estimators=1)
#clf = neighbors.KNeighborsClassifier(n_neighbors=8)
clf = AdaBoostClassifier(n_estimators=30)

clf = clf.fit(features_train,labels_train)

count = 0.0
pred = clf.predict(features_test)
for i in range(0,len(pred)):
    if pred[i]==labels_test[i]:
        count += 1
        accuracy = count/len(pred)
#accuracy = clf.score(features_test,labels_test)
print "Accuracy : ", accuracy

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
