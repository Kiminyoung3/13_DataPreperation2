import matplotlib.pyplot as plt
import pandas as pd
import scipy as sp
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Binarizer

header = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
data = pd.read_csv('./data/pima-indians-diabetes.data.csv', names=header)

array=data.values
X=array[:, 0:8]
Y=array[:, 8]

scaler = Binarizer(threshold=0.5)
rescaled_X=scaler.fit_transform(X)
print(rescaled_X)

# scaler = MinMaxScaler(feature_range=(0, 1))

