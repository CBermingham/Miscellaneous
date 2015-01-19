back_projection.py

This script uses a simple version of the algorithm used by CT scanners, 
the backprojection algorithm, to reconstruct an image.'X-rays' are sent 
through the image at different angles and their attenuation due to the
different 'densities' (greyscale numbers) in the image are recorded.
Projections are created by creating images from the 1D intensity values
the same size as the original image and oriented along the projection
direction and the images are summed together to reconstruct the 
original image. 

Filtering can be used to make the image clearer.