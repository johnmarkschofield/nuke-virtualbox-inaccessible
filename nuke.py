#!/usr/bin/python

import sys


import commands

status, output = commands.getstatusoutput('vboxmanage list vms')
if status != 0:
    print('ERROR: "vboxmanage list vms" failed.')
    print('Status was %s and output was %s' % (status, output))
    sys.exit(10)

if len(output) == 0:
    print('No inaccessible VMs found')
    sys.exit(0)

print('Removing inaccessible VMs:')
for aline in output.split('\n'):
    name = aline.split(' ')[0]
    if "inaccessible" not in name:
        continue
    guid = aline.split(' ')[1]
    status, output = commands.getstatusoutput('vboxmanage unregistervm %s' % guid)
    if status != 0:
        print('ERROR: "vboxmanage unregistervm %s" failed.' % guid)
        print('Status was %s and output was %s' % (status, output))
