
# coding: utf-8

# In[77]:

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
    
   


# In[78]:

def sor(x,i=0):
    '''
    objective : To sort a list
    input     : a list
    output    : new sorted list
    '''
    '''
    Approach : By swapping comparing the number with each element of list and then place it in suitable position  
    '''
    
    if x[i] > x[i+1]:
        x[i],x[i+1] = x[i+1],x[i]
        sor(x,i=i+1)
    
        


# In[80]:

a=[1,2,3,5,6]
ins(a,10)
a


# In[ ]:



