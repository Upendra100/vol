#Q.1- Sort a list in reverse order=====================================

words=['hello', 'this', 'is', 'python']
print(words[::-1])


#Q.2- Short a list on their length ===========================================

words=['hello', 'this', 'is', 'python']
rev=sorted(words, key=len)
print(rev)


#Q.3- Sort the list based on the first character of each element ====================================

names=['apple','google','yahoo','amazon','facebook','instagram','microsoft','zomato']
names.sort()
print(names)


#Q.4- Sort the list based on the last character of each element ====================================

names=['apple','google','yahoo','amazon','facebook','instagram','microsoft','zomato']
names.sort(key=lambda item:item[-1])
print(names)


#Q.5- Sort the dictionary based on the key =======================================

prices = {'ACME':45.23, 'APPL':612.78, 'IBM':205.55, 'HPQ':37.20, 'FB':10.75}
d=sorted(prices.items(),key=lambda item:item[0])
print(d)


#Q.6- Sort the dictionary based on the value =======================================

prices = {'ACME':45.23, 'APPL':612.78, 'IBM':205.55, 'HPQ':37.20, 'FB':10.75}
d=sorted(prices.items(),key=lambda item:item[-1])
print(d)


#Q.7-sort the dictionary based on the length of key ===============================

prices = {'ACME':45.23, 'APPL':612.78, 'IBM':205.55, 'HPQ':37.20, 'FB':10.75}
d=sorted(prices.items(),key=lambda item:len(str(item[-1])))


#Q.8 -sort the dictionary based on the length of value ===============================

prices = {'ACME':45.23, 'APPL':612.78, 'IBM':205.55, 'HPQ':37.20, 'FB':10.75}
d=sorted(prices.items(),key=lambda item:len(str(item[-1])))
print(d)


#Q.9- sort the dictionary based on the last char of the key/value =========================

prices = {'ACME':45.23, 'APPL':612.78, 'IBM':205.55, 'HPQ':37.20, 'FB':10.75}
d=sorted(prices.items(), key=lambda item:item[0][-1])
print(d)


#Q.10- sort the dictionary based on the first char of the key/value =========================

prices = {'ACME':45.23, 'APPL':612.78, 'IBM':205.55, 'HPQ':37.20, 'FB':10.75}
d=sorted(prices.items(), key=lambda item:item[0])
print(d)


#Q.11- Write a function that accepts two string and returns True if the two strings are Anagrams if each other

word1='silent'
word2='listen'
def check(word1, word2):
    if (sorted(word1) == sorted(word2)):
        return("This string is Anagram")
    else:
        return("This string is not Anagram")
print(check(word1, word2))


#Q.12- Grouping Anagrams =================

words=['eat','ate','tea','hello','silent','listen']
d={}

for word in words:
    key=''.join(sorted(word))
    if key not in d:
        d[key]=[word]
    else:
        d[key].append(word)
print(d)


#Q.13- What is the difference between defaultdict and normal dict ==============



#Q.14- Program to print all the largest number in a list ==================

list=[1,3,7,9,4,9]
largest=0
for l in list:
    if l>largest:
        largest=l
for l in range(0,len(list)):
    if largest==list[l]:
        print(list[l])



#Q.15- Print longest non repeated word in sentence =============

sentence='hello python is programming language and programmin is fun'
words=sentence.split()
longest=''
for word in words:
    if len(word) > len(longest) and words.count(word) == 1:
        longest=word
print(longest)


#Q.16- Print longest word in sentence =====================

sentence='hello python is programming language and programmin is fun'
words=sentence.split()
rev=sorted(words, key=len)[-1]
print(rev)


#Q.17- Print largest number in the list================================

list=[1,3,7,9,4]
largest=0
for l in list:
    if l>largest:
        largest=l
print(largest)


#Q.18- Print shortest word in sentence ==================

sentence='hello python is programming language and programmin is fun'
words=sentence.split()
rev=sorted(words, key=len, reverse=True)[-1]
print(rev)


#Q.19- Print all the shortest word in sentence =====================

sentence='hello is python is programming language and programming is fun'
words=sentence.split()
allsmallest=words[0]
for word in words:
    if len(word) < len(allsmallest):
        allsmallest=word
for word in words:
    if len(allsmallest) == len(word):
        print(word)


#Q.20- Print all the largest word in sentence ====================

sentence='hello python is programming language and programming is fun'
words=sentence.split()
alllargest=''
for word in words:
    if len(word) > len(alllargest):
        alllargest=word
for word in words:
    if len(alllargest) == len(word):
        print(word)


#Q21.- Print least number in the list ==========================

num=[5,7,4,2,7,8]
print(sorted(num)[0])


#Q.22- Print all the least number in the list =================

num=[5,7,4,2,7,8,2]
small = num[0]
for i in num:
    if i<small:
        small=i
for i in range(0,len(num)):
    if small == num[i]:
        print(num[i])




#########################################################################################################
#########################################################################################################         
# Using Comprehension

#Q.23- Building a list of prime nubmers from 1-50

num=5
      
res=[num%i for i in range(2,num)]
      
all(res)

#Q.24- Reverse the item of a list if the item is of odd length string otherwise keep the item as is:
# names={'apple','google','yahoo','facebook','yelp','flipkart','gmail','instagram','microsoft'}

rev_odd=[name if len(name)%2!=0 else name for name in names]
print(rev_odd)


#######################################################################################################
#######################################################################################################
#Using lambda()
#we do not use loop in lambda function


# Q.25- WAP to create a lambda function that adds 15 to a given number passed

num_add = lambda num : (num+15)
print(num_add(15))


#Q.26- Lambda function to square and cube of any number

sc = lambda num : (num **2 , num **3)
print(sc(5))


#Q.27- Create a lambda function that multiply of two arguments

mul= lambda num1,num2 : (num1*num2)
print(mul(5,6))


#Q.28- Program to add 2 numbers

add = lambda num1,num2 : num1+num2
print(add(10,20))

#Q-29- Program to solve the expression a **2 + b **2 + 2 * a * b

for1 = lambda num1,num2 : (num1 **2 + num2 **2 + 2*num1*num2)
print(for1(5,6))


#Q.30- Program to solve the expression 2*a +3*b +4*c

for2 = lambda num1,num2,num3 : (2*num1 + 3*num2 + 4*num3)
print(for2(10,20,30))

#Q.31- Program to return last element of any sequence

def last_seq(sentence):
    words=sentence.split()
    return words[-1]

s_q = lambda sentence : last_seq(sentence)
print(s_q("hello this is python language"))


#Q.32- Program to check if the number is even or odd

def even_odd(num):
    if num%2==0:
        return(f"{num} is even")
    else:
        return(f"{num} is odd")
eo = lambda num : even_odd(num)
print(eo(10))


#Q.33- Program to check if the string is palindrome or not

palindrome= lambda word : word==word[::-1]
print(palindrome('malayalam'))