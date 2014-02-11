import hashlib

lorem = '''Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam nonummy nibh.'''

h = hashlib.sha1()
h.update(lorem)
print h.hexdigest()
