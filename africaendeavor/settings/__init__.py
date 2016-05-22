from .base import *

try:
	from .local import *
	live = False
	print "woooow"
except:
	live = True

if live:
	from .production import *