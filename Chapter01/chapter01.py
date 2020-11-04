#!/usr/bin/env python
# coding: utf-8

# # Scientific Computing with Python (Second Edition)
# ## Chapter 01

# *We start by importing all from Numpy. As explained in this chapter the examples are written assuming this import is initially done.*

# ## 1.1 Some Installation and configuration instructions

# *No code in this book section*

# ## 1.2 Program and program flow
# ### 1.2.1 Comments

# In[ ]:


# This is a comment of the following statement
a = 3  # ... which might get a further comment here  


# ## 1.3 Basic Datatypes
# ### 1.3.1 Numbers

# In[ ]:


from numpy import *


# In[ ]:


2 ** (2 + 2) # 16


# In[ ]:


1j ** 2 # -1


# In[ ]:


1. + 3.0j


# ### 1.3.2 Strings

# In[ ]:


'valid string'


# In[ ]:


"string with double quotes"


# In[ ]:


"you shouldn't forget comments"


# In[ ]:


'these are double quotes: ".." '


# In[ ]:


"""This is
 a long,
 long string"""


# ### 1.3.3 Variables

# In[ ]:


x = [3, 4] # a list object is created

y = x # this object now has two labels: x and y

del x # we delete one of the labels
del y # both labels are removed: the object is deleted

x = [3, 4] # a list object is created
print(x)


# ### 1.3.4 Lists

# In[ ]:


L1 = [5, 6]

L1[0] # 5


# In[ ]:


L1[1] # 6


# *Uncomment the next line in order to see the error*

# In[ ]:


# L1[2] # raises IndexErrorL1 = [5, 6]


# In[ ]:


L1[0] # 5


# In[ ]:


L1[1] # 6


# *Uncomment the next line in order to see the error*

# In[ ]:


# L1[2] # raises IndexError


# In[ ]:


L2 = ['a', 1, [3, 4]]


# In[ ]:


L2[0] # 'a'


# In[ ]:


L2[2][0] # 3


# In[ ]:


L2[-1] # last element: [3,4]


# In[ ]:


L2[-2] # second to last: 1


# In[ ]:


print(list(range(5))) # returns [0, 1, 2, 3, 4]


# In[ ]:


len(['a', 1, 2, 34]) # returns 4


# In[ ]:


len(['a',[1,2]]) # returns 2


# In[ ]:


L = ['a', 'b', 'c']

L[-1] # 'c'


# In[ ]:


L.append('d')

L # L is now ['a', 'b', 'c', 'd']


# In[ ]:


L[-1] # 'd'


# ### 1.3.5 Operations on Lists

# In[ ]:


L1 = [1, 2]
L2 = [3, 4]
L = L1 + L2 # [1, 2, 3, 4]
L


# In[ ]:


L = [1, 2]
3 * L # [1, 2, 1, 2, 1, 2]


# ### 1.3.6 Boolean Expressions

# In[ ]:


2 >= 4  # False


# In[ ]:


2 < 3 < 4 # True


# In[ ]:


2 < 3 and 3 < 2 # False


# In[ ]:


2 != 3 < 4 or False # True


# In[ ]:


2 <= 2 and 2 >= 2 # True


# In[ ]:


not 2 == 3 # True


# In[ ]:


not False or True and False # True!


# ## 1.4 Repeating statements with loops

# In[ ]:


L = [1, 2, 10]
for s in L:
    print(s * 2) # output: 2 4 20


# In[ ]:


my_list = [...] # define a list
for elt in my_list:
    ...   #do_something
    ...   #something_else
print("loop finished") # outside the for block


# ### 1.4.1 Repeating a task

# In[ ]:


n = 30
for iteration in range(n):
    ... # a statement here  gets executed n times


# ### 1.4.2 break and else

# In[ ]:


x_values=[0.5, 0.7, 1.2]
threshold = 0.75
for x in x_values:
    if x > threshold:
        break
    print(x)


# In[ ]:


x_values=[0.5, 0.7]
threshold = 0.75
for x in x_values:
    if x > threshold:
       break
else:
    print("all the x are below the threshold")


# ##  1.5 Conditional statements

# In[ ]:


x = 5
if x >= 0:
    print(x)
else:
    print(-x)


# ## 1.6 Encapsulating code with functions

# In[ ]:


def f(x):
    return 2*x + 1


# In[ ]:


f(2) # 5


# In[ ]:


f(1) # 3


# ## 1.7 Understanding Scripts and modules

# In[ ]:


z = []
for x in range(10):
    if f(x) > pi:
        z.append(x)
    else:
        z.append(-1)
print(z)


# ### 1.7.1 Simple modules - collecting functions

# *The next command requires that the file smartfunctions.py exists in the same folder as this file*

# In[ ]:


exec(open('smartfunctions.py').read())


# ### 1.7.2  Using modules and namespaces

# *The next commands require that the file smartfunctions.py exists in the same folder as this file*

# In[ ]:


import smartfunctions
print(smartfunctions.f(2))      # 5


# In[ ]:


from smartfunctions import g    #import just this function
print(g(1)) # 0


# In[ ]:


from smartfunctions import *    #import all
print(h(2)*f(2))                # 1.0


# ## 1.8 Python Interpreter

# In[ ]:


def f(x):
    return y**2  
a = 3   # here both a and f are defined


# *To see the runtime error you have to uncomment the next command*

# In[ ]:


# f(2) # error, y is not defined


# ## 1.9 Summary

# *No code in this book section*
