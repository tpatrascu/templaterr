#!/usr/bin/env python

import sys
import yaml
from mako.template import Template
from mako.runtime import Context
from mako import exceptions
from StringIO import StringIO
import pprint

data = []
if len(sys.argv) > 0:
	data = yaml.load(open(sys.argv[1]))
else:
	print "Usage: cat tplfile | " + sys.argv[0] + " mappings.yml > outfile"
	sys.exit()

templatelist = [x for x in sys.stdin]
templatestring = ''.join(templatelist)

mytemplate = Template(templatestring)
buf = StringIO()
ctx = Context(buf, data=data)

# prints exception and the output text up to where it was able to render it
try:
	mytemplate.render_context(ctx)
except:
	print(exceptions.text_error_template().render())

print(buf.getvalue())