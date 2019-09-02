#!/usr/python
#
# A company has an error reporting process that keeps track of the 
# SKU (Stock Keeping Unit) number , whenever a customer returns it.
# file is just a list of numbers between 1 and 30
# You have been asked to generate a report on
# which SKUs were returned, and how many retruns there were
# To test your code, we will generate 100 returns, with SKU numbers between
# 1 and 30
#generate 100 random numbers between 1 and 30
import random
# initialize the SKU list to be empty
skus =[]
#print range(0,100)

for i in range(0,100):
# generate a random number between 0 and 1, and turn it into a number between
# 1 and 30 
    skus.append( int(random.random() *30 + 1))
print" The skus that were returned this month are:"
print skus
print
# Sort the SKUs so they are in ascending order
skussorted=skus.sort()
print "SKUs sorted"
print skus

# Now go through the list of sorted skus and build dictionary of 
# skus and how many duplicates there are
# create an empty dictionary called skudict
skudict=dict()
# loop through the sku list
for i in skus:
# if sku i is in the dictionary, add 1 to the count
    if i in skudict:
       skudict[i] += 1
    else:
        skudict[i] = 1;
# print out the skus and the count of returns
for i in  skudict:
     print i, skudict[i]

skudict.sort(key=lambda tup1: tup1[1], reverse=True)
print skudict

