#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 20:55:50 2020

@author: bikash
"""

import os
import sys
import argparse
from pathlib import Path
from distutils.dir_util import copy_tree
from jinja2 import Template

def check_arg(args=None):
    '''arguments.
    '''
    parser = argparse.ArgumentParser(prog='py2webapp',
                     description='Convert your scripts to webapp',
                     epilog='github@bkb3')
    parser.add_argument('-v', '--version',
                    action='version',
                    version='%(prog)s ' + '1',
                    help="Show program's version number and exit.")
    parser.add_argument('-f', '--inputscriptfile',
                    help='Your script to convert to webapp',
                    required=True)
    parser.add_argument('-c', '--config',
                    help='Configuration file',
                    required=True)

    results = parser.parse_args(args)
    return (results.inputscriptfile, results.config)

def main():
    root_path = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(root_path, 'app_template.py'), 'r') as t:
        template = t.read()

    with open(c, 'r') as cnf:
        config = cnf.read()

    tm = Template(template)

    script_name = Path(f).stem + Path(f).suffix
    script_dir = Path(f).resolve().parent



    with open(os.path.join(script_dir, 'app.py'), 'w') as r:
        r.write(tm.render(config=config, script_name=script_name))


    for directory in ['static', 'templates']:
        source = os.path.join(root_path, directory)
        destination = os.path.join(script_dir, directory)
        copy_tree(source, destination)

    print('\n===========================================\n'
          'App generated as app.py!'
          '\nNow, make your script executable by using:\n'
          '\tchmod +x {}\n'
          'Then run the app as following:\n'
          '\tpython3 app.py\n'
          'The app will run at http://localhost:5050\n'
          '\U0001F6F8 \U0001F60A \n'
          '===========================================\n'.format(script_name))


if __name__ == '__main__':
    f, c = check_arg(sys.argv[1:])
    main()