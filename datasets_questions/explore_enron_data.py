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

james =  enron_data["PRENTICE JAMES"]
print james["restricted_stock"] + james["exercised_stock_options"]

#wesley = enron_data['COLWELL WESLEY']
#email_indexes = ('to_messages','from_messages', 'from_this_person_to_poi', 'from_poi_to_this_person')

#email_count = 0
#for index in email_indexes:
#    email_count += wesley[index]
    
print enron_data["SKILLING JEFFREY K"]["total_payments"]
print enron_data["FASTOW ANDREW S"]["total_payments"]
print enron_data["LAY KENNETH L"]["total_payments"]


email_count = 0
salary_count = 0
total_payments_na = 0
for person in enron_data.values():
    if(person['salary'] != 'NaN'):
        salary_count+=1
    if(person['email_address'] != 'NaN'):
        email_count+=1
    if(person['total_payments'] == 'NaN'):
        total_payments_na+=1
print "total emails: ", email_count, " Total salaries: ", salary_count

print "num and % missing payments: ", total_payments_na, (float(total_payments_na)/len(enron_data)),"%"