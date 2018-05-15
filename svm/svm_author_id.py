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
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

clf = SVC(kernel = "rbf", C=10000.0)
t0 = time()
clf.fit(features_train, labels_train)
print "Training time ", round(time()-t0, 3)," seconds"
pred = clf.predict(features_test)
print "accuracy score ", accuracy_score(labels_test, pred)
print "10th ", "Chris" if pred[10] == 1 else "Sara"
print "26th ", "Chris" if pred[26] == 1 else "Sara"
print "50th ", "Chris" if pred[50] == 1 else "Sara"
print "Chris Emails predicted ", len([x for x in pred if x == 1])
print "Sara Emails predicted ", len([x for x in pred if x == 0])
#########################################################


