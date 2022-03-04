

import numpy as np
import pandas as pd


class LearningVectorQuantization:
    """
    Learning Vector Quantization
    params:
        alpha: learning rate
        n_protos_class: the number of prototypes each class should be reduced to
        n_iter: number of iterations to make to find the most suitable positions for prototypes
    """
    def __init__(self, alpha=0.6, n_protos_class=1, n_iter=20):
        self.alpha = alpha
        self.n_prot_class = n_protos_class
        self.n_iter = n_iter
    
    def fit(self, X, y):
        """
        Load training data and train model
        X: numpy array of features
        y: Classes
        """
        if isinstance(X, pd.DataFrame):
            X=X.to_numpy()
        if isinstance(y, pd.DataFrame):
            y=y.to_numpy()
        self.tr_data = X
        self.classes_ = y
        self.uClasses = np.unique(self.classes_)
        self.n_samples, self.n_features = np.shape(X)
        self.n_classes = np.shape(y)[0] # Necessary?
        self.w, self.l = self.learnLVQModel()
        return self
    
    @property
    def class_count_(self):
        cl_cnt = ""
        return("Under Construction...")
    @property
    def feature_count_(self):
        return("Under Construction...")
    
    # Not used anymore.. remove?
    def return_weights_labels(self):
        return self.w, self.l
    
    def predict(self, xval):
        if isinstance(xval, pd.DataFrame):
            xval=xval.to_numpy()
        nrowsprotos, _ = np.shape(self.w) # Get number of prototypes from training data
        nrows, _ = np.shape(xval) # Get number of samples in validation data
        y_pred = []
        for h in range(nrows):                      # Distance Matrix: create row for each validation sample with a column for each prototype
            dist = [0] * nrowsprotos
            for j in range(nrowsprotos):
                # dist[j] = np.linalg.norm(xval.to_numpy()[h,:] - self.w[j])    # add distance between sample[h] and proto[j] to  distance matrix
                dist[j] = np.linalg.norm(xval[h,:] - self.w[j]) 
            mn = np.min(dist)                                                  # Find minimum distance for sample[h]
            mnidx = dist.index(mn)                                              # Get index of min dist
            predictedLabel = self.l[mnidx]                                      # Use index of min dist to get label
            y_pred.append(predictedLabel)
        return y_pred

    def getWinner(self, trainingDataPoint, protosWeights):
        nprotos, _ = np.shape(protosWeights)
        d = [0] * nprotos
        for i in range(nprotos):
            d[i] = np.linalg.norm(trainingDataPoint - protosWeights[i])
        mn = min(d)
        widx = d.index(mn)
        return widx

    def initProtos(self):
        """ Initiate Prototypes n prototypes for each class """
        protosWeights = []
        protosLabels = []
        for clss in self.uClasses:
            for j in range(self.n_prot_class):
                idx = np.nonzero(self.classes_ == clss)
                mn = np.array(self.tr_data[idx[0],:]).min(axis=0)
                mx = np.array(self.tr_data[idx[0],:]).max(axis=0)
                protosWeights.append(np.array(np.random.random(self.n_features)) * (mx - mn) + mn)
                protosLabels.append(clss)
        return protosWeights, protosLabels

    def learnLVQModel(self):
        """ Initialize the prototypes randomly """
        [protosWeights, protosLabels] = self.initProtos()
        for t in range(self.n_iter):
            # Learning rate alpha decreases over time
            alpha = np.exp((-1*self.alpha) * t)

            for i in range(self.n_samples):          # For each datapoint in training data:
                widx = self.getWinner(self.tr_data[i,:], protosWeights) # Find closest prototype for datapoint[i]
                if protosLabels[widx] == self.classes_[i]:
                    # The winner prototype is of the same class: Move closer to datapoint
                    protosWeights[widx] = protosWeights[widx] + alpha * (self.tr_data[i] - protosWeights[widx])
                else:
                    # The winner prototype is of different class: Move away from datapoint
                    protosWeights[widx] = protosWeights[widx] - alpha * (self.tr_data[i] - protosWeights[widx])
        return protosWeights, protosLabels

if __name__ == "__main__":
    #X = None
    #y = None
    #X_val = None
    nprotos = 2
    clf = LearningVectorQuantization(nprotos)
    #clf.fit(X, y)
    #y_pred = clf.predict(X_val)
