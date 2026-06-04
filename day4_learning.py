# import numpy as np               //NUMPY ATTRIBUTES AND PROPERTIES
# arr = np.array([1,2,3,4,5])
# print(arr.shape)
# print(arr.ndim)
# print(arr.itemsize)
# print(arr.dtype)
# print(arr.astype(float))
# print(arr.size)
# arr2 = np.array([[.1,.2,.3],[.4,.5,.6]])
# print(arr2)                      //EXAMPLE 2
# print(arr2.shape)
# print(arr2.ndim)
# print(arr2.itemsize)
# print(arr2.dtype)
# print(arr2.astype(int))
# print(arr2.size)
# arr3 = np.linspace(0,50,6)       //EXAMPLE 3
# print(arr3)
# print(arr3.shape)
                 #CODE TO CHECK AND PROVE THAT LESS MEMORY IS USED IN NUMPY THEN PYTHON LIST 
# lista = range(100)   
# import sys
# print(sys.getsizeof(87)*len(lista))
# import numpy as np
# arr = np.arange(100)
# print(arr.itemsize*arr.size)
                                         #CODE TO PROVE THAT IT IS FASTER and convient because it has small code
# import time
# x = range(10000000)
# y = range(10000000,20000000)
# start_time = time.time()
# c = [(x+y) for x,y in zip(x,y)]
# print(time.time()-start_time)
# import numpy as np
# a = np.arange(10000000)
# b = np.arange(10000000,20000000)
# start_time = time.time()
# c = a+b
# print(time.time()-start_time)