
from urllib import urlopen
import csv

u = "http://mta.info/developers/data/nyct/turnstile/turnstile_130209.txt"
reader = csv.reader(urlopen(u))

# reader is an object...
print type(reader)

# ... and one of its attributes is the number of lines we've read so far
print reader.line_num

# From reader we can grab rows of data one at a time...
row = reader.next()
print row
print reader.line_num

# We see each row is a list, with the individual data values separated
# by commas in the file are now separate list elements. The subway
# rows we want correspond to "R173" in the first and "R159" in the 
# second element

reader = csv.reader(urlopen(u))
ourdata = []

for row in reader: 
    if row[0]=="R173" and row[1]=="R159":
       ourdata.append(row)

print ourdata

# Tell me about each row in the file -- Do they all have
# the same number of entries? Is it one row per turnstile?

# How many turnstiles are there at our stop?

# Tell me about the data for each turnstile? What dates do they cover?

# Is this form of the data easy or hard to work with? Come up with
# a question you might ask or a display you might make and think about
# how easy it is to pull the data in this form.


