# Image Compression Library using K-Means Clustering
## Created by Fransiscus Emmanuel Bunaren
## Based on [Python Data Science Handbook by Jake VanderPlas](https://jakevdp.github.io/PythonDataScienceHandbook/05.11-k-means.html)

This library can compress an image by doing clustering to cluster millions of colors into n colors.

In theory, there are many colors in an image that are very similar to each other, which is indistinguishable to human eyes. Since most of the time, human eyes cannot tell the difference between those colors, we can group those colors into one color. To perform clustering, we can use K-Means to construct clusters of colors.

## How to use

You can simply import the `ImageCompression.py` file to your Python project. The method `compress` in that file consists of three arguments.

- `filename` : The filename of an image that you want to compress
- `destination` : A filepath where you want to save the compressed image
- `number_of_colors` : The number of color clusters that you want to construct (16 is the default value)

Note : The image quality will be better for higher number of color clusters. If you feel that the image quality is poor, you can try to increase the number of color clusters.

The method above will return `True` if the compression process has finished. 
If there is an exception occured, then it will return `False`.

See `example.py` file for example usage.

