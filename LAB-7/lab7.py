from sklearn.cluster import KMeans
from sklearn import preprocessing
from sklearn.mixture import GaussianMixture 
from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset = load_iris()
print("\n IRIS Dataset:\n", dataset.data)
print("\n IRIS Features:\n", dataset.feature_names) 
print("\n IRIS Target:\n", dataset.target)
print("\n IRIS Target:\n", dataset.target_names)

X = pd.DataFrame(dataset.data) 
X.columns=['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width'] 

y=pd.DataFrame(dataset.target)
y.columns=['Targets']

print(y)

plt.figure(figsize=(8,5))
colormap=np.array(['red','lime','blue'])

# Plotting without Clustering
plt.subplot(1,3,1) 
plt.scatter(X.Petal_Length,X.Petal_Width,c=colormap[y.Targets],s=20) 
plt.title('Before Clustering')

# Plotting with K-Means Clustering
plt.subplot(1,3,2)
model = KMeans(n_clusters=3)
model.fit(X) 
predY = np.choose(model.labels_,[0,1,2]).astype(np.int64) 
plt.scatter(X.Petal_Length,X.Petal_Width,c=colormap[predY],s=20) 
plt.title('KMeans Clustering')

# Plotting with EM using GMM Clustering
scaler=preprocessing.StandardScaler() 
scaler.fit(X)
xsa=scaler.transform(X) 
xs=pd.DataFrame(xsa,columns=X.columns) 
gmm=GaussianMixture(n_components=3) 
gmm.fit(xs)

y_cluster_gmm=gmm.predict(xs) 
plt.subplot(1,3,3)
plt.scatter(X.Petal_Length,X.Petal_Width,c=colormap[y_cluster_gmm],s=20) 
plt.title('GMM with EM Clustering')
plt.show();