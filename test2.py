
from owlApiv2 import *

# the first example

# define domainName and owlPath
domainName = "testKG"
owlPath = " "

# dismantling owl
header, opList, dpList, classesList, indsList, footer = readOwl(owlPath, domainName)

# assemble owl
generateOwl(header, opList, dpList, classesList, indsList, footer, domainName)