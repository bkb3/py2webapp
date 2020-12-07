#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 12:24:33 2020

@author: bikash
"""

import sys
from distutils.spawn import find_executable
import argparse
from subprocess import run, PIPE, DEVNULL

def check_arg(args=None):
    '''arguments.
    '''
    parser = argparse.ArgumentParser(prog='Program',
                     description='Description',
                     epilog='Author')
    parser.add_argument('-v', '--version',
                    action='version',
                    version='%(prog)s ' + '1',
                    help="Show program's version number and exit.")
    parser.add_argument('-s', '--sequence',
                    type=str,
                    help='Input sequence',
                    required=True)

    results = parser.parse_args(args)
    return (results.sequence)


def main():
    '''Main func
    '''
    new_ = run(['RNAfold', '--noPS'], input=s.encode(), stdout=PIPE, stderr=PIPE)
    
    results = [new_.stdout.decode().split('\n')[1].split(' ')[1][1:-1], 
                new_.stdout.decode().split('\n')[1].split(' ')[0],
                new_.stdout.decode().split('\n')[0]
    ]

    #return results

    result_dict = {}
    result_dict["MFE"] = results[0]
    result_dict["Bracket notation"] = results[1]
    result_dict["Sequence"] = results[2]
    print(result_dict)

if __name__ == '__main__':
    s = check_arg(sys.argv[1:])
    if find_executable('RNAfold') is None:
        print('\nInstall RNAfold first!')
        exit()
    main()
