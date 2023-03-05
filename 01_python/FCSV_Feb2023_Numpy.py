import numpy as np

arr = np.array([1, 2, 3])
print(arr)
print(type(arr))


print(arr.ndim)
print(arr.dtype)

#float array
arr_float = np.array([1, 2, 3], dtype=np.float64)
print(arr_float.dtype)


#array 2d
arr_2d = np.array(
    [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
     ])
print(arr_2d.ndim)

print(arr_2d)
print(arr)


arr_3d = np.array(
    [
     [
      [1, 2, 3],
      [4, 5, 6]
      ],[
      [7, 8, 9], 
      [10, 11, 12]
          ] 

     ])
          
print(arr_3d)
print(arr_3d.ndim)



print(arr.shape)
print(arr_2d.shape)
print(arr_3d.shape)

#(satr, sotoun, omgh!)

#zero array
arr_zero = np.zeros((2, 3), dtype=np.int32)
print(arr_zero)


#one array
arr_one = np.ones((2, 3, 4), dtype=np.int32)
print(arr_one)


# arange(start, end, step)
a = np.arange(1, 10, 2)
print(a)
print(type(a))

#linspace
b = np.linspace(1, 2, 5)
print(b)


#indexing & slicing
arr_1d = np.array([0, 1, 2, 3, 4, 5, 6])
print(arr_1d[0]) #0
print(arr_1d[4]) #4
print(arr_1d[-1]) #6


arr_1d_slicing = arr_1d[2:5]
print(arr_1d_slicing)


arr_2d = np.array([
    [1, 2, 3], 
    [4, 5, 6]
    ])

print(arr_2d.shape)
print(arr_2d[1, 1])
arr_2d_slicing = arr_2d[0:1,0:2]
print(arr_2d_slicing)



arr_3d = np.array([
    [
     [1, 2], [3, 4], [5, 6]
     ], 
    [
     [7, 8], [9, 10], [11, 12]
     ]
    ])

print(arr_3d.shape)
print(arr_3d[0, 0, 1])


# View , Copy!
a = np.array([
    [80, 81, 82], [83, 84, 85]
    ])


b = a[0:, 0:2]
c = a[0:, 0:2].copy()
#print(a)
#print(b)
b[0 , 0] = 0
c[0 , 0] = 0
print(b)
print(c)
print(a)


#add
i = np.array([
    [1, 2], [5, 6]
    ])


j = np.array([
    [5, 10], [25, 30]
    ])


#k = i + j
s = np.add(i, j)
h = np.subtract(i, j)
v = np.multiply(i, j)
d = np.divide(i, j)

print(s)
print(h)
print(v)
print(d)







