#!usr/bin/env python
#coding: utf-8

import xlrd
#import xlwt
import mmap
import time
import os
from xlrd import open_workbook
from xlutils.copy import copy
from xlutils.filter import process,XLRDReader,XLWTWriter
# Patch: add this function to the end of xlutils/copy.py


class XlsManager(object):

    def _copy2(self,wb):
        w = XLWTWriter()
        process(XLRDReader(wb,'unknown.xls'),w)
        
        return w.output[0][1], w.style_list    

    def __init__(self,file=None,keeping_format=True):
        
        assert os.path.exists(file), "File: {} NOT Found!".format(file)
        self.rdbook = xlrd.open_workbook(file, formatting_info=keeping_format)
        self.wtbook, self.style_list = self._copy2(self.rdbook)

    def read_xls_cell(self, row, col, sheetx=0, sheet_name=None):

        if sheet_name:
            sheet = self.rdbook.sheet_by_name(sheet_name)
        else:
            sheet = self.rdbook.sheet_by_index(sheetx)

        return sheet.cell(row, col).value

    def read_xls_to_dict_list(self, sheetx=0, sheet_name=None, key_rows = 0):

        if sheet_name:
            sheet = self.rdbook.sheet_by_name(sheet_name)
        else:
            sheet = self.rdbook.sheet_by_index(sheetx)

        # read header values into the list
        keys = [sheet.cell(key_rows, col_index).value for col_index in range(sheet.ncols)]

        dict_list = []
        for row_index in range(1, sheet.nrows):
            d = {keys[col_index]: sheet.cell(row_index, col_index).value
                 for col_index in range(sheet.ncols)}
            dict_list.append(d)

        return dict_list



    def write_xls(self,row,col,data,sheetx = 0):
        
        rdsheet = self.rdbook.sheet_by_index(sheetx)
        self.wtsheet = self.wtbook.get_sheet(sheetx)
        xf_index = rdsheet.cell_xf_index(row, col)
        self.wtsheet.write(row, col, data, self.style_list[xf_index])
        
        
    def save_file(self,file_name):
        self.wtbook.save(file_name)        
        


if __name__=='__main__':
    test = XlsManager('Server_XCSA_Record_new.xls')
    test.write_xls(19, 0, 'First test!')
    test.save_file('test_1.xls')




