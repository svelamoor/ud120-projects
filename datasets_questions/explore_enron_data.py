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

print enron_data.items() 
#print len(enron_data)
print len(enron_data["SKILLING JEFFREY K"])

pois = {k:v for (k,v) in enron_data.iteritems() if v['poi'] == True}
print "Persons of Interest -- ", len(pois)

print enron_data["PRENTICE JAMES"]["total_stock_value"]
print enron_data["COLWELL WESLEY"]['from_this_person_to_poi']
print enron_data["SKILLING JEFFREY K"]['exercised_stock_options']
print "Skilling ", enron_data["SKILLING JEFFREY K"]['total_payments']
print "Fastow ", enron_data["FASTOW ANDREW S"]['total_payments']
print "Lay ", enron_data["LAY KENNETH L"]['total_payments']


def findNaNs(dict, field):
	return len([k for (k,v) in dict.items() if v[field] == 'NaN'])

defined_salary = [k for (k,v) in enron_data.items() if v['salary'] != 'NaN']
known_email_address = [k for (k,v) in enron_data.items() if v['email_address'] != 'NaN']

print "Salary ", len(defined_salary), " known email address - ", len(known_email_address)

print "Unknown total payments for ", findNaNs(enron_data, 'total_payments'), " people which represents ", 1.0*findNaNs(enron_data, 'total_payments')/len(enron_data)*100.0 , " percentage of all of the dataset"
print "Unknown total payments for POIS ", findNaNs(pois, 'total_payments'), " people which represents ", 1.0*findNaNs(pois, 'total_payments')/len(pois)*100.0 , " percentage of all POIs"
