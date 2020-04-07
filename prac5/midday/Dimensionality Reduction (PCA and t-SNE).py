#%%
"""PCA
PCA can be implemented very simply in Matlab or Python. Given a dataset (as a matrix X), 
the covariance matrix can be found using the Matlab covariance function (cov(X)).Then, the 
eigenvectors and eigenvalues of this covariance matrix are the principal component(vectors) 
and principal values respectively. The eigenvalues reflect the amount of variance accounted for 
by each principal component and are ordered. To perform dimensionality reduction (e.g. down to 2 dimensions), 
we need to multiply X by the two eigenvectors withthe largest corresponding eigenvalues.
"""
import numpy as np
def PCA(X, num_components=2):
    cov_X = np.cov(X)
    

# %%


# %%

# it works just like jupyter