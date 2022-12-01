import sys
sys.path.append("../code/")

import pytest
import unittest

import symptoms_calculator

a = symptoms_calculator.symptomsCalculator()

class testReturnValues(unittest.TestCase):
    '''The given class tests all the symptoms of the Diseases and outputs the relative result'''
    
    def test_acidBaseDisorder(self):
        
        '''The function determines whether the patient has Acid Base Disorder utilizing its Medical Report's Constraints'''
        
        temp1, temp2 = a.acidBaseDisorder(15, 31) 
        self.assertEqual(temp1, True) and self.assertEqual(temp2, False)
    
    def test_hyperCholesterolemia(self):
        
        '''The function determines whether the patient has Hyper Cholesterolemia utilizing its Medical Report's Constraints'''
        
        temp = a.hyperCholesterolemia(160) 
        self.assertEqual(temp, False)
    
    def test_hypertension(self):
        
        '''The function determines whether the patient has Hypertension utilizing its Medical Report's Constraints'''
        
        temp = a.hypertension(145, 95) 
        self.assertEqual(temp, True) 
    
    def test_kidneyInjury(self):
        
        '''The function determines whether the patient has Kidney Injury utilizing its Medical Report's Constraints'''
        
        temp1, temp2, temp3, temp4 = a.kidneyInjury(1.5, 1.1) # pragma: no cover
        if ((temp1 == True) and (temp2 == False) and (temp3 == False) and (temp4 == True)): 
            temp = True
        else: # pragma: no cover
            temp = False
        self.assertEqual(temp, True) 
    
    def test_obesity(self):
        
        '''The function determines whether the patient has Obesity utilizing its Medical Report's Constraints'''
        
        temp = a.obesity(180, 72) 
        self.assertEqual(temp, False) 
