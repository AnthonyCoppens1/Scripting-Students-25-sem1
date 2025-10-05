# %% [markdown]
# # Python basics week 03: class of 3/10
# working with packages --> numpy, pythonic code
# arrays, ...
# 
# Let's say you've got problems with packages --> https://www.dataquest.io/blog/install-pip-windows/

# %%
! pip install numpy

# %% [markdown]
# ## Importing Numpy

# %%
import numpy
import numpy as np
from numpy import arange

# %% [markdown]
# ## Creating arrays
# Arrays --> all elements have to be the same type, similar to c#

# %%
import numpy as np
list = [1,5,8,10,3]
print(list)

array = np.array(list)
print(array)

#list --> seen as a whole and can now be added completely twice
#array will store each element and multiply it.

print(list * 2)
print(array * 2)

list.append(2)
print(list)
#array.append(2) --> just doesn't work, because of fixed size

#1D arrays
print(np.arange(10)) #every number equivalent to indexes from 0 - 9
print(np.zeros(10)) #10 0's --> x amount of 0's
print(np.ones(10))
print(np.full(10,5))

print(np.random.randint(-5,6, 10)) #generates random numbers, low point, high point (not inc), amount
print(np.random.random(10)) #random floats in array of size x

# %% [markdown]
# ## Reshaping and converting arrays

# %%
import numpy as np
#for safety --> calling array again and giving it values
array = np.random.randint(-5,6,10)
print(array)
print(array.shape) #length
print(array.ndim) #number of dimensions of your array

print("array has number of datatype:", array.dtype)

array_float = array.astype('f') 
#astype converts from a type into the other
#i - integer / b - boolean / f - float / M - datetime / S - string / however words also work --> str, int, bool, float
print(array_float)
array_string = array.astype(str)
print(array_string)

#2D arrays
array_2D = np.reshape(array, (2,5))
print(array_2D)
print(array_2D.ndim)
print(array_2D.shape)

array_2D = np.reshape(array, (5,2))
print(array_2D)

#reshaping has to result in a perfect match --> cannot reshape into something that the original cannot be split by
#array_2D = np.reshape(array, (3,3))
#print(array_2D)

array_2D = np.reshape(array, (10,1)) #also possible
print(array_2D)

array_2D = np.reshape(array, (-1,5))
print(array_2D)


# %% [markdown]
# ## slicing arrays
# [start : end : step]
# - start = starting index
# - end = ending index (not included)
# - step = stepsize

# %%
import numpy as np
array = np.array([6, 8, 2, 9, 3, 1, 4, 7, 0, 5])
print(array)

print(array[1:5:1]) #[8 2 9 3]
print(array[1:5:])#default step is same as 1
print(array[1:5:2]) #[8 9]

print(array[0:5:1]) #[6 8 2 9 3]
print(array[:5:1]) #[6 8 2 9 3]

print(array[0::1]) #[6 8 2 9 3 1 4 7 0 5]
print(array[0:10:1])

#reverse
print(array[::-1])
print(array[::-2])

print(array[0:10:-1]) #shows nothing
print(array[10::-1]) #leave the end blank to do the full reverse, else you just add your index (not included)


# %% [markdown]
# ## Some extra work with arrays

# %%
a = np.arange(0, 10)
b = np.arange(9, -1, -1)
print(a,b)
print(a + b)
print(a - b)
print(a * b)
print(np.where(a % 2 == 0, a + 1, a)) #--> condition, x, y --> x if true, y if false

print(np.where(b > 5))
print(np.where(b > 5, b, 0))
print()

b = np.reshape(b, (2, 5))
print(b)
print()

print(b.sum(axis=0)) #sum of columns
print(b.sum(axis=1)) #sum of rows
print(b.cumsum(axis=1)) #cumulative sum of numbers, calculating then printing 1 at a time.

print()
print(a.sum())
print(a.min())
print(a.max())

print(np.sqrt(a))
print(np.sqrt(a.max()))

# %% [markdown]
# ### Exercise: It's magic time!!!
# Read in a 1D array and a number of rows! Convert the array to 2D, calculate the sum of each column and if all sums are equal --> provide a message saying: it's a magic table<br><br>
# 
# <b>input</b><br>
# 2 7 0 8 4 1 1 0 10<br>
# 3<br>
# <b>output</b><br>
# True
# <pre>
# 2 7 0<br>
# 8 4 1<br>
# 1 0 10<br>
# <i> 11 11 11</i> --> MAGIC TABLE
# </pre>

# %%
import numpy as np
s = input() # 2 7 0 8 4 1 1 0 10
array1D = np.array(s.split(" "))
array1D = array1D.astype(int)
rows = int(input())
col = int(len(array1D) / rows)

array = np.reshape(array1D, (rows, col))
print(array)

sums = np.sum(array, axis = 0) #0 = cols
print(sums)

total = np.sum(sums)
if total // rows == sums[0]:
    print("MAGIC TABLE")
else:
    print("NO MAGIC TABLE")








def generate():
    return list

def main():
    everything

if __name__ == "__main__":
    main()