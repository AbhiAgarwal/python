# http://www.skymind.com/~ocrow/python_string/
# method6 is the most efficient (in tested speed)
loop_count = 30

def method1(): # Naive appending
  out_str = ''
  for num in xrange(loop_count):
    out_str += `num`
  return out_str

def method2(): # MutableString class
  from UserString import MutableString
  out_str = MutableString()
  for num in xrange(loop_count):
    out_str += `num`
  return out_str

def method3(): # Character arrrays
  from array import array
  char_array = array('c')
  for num in xrange(loop_count):
    char_array.fromstring(`num`)
  return char_array.tostring()

def method4(): # Build a list of strings, then join it
  str_list = []
  for num in xrange(loop_count):
    str_list.append(`num`)
  return ''.join(str_list)

def method5(): # Write to a pseudo file
  from cStringIO import StringIO
  file_str = StringIO()
  for num in xrange(loop_count):
    file_str.write(`num`)
  return file_str.getvalue()

def method6(): # List comprehensions
  return ''.join([`num` for num in xrange(loop_count)])
