#########################################################################################################
#########################################################################################################
#Using filter() donot use loop

#Q.34- Program to print only even numbers in the range 1-50

def even(number):
    return number%2==0
print(list(filter(even,range(1,50))))


#Q.35- Program to print only odd numbers in the range 1-50

def even(number):
    return number%2!=0
print(list(filter(even,range(1,50))))


#Q.36- Build a list with only even with even length string using filter func

names = ['apple','google','yahoo','facebook','yelp','flipkart','gmail','instagram','microsoft']
def enames(string):
    return len(string)%2==0
print(list(filter(enames,names)))


#Q.37- Returns the string if the string is starting from vowel character

names = ['laura','steve','bill','james','bob','greig','scott','alex','ive']
def vowel(names):
    return names[0] in 'aeiou'
print(list(filter(vowel,names)))


#Q.38- Program to return only positive values in the list

numbers = [-2,-1,0,1,2]
def pos(num):
    return num>=0
print(list(filter(pos,numbers)))

#Q.39- Program to print prime numbers from 1-50

def prime_num(num):
    if num<=1:
        return num
    else:
        for d in range(2,num):
           if num%d==0:
              return num
              break
           else:
              return num
              break
print(list(filter(prime_num,range(1,50))))

#Q.40- Program to extract only negative numbers from the list

numbers = [-2,-1,0,1,2]
def pos(num):
    return num<0
print(list(filter(pos,numbers)))



######################################################################################################
######################################################################################################
#Using map()  donot use loop

#Q.41- WAP to square and cube every number in a given list of integers

numbers=[1,2,3,4,5]
sc = lambda num : (num **2 , num **3)
print(list(map(sc,numbers)))

#Q.42- WAP to find if a given string starts with a given characher

names = ['laura','steve','bill','james','bob','greig','scott','alex','ive']
char='b'
def a_start_char(names):
    return names[0] in char
print(list(map(a_start_char,names)))

###############################################################################################
#Q.43- WAP to convert negative numbers in a given list to positive numbers

num=[-1,-2,-3,-4,-5]
def ntop(num):
        return(abs(num))
print(list(map(ntop,num)))


#Q.44- WAP to return a list of elements raised to the power of their indices

l=[1,2,3,4,5]
def func(num):
    index,item = num  #Unpacking
    return(item **index)
print(list(map(func,enumerate(l))))

#Q.45- WAP to calculate the sum of the positive and negative numbers of a given list

l=[1,2,3,-4,-6,8]

pos = lambda num : num > 0
neg = lambda num: num < 0
pos_sum = sum(list(filter(pos,l)))
neg_sum = sum(list(filter(neg,l)))
print(pos_sum,neg_sum)