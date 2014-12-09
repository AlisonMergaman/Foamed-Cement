# -*- coding: utf-8 -*-
"""
Calibrations Report
Created on Sep 25 2014

The actual calibration resport is determined by the CT 
scanner based on the grometry of the voxels. 
This program finds the area of the portion cut out from 
the CT image.

To run program, run BC_GUI.py

@author: Alison Mergaman
Alison.Mergaman@contr.netl.doe.gov
"""

   
        
def calibration(voxel, out_directory, v, file_count, skip_row, count_i):
    save_file= out_directory + 'CT Calibration Summary.cal'    
    
    with open(save_file, 'w') as Foo:       
        
        first = v*voxel
        second = voxel*skip_row
        third = first*second
        fourth = third*count_i
        fifth = fourth*file_count
#        fifth=fourth*skip_file
        sixth = fifth*10**(-8)

        
        Foo.write('Area in cm^2\n\n')
        Foo.write('1D\n')
        Foo.write('Length Traversed x voxel size(microns) = Equation 1\n')
        Foo.write('{0} x {1} = {2}\n\n'.format(v, voxel, first))
        Foo.write('2D\n')
        Foo.write('Voxel size(microns) x Number of rows skipped = Equation 2\n')
        Foo.write('{0} x {1} = {2}\n'.format(voxel, skip_row,  second))
        Foo.write('Equation 1 x Equation 2 = Equation 3\n')
        Foo.write('{0} x {1} = {2}\n'.format(first, second, third))
        Foo.write('Equation 3 x Number of Lines in each slice analyzed= Equation 4\n')
        Foo.write('{0} x {1} = {2}\n\n'.format(third, count_i, fourth))
        Foo.write('3D\n')
#        Foo.write('Equation 4 x Number of files skipped= Equation 5\n')
#        Foo.write('{0}x{1}={2}\n'.format(fourth, skip_file, fifth))
        Foo.write('Equation 5 x Number of Files analyzed\n')
        Foo.write('{0} x {1} = {2}\n\n'.format(fourth, file_count, fifth))
        Foo.write('Converting microns into centimeters\n')
        Foo.write('{0} x 10^(-8) = {1}cm^2\n\n'.format(fifth, sixth))

        
        if sixth<46:
            Foo.write('{0}cm^2 < 46cm^2\n'.format(sixth))
            Foo.write('Rerun code with larger Skip Row')
        
        
        
        
        
        
        
        
        
        
        
        