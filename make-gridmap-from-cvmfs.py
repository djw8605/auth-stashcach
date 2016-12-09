#!/usr/bin/python

import subprocess
import re
import xattr

# Run the command "attr -qg authz /cvmfs/ligo.osgstorage.org"
xattr_out = xattr.get('/cvmfs/ligo.osgstorage.org', 'user.authz')

for line in xattr_out.split("\n"):
    if ('"' in line) or (not line.startswith('/')):
        continue
    print '"' + line + '" ligo'

