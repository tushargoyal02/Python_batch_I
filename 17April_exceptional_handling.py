#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Exceptional handling
# exceptions  => unwanted condition => program terminate ( may give 
# different result)


# In[3]:


x=10
print("hello")
x/y
print("regex")


# In[8]:


x=10
x/y


# In[9]:


# try  , except

try:
    x=10
    print("hello")
    x/y
    print("regex")
except:
    print("Error occured")


# In[13]:


try:
    x=10
    print("hello")
    x/0
    print("regex")
except NameError:
    print("Error occured")


# In[14]:


try:
    x=10
    print("hello")
    x/0
    print("regex")
except NameError:
    print("Error occured")
    
except ZeroDivisionError:
    print("Zero Error occured")


# In[19]:


try:
    x=10
    print("hello")
    x/y
    print("regex")
except (NameError,ZeroDivisionError):
    print("Error occured")
except Exception:
    print("Other error handles")


# In[23]:


# to define the reason for the exception
try:
    x=10
    print("hello")
    x[0]
    print("regex")
except (NameError,ZeroDivisionError) as e:
    print("Error occured",e)
except Exception as e:
    print("Other error handles",e)


# In[25]:


try:
    x=10
    print("hello")
    
    try:
        x/y
    except:
        print("Error")
    
    print("regex")

except (NameError,ZeroDivisionError) as e:
    print("Error occured",e)


# In[29]:


try:
    x=10
    print("hello")
    x/0
    print("regex")

except (NameError,ZeroDivisionError) as e:
    print("Error occured",e)

else:
    print("hello tushar")


# In[32]:


try:
    
    x=10
    print("hello")
    print("regex")

except (NameError,ZeroDivisionError) as e:
    print("Error occured",e)

finally:
    print("hello tushar")


# In[ ]:





# In[36]:


# raise 
age=int(input("Enter a number: "))

try:
    if age<18:
        raise ValueError
    else:
        print("Age is more than 18")
except ValueError as e:
    print("Value error is handled")


# In[ ]:


# basic of Python
# data type
# conditional
# loops  for while  ( nested)
# list, tuple, dictionary, set
# functions
# argument in functions
# lambda functions
# lambda vs def functions
# high order  & first class functions
# File handling
# exceptional handling



