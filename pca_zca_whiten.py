# -*- coding: utf-8 -*-
"""
Created on Wed Dec 09 20:35:35 2015

@author: Freeya Wang
"""
#patches is a data matrix the rows represent features , the cols represent samples


def PCA_ZCA_whiten(patches):
    import numpy as np
    sigma = patches.dot(patches.transpose()) / patches.shape[1]
    (u, s, v) = np.linalg.svd(sigma)
    
# Number of components to retain    
    k = 0
    for k in range(s.shape[0]):
        if s[0:k].sum() / s.sum() >= 0.999:
            break
    print 'Optimal k to retain 99% variance is:', k
    patches_tilde = u[:, 0:k].transpose().dot(patches)#reducing the data dimension
    patches_hat = u.dot(np.resize(patches_tilde, patches.shape))#recovering an approximation of the data
    '''    
    num_samples = patches.shape[1]
    random_sel = random.sample(range(num_samples), 1024)
    display_network.display_network(patches_hat[:, random_sel], 'pca_tilde.png')
    display_network.display_network(patches[:, random_sel], 'origin_Sel.png')
#     
    patches_rot = u.transpose().dot(patches)#rotating the data
    #Regularizaton parameter
    epsilon = 0.1
    
    #The different components of the data are uncorrelated and have unit variance.
    patches_pcawhite = np.diag(1 / (s + epsilon)).dot(patches_rot)
    #When using ZCA whitening (unlike PCA whitening), we usually keep all \textstyle n dimensions of the data, and do not try to reduce its dimension
    patches_zcawhite = u.dot(patches_pcawhite)
    display_network.display_network(patches_zcawhite[:, random_sel], 'pca_zcawhite.png')
    '''
    return patches_hat,patches_pcawhite,patches_zcawhite
