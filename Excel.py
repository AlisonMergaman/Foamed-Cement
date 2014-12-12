# -*- coding: utf-8 -*-
"""
Excel Calculations
Created on Thu Sep 25 2014

This program puts the list of the variables with their respective sorected variables, means, standard deviations, variances, 
and minimum/maximums into an excel file.

To run program, run BC_GUI.py

@author: mergamana
"""
import numpy as np
import xlwt
import itertools
#from Comb_Plots import comb_plots

def excel(out_directory, a_con, pa, acl, sf, vf, name_plot):
          
    m=np.mean(a_con)          ##Making the variables for mean, standard deviation, variance, and minimum/maximum
    m='%.3f' %(m)
    ms=np.std(a_con) 
    ms='%.3f' %(ms)          
    mv=np.var(a_con)
    mv='%.3f' %(mv)
    mm=np.min(a_con)
    mm='%.3f' %(mm)
    mma=np.max(a_con)
    mma='%.3f' %(mma)
    mminmax=[mm, mma]
    mnew=sorted(a_con)
#    mnew='%.3f' %(mnew)
    n=np.mean(pa)
    n='%.3f' %(n)
    ns=np.std(pa)
    ns='%.3f' %(ns)
    nv=np.var(pa)
    nv='%.3f' %(nv)
    nn=np.min(pa)
    nn='%.3f' %(nn)
    nna=np.max(pa)
    nna='%.3f' %(nna)
    nminmax=[nn, nna]
    nnew=sorted(pa)
#    nnew='%.3f' %(nnew)
    o=np.mean(acl)
    o='%.3f' %(o)
    os=np.std(acl)
    os='%.3f' %(os)
    ov=np.var(acl)
    ov='%.3f' %(ov)
    oo=np.min(acl)
    oo='%.3f' %(oo)
    ooa=np.max(acl)
    ooa='%.3f' %(ooa)
    ominmax=[oo, ooa]
    onew=sorted(acl)
#    onew='%.3f' %(onew)
    q=np.mean(sf)
    q='%.3f' %(q)
    qs=np.std(sf)
    qs='%.3f' %(qs)
    qv=np.var(sf)
    qv='%.3f' %(qv)
    qq=np.min(sf)
    qq='%.3f' %(qq)
    qqa=np.max(sf)
    qqa='%.3f' %(qqa)
    qminmax=[qq, qqa]
    qnew=sorted(sf)
#    qnew='%.3f' %(qnew)
    r=np.mean(vf)
    r='%.3f' %(r)
    rs=np.std(vf)
    rs='%.3f' %(rs)
    rv=np.var(vf)
    rv='%.3f' %(rv)
    rr=np.min(vf)
    rr='%.3f' %(rr)
    rra=np.max(vf)
    rra='%.3f' %(rra)
    rminmax=[rr, rra]
    rnew=sorted(vf)
#    rnew='%.3f' %(rnew)
    
    t=0
    
    book = xlwt.Workbook()              #Sending it to an excel worksheet
    sh = book.add_sheet('sheet1')
       
    col_width = 256 * 20                        # 20 characters wide

    try:
        for i in itertools.count():
            sh.col(i).width = col_width
    except ValueError:
        pass
     
    col1='Air Content'                  #The variable labels
    col2='Sorted Air Content'
    col3='Min/Max'
    col4='Mean'
    col5='Standard Deviation'
    col6='Variance'
    col7='Average Chord Length'
    col8='Sorted Average Chord Length'    
    col9='Min/Max'
    col10='Mean'
    col11='Standard Deviation'
    col12='Variance'
    col13='Spacing Factor'
    col14='Sorted Spacing Factor'
    col15='Min/Max'
    col16='Mean'
    col17='Standard Deviation'
    col18='Variance'
    col19='Paste Air Ratio'
    col20='Sorted Paste Air Ratio'
    col21='Min/Max'
    col22='Mean'
    col23='Standard Deviation'
    col24='Variance'
    col25='Void Frequency'
    col26='Sorted Void Frequency'
    col27='Min/Max'
    col28='Mean'
    col29='Standard Deviation'
    col30='Variance'
    
    sh.write(t, 0, col1)          #Writing the variables in the specified columns.
    sh.write(t, 1, col2)
    sh.write(t, 2, col3)
    sh.write(t, 3, col4)
    sh.write(t, 4, col5)
    sh.write(t, 5, col6)
    sh.write(t, 6, col7)
    sh.write(t, 7, col8)
    sh.write(t, 8, col9)
    sh.write(t, 9, col10)
    sh.write(t, 10, col11)
    sh.write(t, 11, col12)
    sh.write(t, 12, col13)
    sh.write(t, 13, col14)
    sh.write(t, 14, col15)
    sh.write(t, 15, col16)
    sh.write(t, 16, col17)
    sh.write(t, 17, col18)
    sh.write(t, 18, col19)
    sh.write(t, 19, col20)
    sh.write(t, 20, col21)
    sh.write(t, 21, col22)
    sh.write(t, 22, col23)
    sh.write(t, 23, col24)
    sh.write(t, 24, col25)
    sh.write(t, 25, col26)
    sh.write(t, 26, col27)
    sh.write(t, 27, col28)
    sh.write(t, 28, col29)
    sh.write(t, 29, col30)
    


    
    for j, e1 in enumerate(a_con, t+1):            #The for loops loop through the list of numbers in the variables.
        sh.write(j, 0, e1)
#    print(str(a_con).count(j))
    for j, e2 in enumerate(mnew, t+1):
        sh.write(j, 1, e2)
    for j, e3 in enumerate(mminmax, t+1):
        sh.write(j, 2, e3)    
    sh.write(t+1, 3, m)
    sh.write(t+1, 4, ms)
    sh.write(t+1, 5, mv)
    
    
    for j, e3 in enumerate(acl, t+1):
        sh.write(j, 6, e3)
    for j, e4 in enumerate(onew, t+1):
        sh.write(j, 7, e4)    
    for j, e5 in enumerate(ominmax, t+1):
        sh.write(j, 8, e5)
    sh.write(t+1, 9, o)
    sh.write(t+1, 10, os)
    sh.write(t+1, 11, ov)
    
    
    for j, e6 in enumerate(sf, t+1):
        sh.write(j, 12, e6)
    for j, e7 in enumerate(qnew, t+1):
        sh.write(j, 13, e7)
    for j, e8 in enumerate(qminmax, t+1):
        sh.write(j, 14, e8)
    sh.write(t+1, 15, q)
    sh.write(t+1, 16, qs)
    sh.write(t+1, 17, qv)
    
       
    for j, e9 in enumerate(pa, t+1):
        sh.write(j, 18, e9)
    for j, e10 in enumerate(nnew, t+1):
        sh.write(j, 19, e10)
    for j, e11 in enumerate(nminmax, t+1):
        sh.write(j, 20, e11)
    sh.write(t+1, 21, n)
    sh.write(t+1, 22, ns)
    sh.write(t+1, 23, nv)
    
    
    for j, e12 in enumerate(vf, t+1):
        sh.write(j, 24, e12)
    for j, e13 in enumerate(rnew, t+1):
        sh.write(j, 25, e13)
    for j, e14 in enumerate(rminmax, t+1):
        sh.write(j, 26, e14)
    sh.write(t+1, 27, r)
    sh.write(t+1, 28, rs)
    sh.write(t+1, 29, rv)
    
#    comb_plots(name_plot)
    book.save(out_directory + name_plot + ' Calculations.xls')

#name_plot = ' '