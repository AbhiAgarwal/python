# MD5 Example
import hashlib

lorem = '''Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh.'''

# You've to first create the hash object, and then add the data and then call digest() or hexdigest() to print it
h = hashlib.md5()
h.update(lorem)
print h.hexdigest() # or you can do h.digest(), but it is in a binary digest value
