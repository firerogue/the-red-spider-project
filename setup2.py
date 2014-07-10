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

# TODO: once script is complete move lots of stuff into pre-defined constants
# so that changes will be easier to make

import sys
import os, os.path
import subprocess
import argparse

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
    def is_src_root(path):
        if not os.path.exists(path)
          or not os.path.exists(os.path.join(path, 'src'))
          or not os.path.exists(os.path.join(path, 'src', 'rsshell.py'))
          or not os.path.exists(os.path.join(path, 'install'))
          or not os.path.exists(os.path.join(path, 'install', 'rsshell.py')):
            return True
    
    src_dir = abspath(raw_input("You have run the setup script from `%s`. If this is where I can find the project source, press enter. Otherwise tell me where I can?"%run_dir) or run_dir)
    while not is_src_root(src_dir):
        src_dir = abspath(raw_input("I couldn't find the project source in `%s`. Maybe you misspelled the path or moved it elsewhere?"%src_dir))
        
    # src_dir now contains a directory with src and install subfolders, with rsshell source and install directions respectively
    return src_dir

def main():
    print("Hello! welcome to the red spider project management script!")
    
    # build command line argument list
    parser = argparse.ArgumentParser(description="Red Spider Install Manager",
                                     usage="%(prog)s [-m|-i [-d]|-u]",
                                     )
    parser.add_argument('-m','--move', action='store_const', dest='action', const='move')
    parser.add_argument('-u','--uninstall', action='store_const', dest='action', const='uninstall')
    parser.add_argument('-i','--install', action='store_const', dest='action', const='install')
    parser.add_argument('-d','--default','--make-default', action='store_true')
    parser.add_argument('--dev', action='store_true')