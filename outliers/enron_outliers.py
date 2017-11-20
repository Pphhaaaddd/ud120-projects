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
# matplotlib.pyplot.show()

i = -1
max_stock = 0
min_stock = 999999999
max_sal = 0
min_sal = 999999999
for point in data_dict:
    i += 1
    # if( data_dict[data_dict.keys()[i]]["salary"] != "NaN" and data_dict[data_dict.keys()[i]]["salary"] > 1000000 and data_dict[data_dict.keys()[i]]["bonus"] > 5000000):
    #     print i , point, data_dict[data_dict.keys()[i]]["salary"]
    if(data_dict[data_dict.keys()[i]]["exercised_stock_options"] != "NaN"):
        if(data_dict[data_dict.keys()[i]]["exercised_stock_options"] > max_stock):
            max_stock = data_dict[data_dict.keys()[i]]["exercised_stock_options"]
        if(data_dict[data_dict.keys()[i]]["exercised_stock_options"] < min_stock):
            min_stock = data_dict[data_dict.keys()[i]]["exercised_stock_options"]

    if(data_dict[data_dict.keys()[i]]["salary"] != "NaN"):
        if(data_dict[data_dict.keys()[i]]["salary"] > max_sal):
            max_sal = data_dict[data_dict.keys()[i]]["salary"]
        if(data_dict[data_dict.keys()[i]]["salary"] < min_sal):
            min_sal = data_dict[data_dict.keys()[i]]["salary"]


print "Max Value (exercised_stock_options): " , max_stock
print "Min Value (exercised_stock_options): " , min_stock

print "Max Value (salary): " , max_sal
print "Min Value (salary): " , min_sal


# print data_dict[data_dict.keys()[66]]
# print data_dict[data_dict.keys()[67]]
# print data_dict[data_dict.keys()[68]]
# print data_dict[data_dict.keys()[69]]
# print data_dict[data_dict.keys()[70]]
