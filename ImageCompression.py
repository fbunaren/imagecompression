# Image Compression Library using K-Means Algorithm
# Created by Fransiscus Emmanuel Bunaren

# To know more about K-Means Clustering :
# https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html

from sklearn.cluster import MiniBatchKMeans
import numpy as np
import matplotlib.image as mpimg
import warnings
import imageio


def compress(filename, destination, number_of_colors=16):
    try:
        warnings.simplefilter('ignore')
        img = mpimg.imread(filename)

        data = img / 255.0
        data = data.reshape(img.shape[0] * img.shape[1], img.shape[2])

        kmeans = MiniBatchKMeans(number_of_colors)
        kmeans.fit(data)

        new_colors = np.asarray(kmeans.cluster_centers_[kmeans.predict(data)])
        compressed_image = new_colors.reshape(img.shape)

        imageio.imwrite(
            destination,
            (compressed_image *
             255.0).astype(
                np.uint8))
        return True
    except BaseException:
        return False
