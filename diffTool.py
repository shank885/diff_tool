# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 18:27:39 2019

@author: shashank shekhar
"""
import re

# deftools class 
class defTool():
    
    # method to find common entries in file_A and file_B
    def getCommon(self, file_A, file_B):
        
        # list to store common entries
        common = []
        
        # serach for common entries in file_A and file_B
        for item in file_A:
            if item in file_B:
                common.append(item)
        
        # return common entries
        return common
    
    # method to find file1 diff file2
    def getDiff(self, file_A, file_B):
        
        # list to store entries present in file_A but not in file_B
        diff = []
        
        # search for entries present in file_A but not in file_B
        for item in file_A:
            if item not in file_B:
                diff.append(item)
    
        # return diff entries
        return diff    
    


if __name__ == '__main__':
    
    # open files in read mode
    file1 = open('data/file1.txt', 'r')
    file2 = open('data/file2.txt', 'r')
    
    # store data present in files in a string
    file1_data = file1.read()
    file2_data = file2.read()
    
    # close files
    file1.close()
    file2.close()

    # regular expression to find words in the data
    regex = r'\w+'
    file1_items = set(re.findall(regex, file1_data))
    file2_items = set(re.findall(regex, file2_data))
    
    #create an instance of class defTools
    deftool = defTool()

    # get common words in file1 and file2    
    common = deftool.getCommon(file1_items, file2_items)
    print("----------- Common words in file1 and file2 -------------")
    print('\n'.join(sorted(common)))
    
    # get words in (file1 - file2)
    file1_diff_file2 = deftool.getDiff(file1_items, file2_items)
    print('----------- Words in (file1 - file2) ------------')
    print('\n'.join(sorted(file1_diff_file2)))
    
    # get words in (file2 - file1)
    file2_diff_file1 = deftool.getDiff(file2_items, file1_items)
    print('----------- Words in (file2 - file1) ------------')
    print('\n'.join(sorted(file2_diff_file1)))