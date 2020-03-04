#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Copyspecial Assignment"""

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import re
import os
import shutil
import subprocess
import argparse
import sys


# This is to help coaches and graders identify student assignments
__author__ = "???"


# +++your code here+++
# Write functions and modify main() to call them


def get_special_paths(dir):
    """get_special_paths(dir) -- returns a list of the absolute paths of the special files in the given directory"""
    file_list = os.listdir(dir)
    absolute_path_list = []
    for file in file_list:
        special_file = re.findall(r'__\w+__', file)
        if special_file:
            absolute_path_list.append(os.path.abspath(file))
    return absolute_path_list


def copy_to(paths, dir):
    """copy_to(paths, dir) given a list of paths, copies those files into the given directory"""
    # if not os.path.exists(dir):
    #     os.makedirs(dir)
    # for path in paths:
    #     shutil.copy(path, dir)
    cwd = os.getcwd()
    if not os.path.exists(paths):
        create_dir = 'mkdir -p {0}'.format(paths)
        os.system(create_dir)
    else:
        print("Paths exists")
    for file in dir:
        os.chdir(cwd)
        shutil.copy(file, paths)


def zip_to(paths, zippath):
    """Creates zip file from special files"""
    paths = list(paths)
    command = "zip -j {} {}".format(zippath, ' '.join(paths))
    print("Command I'm going to do: ")
    print(command)
    os.system(command)


def main():
    # This snippet will help you get started with the argparse module.
    parser = argparse.ArgumentParser()
    parser.add_argument('--todir', help='dest dir for special files')
    parser.add_argument('--tozip', help='dest zipfile for special files')
    parser.add_argument('fromdir', help='dir to look for local files')

    args = parser.parse_args()

    # Read the docs and examples for the argparse module about how to do this.
    all_paths = get_special_paths(args.fromdir)

    # Parsing command line arguments is a must-have skill.
    # This is input data validation.  If something is wrong (or missing) with any
    # required args, the general rule is to print a usage message and exit(1).

    # +++your code here+++
    # Call your functions
    if args.todir:
        copy_to(args.todir, all_paths)
    if args.tozip:
        zip_to(all_paths, os.path.join(os.getcwd(), args.tozip))

    if not args.todir and not args.tozip:
        for file in all_paths:
            print(os.path.abspath(file))
    # +++your code here+++
    # Call your functions


if __name__ == "__main__":
    main()
