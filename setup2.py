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
''' returns an absolute path to file with homefolder are environment
    variables expanded, and without symlinks '''
    nouser = os.path.expanduser(file)
    novars = os.path.expandvars(nouser)
    nosym = os.path.realpath(nosym)
    return nosym

def get_src_dir():
''' returns the directory with the project's source '''
    # find path the setup script is run from
    run_dir = os.path.dirname(abspath(os.path.join(os.getcwd(), sys.argv[0])))
    
    # get the source directory for the project
    src_dir = abspath(raw_input("You have run the setup script from `%s`. If this is where I can find the project source, press enter. Otherwise tell me where I can?"%run_dir) or run_dir)
    while not os.path.exists(src_dir):
        src_dir = abspath(raw_input("I couldn't find the project source in `%s`. Maybe you misspelled the path or moved it elsewhere?"%src_dir))
        