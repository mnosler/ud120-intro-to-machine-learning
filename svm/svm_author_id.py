#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
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

from sklearn import svm

kernelType = "rbf"
myC = 10000
clf = svm.SVC(kernel=kernelType, C=myC)

#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 

print("Beginning Training...")
timeToFit = time()
clf.fit(features_train, labels_train)
print "Time to fit ", kernelType, " C=", myC, ": ", time() - timeToFit 
print "Accuracy: ", clf.score(features_test, labels_test)

predictions = clf.predict(features_test)

chris_predictions = 0
for prediction in predictions:
    if(prediction == 1):
        chris_predictions += 1

print "there are ", chris_predictions, "number of emails predicted to be Chris"
#########################################################


