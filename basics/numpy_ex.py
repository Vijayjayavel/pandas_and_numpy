# excersies in numpy

import numpy as np

print(np.__version__ )# show the version of the numpy

arr=np.array([1,2,3,4])
print(arr) # (ex: 1D array)

arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr) # ex: 2D array

arr=np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr) # ex: 3D array

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim) # show dimensions of array

x=np.array([222221,2,3,4])
print(x[0]) # print array 0th element
print([x[1]+x[3]]) # print addition of respective array element

y=np.array([[1,2,3],[4,5,6]])
print(y[0,2]) #return y[a,b]   a=array index,b=element index

z=np.array([[[1,2,3],[4,5,6]],[[6,7,8],[3,2,1]]])
print(z[0,1,2]) #return z[a,b,c]   a=dim,b=array index,c=element index

print(y[1,1:3]) # slicing 2d array

print(z[1,1,::-1]) # slicing 3d array

print(z[:,1,2]) # return 2 indexed element in all dimesion 1st array

print(y.dtype) # return datatype of y array

a=np.array([1,2,3],dtype='c')
print(a)

b=np.array([1.2,3.4,6.7,0])
print(b.astype('i')) # print b array in integer data type
print(b.astype('bool')) # return false where 0 else true

c=np.array([1,3,5,7])
d=c.copy() # does not affect original list viceversa
e=c.view() # does affect the original list viceversa
d[2]=0
print(c,d,e)
e[1]=55
print(c,d,e)

f=np.array([[4,6,7,8],[23,4,5,6]])
print(f.shape) # return shape of the array
g=np.array([1,2,4],ndmin=5) # return array with mentioned dimension
print(g)

h=np.array([i for i in range(9)])
print(h.reshape(3,3)) # re shaping the matrix

i=np.array([i for i in range(12)])
print(i.reshape(3,2,2))

j=np.array([[1,2,3],[4,5,6],[7,8,9]])
print((j.reshape(-1))) # -1 hepls to reshape into 1d array

k=np.array([[1,2,3],[4,5,6]])
for x in k:
    print(x) # print lists in k array

for x in k:
    for y in x:
        print(y) # print elements in k array ( no. of for loops depends upon dimension of the array)

l=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[11,22,33]]])
for x in l:
    for y in x:
        for z in y:
            print(z) #print every element in 3d array

for x in np.nditer(l):
    print(x)  # simple numpy fun to avoid multiple loop

for x in np.nditer(l,flags=['buffered'],op_dtypes='S'):
    print(x) # print with some other data type

for i,x in np.ndenumerate(l):
    print(i,x) # print with index

a1=np.array([1,2,3])
a2=np.array(['a','b','c'])

arr=np.concatenate((a1,a2))
print(arr) # joining of two array with same data type (result array dtype will became string since one of the dtype is sring)
print(arr.dtype)

a=np.array([[1,2,3],[4,5,6]])
b=np.array([[2,3,4],[5,6,7]])
c=np.concatenate((a,b),axis=0) # joining with axis of two array
print(c)

d=np.stack((a,b),axis=1)
print(d) # same as concatenate but if you not mention axis it consider it as 0


e=np.hstack((a,b))
print(e) # stack it horozontally and then concatenate

f=np.vstack((a,b))
print(f) # stack it vertically and then concatenate

g=np.dstack((a,b))
print(g) # stack element wise in both array

x=np.array([i for i in range(12)])

a=np.array_split(x,5)
print(a) #splitting array with flexible number of elements too

b=np.split(x,3)
print(b) #it will divide with equal number of elements


arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3) # splitting horizontally
print(newarr)
newarr=np.vsplit(arr,3) #splitting vertically
print(newarr)

c=np.array([i for i in range(1,9)])

x=np.where(c==6) # inside depends on the condition it will return the index of the element
print(x) # print index of number 6 in array c

d=np.array([3,4,2,5,9,7,6])
v=np.searchsorted(d,7) # this will return the index of number to be positioned so that the search will be efficient
print(v)
w=np.searchsorted(d,3,side='right')
print(w)

a=np.array([1,3,5,7])
b=np.searchsorted(a,[2,4,8])
print(b)

a=np.array([3,2,35,63,8,2])
print(np.sort(a)) # it return copy of array not change original array

a=np.array([1,2,3,4])
y=[False,True,False,True]
print(a[y]) # return array elements wrt array y True values
