# -*- coding: utf-8 -*-
"""
Created on Wed Nov 19 21:39:55 2014
 
@author: Cantwell
"""
import numpy as np
from skimage import filter
 
class corescan:
    'Common base class for corescan.'
 
    def __init__(self, fid):
        """Base object for corescan.
     
        Input:
            - fid, a file location for a tab-delimited file containing zeros
              where matrix is present and a constant, finite value where voids
              are present
            - fid, a numpy array. 
 
        Example:
            >>> import pycoresis as pcs
            >>> fid = r'C:\YOUR\FILE\HERE.txt'
            >>> crs = pcs.corescan(fid)
            Data loaded from :  'C:\YOUR\FILE\HERE.txt'
            Array shape is   :  (200, 200)
            Mean porosity is :  0.0932
        """
         
        if fid.__class__ == str:
            self.data = np.loadtxt(fid, delimiter='\t')
            self.fileid = fid
            print "Data loaded from : ", fid
        else:
            self.data = np.asarray(fid) 
            self.fileid = fid.__class__
            print "Data loaded from : ", fid.__class__
 
 
        self.shape = np.shape(self.data)
        self.porosity = np.mean(self.data)/np.max(self.data)
        print "Array shape is   : ", self.shape
        print "Mean porosity is : ", self.porosity
    
    def displayFid(self):
        """Print file information to terminal.
     
        Input:
            - none
 
        Example:
            >>> import pycoresis as pcs
            >>> fid = r'C:\YOUR\FILE\HERE.txt'
            >>> crs = pcs.corescan(fid)
            >>> crs.displayFID()
            Data loaded from :  'C:\YOUR\FILE\HERE.txt'
        """
        print "Data loaded from : ", self.fileid
        return self.fileid
    
    def displayShape(self):
        """Print scan shape information to terminal.
     
        Input:
            - none
 
        Example:
            >>> import pycoresis as pcs
            >>> fid = r'C:\YOUR\FILE\HERE.txt'
            >>> crs = pcs.corescan(fid)
            >>> crs.displayShape()
            Array shape is   :  (200, 200)
        """
        print "Array shape is   : ", self.shape
        return self.shape
    
    def displayPorosity(self):
        """Print scan porosity to terminal.
     
        Input:
            - none
 
        Example:
            >>> import pycoresis as pcs
            >>> fid = r'C:\YOUR\FILE\HERE.txt'
            >>> crs = pcs.corescan(fid)
            >>> crs.displayPorosity()
            Mean porosity is :  0.0932
        """
        print "Mean porosity is : ", self.porosity
        return self.porosity
         
    def getVoidPts(self):
        """Retrieve list of pixel coordinates where voids are present.
     
        Input:
            - none
 
        Example:
            >>> import pycoresis as pcs
            >>> fid = r'C:\YOUR\FILE\HERE.txt'
            >>> crs = pcs.corescan(fid)
            >>> crs.getVoidPts()
            array([[  0,  44],
                   [  0,  45],
                   [  0,  46],
                   ..., 
                   [199, 112],
                   [199, 129],
                   [199, 130]])
        """
        voidspaces = np.where(self.data == np.max(self.data))
        self.voidcoords = np.transpose(voidspaces)
        return self.voidcoords
         
    def getVoidBorder(self):
        """Create boolean array where border points are True and all others
        False.
     
        Input:
            - none
 
        Example:
            >>> import pycoresis as pcs
            >>> fid = r'C:\YOUR\FILE\HERE.txt'
            >>> crs = pcs.corescan(fid)
            >>> crs.getVoidBorder()
            Number of border points : 2449
            Number of border points : 3245
            array([[ True,  True,  True, ...,  True,  True,  True],
                   [ True, False, False, ..., False, False,  True],
                   [ True, False, False, ..., False, False,  True],
                   ..., 
                   [ True, False, False, ..., False, False,  True],
                   [ True, False, False, ..., False, False,  True],
                   [ True,  True,  True, ...,  True,  True,  True]], dtype=bool)
        """
 
        self.voidedges = filter.canny(self.data)
        point_num = np.where(self.voidedges==True)
        self.pointnum = np.size(point_num[0])
        print "Number of border points :", self.pointnum
        return self.voidedges
         
    def _getPointScalar(self, x_pos, y_pos):
        row_diff = np.meshgrid(range(self.shape[0]), 
                               range(self.shape[1]))[0]- x_pos
        col_diff = np.meshgrid(range(self.shape[0]), 
                               range(self.shape[1]))[1]- y_pos
        r_new = row_diff**2 + col_diff**2
        r_new = np.asarray(r_new,dtype=float)
        _e_field = 1/np.sqrt(r_new)
#        _e_xdir = row_diff * _e_field
#        _e_ydir = col_diff * _e_field
        return _e_field #, _e_xdir, _e_ydir
 
    def _poisson_solver(self):
         
        """
        from http://www.inf.ethz.ch/personal/tulink/FEM14/Ch1_ElmanSyvesterWathen_Ox05.pdf
        a solver for the Square domain, constant source function f(x) ≡ 1, zero
        boundary condition.
        """
         
        row, col = np.meshgrid(range(self.shape[1]), 
                               range(self.shape[0]))
        row = np.asarray(row, dtype=float)
        col = np.asarray(col, dtype=float)
        row = 2 * row / self.shape[1] - 1
        col = 2 * col / self.shape[0] - 1
        t_1 = 1 - row**2 * 0.5
        t_2 = 16 / np.pi**3
        t_3 = 0
        for idx in np.arange(1,12,2):        
            t_3_1 = idx * np.pi * (1 + row) * 0.5
            t_3_2 = idx * np.pi * (1 + col) * 0.5
            t_3_3 = idx * np.pi * (1 - col) * 0.5
            t_3_0 = (np.sin(t_3_1) / (idx**3 * np.sinh(idx * np.pi)) *
                    (np.sinh(t_3_2) + np.sinh(t_3_3)))
            t_3 += t_3_0
        poisson_solution = t_1 - t_2 * t_3
        return poisson_solution
 
         
    def getScalarField(self):
         
        """Create array consisting of a potential surface of the core scan
        wherein each border point is considered as being a source.
     
        Input:
            - none
 
        Example:
            >>> import pycoresis as pcs
            >>> fid = r'C:\YOUR\FILE\HERE.txt'
            >>> crs = pcs.corescan(fid)
            >>> crs.getScalarField()
            Number of border points : 2449
            Completed :  0 of 2449
            Completed :  100 of 2449
            ...
            Completed :  2400 of 2449
        """
         
        self.E_field = np.zeros_like(self.data)
        self.E_xdir = np.zeros_like(self.data)
        self.E_ydir = np.zeros_like(self.data)
        _v_edges = self.getVoidBorder()
        _v_edge_pts = np.where(_v_edges==True)
        _v_edge_pts = np.transpose(_v_edge_pts)
        for idx, vals in enumerate(_v_edge_pts):
            self.E_field += self._getPointScalar(vals[0], vals[1])[0]
#            self.E_xdir += self._getPointScalar(vals[0], vals[1])[1]
#            self.E_ydir += self._getPointScalar(vals[0], vals[1])[2]
            if idx%100 == 0:
                print "Completed : ", idx, "of", self.pointnum
        self.E_field = np.transpose(self.E_field)
        self.E_field = self.E_field / self._poisson_solver()
        data_bool = np.asarray(self.data,dtype=bool)
        self.E_field[np.where(data_bool == True)] = np.nan
        self.E_field[np.where(self.voidedges == True)] = np.nan
        self.E_field[np.where(self.E_field == np.inf)] = np.nan
        return self.E_field