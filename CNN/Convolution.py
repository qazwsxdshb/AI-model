import numpy as np
class Convolution:
    def __init__(self,Feature:list[list]) -> None:
        self.Feature=Feature

    def run(self,img):
        img,ans=np.array(img),[]
        for y in range(len(img)-len(self.Feature)+1):
            tmp=[]
            for x in range(len(img[0])-len(self.Feature[0])+1):
                tmp.append(self.mul_matrix(img[y:y+len(self.Feature[0]),x:x+len(self.Feature)]))
            ans.append(tmp)
        return ans
    
    def mul_matrix(self,img,ans=0):
        for x in range(len(self.Feature[0])):
            for y in range(len(self.Feature)):
                ans+=self.Feature[x][y]*img[x][y]
        return ans

ans=Convolution([[0,0,1],[1,0,0],[0,1,1]])
ans.run([[0,0,0,0,0,0,0],[0,1,0,0,0,1,0],[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,1,0,0,0,1,0],[0,0,1,1,1,0,0],[0,0,0,0,0,0,0]])

