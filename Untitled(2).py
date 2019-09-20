
# coding: utf-8

# In[91]:

def ins(x,num):
    '''
    objective : To insert the element in appropriate position in a  list
    input     : a list
                a number to be inserted
    output    : new sorted list
    '''
    '''
    Approach : By comparing the number with each element of list and then place it in suitable position  
    '''
    x.insert(0,num)
    sor(x)
    
   


# In[94]:

def sor(x,i=0):
    '''
    objective : To sort a list
    input     : a list
    output    : new sorted list
    '''
    '''
    Approach : By swapping comparing the number with each element of list and then place it in suitable position  
    '''
    
    if i+1<len(x):
        if x[i] > x[i+1]:
            x[i],x[i+1] = x[i+1],x[i]
            sor(x,i=i+1)

        


# In[98]:

a=[1,2,3,5,6]
ins(a,3)
a


# In[ ]:




# In[ ]:



