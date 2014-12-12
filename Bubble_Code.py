# -*- coding: utf-8 -*-
"""
Main Code
Created on Aug 20 2014

This is the main part of the bubble/cement coding program. 
Here It goes throw how many rows to skips, and where to start
and stop along the column of a specific row. The outuput is 
formmated in a way to clearly read what our conclusions of
the code will be.

To run program, run BC_GUI.py

@author: Alison Mergaman
Alison.Mergaman@contr.netl.doe.gov
"""
import numpy as np
from ASTM import ASTM
#import matplotlib.pyplot as plt

def Main(filename, outfile, start_row, skip_row):
    with open(outfile, 'w') as Foo:
        data = np.loadtxt(filename)
        
#        v=len(data)
        #print(v)
        

        
        nrow = data.shape[0]         
        ncol = data.shape[1]
        v=int(ncol)
#        print v
        
#        print data.shape
        
        air=[]
        pasteair=[]
        avg=[]
        spac=[]
        void=[]
        
        count_i = 0#np.ceil((nrow - start_row)/skip_row)
        for i in xrange(start_row, nrow, skip_row):  
        ##In the GUI you input what row to start on, and whow many rows to skip. 
        ##If pulling the text files from excel, be sure to start a row before  
        #you woudld want to start. Python is index at 0, so 1 in excel is row 0
        # in python.
            
            void_inds = [] #empty list
#            count_i += 1
            for j in xrange(0, ncol):     
            ##Loop across cols of the ith row at column j from 2 to the end of the row for that section
            ##Start at index 1 and goes to the end of the line.
                if data[i, j] != data[i, j-1]:   
                ##This if statements will give the bubble index points. 
                    void_inds.append((j+1))
#                    v=len(data)
#                    print(v)
           
            if len(void_inds)>1:            
                ##This in done just incase a line does not have any bubbles in them.
                count_i += 1
                Foo.write('Row {0}\nIndices:{1}\n'.format(i+1, 
                          void_inds))   
                          ##Prints the row and the index change between 

                b_size, c_size, b, c, a_con, p_con, pa, acl, ss, sf, vf=ASTM(void_inds,v)  #a bubble and cement paste.
    
                new_inds = []
                if data[i,0]==255:                                         
                    begin_bubble='Incomplete Bubble in the first index'     
                    ##We do not want implete bubbles, so tif they occur, which will
                    #be at either the beginning of end of the line, it will be
                    #stated there is an incomplete bubble, and then thrown out.
                    new_inds=void_inds[1:]                                  
                else:
                    begin_bubble='  '
                                        
                if data[i,-1]==255:
                    end_bubble='Incomplete Bubble in the last index'
                    if new_inds:
                        new_inds=new_inds[:-1]
                    else:
                        new_inds=void_inds[:-1]
                else:
                    end_bubble='  '
               
         
                if new_inds:               
                    ##If there there is an incomplete bubble, 
                     #then the indicies could be rearranged. If this happens
                     #there is no reason to print out the original index information.
                    Foo.write('\nBubble Begin: {0}\nBubble End: {1}\n\n'.format(begin_bubble, end_bubble))

                    Foo.write('New Indicies: {0}\n'.format(new_inds))
                    b_size, c_size, b, c, a_con, p_con, pa, acl, ss, sf, vf=ASTM(new_inds,v)

                ##This section just prints out the calculations from ASTM.py with labels.
                Foo.write('Bubble Sizes: {0}\n'.format(b_size))
                Foo.write('Bubble Count: {0}\n'.format(len(b_size)))
                Foo.write('Sum of Bubbles: {0}\n'.format(b))
                Foo.write('Cement Sizes: {0}\n'.format(c_size))
                Foo.write('Cement Count: {0}\n'.format(len(c_size)))
                Foo.write('Sum of Cement: {0}\n'.format(c))
                Foo.write('Air Content: {0}\n'.format(a_con))
                Foo.write('Paste Content: {0}\n'.format(p_con))
                Foo.write('Paste Air Ratio: {0}\n'.format(pa))
                Foo.write('Average Chord Length: {0}\n'.format(acl))
                Foo.write('Specific Surface: {0}\n'.format(ss))
                if pa<=4.342:
                    Foo.write('pa<=4.342\n')
#                    Foo.write('{0}/({1}*({2}))\n'.format(c, 4, v))
                elif pa>4.342:
                    Foo.write('pa>4.342\n')
#                    Foo.write('({0}/{1})*({2}*(({3}+{4})**{5})-{6})'.format(3, ss, 1.4, 1, pa, 1/3, 1))
                Foo.write('Spacing Factor: {0}\n'.format(sf))  
                Foo.write('Void Frequency: {0}\n'.format(vf))
                Foo.write('\n\n\n')
                
                
                
               ##These will be used for the histograms, 
                #want to combine all the claculations for each variable together 
                #to form a fliud histogram.
                air.append(a_con)
                pasteair.append(pa)
                avg.append(acl)
                spac.append(sf)
                void.append(vf)
        
#                plt.plot(a_con, len(b_size))
                
        
            

        Foo.write('\n\n')
        Foo.write('Length Traversed: {0}\n'.format(v))
        Foo.write('Number of lines: {0}\n'.format(count_i))

       
        return(air, pasteair, avg, spac, void, v, count_i)

 

    