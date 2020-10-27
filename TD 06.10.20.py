Python 3.8.5 (v3.8.5:580fbb018f, Jul 20 2020, 12:11:27) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> print (value)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    print (value)
NameError: name 'value' is not defined
>>> 
>>> 
>>> 
>>> ddef is_palindrome(a):
	
SyntaxError: invalid syntax
>>> def is_palindrome(a):
	for i in range (len(a)//2) :
		if a [0] != a [-1]
		
SyntaxError: invalid syntax
>>> def is_palindrome(a):
	for i in range (len(a)//2) :
		if a [i] != a [-i-1]:
			return False
		return True
 assert is_palindrome("Bonjour") ==
 
SyntaxError: unindent does not match any outer indentation level
>>> def is_palindrome(a):
	for i in range (len(a)//2) :
		if a [i] != a [-i-1]:
			return False
		return True

	
>>> 
>>> 
>>> is_palindrome ("Bonjour")
False
>>> 
>>> def bubbleSort(liste_a_trier):
	for i in range (len(a)) :
		if len(a) > len( :
				 
SyntaxError: invalid syntax
>>> def bubbleSort(liste_a_trier):
	n=len(liste_a_trier)
	while n>0:
		for i in range (n-1):
			if liste_a_trier [i] > liste_a_trier [i+1]:
				liste_a_trier [i] , liste_a_trier [i+1] = liste_a_tier [i+1] , liste_a_trier [i]
			else:
				continue
		n-=1
	return liste_a_trier

>>> arr = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(arr)
SyntaxError: multiple statements found while compiling a single statement
>>> arr = [64, 34, 25, 12, 22, 11, 90]bubbleSort(arr)
SyntaxError: invalid syntax
>>> arr = [64, 34, 25, 12, 22, 11, 90]
>>> bubbleSort(arr)
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    bubbleSort(arr)
  File "<pyshell#35>", line 6, in bubbleSort
    liste_a_trier [i] , liste_a_trier [i+1] = liste_a_tier [i+1] , liste_a_trier [i]
NameError: name 'liste_a_tier' is not defined
>>> def bubbleSort(liste_a_trier):
	n=len(liste_a_trier)
	while n>0:
		for i in range (n-1):
			if liste_a_trier [i] > liste_a_trier [i+1]:
				liste_a_trier [i] , liste_a_trier [i+1] = liste_a_trier [i+1] , liste_a_trier [i]
			else:
				continue
		n-=1
	return liste_a_trier

>>> arr = [64, 34, 25, 12, 22, 11, 90]
>>> bubbleSort(arr)
[11, 12, 22, 25, 34, 64, 90]
>>> [11, 12, 22, 25, 34, 64, 90]
[11, 12, 22, 25, 34, 64, 90]
>>> def insertionSort(liste_a_trier):
	