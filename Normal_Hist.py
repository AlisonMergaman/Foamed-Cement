# -*- coding: utf-8 -*-
"""
Changing the histogram format
Created on Sep 25 2014

This program changes the original histogram so that the 
y-axis equals up to 1.0, and the bin width from the first column
to the last column.

To run program, run BC_GUI.py

@author: mergamana
"""
import numpy as np
import matplotlib.pyplot as plt

def normal_hist(x, bins=20, range=(0,1), facecolor='g'):                   
    hist, bins = np.histogram(x, bins=bins, range=range)             
    hist = hist.astype('float64')/sum(hist)
    width = bins[1:] - bins[:-1]
    plt.cla()
    plt.bar(bins[:-1], hist, width=width, facecolor=facecolor)
    
    

    