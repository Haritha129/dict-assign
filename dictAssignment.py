# Delete a list of keys from a dictionary
''''sample_dict={"name":"hari","age":22,"salary":35000}
keys=["name","salary"]
for i in keys:
   sample_dict.pop(i)
print(sample_dict)'''

# count the frequency of each character in a given string using a dictionary?
'''g='haritha'
v={}
for i in g:             
   if i not in v:       
       v[i]=1   
   else:                                                                    
      v[i]+=1      
print(v)     
'''
# swap keys and values in a dictionary
'''v={"name":"hari","age":22,"salary":35000}
res={}
for keys,values in v.items():
   res[values]=keys
print(res)'''

# write a program to sum all the values in a dictionary
'''v={'a':10,'b':20,'c':40}
sum=0
for i in v:
     sum+=v[i]
print(sum)    '''            

# created a nested dictionary for student details(name,roll,marks)
'''v={1:{'name':'haritha', 'rollno': '4e7', 'marks':505},
   2:{'name':'lakshmi','rollno':456,'marks':508}},
print(v)'''

# convert a dictionary to a list of tuples.
'''L={"L":15,"M":17,"N":19,"X":21,"Y":23,"O":25}
for x in L.items():
     print(x)'''
# 7. Write a program to store names as keys and their lengths as values. 
'''S=["python","developer","stack","java","c++"]
res={}
for x in S:
    res[x]=len(x)
print(res)'''

# 8. Create a dictionary for numbers 1 to 5, where the value is "even" if the number is even, and 
# "odd" if the number is odd 
M={'odd':1,'even':2,'odd':3,'even':4,'odd':5}
L={}
for i in range (1,6):
    if i%2==0:
        L[i]="even"
else:
       L[i]="odd"
print(L)

# 9. Create Reverse Word Dictionary 
# Given list of words: 
# words = ["cat", "dog", "bat"] 
# Create a dictionary with words as keys and their reversed strings as values 
words = ["cat", "dog", "bat"] 
L={}
for x in words:
    res=""
    for i in x:
        res=i+res
    L[x]=res 
print(L)                           


