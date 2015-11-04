from sys import argv

script, filename = argv

print "Now I'm going to open the file %r." % filename
txt = open(filename)

print "These are the content of file %r:" % filename
print txt.read()

print "Now I'm going to close the file."
txt.close()