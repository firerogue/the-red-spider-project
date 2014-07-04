#! /usr/bin/env python2
from __future__ import print_function

''' setup2.py
Initial setup script for the Red Spider Project, completely rewritten from the
ground up by Lior

Copyright 2012, 2013 Julian Gonggrijp
Copyright 2014       Lior Ramati
Licensed under the Red Spider Project License.
See the License.txt that shipped with your copy of this software for details.

A -q option to make it less verbose would probably be nice. Until we
have a dedicated 'update' command we'll need to run the setup every
time one of the commands has been changed on master.
'''

import sys
import os, os.path
import subprocess
import rsupdate

def abspath(file):
    nouser = os.path.expanduser(file)
    novars = os.path.expandvars(nouser)
    nosym = os.path.realpath(nosym)
    return nosym

def get_src_dir():
    run_dir = abspath(os.path.join(os.getcwd(), sys.argv[0]))
    
