from sys import argv
from os.path import exists

script, from_file, to_file = argv

# Now we do copying with one line code.

open(to_file,'w').write(open(from_file).read())