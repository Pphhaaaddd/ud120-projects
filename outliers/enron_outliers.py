#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
features = ["salary", "bonus"]
data_dict.pop("TOTAL",0)
data = featureFormat(data_dict, features)


### your code below
for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()

i = -1
max = 0
min = 999999999
for point in data_dict:
    i += 1
    # if( data_dict[data_dict.keys()[i]]["salary"] != "NaN" and data_dict[data_dict.keys()[i]]["salary"] > 1000000 and data_dict[data_dict.keys()[i]]["bonus"] > 5000000):
    #     print i , point, data_dict[data_dict.keys()[i]]["salary"]
    if(data_dict[data_dict.keys()[i]]["exercised_stock_options"] > max and data_dict[data_dict.keys()[i]]["exercised_stock_options"] != "NaN"):
        # print i , point, data_dict[data_dict.keys()[i]]["exercised_stock_options"]
        max = data_dict[data_dict.keys()[i]]["exercised_stock_options"]
    if(data_dict[data_dict.keys()[i]]["exercised_stock_options"] < min and data_dict[data_dict.keys()[i]]["exercised_stock_options"] != "NaN"):
        # print i , point, data_dict[data_dict.keys()[i]]["exercised_stock_options"]
        min = data_dict[data_dict.keys()[i]]["exercised_stock_options"]
print "Max Value (exercised_stock_options): " , max
print "Min Value (exercised_stock_options): " , min
# print data_dict[data_dict.keys()[66]]
# print data_dict[data_dict.keys()[67]]
# print data_dict[data_dict.keys()[68]]
# print data_dict[data_dict.keys()[69]]
# print data_dict[data_dict.keys()[70]]
