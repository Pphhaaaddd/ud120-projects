#!/usr/bin/python

"""
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000

"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "Number of people: " , len(enron_data)

print "Number of features per person: " , len(enron_data["SKILLING JEFFREY K"])

#print enron_data["SKILLING JEFFREY K"]
count = 0
for data in enron_data:
    if (enron_data[data]["poi"]==1):
        count += 1

print "Number of POIs: " , count

print "Stock value of James Prentice: " , enron_data["PRENTICE JAMES"]["total_stock_value"]

print "Wesley Colwell to POIs: " , enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]

print "Money earned by Jeffrey K Stilling: " , enron_data["SKILLING JEFFREY K"]["long_term_incentive"]
print "Money earned by Andrew Fastow: " , enron_data["FASTOW ANDREW S"]["long_term_incentive"]
print "Money earned by Kenneth Lay: " , enron_data["LAY KENNETH L"]["long_term_incentive"]
