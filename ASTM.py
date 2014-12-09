# -*- coding: utf-8 -*-
"""
ASTM Function
Created on Sep 25 2014

This program are for the calculations based off of ASTM C457, and 
the bubble and cement paste sizes along the spcific row.

To run program, run BC_GUI.py

@author: Alison Mergaman
Alison.Mergaman@contr.netl.doe.gov
"""


def ASTM(inds,v):                         
    b_size=[]
    c_size=[]    
       
    for k in xrange(1, len(inds), 2):               #To find the calculations for ASTM C457, you must find the bubble and 
        b_size.append(inds[k]-inds[k-1])            #cement paste sizes. This code puts the sizes in two sepatared lists
                                                    #for bubble and cement.
    c_size.append(inds[0])
    for h in xrange(2, len(inds), 2):
        c_size.append(inds[h]-inds[h-1])
    c_size.append(v-inds[-1])
    
    b=sum(b_size)                       #This entire section is taken from the calcualtions in ASTM C457.
    c=sum(c_size)                       #These calculations will be printed out in Bubble_Code.py
    a_con=(b*100)/float(v) #Air Content
    p_con=(c*100)/float(v) #Paste Content
    pa=p_con/float(a_con) # Paste Air Ratio
#    print pa
    acl=(b/float(len(b_size))) #Average Chord Length
    ss=(4/float(acl)) #Specific Surface
    if pa<=4.342:
        sf=c/(4*float(len(b_size))) #Powers Spacing Factor (when Paste Air Ratio is less than or equal to 4.342)
        
    elif pa>4.342:
        sf=(3/float(ss))*(1.4*((1+(pa))**(1/3.))-1)  #Powers Spacing Factor (when Paste Air Ratio is greater than to 4.342)
#    print sf    
    vf=len(b_size)/float(v) #Void Frequency
    

    return (b_size, c_size, b, c, a_con, p_con, pa, acl, ss, sf, vf)