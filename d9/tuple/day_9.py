"""'''
tuple
-----
*tuple is an data structure
*represented in ()
*ordered
*indexing
*slicing
*duplicate elements are allowed
*immutable(it can't change or edit the tuple)

x=(1,2,3,4,4)
x[0]=1
x[2]=3
x[-3]=2
x[1:3]=[2,3]
x[-1:-3]=[4,4]
x[::-1]=[4,4,3,2,1]
x.count(2)=1
x.count(4)=2

--------------------------------------------------------------------------------------------
'''
x=(1,2,3,4,5)
y=list(x)
print(y)#[1,2,3,4,5]
y.append(8)
x=tuple(y)
print(x)
print(type(x))

'''
--------------------------------------------------------------------------------------------
set
----
*data structure
*represented in {}
*no indexing
*unordered
*duplicates are not allowed
*True=1,False=0
*each item are unique in set
*mutable(we can edit set items)

'''
a={}
print(type(a))#it will show dict so

#to show type of empty set we have to give like
y=set()
print(type(y))#it will show set

#-----------------------------------------------
#add
#----
s={5,3,"33",True}
s.add(99)
print(s)

#remove
#------
s={5,3,"33",True}
s.remove(3)
s.remove(7)#it will show error(item not exist)
print(s)

#discard
#------
s={5,3,"33",True}
s.discard(3)
s.discard(7)#it will not show error ,it will print the set
print(s)#

"""
setA={"red","blue","green"}
setB={"yellow","blue","orange"}

print(setA)
print(setB)

#operations on set
#-----------------

#union
#-----
print(setA.union(setB))#{'orange', 'yellow', 'red', 'green', 'blue'}
print(setA.update(setB))#{'orange', 'yellow', 'red', 'green', 'blue'} same but it will assain to setA
print(setA)

#intersection
#------------
print(setA.intersection(setB)) #{'blue'}
setA. intersection_update(setB)
print(setA) # {'blue'}
print(setA.difference(setB)) # {'red', 'green'}
setA.difference_update(setB)
print(setA) # {'red'. 'green

#symmetric_difference
#--------------------
print(setA.symmetric_difference (setB)) #{'green', 'orange', 'red', 'yellow'}
setA.symmetric_difference_update(setB)
print(setA)#('green', 'orange', 'red', 'yellow')


#---------------------------------------------------------------------------------------------

#functions on set
#----------------

#superset
#---------
a={1,2,3,4,5,6}# a is superset of b
b={3,4}

#subset
#------
a={1,2,3,4,5,6}
b={3,4}#b is subset of a

a={1,2,3,4,5}
b={4,5}
c={7,8,9}

#issuperset
#----------

print(a.issuperset(b)) # True
print(b.issuperset(a)) # False

#issubset
#----------
print(b.issubset(a)) # True
print(a.issubset(b)) # False

#isdisjoint
#-----------
print(c.isdisjoint(b)) # True
print(a.isdisjoint(b)) #False

#--------------------------------------------------------------------------------------------









