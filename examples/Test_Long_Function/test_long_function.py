#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 10 17:49:55 2020

@author: bikash
"""

import sys
import argparse
from time import sleep
import numpy as np
from scipy import special


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
    parser.add_argument('-s', '--inputSequence',
                    type=str,
                    help='Input sequence',
                    required=True)
    parser.add_argument('-t', '--testSequence',
                    type=str,
                    help='Test sequence',
                    required=True)
    parser.add_argument('-x', '--inputNumber',
                    type=int,
                    help='Numerical Input',
                    required=True)



    results = parser.parse_args(args)
    return (results.inputSequence, results.testSequence, \
        results.inputNumber,)


def main():
    '''Main func. It does some computation and prints
    results. Simulating long work by sleep
    '''

    sleep(10)

    # This is the results after processing (faked here)
    results = ['String from result' , 123131231, \
        'Plot generated with {} points'.format(x)]
    # return results

    # Make a dict. This allows formatting nicely in html.
    # Replace "Analysis 1, 2,.." with your names.
    result_dict = {}
    result_dict["Analysis 1"] = results[0]
    result_dict["Analysis 2"] = results[1]
    result_dict["Analysis 3"] = results[2]

    # If your function returns data you want to plot, send them to the dict
    # as x and y
    # Currently available types = 'line' or 'bar' 
    plot_data_x = np.round(np.linspace(-2*np.pi, 2*np.pi, x), 2).tolist()
    plot_data_y0 = np.round(np.sin(plot_data_x), 2).tolist()
    plot_data_y1 = np.round(special.j0(plot_data_x), 2).tolist()
    plot_data_y2 = np.round(special.airy(plot_data_x)[0], 2).tolist()
    result_dict["Plot"] = {
        'x': plot_data_x,
        'y': [plot_data_y0, plot_data_y1, plot_data_y2],
        'type': 'line',
        'xlabel': 'Angle (radians)',
        'ylabel': ['Sin', 'BesselJ0', 'Airy']
    }



    # Print dict. [IMPORTANT]
    print(result_dict)

if __name__ == '__main__':
    s, t, x = check_arg(sys.argv[1:])
    main()
