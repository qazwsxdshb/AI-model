import Convolution
import cv2
import numpy as np 

f=cv2.imread("test.png")
img=np.array(f)
ans=Convolution.Convolution([[1,0,-1],[2,0,-2],[1,0,-1]])

tt = np.stack([ans.run(img[:,:,i]) for i in range(3)], axis=2)
tt=np.array(tt,np.uint8)
print(tt[0][0])
print(tt.shape, tt.dtype)
cv2.imshow('My Image', tt)
cv2.waitKey(0)