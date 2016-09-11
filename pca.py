#coding=utf-8
import char

import numpy as np

# Features are in columns
def pca(dataMat, topNfeat=5):
    # Calculate mean & std -> row vector
    miu = np.mean(dataMat, axis=0)
    sigma = np.std(dataMat)

    # Normalization
    stded = (dataMat - miu) / sigma

    covMat = np.cov(stded, rowvar=False) #求协方差方阵
    eigVals, eigVects = np.linalg.eig(np.mat(covMat)) #求特征值和特征向量

    # Sort eigenvalues
    # argsort returns indexes
    eigValInd = np.argsort(eigVals)

    eigValInd = eigValInd[:-(topNfeat + 1):-1]
    redEigVects = eigVects[:, eigValInd]       # 除去不需要的特征向量

    lowDDataMat = stded * redEigVects    #求新的数据矩阵
    reconMat = (lowDDataMat * redEigVects.T) * sigma + miu
    return lowDDataMat, reconMat


import Image, ImageDraw

unwindData = []
for ich in '!@#oe':
    im = Image.new("RGB", char.CHAR_SIZE, "white")
    draw = ImageDraw.Draw(im)

    draw.text((0, 0, 0, 0), ich, fill="black", font=char.font)

    import itertools as it
    eachpix = it.product(\
        range(char.CHAR_WIDTH),\
        range(char.CHAR_HEIGHT))

    grayPxs = [sum(im.getpixel(xy)) / 3 for xy in eachpix]
    unwindData.append(grayPxs)

datamat = np.mat(unwindData)

lowerDimensionalData, other = pca(datamat)
print lowerDimensionalData
