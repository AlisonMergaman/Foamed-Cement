# -*- coding: utf-8 -*-
"""
The Combined Plots and Directory/Output Directory
Created on Sep 25 2014

This program first deals with the directory and output directory. 
It makes sure to put a '\' at the end of the
file. Aldo, making sure to only read '*.txt' files from the 
directory, and outputting '.out' files into the Output
directory.

The next part of the program combineds all of the variables 
together to form 'combined histograms'.

To run program, run BC_GUI.py

@author: mergamana
"""
from glob import glob
from Calibration import calibration
from Excel import excel
from Normal_Hist import normal_hist
import matplotlib.pyplot as plt
from Bubble_Code import Main
import pylab as P
#from collections import Counter
#from Excel import excel
import numpy as np
import os
#from scipy.stats import norm, rayleigh
#import matplotlib.mlab as mlab

def comb_plots(directory, out_directory, skip):
#    open(directory, 'w').close() 
    air_con=[]
    paste_air=[] 
    avg_ch=[] 
    spac_fac=[] 
    freq=[]

    print directory  
    


    if directory[-1] != '\\':                ##This only works if the file has a '\' at the end.
        directory = directory + '\\'
        
    if out_directory[-1] != '\\':
        out_directory = out_directory + '\\'

    
    files = glob(directory + '*.txt')##Only uses files ending in '.txt'
    if not(files):
        files = glob(directory + '.*.txt')
    files = files[::skip]
    
    #Delete Files in Output Directory
    for fn in os.listdir(out_directory):
        if fn != 'Thumbs.db':
            os.remove(out_directory + fn)
    
    for file_name in files:        
        file_output = out_directory + file_name[start_ind:-4] + '.out'   
#        os.remove(out_directory)
        #Nmes the files '.out'.

    
      
    
        a, p, ch, s, f, v, count_i = Main(file_name, 
                                          file_output, start_row, skip_row)   #Calling variables from Bubble_Code.py
        air_con += a
        paste_air += p
        avg_ch += ch
        spac_fac += s
        freq += f
    
#    mu, sigma=mean(a_con), std(a_con)
    
    #Making the histograms
    plt.subplot(1, 1, 1)    
    
    
    file_output=out_directory + 'Combined Air Content' + '.png' 
    normal_hist(air_con, 50, range=(0, airxa), facecolor='g')
    mu_ac= np.mean(air_con)
    sigma_ac= np.std(air_con)
    plt.title(name_plot +'\nCombined Air Content') 
    plt.text(50, .1, r'$\mu=%.3f,\ \sigma=%.3f$' %(mu_ac, sigma_ac))
    plt.xlabel('Air Content')
    plt.ylabel('Frequency')
    plt.axis([0, airxa, 0, airya])
    j=np.linspace(0, airxa, num=50)
    y = P.normpdf(j, mu_ac, sigma_ac)*airxa/50
    P.plot(j, y, 'k', linewidth=1.5)
    plt.axvline(mu_ac, color='b', linestyle='dashed', linewidth=2)
    plt.savefig(file_output)
    
    
    
    file_output=out_directory + 'Combined Average Chord Length' + '.png' 
    normal_hist(avg_ch, 50, range=(0, aclxa),facecolor='violet')
    mu_avg=np.mean(avg_ch)
    sigma_avg=np.std(avg_ch)
    plt.title(name_plot +'\nCombined Average Chord Length' )
    plt.text(60, .15, r'$\mu=%.3f,\ \sigma=%.3f$' %(mu_avg, sigma_avg))
    plt.xlabel('Average Chord Length')
    plt.ylabel('Frequency')
    plt.axis([0, aclxa, 0, aclya])
    x=np.linspace(0, aclxa, num=50)
    w = P.normpdf(x, mu_avg, sigma_avg)*aclxa/50
    P.plot(x, w, 'k', linewidth=1.5)
    plt.axvline(mu_avg, color='b', linestyle='dashed', linewidth=2)
    plt.savefig(file_output)
    plt.cla()
    
    
    file_output=out_directory + 'Combined Paste Air Ratio' + '.png'
    normal_hist(paste_air, 50, range=(0, paxa), facecolor='y')
    mu_pa= np.mean(paste_air)
    sigma_pa= np.std(paste_air)
    plt.title(name_plot +'\nCombined Paste Air Ratio')
    plt.text(20, .3, r'$\mu=%.3f,\ \sigma=%.3f$' %(mu_pa, sigma_pa))
    plt.xlabel('Paste Air Ratio')
    plt.ylabel('Frequency')
    plt.axis([0, paxa, 0, paya])
    x=np.linspace(0, paxa, num=50)
#    y = P.gamma(mu_pa, sigma_pa, x)*paxa/20
    y = P.normpdf(x, mu_pa, sigma_pa)*paxa/50
    P.plot(x, y, 'k', linewidth=1.5)
    plt.axvline(mu_pa, color='b', linestyle='dashed', linewidth=2)
    plt.savefig(file_output)
    plt.cla()
    

    
    
    file_output=out_directory + 'Combined Spacing Factor' + '.png' 
    normal_hist(spac_fac, 50, range=(0, spacxa),facecolor='orange')
    mu_spac=np.mean(spac_fac)
    sigma_spac=np.std(spac_fac)
    plt.title(name_plot +'\nCombined Spacing Factor') 
    plt.text(20, .1, r'$\mu=%.3f,\ \sigma=%.3f$' %(mu_spac, sigma_spac))
    plt.xlabel('Spacing Factor')
    plt.ylabel('Frequency') 
    plt.axis([0, spacxa, 0, spacya])
    x=np.linspace(0, spacxa, num=50)
    h = P.normpdf(x, mu_spac, sigma_spac)*spacxa/50
    P.plot(x, h, 'k', linewidth=1.5)
    plt.axvline(mu_spac, color='b', linestyle='dashed', linewidth=2)
    plt.savefig(file_output)
    plt.cla()
    
    
    file_output=out_directory + 'Combined Void Frequency' + '.png'   
    normal_hist(freq, 50, range=(0, voidxa),facecolor='red')
    mu_freq=np.mean(freq)
    sigma_freq=np.std(freq)
    plt.title(name_plot +'\nCombined Void Frequency')
#    plt.text(.025, .2, r'$\mu=%.3f,\ \sigma=%.3f$' %(mu_freq, sigma_freq))
    plt.text(.025, .2, r'$\mu=%.3f,\ \sigma=%.3f$' %(mu_freq, sigma_freq))
    plt.xlabel('Void Frequency')
    plt.ylabel('Frequency')
    plt.axis([0, voidxa, 0, voidya])
    x=np.linspace(0, voidxa, num=50)
    g = P.normpdf(x, mu_freq, sigma_freq)*voidxa/50
    P.plot(x, g, 'k', linewidth=1.5)
    plt.axvline(mu_freq, color='b', linestyle='dashed', linewidth=2)
    plt.savefig(file_output)
    plt.cla()    
    
    



    
    file_count=len(files)

    
    #Calling the programs from Calibration.py and Excel.py
    calibration(voxel, out_directory, v, file_count, skip_row, count_i)
    excel(out_directory, air_con, paste_air, avg_ch, spac_fac, freq, name_plot)

    
#These are filler variables, but will be changed when the GUI is run.   
start_row = 19
skip_row = 40 
voxel=0.00039
start_ind = -8
name_plot = ' '
#skip_file= 40

airxa = 0
aclxa = 0
paxa = 0
spacxa = 0
voidxa = 0
airya = 0
aclya = 0
paya = 0
spacya = 0
voidya = 0