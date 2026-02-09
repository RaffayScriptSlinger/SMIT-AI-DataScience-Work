# Numpy Python Library

import numpy as np

# Import Image Libraray

from PIL import Image 

#Normal List 
myList = [1,2,3,4,5,6,7,8,9,10]

#Numpy Array
np_Arr = np.array([1,2,3,4,5,6])

print(myList)
print(np_Arr)

npArr = np.array([1,2,3,4,5,6,])

#2D Array
npArr_01 = np.array([[1,2,3],
                     [5,9,8]])

print(npArr_01)

#Filling all Values Of array with zero
z = np.zeros((5,5))

print(z)
print(z[0][1])

#Filling all Values Of array with Ones
o = np.ones(4)
print(o)

#Full all Values Of array with third parameter One First Two We decide row And Colums
f = np.full((2,5),7)
print(f)

#First One is Start Secound On is end And las parameter is step 
a = np.arange(1,10,3)
print(a)

# Adding numpy array elements
 
npArr_03 = np.array([1,2,3,4,5])

print(npArr_03[2] + npArr_03[4])

# 3D Array

arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr[0,1,1])


# Generating Random Values In Array
newArr = np.random.rand(4,4)

print(newArr)


#Checking Size ,Data type ,shape 
print("Size Of Array is " , newArr.size)

print("Data Type Of Array is " , newArr.dtype)


print("Shape Of Array is " , newArr.shape)

# ImageWorking

img  = Image.open("CarImage.jpg")
img.show()

print(f"Image Size is {img.size} and image format {img.format} mode is {img.mode}  ")

# Universal Function

arr6 =   np.arange(1,10,2)

print(arr)

print(np.sqrt(arr6))
print(np.exp(arr6))


x = np.random.rand(6)
y = np.random.rand(6)

print(x)
print(y)