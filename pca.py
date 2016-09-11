# coding=utf-8
import char

import numpy as np


# Features are in columns
def pca(data, reduced_dim=5):
    # Calculate mean & std -> row vector
    miu = np.mean(data, axis=0)
    sigma = np.std(data)

    # Normalization
    ndata = (data - miu) / sigma

    cov_mat = np.cov(ndata, rowvar=False)
    eigvals, eigvects = np.linalg.eig(np.mat(cov_mat))

    # Sort eigenvalues
    # argsort returns indexes
    eig_idx = np.argsort(eigvals)

    eig_idx = eig_idx[:-(reduced_dim + 1):-1]
    transmat = eigvects[:, eig_idx].real

    # Use Eigenvectors to reduce the raw data
    low_d_data = ndata * transmat
    return low_d_data, transmat


charUnwind = []
for ich in char.charset:
    im = char.draw_char(ich)

    # grayPxs = im.resize((3, 3), resample=Image.ANTIALIAS).getdata()
    grayPxs = im.getdata()

    charUnwind.append(grayPxs)

charMat = np.mat(charUnwind)

charFeature, transformer = pca(charMat)


def find_most_fit(img):
    ftr = np.mat(img.getdata())
    reduced_ftr = ftr * transformer

    ftrt = reduced_ftr.repeat(len(charFeature), axis=0)
    criteria = np.absolute(ftrt - charFeature).mean(axis=1, dtype=np.float32)

    best_idx = criteria.argmin()

    return char.charset[best_idx]
