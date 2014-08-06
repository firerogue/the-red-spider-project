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

def get_rsp_src_dir(src_arg):
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
            return False
        return True
    
    src_dir = abspath(src_arg or raw_input("You have run the setup script from `%s`. If this is where I can find the project source, press enter. Otherwise tell me where I can?"%run_dir) or run_dir)
    while not is_src_root(src_dir):
        src_dir = abspath(raw_input("I couldn't find the project source in `%s`\
            . Maybe you misspelled the path or moved it elsewhere?"%src_dir))
        
    # src_dir now contains a directory with src and install subfolders, with rsshell source and install directions respectively
    return src_dir

def main():
    ''' main is in charge of reading command line arguments, discerning the run
        mode, and passing the command line args to the run mode's main function '''
    print("Hello! welcome to the red spider project management script!")
    
    # build command line argument list
    parser = argparse.ArgumentParser(description="Red Spider Install Manager",
                                     usage="%(prog)s [-m|-i [-d]|-u]",
                                     epilog="These flags are provided for convenience. If left unsupplied, the program will request them during execution")
    # mode args
    # if more modes are added, they should get a command line option here
    # required: action='store_const', dest='action', and const=<function name>
    # the function is the mode's "main()" and accepts the parsed args object
    parser.add_argument('-m','--move', action='store_const', dest='action',
                        const=move, help="Move an installation from source to dest")
    parser.add_argument('-u','--uninstall', action='store_const', dest='action',
                        const=uninstall, help="Uninstall the project at source")
    parser.add_argument('-i','--install', action='store_const', dest='action',
                        const=install, help="Install the a copy of the project in source to dest")
    
    # behaviour args
    parser.add_argument('-d','--default','--make-default', action='store_true',
                        help="For use with -m and -i. Makes the new project rsshell's default")
    parser.add_argument('--dev', action='store_true', help=argparse.SUPPRESS)
    
    # location args
    parser.add_argument('--source', metavar="folder", action='store',
                        help="The source folder. See -m,-u, and -i for usage")
    parser.add_argument('--dest','--destination', metavar="folder", action='store',
                        help="The Destination folder. Unused by -u. See -m, and -i for usage.")
    
    # get command line args
    args = parser.parse_args()
    
    # function to call gets stored here by the parser,
    # and it accepts the parsed args object as input
    if 'action' in args and args['action'] in not None: args['action'](args)
    # if the action wasn't given on the command line, get it interactively
    else: get_action()(args)

def install(clargs):
    ''' install is the "main" function in charge of creating a new installation of the project.
        clargs is the args object the command line parser returns, and is used as a starting point
        for the various flags and paths needed to install the red spider project '''
    # TODO: write function body
    # function calls:
    # get_rsp_src_dir - obtain directory with project source
    # get_install_dir - obtain the install destination
    # is_global_install - system wide or single user install?
    # gen_rc_file - generate the rsshell rc file
    # set_default_root - set the default root in the rc file
    pass
  
def uninstall(clargs):
    ''' uninstall is the "main" function in charge of removing an old installation of the project.
        clargs is the args object the command line parser returns, and is used as a starting point
        for the various flags and paths needed to install the red spider project '''
    # TODO: write function body
    # function calls:
    # get_rsp_dir - obtain root of installation to uninstall
    # do_persist - should i keep rc settings for the install?
    # for_each_file_do - delete all the files
    # get_rsp_dir - obtain root of alternative default root
    # set_default_root - set the default root in the rc file
    pass