

get_ipython().run_line_magic('matplotlib', 'notebook')
import cv2
import numpy as np
import matplotlib.image  as mpimg
import matplotlib.pyplot as plt



ex='/home/shaxpy/Downloads/Search and Sample bot/calib_img/5.jpg'
img=mpimg.imread(ex)
plt.imshow(img)




get_ipython().run_line_magic('matplotlib', 'inline')

def perspect_transform(img,src,dst):
    m=cv2.getPerspectiveTransform(src,dst)
    warped=cv2.warpPerspective(img,m,(img.shape[1],img.shape[0]))
    return warped
sze=5
bottom=6
source=np.float32([[14,139],[301,140],[200,96],[118,96]])
dest=np.float32([[img.shape[1]/2-sze,img.shape[0]-bottom],
                 [img.shape[1]/2+sze,img.shape[0]-bottom],
                 [img.shape[1]/2+sze,img.shape[0]- 2*sze-bottom],
                 [img.shape[1]/2-sze,img.shape[0]- 2*sze-bottom],])

warped=perspect_transform(img,source,dest)
fig=plt.figure(figsize=(12,6))
plt.imshow(warped)






