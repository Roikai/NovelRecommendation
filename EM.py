import numpy as np  
from sklearn import datasets  
from sklearn.cluster import KMeans  
from sklearn.mixture import GaussianMixture  
# 读取数据  
iris=datasets.load_iris()  
x=iris.data[:,:2]  
y=iris.target  
mu = np.array([np.mean(x[y == i], axis=0) for i in range(3)])    
print('实际均值 = \n', mu)  
#K-Means  
kmeans=KMeans(n_clusters=3,init='k-means++',random_state=0)  
y_hat1=kmeans.fit_predict(x)  
y_hat1[y_hat1==0]=3  
y_hat1[y_hat1==1]=0  
y_hat1[y_hat1==3]=1  
mu1=np.array([np.mean(x[y_hat1 == i], axis=0) for i in range(3)]) 
print('分类正确率为',np.mean(y_hat1==y))  
print('K-Means均值 = \n', mu1)
gmm=GaussianMixture(n_components=3,covariance_type='full', random_state=0)  
gmm.fit(x)  
print('GMM均值 = \n', gmm.means_)  
y_hat2=gmm.predict(x) 
y_hat2[y_hat2==1]=3  
y_hat2[y_hat2==2]=1  
y_hat2[y_hat2==3]=2  
print('分类正确率为',np.mean(y_hat2==y))
