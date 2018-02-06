# Python basics

## Input and Output


```python
print ("Python is really a great language,", "isn't it?")
print ("bharat",end=" ")
```
end=" " means do not print newline at the end instead print " ".


```python
x=input("Enter data:")
```

Input() functions read data from keyboard as string,

```python
object = open(file_name [, access_mode][, buffering])
onject.tell()
object.seek(offset[, from])
object.read([count])
object.write(string)
object.close()
```
use "r+" access mode .

```python
file.closed
file.mode
file.name
```
attributes related to a file object

```python
os.rename(current_file_name, new_file_name)
os.remove(file_name) 
os.mkdir("newdir") 
os.chdir("newdir")
os.getcwd() #gives fully qualified path 
os.rmdir('dirname') #it can only remove empty directory 
```
**import os** is necessary is to use all these functions


```python
```

```python
```


## Numbers 


## IF else 
Python programming language assumes any non-zero and non-null values as TRUE, and
any zero or null values as FALSE value.

```python

if expression: statement(s) # one-line if

if expression1:
	statement(s)
elif expression2:
	statement(s)
elif expression3:
	statement(s)
else:
	statement(s)
```

## Loops

```python


while expression: statement(s) # one-line if

while expression:
	statement(s)

while expression:
	statement(s)
else:
	statement(s)

for iterating_var in sequence:
	statements(s)

len(data_structure) #returns the nuber of element in data structure

```
If the else statement is used with a for loop, the else block is executed only if for
loops terminates normally (and not by encountering break statement).


## Functions


```python
def functionname( parameters ):
	"function_docstring"
	function_suite
	return [expression]


def func( list ):
	"This func will not cause any change in list2"
	list = [x,y,z] # This would create a new local parameter instead of modifing old one.
	return
list = [x,y,z]
func( list )
```
All parameters (arguments) in the Python language are passed by reference. It means if
you change what a parameter refers to within a function, the change also reflects back in
the calling function.


```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```


```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

## Strings 

Python treats single quotes the same as double quotes. SO there is no **char** type.
it follows the usal slicing scheme.


```python
str='string'
str.upper() #returns  all the characters to upper case
str.lower() #converts all the characters to lowercase
str.capitalize() #returns a copy of the string with only its first character capitalized.
str.center(width[, fillchar]) # returns string that is at least width characters wide, created by padding the string with the character fillchar (default is a space).
str.count(sub, start= 0,end=len(string)) #returns the number of occurrences of substring sub in the range [start, end].
str.encode(encoding='UTF-8',errors='strict') #returns an encoded version of the string.
Str.decode(encoding='UTF-8',errors='strict') #returns the decoded version of string
str.endswith(suffix[, start[, end]]) # It returns True if the string ends with the specified suffix
str.expandtabs(tabsize=8) # returns a copy of the string in which tab characters have been added using spaces.
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```

```python
```



## Arithmatic Operation


## Loops

```python
while condition:
	statement1
	statement2
	condition update 
```

```python
for x in a:
	statement1
	statement2
```


## data structure 

```python 
range(a,l,d)
```
it generate a AP : a,a+d, ..... a+nd such that a+nd <= l



## Lists

```python

list2 = [x, y, z ];
list.append(x)
list.extend(iterable)
list.insert(i, x)
list.remove(x)
list.pop([i])
list.clear()
list.index(x[, start[, end]])
list.count(x)
list.sort(key=None, reverse=False)
list.reverse()
list.copy()
del list[index] #if we know the index of element to be deleted
cmp(list1,list2)
len(list)
max(list)
min(list)
list(seq) #typecasting other sequence to list
```
list is that items in a list need not be of the same type.
you can perform slicing operatio on list and strins
Lists respond to the + and * operators much like strings;

## Stack 
```python
list.append(x) #stack.push(x)
list.pop(x) #stack.pop()
```

## Sets

```python
myset = {x, y} # Directly assigning values to a set
myset = set()  # Initializing a set
myset = set(['a', 'b']) # Creating a set from a list
myset.add('c')
myset.update(iterable) # update() only works for iterable objects
myset.discard(x) # does not throw any error	
myset.remove(x)
a.union(b) # Values which exist in a or b
a.intersection(b) # Values which exist in a and b
a.difference(b) # Values which exist in a but not in b

```

## tuples

```python
tuple=(x,y,z)
tuple = (x,)
del tup #individual elements can not be deleted in tuple	
cmp(tuple1,tuple2)
len(tuple)
max(tuple)
min(tuple)
tuple(seq) #typecasting other sequence to list
```
Tuples respond to the + and * operators much like strings but result is a new tuple
sequences, indexing and slicing work the same way for tuples as they do for strings.
To write a tuple containing a single value you have to include a comma, even though there is only one value −

A tuple is a sequence of immutable Python objects. 














