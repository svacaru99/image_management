#!/usr/bin/env python
import os,sys
dirs=[ r for r,s,f in os.walk(".") if r != "."]
for i in dirs:
    os.makedirs(os.path.join(sys.argv[1],i)) 
    
# Command Line Usage
# python -c 'import os,sys;dirs=[ r for r,s,f in os.walk(".") if r != "."];[os.makedirs(os.path.join(sys.argv[1],i)) for i in dirs]' ~/new_destination
