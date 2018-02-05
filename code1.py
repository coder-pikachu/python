import os
from scipy import misc

min_shape=(100000000,100000000)
	max_shape=(0,0)
    for j,i in enumerate(os.listdir()):
        ig=misc.imread(i)
        ht,wd,_= ig.shape
        misc.imsave("train_"+str(j)+".jpg",ig[:,:wd//2,:])
        misc.imsave("label_"+str(j)+".jpg",ig[:,wd//2:,:])
        if(min_shape>(ht,wd)):
            min_shape=(ht,wd)
        if(max_shape<(ht,wd)):
            max_shape=(ht,wd)
         
max_shape
