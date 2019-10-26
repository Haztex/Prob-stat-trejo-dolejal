#!/usr/bin/env python
# coding: utf-8

# ## SUMMARY OF READING PYTHON 3

# In the first part of the reading it tells us about how to create comments and why they are important in coding.

# Comments are used to tell you what to do in the code, also they are used to disable temporary parts of your code.

# ## Example of Comments 1.1

#  #Hi, this is a comment, you must type '#' before any comment in your code if you don't, the program will give you an error.

# In[ ]:


#This is a comment


# If you want to comment multiple lines, you must put # in front of each line

# ## - How to place a text in the code

# Sometimes you want to place a text showing a function of a process in the code, you must use the function print with a variable or if you don't have defined variables, you can write text between quotation marks.

# ## - Examples of text

# In[4]:


# Example 1.1 text with a defined variable (This is a comment)
x = "Hello World"

print(x)


# In[5]:


# Example 1.2 text without defined variable (This is a comment)
print ("Hello world")


# ## Numbers and Math in Python 3

# Python has a lot of math symbols, here are some of them.

# In[8]:


# + plus
# - minus
# / slash
# * asterisk
# % percent
# < less-than
# > greather-than
# <= less-than-equal
# >= greather-than-equal


# A basic example could be:

# In[9]:


print ("What is 3 + 2?", 3 + 2)
print ("What is 5 - 7?", 5 - 7)


# Also you can do multiple operations, here is other example:

# In[11]:


print("I will now count my chickens:")
print("Hens", 30 + 25 / 6)
print("Roosters", 150 - 45 * 6 % 3)


# ## Variables and Names

# In programming a variable is nothing more than a name for something, for example you can name "High 1" as "H1", Programmers use these variables to make easier the reading of the code.

# ## Example Variables 1.1

# In[12]:


cars = 100
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
print("There are", cars, "Cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today.")
print("We have", passengers, "to carpool today.")


# ## More Variables
# 

# 
# A string is how you make something what your program might give to a human, you can print those strings, save strings to files or  send strings to web servers. 
# 
# "Format String" is basically the use of "double-quotes" around a piece of text you have been making.

# There are some embed variables inside a string by using a special {} sequence and then put the variable inside the those characters {}, you must start writing the letter f that ask python to put variables in there.

# ## Example of Variables 1.2

# In[15]:


my_name = 'Emerson'
my_age = 19
my_height = 1.83 #Meters tall
my_weight = 80 #lbs
my_eyes = 'brown'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}")
print(f"He's {my_height} meters tall")
print(f"He's {my_weight} kilos heavy")
print(f"He's got {my_eyes} and {my_hair} hair")
print(f"He usually clean your teeth in order to have it {my_teeth}")


# ## Strings and Text

# You already now how to make an string at this point you should know that strings are a bit of text that you want to display for something and in order to create an string you need to write something in simple-quotes or doble-quotes, Now but we are going to make some complex strings. 
# 
# Note: Strings can contain any number of variables that are in your python script.

# In[41]:


types_of_food = 5
x = f"There are {types_of_food} types of food."

binary = "binary"
do_not = "Don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"i said: {x}")
print(f"I also said: '{y}'")

hilarious = False

joke_evaluation = "Isn't that real"
print(joke_evaluation.format(hilarious))

w = "My father told me when i was just a child"
e = " Live a life that you will remember"

print(w + e)


# ## More Printing

# This is a compilation of the last 6 exercises and this is basic, here we show you how to print a lot of variables in 1 text as last 6 excercises.

# In[28]:


print("I want a car")
print("I deserve it for my grades at University")

L1 = "C"
L2 = "A"
L3 = "R"

print(L1 + L2 + L3)


# ## Complex Printing

# Here we are going to see how to do a more omplicated formatting of a string.

# In[32]:


formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format("green", "blue", "yellow", "red"))
print(formatter.format(formatter, formatter, formatter, formatter))


# Formatter in this example is a function that help us to turn the formatter into variable into other strings.

# ## Printing 

# In[35]:


days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)


# ## Magic? What was that?

# In the last excercise you saw a backslash character encoding different type of characters into a string, that is new and also is important for programming in python, you also know about the single-quote or double-quote inside the string. Here is some examples of uses of backlash.

# In[40]:


hi = "\t Hi"
dog = "Not\Here"
sep = "Hi \ we \ are \ distanced"
sad = """
I like these songs:
\t* Rich & Sad - Post Malone
\t* Goodbyes - Post Malone
\t* Saint-tropes - Post Malone

"""

print(hi)
print(dog)
print(sep)
print(sad)


# In[42]:


#Emerson Trejo Dolejal 3A
#Jose Alfredo Hernandez Melendez 3A


# In[ ]:




