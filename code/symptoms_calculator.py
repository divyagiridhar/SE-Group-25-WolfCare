class symptomsCalculator:
    
    '''The given class calculates all the symptoms of the Diseases using the required constraints from the Medical Reports and outputs the relative result'''

    def acidBaseDisorder(self, minbicarbonate, maxbicarbonate):
        
        '''The function calculates whether the patient has Acid Base Disorder utilizing its Medical Report's Constraints'''
        
        # For Metabolic Acidosis
        if (minbicarbonate < 18.0): 
            a = True
        else: 
            a = False
        
        #For Metabolic Alkalosis
        if (maxbicarbonate > 30.0): 
            b = True
        else: 
            b = False
        
        return a, b
    
    def hyperCholesterolemia(self, maxcholestrol, prevMaxCreatinine):
        
        '''The function calculates whether the patient has Hyper Cholesterolemia utilizing its Medical Report's Constraints'''
        
        if (maxcholestrol > 2000): 
            return True
        else:
            return False
    
    def hypertension(self, sbp, dbp):
        
        '''The function calculates whether the patient has Hypertension utilizing its Medical Report's Constraints'''
        
        if (sbp > 140) and (dbp > 90):
            return True
        else: 
            return False
    
    def kidneyInjury(self, maxCreatinine):
        
        '''The function calculates whether the patient has Kidney Injury utilizing its Medical Report's Constraints'''
        
        # For Acute
        if (((maxCreatinine) > (1.5 * prevMaxCreatinine)) or ((maxCreatinine > 1.2) and (prevMaxCreatinine <= 1.2))):
            a = True
        else: 
            a = False
        
        #For Chronic
        if ((maxCreatinine > 1.2) and (prevMaxCreatinine > 1.2)): 
            b = True
        else: 
            b = False
        
        #For Acute on Chronic
        if ((maxCreatinine > 1.2) and (prevMaxCreatinine > 1.2) and ((maxCreatinine) > (1.5 * prevMaxCreatinine))): 
            c = True
        else:
            c = False
        
        #For Not otherwise specified
        if (maxCreatinine > 1.2):
            d = True
        else:
            d = False
            
        return a, b, c, d
        
    def obesity(self, height, weight):
        
        '''The function calculates whether the patient has Obesity utilizing its Medical Report's Constraints'''
        
        if (height > 0) and (weight > 0):
            bmi = (weight)/((height/1000)*(height/100))
        
        if bmi > 30:
            return True
        else:
            return False
