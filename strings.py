#!/usr/bin/python
a_string = "another string"
my_string = 'my string'
print len(my_string)
print my_string.upper()
print "HELLO"[0]
print "This is %s. This is %s." % (my_string, a_string)

print "hi " +str(3)

def censor(text, word):
    l = len(word)
    r = '*'*l
    return text.replace(word, r)

print censor('What the flip is wrong?', 'flip')