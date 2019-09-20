#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[4]:


print(random.randint(0,4))


# In[5]:


print(random.randint(0,4))


# In[6]:


print(random.randint(0,4))


# In[9]:


part1 = ["Putin", "Hillary", "Obama", "Fake News,", "Mexico", "Arnold Schwarzenegger", "The Democrats"]
part2 = ["not talent,", "on the way down, ", "reall poor numbers,", "nasty tone,", "looking like a fool"]
part3 = ["got destroyed by my ratings.", "rigged the election.", "had a much smaller crowd."]
part4 = ["So sad", "Apologize", "So true", "Media wont report", "Big troube", "Fantastic job", "Stay tuned"]


# In[16]:


best_words = [part1, part2, part3, part4]


# In[12]:


print(best_words)


# In[13]:


best_words[2]


# In[14]:


for part in best_words:
    print(part)


# In[32]:


sentence = []

for part in best_words:
    r = random.randint (0, len(part) - 1)
    sentence.append(part[r])

print(" ".join(sentence) + "!")


# In[ ]:




