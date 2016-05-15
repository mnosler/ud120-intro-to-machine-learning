def classify(features_train, labels_train):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
        
    ### your code goes here!
    from sklearn import svm
    clf = svm.SVC(kernel="rbf", gamma=100., C=1000)
    clf.fit(features_train, labels_train)
    return clf
