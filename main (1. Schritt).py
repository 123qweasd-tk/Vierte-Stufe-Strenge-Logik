from datetime import datetime
import csv

def total_formula_deduction_first_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[0] == "n":    #caluculates potential "n"-values of first value
        return("n")
    elif second_formula[0] == "n":
        return("n")
    elif third_formula[0] == "n":
        return("n")
    elif fourth_formula[0] == "n":
        return("n")
    else: #calculates potential "u"-values of first value
        return("u")

def total_formula_deduction_first_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[0] == "a" and second_formula[1] == "n":    #calculates potential "a"-values of first value
        return("a")
    elif first_formula[0] == "a" and third_formula[1] == "n":
        return("a")
    elif first_formula[0] == "a" and fourth_formula[1] == "n":
        return("a")
    elif second_formula[0] == "a" and first_formula[2] == "n":
        return("a")
    elif second_formula[0] == "a" and third_formula[2] == "n":
        return("a")
    elif second_formula[0] == "a" and fourth_formula[4] == "n":
        return("a")
    elif third_formula[0] == "a" and first_formula[1] == "n":
        return("a")
    elif third_formula[0] == "a" and second_formula[2] == "n":
        return("a")
    elif third_formula[0] == "a" and fourth_formula[2] == "n":
        return("a")
    elif fourth_formula[0] == "a" and first_formula[4] == "n":
        return("a")
    elif fourth_formula[0] == "a" and second_formula[4] == "n":
        return("a")
    elif fourth_formula[0] == "a" and third_formula[4] == "n":
        return("a")
    else: #calculates potential "u"-values of first value
        return("u")

def total_formula_deduction_second_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[0] == "n":    #caluculates potential "n"-values of second value
        return("n")
    elif second_formula[1] == "n":
        return("n")
    elif third_formula[1] == "n":
        return("n")
    elif fourth_formula[1] == "n":
        return("n")
    else: #calculates potential "u"-values of second value
        return("u")

def total_formula_deduction_second_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[0] == "a" and second_formula[0] == "n":    #calculates potential "a"-values of second value
        return("a")
    elif first_formula[0] == "a" and third_formula[0] == "n":
        return("a")
    elif first_formula[0] == "a" and fourth_formula[0] == "n":
        return("a")
    elif second_formula[1] == "a" and first_formula[2] == "n":
        return("a")
    elif second_formula[1] == "a" and third_formula[3] == "n":
        return("a")
    elif second_formula[1] == "a" and fourth_formula[5] == "n":
        return("a")
    elif third_formula[1] == "a" and first_formula[1] == "n":
        return("a")
    elif third_formula[1] == "a" and second_formula[3] == "n":
        return("a")
    elif third_formula[1] == "a" and fourth_formula[3] == "n":
        return("a")
    elif fourth_formula[1] == "a" and first_formula[4] == "n":
        return("a")
    elif fourth_formula[1] == "a" and second_formula[5] == "n":
        return("a")
    elif fourth_formula[1] == "a" and third_formula[5] == "n":
        return("a")
    else: #calculates potential "u"-values of second value
        return("u")

def total_formula_deduction_third_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[1] == "n":    #caluculates potential "n"-values of third value
        return("n")
    elif second_formula[2] == "n":
        return("n")
    elif third_formula[0] == "n":
        return("n")
    elif fourth_formula[2] == "n":
        return("n")
    else: #calculates potential "u"-values of third value
        return("u")

def total_formula_deduction_third_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[1] == "a" and second_formula[3] == "n":    #calculates potential "a"-values of third value
        return("a")
    elif first_formula[1] == "a" and third_formula[1] == "n":
        return("a")
    elif first_formula[1] == "a" and fourth_formula[3] == "n":
        return("a")
    elif second_formula[2] == "a" and first_formula[3] == "n":
        return("a")
    elif second_formula[2] == "a" and third_formula[2] == "n":
        return("a")
    elif second_formula[2] == "a" and fourth_formula[6] == "n":
        return("a")
    elif third_formula[0] == "a" and first_formula[0] == "n":
        return("a")
    elif third_formula[0] == "a" and second_formula[0] == "n":
        return("a")
    elif third_formula[0] == "a" and fourth_formula[0] == "n":
        return("a")
    elif fourth_formula[2] == "a" and first_formula[5] == "n":
        return("a")
    elif fourth_formula[2] == "a" and second_formula[6] == "n":
        return("a")
    elif fourth_formula[2] == "a" and third_formula[4] == "n":
        return("a")
    else: #calculates potential "u"-values of third value
        return("u")

def total_formula_deduction_fourth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[1] == "n":    #caluculates potential "n"-values of fourth value
        return("n")
    elif second_formula[3] == "n":
        return("n")
    elif third_formula[1] == "n":
        return("n")
    elif fourth_formula[3] == "n":
        return("n")
    else: #calculates potential "u"-values of fourth value
        return("u")

def total_formula_deduction_fourth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[1] == "a" and second_formula[2] == "n":    #calculates potential "a"-values of fourth value
        return("a")
    elif first_formula[1] == "a" and third_formula[0] == "n":
        return("a")
    elif first_formula[1] == "a" and fourth_formula[2] == "n":
        return("a")
    elif second_formula[3] == "a" and first_formula[3] == "n":
        return("a")
    elif second_formula[3] == "a" and third_formula[3] == "n":
        return("a")
    elif second_formula[3] == "a" and fourth_formula[7] == "n":
        return("a")
    elif third_formula[1] == "a" and first_formula[0] == "n":
        return("a")
    elif third_formula[1] == "a" and second_formula[1] == "n":
        return("a")
    elif third_formula[1] == "a" and fourth_formula[1] == "n":
        return("a")
    elif fourth_formula[3] == "a" and first_formula[5] == "n":
        return("a")
    elif fourth_formula[3] == "a" and second_formula[7] == "n":
        return("a")
    elif fourth_formula[3] == "a" and third_formula[5] == "n":
        return("a")
    else: #calculates potential "u"-values of fourth value
        return("u")

def total_formula_deduction_fifth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[2] == "n":    #caluculates potential "n"-values of fifth value
        return("n")
    elif second_formula[0] == "n":
        return("n")
    elif third_formula[2] == "n":
        return("n")
    elif fourth_formula[4] == "n":
        return("n")
    else: #calculates potential "u"-values of fifth value
        return("u")

def total_formula_deduction_fifth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[2] == "a" and second_formula[1] == "n":    #calculates potential "a"-values of fifth value
        return("a")
    elif first_formula[2] == "a" and third_formula[3] == "n":
        return("a")
    elif first_formula[2] == "a" and fourth_formula[5] == "n":
        return("a")
    elif second_formula[0] == "a" and first_formula[0] == "n":
        return("a")
    elif second_formula[0] == "a" and third_formula[0] == "n":
        return("a")
    elif second_formula[0] == "a" and fourth_formula[0] == "n":
        return("a")
    elif third_formula[2] == "a" and first_formula[3] == "n":
        return("a")
    elif third_formula[2] == "a" and second_formula[2] == "n":
        return("a")
    elif third_formula[2] == "a" and fourth_formula[6] == "n":
        return("a")
    elif fourth_formula[4] == "a" and first_formula[6] == "n":
        return("a")
    elif fourth_formula[4] == "a" and second_formula[4] == "n":
        return("a")
    elif fourth_formula[4] == "a" and third_formula[6] == "n":
        return("a")
    else: #calculates potential "u"-values of fifth value
        return("u")

def total_formula_deduction_sixth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[2] == "n":    #caluculates potential "n"-values of sixth value
        return("n")
    elif second_formula[1] == "n":
        return("n")
    elif third_formula[3] == "n":
        return("n")
    elif fourth_formula[5] == "n":
        return("n")
    else: #calculates potential "u"-values of sixth value
        return("u")
    
def total_formula_deduction_sixth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[2] == "a" and second_formula[0] == "n":    #calculates potential "a"-values of sixth value
        return("a")
    elif first_formula[2] == "a" and third_formula[2] == "n":
        return("a")
    elif first_formula[2] == "a" and fourth_formula[4] == "n":
        return("a")
    elif second_formula[1] == "a" and first_formula[0] == "n":
        return("a")
    elif second_formula[1] == "a" and third_formula[1] == "n":
        return("a")
    elif second_formula[1] == "a" and fourth_formula[1] == "n":
        return("a")
    elif third_formula[3] == "a" and first_formula[3] == "n":
        return("a")
    elif third_formula[3] == "a" and second_formula[3] == "n":
        return("a")
    elif third_formula[3] == "a" and fourth_formula[7] == "n":
        return("a")
    elif fourth_formula[5] == "a" and first_formula[6] == "n":
        return("a")
    elif fourth_formula[5] == "a" and second_formula[5] == "n":
        return("a")
    elif fourth_formula[5] == "a" and third_formula[7] == "n":
        return("a")
    else: #calculates potential "u"-values of sixth value
        return("u")

def total_formula_deduction_seventh_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[3] == "n":    #caluculates potential "n"-values of sixth value
        return("n")
    elif second_formula[2] == "n":
        return("n")
    elif third_formula[2] == "n":
        return("n")
    elif fourth_formula[6] == "n":
        return("n")
    else: #calculates potential "u"-values of sixth value
        return("u")

def total_formula_deduction_seventh_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[3] == "a" and second_formula[3] == "n":    #calculates potential "a"-values of sixth value
        return("a")
    elif first_formula[3] == "a" and third_formula[3] == "n":
        return("a")
    elif first_formula[3] == "a" and fourth_formula[7] == "n":
        return("a")
    elif second_formula[2] == "a" and first_formula[1] == "n":
        return("a")
    elif second_formula[2] == "a" and third_formula[0] == "n":
        return("a")
    elif second_formula[2] == "a" and fourth_formula[2] == "n":
        return("a")
    elif third_formula[2] == "a" and first_formula[2] == "n":
        return("a")
    elif third_formula[2] == "a" and second_formula[0] == "n":
        return("a")
    elif third_formula[2] == "a" and fourth_formula[4] == "n":
        return("a")
    elif fourth_formula[6] == "a" and first_formula[7] == "n":
        return("a")
    elif fourth_formula[6] == "a" and second_formula[6] == "n":
        return("a")
    elif fourth_formula[6] == "a" and third_formula[6] == "n":
        return("a")
    else: #calculates potential "u"-values of sixth value
        return("u")

def total_formula_deduction_eighth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[3] == "n":    #caluculates potential "n"-values of eighth value
        return("n")
    elif second_formula[3] == "n":
        return("n")
    elif third_formula[3] == "n":
        return("n")
    elif fourth_formula[7] == "n":
        return("n")
    else: #calculates potential "u"-values of eighth value
        return("u")

def total_formula_deduction_eighth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[3] == "a" and second_formula[2] == "n":    #calculates potential "a"-values of eighth value
        return("a")
    elif first_formula[3] == "a" and third_formula[2] == "n":
        return("a")
    elif first_formula[3] == "a" and fourth_formula[6] == "n":
        return("a")
    elif second_formula[3] == "a" and first_formula[1] == "n":
        return("a")
    elif second_formula[3] == "a" and third_formula[1] == "n":
        return("a")
    elif second_formula[3] == "a" and fourth_formula[3] == "n":
        return("a")
    elif third_formula[3] == "a" and first_formula[2] == "n":
        return("a")
    elif third_formula[3] == "a" and second_formula[1] == "n":
        return("a")
    elif third_formula[3] == "a" and fourth_formula[5] == "n":
        return("a")
    elif fourth_formula[7] == "a" and first_formula[7] == "n":
        return("a")
    elif fourth_formula[7] == "a" and second_formula[7] == "n":
        return("a")
    elif fourth_formula[7] == "a" and third_formula[7] == "n":
        return("a")
    else: #calculates potential "u"-values of eighth value
        return("u")
    

def total_formula_deduction_ninth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[4] == "n":    #caluculates potential "n"-values of ninth value
        return("n")
    elif second_formula[4] == "n":
        return("n")
    elif third_formula[4] == "n":
        return("n")
    elif fourth_formula[0] == "n":
        return("n")
    else: #calculates potential "u"-values of ninth value
        return("u")

def total_formula_deduction_ninth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[4] == "a" and second_formula[5] == "n":    #calculates potential "a"-values of ninth value
        return("a")
    elif first_formula[4] == "a" and third_formula[5] == "n":
        return("a")
    elif first_formula[4] == "a" and fourth_formula[1] == "n":
        return("a")
    elif second_formula[4] == "a" and first_formula[6] == "n":
        return("a")
    elif second_formula[4] == "a" and third_formula[6] == "n":
        return("a")
    elif second_formula[4] == "a" and fourth_formula[4] == "n":
        return("a")
    elif third_formula[4] == "a" and first_formula[5] == "n":
        return("a")
    elif third_formula[4] == "a" and second_formula[6] == "n":
        return("a")
    elif third_formula[4] == "a" and fourth_formula[2] == "n":
        return("a")
    elif fourth_formula[0] == "a" and first_formula[0] == "n":
        return("a")
    elif fourth_formula[0] == "a" and second_formula[0] == "n":
        return("a")
    elif fourth_formula[0] == "a" and third_formula[0] == "n":
        return("a")
    else: #calculates potential "u"-values of ninth value
        return("u")

def total_formula_deduction_tenth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[4] == "n":    #caluculates potential "n"-values of tenth value
        return("n")
    elif second_formula[5] == "n":
        return("n")
    elif third_formula[5] == "n":
        return("n")
    elif fourth_formula[1] == "n":
        return("n")
    else: #calculates potential "u"-values of tenth value
        return("u")

def total_formula_deduction_tenth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[4] == "a" and second_formula[4] == "n":    #calculates potential "a"-values of tenth value
        return("a")
    elif first_formula[4] == "a" and third_formula[4] == "n":
        return("a")
    elif first_formula[4] == "a" and fourth_formula[0] == "n":
        return("a")
    elif second_formula[5] == "a" and first_formula[6] == "n":
        return("a")
    elif second_formula[5] == "a" and third_formula[7] == "n":
        return("a")
    elif second_formula[5] == "a" and fourth_formula[5] == "n":
        return("a")
    elif third_formula[5] == "a" and first_formula[5] == "n":
        return("a")
    elif third_formula[5] == "a" and second_formula[7] == "n":
        return("a")
    elif third_formula[5] == "a" and fourth_formula[3] == "n":
        return("a")
    elif fourth_formula[1] == "a" and first_formula[0] == "n":
        return("a")
    elif fourth_formula[1] == "a" and second_formula[1] == "n":
        return("a")
    elif fourth_formula[1] == "a" and third_formula[1] == "n":
        return("a")
    else: #calculates potential "u"-values of tenth value
        return("u")

def total_formula_deduction_eleventh_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[5] == "n":    #caluculates potential "n"-values of eleventh value
        return("n")
    elif second_formula[6] == "n":
        return("n")
    elif third_formula[4] == "n":
        return("n")
    elif fourth_formula[2] == "n":
        return("n")
    else: #calculates potential "u"-values of eleventh value
        return("u")

def total_formula_deduction_eleventh_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[5] == "a" and second_formula[7] == "n":    #calculates potential "a"-values of eleventh value
        return("a")
    elif first_formula[5] == "a" and third_formula[5] == "n":
        return("a")
    elif first_formula[5] == "a" and fourth_formula[3] == "n":
        return("a")
    elif second_formula[6] == "a" and first_formula[7] == "n":
        return("a")
    elif second_formula[6] == "a" and third_formula[6] == "n":
        return("a")
    elif second_formula[6] == "a" and fourth_formula[6] == "n":
        return("a")
    elif third_formula[4] == "a" and first_formula[4] == "n":
        return("a")
    elif third_formula[4] == "a" and second_formula[4] == "n":
        return("a")
    elif third_formula[4] == "a" and fourth_formula[0] == "n":
        return("a")
    elif fourth_formula[2] == "a" and first_formula[1] == "n":
        return("a")
    elif fourth_formula[2] == "a" and second_formula[2] == "n":
        return("a")
    elif fourth_formula[2] == "a" and third_formula[0] == "n":
        return("a")
    else: #calculates potential "u"-values of eleventh value
        return("u")

def total_formula_deduction_twelveth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[5] == "n":    #caluculates potential "n"-values of twelveth value
        return("n")
    elif second_formula[7] == "n":
        return("n")
    elif third_formula[5] == "n":
        return("n")
    elif fourth_formula[3] == "n":
        return("n")
    else: #calculates potential "u"-values of twelveth value
        return("u")

def total_formula_deduction_twelveth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[5] == "a" and second_formula[6] == "n":    #calculates potential "a"-values of twelveth value
        return("a")
    elif first_formula[5] == "a" and third_formula[4] == "n":
        return("a")
    elif first_formula[5] == "a" and fourth_formula[2] == "n":
        return("a")
    elif second_formula[7] == "a" and first_formula[7] == "n":
        return("a")
    elif second_formula[7] == "a" and third_formula[7] == "n":
        return("a")
    elif second_formula[7] == "a" and fourth_formula[7] == "n":
        return("a")
    elif third_formula[5] == "a" and first_formula[4] == "n":
        return("a")
    elif third_formula[5] == "a" and second_formula[5] == "n":
        return("a")
    elif third_formula[5] == "a" and fourth_formula[1] == "n":
        return("a")
    elif fourth_formula[3] == "a" and first_formula[1] == "n":
        return("a")
    elif fourth_formula[3] == "a" and second_formula[3] == "n":
        return("a")
    elif fourth_formula[3] == "a" and third_formula[1] == "n":
        return("a")
    else: #calculates potential "u"-values of twelveth value
        return("u")

def total_formula_deduction_thirdteenth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[6] == "n":    #caluculates potential "n"-values of thirdteenth value
        return("n")
    elif second_formula[4] == "n":
        return("n")
    elif third_formula[6] == "n":
        return("n")
    elif fourth_formula[4] == "n":
        return("n")
    else: #calculates potential "u"-values of thirdteenth value
        return("u")

def total_formula_deduction_thirdteenth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[6] == "a" and second_formula[5] == "n":    #calculates potential "a"-values of thirdteenth value
        return("a")
    elif first_formula[6] == "a" and third_formula[7] == "n":
        return("a")
    elif first_formula[6] == "a" and fourth_formula[5] == "n":
        return("a")
    elif second_formula[4] == "a" and first_formula[4] == "n":
        return("a")
    elif second_formula[4] == "a" and third_formula[4] == "n":
        return("a")
    elif second_formula[4] == "a" and fourth_formula[0] == "n":
        return("a")
    elif third_formula[6] == "a" and first_formula[7] == "n":
        return("a")
    elif third_formula[6] == "a" and second_formula[6] == "n":
        return("a")
    elif third_formula[6] == "a" and fourth_formula[6] == "n":
        return("a")
    elif fourth_formula[4] == "a" and first_formula[2] == "n":
        return("a")
    elif fourth_formula[4] == "a" and second_formula[0] == "n":
        return("a")
    elif fourth_formula[4] == "a" and third_formula[2] == "n":
        return("a")
    else: #calculates potential "u"-values of thirdteenth value
        return("u")

def total_formula_deduction_fourteenth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[6] == "n":    #caluculates potential "n"-values of fourteenth value
        return("n")
    elif second_formula[5] == "n":
        return("n")
    elif third_formula[7] == "n":
        return("n")
    elif fourth_formula[5] == "n":
        return("n")
    else: #calculates potential "u"-values of fourteenth value
        return("u")

def total_formula_deduction_fourteenth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[6] == "a" and second_formula[4] == "n":    #calculates potential "a"-values of fourteenth value
        return("a")
    elif first_formula[6] == "a" and third_formula[6] == "n":
        return("a")
    elif first_formula[6] == "a" and fourth_formula[4] == "n":
        return("a")
    elif second_formula[5] == "a" and first_formula[4] == "n":
        return("a")
    elif second_formula[5] == "a" and third_formula[5] == "n":
        return("a")
    elif second_formula[5] == "a" and fourth_formula[1] == "n":
        return("a")
    elif third_formula[7] == "a" and first_formula[7] == "n":
        return("a")
    elif third_formula[7] == "a" and second_formula[7] == "n":
        return("a")
    elif third_formula[7] == "a" and fourth_formula[7] == "n":
        return("a")
    elif fourth_formula[5] == "a" and first_formula[2] == "n":
        return("a")
    elif fourth_formula[5] == "a" and second_formula[1] == "n":
        return("a")
    elif fourth_formula[5] == "a" and third_formula[3] == "n":
        return("a")
    else: #calculates potential "u"-values of fourteenth value
        return("u")

def total_formula_deduction_fifteenth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[7] == "n":    #caluculates potential "n"-values of fifthteenth value
        return("n")
    elif second_formula[6] == "n":
        return("n")
    elif third_formula[6] == "n":
        return("n")
    elif fourth_formula[6] == "n":
        return("n")
    else: #calculates potential "u"-values of fifthteenth value
        return("u")

def total_formula_deduction_fifteenth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[7] == "a" and second_formula[7] == "n":    #calculates potential "a"-values of fifthteenth value
        return("a")
    elif first_formula[7] == "a" and third_formula[7] == "n":
        return("a")
    elif first_formula[7] == "a" and fourth_formula[7] == "n":
        return("a")
    elif second_formula[6] == "a" and first_formula[5] == "n":
        return("a")
    elif second_formula[6] == "a" and third_formula[4] == "n":
        return("a")
    elif second_formula[6] == "a" and fourth_formula[2] == "n":
        return("a")
    elif third_formula[6] == "a" and first_formula[6] == "n":
        return("a")
    elif third_formula[6] == "a" and second_formula[4] == "n":
        return("a")
    elif third_formula[6] == "a" and fourth_formula[4] == "n":
        return("a")
    elif fourth_formula[6] == "a" and first_formula[3] == "n":
        return("a")
    elif fourth_formula[6] == "a" and second_formula[2] == "n":
        return("a")
    elif fourth_formula[6] == "a" and third_formula[2] == "n":
        return("a")
    else: #calculates potential "u"-values of fifthteenth value
        return("u")

def total_formula_deduction_sixteenth_value_n_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[7] == "n":    #caluculates potential "n"-values of sixteenth value
        return("n")
    elif second_formula[7] == "n":
        return("n")
    elif third_formula[7] == "n":
        return("n")
    elif fourth_formula[7] == "n":
        return("n")
    else: #calculates potential "u"-values of sixteenth value
        return("u")

def total_formula_deduction_sixteenth_value_a_tet( first_formula,second_formula,third_formula,fourth_formula):
    if first_formula[7] == "a" and second_formula[6] == "n":    #calculates potential "a"-values of sixteenth value
        return("a")
    elif first_formula[7] == "a" and third_formula[6] == "n":
        return("a")
    elif first_formula[7] == "a" and fourth_formula[6] == "n":
        return("a")
    elif second_formula[7] == "a" and first_formula[5] == "n":
        return("a")
    elif second_formula[7] == "a" and third_formula[5] == "n":
        return("a")
    elif second_formula[7] == "a" and fourth_formula[3] == "n":
        return("a")
    elif third_formula[7] == "a" and first_formula[6] == "n":
        return("a")
    elif third_formula[7] == "a" and second_formula[5] == "n":
        return("a")
    elif third_formula[7] == "a" and fourth_formula[5] == "n":
        return("a")
    elif fourth_formula[7] == "a" and first_formula[3] == "n":
        return("a")
    elif fourth_formula[7] == "a" and second_formula[3] == "n":
        return("a")
    elif fourth_formula[7] == "a" and third_formula[3] == "n":
        return("a")
    else: #calculates potential "u"-values of sixteenth value
        return("u")

def syllogism_contradiction_test_tet( first_formula, second_formula, third_formula, fourth_formula):

    conclusion = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    conclusion[0] = total_formula_deduction_first_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[1] = total_formula_deduction_first_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if conclusion[0] == 'n' and conclusion[1] == 'a':
        return ('W')
    conclusion[2] = total_formula_deduction_second_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[3] = total_formula_deduction_second_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if conclusion[2] == 'n' and conclusion[3] == 'a':
        return ('W')
    conclusion[4] = total_formula_deduction_third_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[5] = total_formula_deduction_third_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if conclusion[4] == 'n' and conclusion[5] == 'a':
        return ('W')
    conclusion[6] = total_formula_deduction_fourth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[7] = total_formula_deduction_fourth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if conclusion[6] == 'n' and conclusion[7] == 'a':
        return ('W')
    conclusion[8] = total_formula_deduction_fifth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[9] = total_formula_deduction_fifth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if conclusion[8] == 'n' and conclusion[9] == 'a':
        return ('W')
    conclusion[10] = total_formula_deduction_sixth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[11] = total_formula_deduction_sixth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if conclusion[10] == 'n' and conclusion[11] == 'a':
        return ('W')
    conclusion[12] = total_formula_deduction_seventh_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[13] = total_formula_deduction_seventh_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if conclusion[12] == 'n' and conclusion[13] == 'a':
        return ('W')
    conclusion[14] = total_formula_deduction_eighth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[15] = total_formula_deduction_eighth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if conclusion[14] == 'n' and conclusion[15] == 'a':
        return ('W')
    conclusion[16] = total_formula_deduction_ninth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[17] = total_formula_deduction_ninth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if conclusion[16] == 'n' and conclusion[17] == 'a':
        return ('W')
    conclusion[18] = total_formula_deduction_tenth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[19] = total_formula_deduction_tenth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if conclusion[18] == 'n' and conclusion[19] == 'a':
        return ('W')
    conclusion[20] = total_formula_deduction_eleventh_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[21] = total_formula_deduction_eleventh_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if conclusion[20] == 'n' and conclusion[21] == 'a':
        return ('W')
    conclusion[22] = total_formula_deduction_twelveth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[23] = total_formula_deduction_twelveth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if conclusion[22] == 'n' and conclusion[23] == 'a':
        return ('W')
    conclusion[24] = total_formula_deduction_thirdteenth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[25] = total_formula_deduction_thirdteenth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if conclusion[24] == 'n' and conclusion[25] == 'a':
        return ('W')
    conclusion[26] = total_formula_deduction_fourteenth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[27] = total_formula_deduction_fourteenth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if conclusion[26] == 'n' and conclusion[27] == 'a':
        return ('W')
    conclusion[28] = total_formula_deduction_fifteenth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[29] = total_formula_deduction_fifteenth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if conclusion[28] == 'n' and conclusion[29] == 'a':
        return ('W')
    conclusion[30] = total_formula_deduction_sixteenth_value_n_tet(first_formula, second_formula, third_formula, fourth_formula)
    conclusion[31] = total_formula_deduction_sixteenth_value_a_tet(first_formula, second_formula, third_formula, fourth_formula)
    if conclusion[30] == 'n' and conclusion[31] == 'a':
        return ('W')

    conclusion_solution = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        
    for i in range(16):

        if conclusion_solution[i] == 0 or conclusion_solution[i] == 'u':

            if conclusion[2*i] == 'a':
                conclusion_solution[i] = 'a'
            elif conclusion[2*i] == 'n':
                conclusion_solution[i] = 'n'
            elif conclusion[2*i+1] == 'a':
                conclusion_solution[i] = 'a'
            elif conclusion[2*i+1] == 'n':
                conclusion_solution[i] = 'n'
            else:
                conclusion_solution[i] = 'u'
        
    return (conclusion_solution, 'kW')


def triadic_name_fn( formula, index_premis_circumstance):
    
    list_formulas_names = [[['a', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 1']],\
                            [['a', 'a', 'a', 'a', 'a', 'a', 'a', 'n'], ['$B$\textbullet$C$\textbullet$D$ 2']],\
                            [['a', 'a', 'a', 'n', 'a', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 3']],\
                            [['a', 'a', 'a', 'n', 'a', 'a', 'a', 'n'], ['$B\\sqcup C, C\\cup D, B\\cup D, 1A, 5A$']],\
                            [['a', 'a', 'a', 'a', 'a', 'n', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 5']],\
                            [['a', 'a', 'a', 'a', 'a', 'n', 'a', 'n'], ['$B\\cup C, C\\cup D, B\\sqcup D, 1A, 3A$']],\
                            [['a', 'a', 'a', 'n', 'a', 'n', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 7']],\
                            [['a', 'a', 'a', 'n', 'a', 'n', 'a', 'n'], ['$B\\sqcup C, C\\cup D, B\\sqcup D, 1A$']],\
                            [['a', 'n', 'a', 'a', 'a', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 9']],\
                            [['a', 'n', 'a', 'a', 'a', 'a', 'a', 'n'], ['$B$\textbullet$C$\textbullet$D$ 10']],\
                            [['a', 'n', 'a', 'n', 'a', 'a', 'a', 'a'], ['$B\\cup C, C\\cup D, B\\subset D, 5A, 7A$']],\
                            [['a', 'n', 'a', 'n', 'a', 'a', 'a', 'n'], ['$B\\sqcup C, C\\cup D, B\\subset D, 5A$']],\
                            [['a', 'n', 'a', 'a', 'a', 'n', 'a', 'a'], ['$B\\subset C, C\\cup D, B\\cup D, 3A, 7A$']],\
                            [['a', 'n', 'a', 'a', 'a', 'n', 'a', 'n'], ['$B\\subset C, C\\cup D, B\\sqcup D, 3A$']],\
                            [['a', 'n', 'a', 'n', 'a', 'n', 'a', 'a'], ['$B\\subset C, C\\cup D, B\\subset D, 7A$']],\
                            [['a', 'n', 'a', 'n', 'a', 'n', 'a', 'n'], ['$B\\sqsubset C, C\\cup D, B\\sqsubset D$']],\
                            [['a', 'a', 'a', 'a', 'a', 'a', 'n', 'a'], ['$B$\textbullet$C$\textbullet$D$ 17']],\
                            [['a', 'a', 'a', 'a', 'a', 'a', 'n', 'n'], ['$B\\cup C, C\\sqcup D, B\\cup D, 1A, 2A$']],\
                            [['a', 'a', 'a', 'n', 'a', 'a', 'n', 'a'], ['$B$\textbullet$C$\textbullet$D$ 19']],\
                            [['a', 'a', 'a', 'n', 'a', 'a', 'n', 'n'], ['$B\\sqcup C, C\\sqcup D, B\\cup D, 1A$']],\
                            [['a', 'a', 'a', 'a', 'a', 'n', 'n', 'a'], ['$B$\textbullet$C$\textbullet$D$ 21']],\
                            [['a', 'a', 'a', 'a', 'a', 'n', 'n', 'n'], ['$B\\cup C, C\\sqcup D, B\\sqcup D, 1A$']],\
                            [['a', 'a', 'a', 'n', 'a', 'n', 'n', 'a'], ['$B$\textbullet$C$\textbullet$D$ 23']],\
                            [['a', 'a', 'a', 'n', 'a', 'n', 'n', 'n'], ['$B\\sqcup C, C\\sqcup D, B\\sqcup D, 1A$']],\
                            [['a', 'n', 'a', 'a', 'a', 'a', 'n', 'a'], ['$B$\textbullet$C$\textbullet$D$ 25']],\
                            [['a', 'n', 'a', 'a', 'a', 'a', 'n', 'n'], ['$B\\cup C, C\\sqcup D, B\\cup D, 1A, 2N$']],\
                            [['a', 'n', 'a', 'n', 'a', 'a', 'n', 'a'], ['$B\\cup C, C\\cup D, B\\subset D, 5A, 7N$']],\
                            [['a', 'n', 'a', 'n', 'a', 'a', 'n', 'n'], ['$B\\sqcup C, C\\sqcup D, B\\subset D$']],\
                            [['a', 'n', 'a', 'a', 'a', 'n', 'n', 'a'], ['$B\\subset C, C\\cup D, B\\cup D, 3A, 7N$']],\
                            [['a', 'n', 'a', 'a', 'a', 'n', 'n', 'n'], ['$B\\subset C, C\\sqcup D, B\\sqcup D$']],\
                            [['a', 'n', 'a', 'n', 'a', 'n', 'n', 'a'], ['$B\\subset C, C\\cup D, B\\subset D, 7N$']],\
                            [['a', 'n', 'a', 'n', 'a', 'n', 'n', 'n'], ['$B\\sqsubset C, C\\sqcup D, B\\sqsubset D$']],\
                            [['a', 'a', 'n', 'a', 'a', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 33']],\
                            [['a', 'a', 'n', 'a', 'a', 'a', 'a', 'n'], ['$B$\textbullet$C$\textbullet$D$ 34']],\
                            [['a', 'a', 'n', 'n', 'a', 'a', 'a', 'a'], ['$B\\cup C, C\\subset D, B\\cup D, 5A, 6A$']],\
                            [['a', 'a', 'n', 'n', 'a', 'a', 'a', 'n'], ['$B\\sqcup C, C\\subset D, B\\cup D, 5A$']],\
                            [['a', 'a', 'n', 'a', 'a', 'n', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 37']],\
                            [['a', 'a', 'n', 'a', 'a', 'n', 'a', 'n'], ['$B\\cup C, C\\cup D, B\\sqcup D, 1A, 3N$']],\
                            [['a', 'a', 'n', 'n', 'a', 'n', 'a', 'a'], ['$B\\cup C, C\\subset D, B\\cup D, 5A, 6N$']],\
                            [['a', 'a', 'n', 'n', 'a', 'n', 'a', 'n'], ['$B\\sqcup C, C\\subset D, B\\sqcup D$']],\
                            [['a', 'n', 'n', 'a', 'a', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 41']],\
                            [['a', 'n', 'n', 'a', 'a', 'a', 'a', 'n'], ['$B$\textbullet$C$\textbullet$D$ 42']],\
                            [['a', 'n', 'n', 'n', 'a', 'a', 'a', 'a'], ['$B\\cup C, C\\subset D, B\\subset D, 5A$']],\
                            [['a', 'n', 'n', 'n', 'a', 'a', 'a', 'n'], ['$B\\sqcup C, C\\subset D, B\\subset D, 5A$']],\
                            [['a', 'n', 'n', 'a', 'a', 'n', 'a', 'a'], ['$B\\subset C, C\\cup D, B\\cup D, 3N, 7A$']],\
                            [['a', 'n', 'n', 'a', 'a', 'n', 'a', 'n'], ['$B\\subset C, C\\cup D, B\\sqcup D, 3N$']],\
                            [['a', 'n', 'n', 'n', 'a', 'n', 'a', 'a'], ['$B\\subset C, C\\subset D, B\\subset D$']],\
                            [['a', 'n', 'n', 'n', 'a', 'n', 'a', 'n'], ['$B\\sqsubset C, C\\subset D, B\\sqsubset D$']],\
                            [['a', 'a', 'n', 'a', 'a', 'a', 'n', 'a'], ['$B\\supset C, C\\cup D, B\\cup D, 2A, 6A$']],\
                            [['a', 'a', 'n', 'a', 'a', 'a', 'n', 'n'], ['$B\\supset C, C\\sqcup D, B\\cup D, 2A$']],\
                            [['a', 'a', 'n', 'n', 'a', 'a', 'n', 'a'], ['$B\\supset C, C\\subset D, B\\cup D, 6A$']],\
                            [['a', 'a', 'n', 'n', 'a', 'a', 'n', 'n'], ['$B\\sqsupset C, C\\sqsubset D, B\\cup D$']],\
                            [['a', 'a', 'n', 'a', 'a', 'n', 'n', 'a'], ['$B\\supset C, C\\cup D, B\\cup D, 2A, 6N$']],\
                            [['a', 'a', 'n', 'a', 'a', 'n', 'n', 'n'], ['$B\\supset C, C\\sqcup D, B\\sqcup D$']],\
                            [['a', 'a', 'n', 'n', 'a', 'n', 'n', 'a'], ['$B\\supset C, C\\subset D, B\\cup D, 6N$']],\
                            [['a', 'a', 'n', 'n', 'a', 'n', 'n', 'n'], ['$B\\sqsupset C, C\\sqsubset D, B\\sqcup D$']],\
                            [['a', 'n', 'n', 'a', 'a', 'a', 'n', 'a'], ['$B\\supset C, C\\cup D, B\\cup D, 2N, 6A$']],\
                            [['a', 'n', 'n', 'a', 'a', 'a', 'n', 'n'], ['$B\\supset C, C\\sqcup D, B\\cup D, 2N$']],\
                            [['a', 'n', 'n', 'n', 'a', 'a', 'n', 'a'], ['$B\\supset C, C\\subset D, B\\subset D$']],\
                            [['a', 'n', 'n', 'n', 'a', 'a', 'n', 'n'], ['$B\\sqsupset C, C\\sqsubset D, B\\subset D$']],\
                            [['a', 'n', 'n', 'a', 'a', 'n', 'n', 'a'], ['$B\\cap C, C\\cup D, B\\cup D$']],\
                            [['a', 'n', 'n', 'a', 'a', 'n', 'n', 'n'], ['$B\\cap C, C\\sqcup D, B\\sqcup D$']],\
                            [['a', 'n', 'n', 'n', 'a', 'n', 'n', 'a'], ['$B\\cap C, C\\subset D, B\\subset D$']],\
                            [['a', 'n', 'n', 'n', 'a', 'n', 'n', 'n'], ['$B\\sqcap C, C\\sqsubset D, B\\sqsubset D$']],\
                            [['a', 'a', 'a', 'a', 'n', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 65']],\
                            [['a', 'a', 'a', 'a', 'n', 'a', 'a', 'n'], ['$B$\textbullet$C$\textbullet$D$ 66']],\
                            [['a', 'a', 'a', 'n', 'n', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 67']],\
                            [['a', 'a', 'a', 'n', 'n', 'a', 'a', 'n'], ['$B\\sqcup C, C\\cup D, B\\cup D, 1A, 5N$']],\
                            [['a', 'a', 'a', 'a', 'n', 'n', 'a', 'a'], ['$B\\cup C, C\\supset D, B\\cup D, 3A, 4A$']],\
                            [['a', 'a', 'a', 'a', 'n', 'n', 'a', 'n'], ['$B\\cup C, C\\supset D, B\\sqcup D, 3A$']],\
                            [['a', 'a', 'a', 'n', 'n', 'n', 'a', 'a'], ['$B\\cup C, C\\supset D, B\\cup D, 3A, 4N$']],\
                            [['a', 'a', 'a', 'n', 'n', 'n', 'a', 'n'], ['$B\\sqcup C, C\\supset D, B\\sqcup D$']],\
                            [['a', 'n', 'a', 'a', 'n', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 73']],\
                            [['a', 'n', 'a', 'a', 'n', 'a', 'a', 'n'], ['$B$\textbullet$C$\textbullet$D$ 74']],\
                            [['a', 'n', 'a', 'n', 'n', 'a', 'a', 'a'], ['$B\\cup C, C\\cup D, B\\subset D, 5N, 7A$']],\
                            [['a', 'n', 'a', 'n', 'n', 'a', 'a', 'n'], ['$B\\sqcup C, C\\cup D, B\\subset D, 5N$']],\
                            [['a', 'n', 'a', 'a', 'n', 'n', 'a', 'a'], ['$B\\subset C, C\\supset D, B\\cup D, 3A$']],\
                            [['a', 'n', 'a', 'a', 'n', 'n', 'a', 'n'], ['$B\\subset C, C\\supset D, B\\sqcup D, 3A$']],\
                            [['a', 'n', 'a', 'n', 'n', 'n', 'a', 'a'], ['$B\\subset C, C\\supset D, B\\subset D$']],\
                            [['a', 'n', 'a', 'n', 'n', 'n', 'a', 'n'], ['$B\\sqsubset C, C\\supset D, B\\sqsubset D$']],\
                            [['a', 'a', 'a', 'a', 'n', 'a', 'n', 'a'], ['$B\\cup C, C\\cup D, B\\supset D, 2A, 4A$']],\
                            [['a', 'a', 'a', 'a', 'n', 'a', 'n', 'n'], ['$B\\cup C, C\\sqcup D, B\\supset D, 2A$']],\
                            [['a', 'a', 'a', 'n', 'n', 'a', 'n', 'a'], ['$B\\cup C, C\\cup D, B\\supset D, 2A, 4N$']],\
                            [['a', 'a', 'a', 'n', 'n', 'a', 'n', 'n'], ['$B\\sqcup C, C\\sqcup D, B\\supset D$']],\
                            [['a', 'a', 'a', 'a', 'n', 'n', 'n', 'a'], ['$B\\cup C, C\\supset D, B\\supset D, 4A$']],\
                            [['a', 'a', 'a', 'a', 'n', 'n', 'n', 'n'], ['$B\\cup C, C\\sqsupset D, B\\sqsupset D$']],\
                            [['a', 'a', 'a', 'n', 'n', 'n', 'n', 'a'], ['$B\\cup C, C\\supset D, B\\supset D, 4N$']],\
                            [['a', 'a', 'a', 'n', 'n', 'n', 'n', 'n'], ['$B\\sqcup C, C\\sqsupset D, B\\sqsupset D$']],\
                            [['a', 'n', 'a', 'a', 'n', 'a', 'n', 'a'], ['$B\\cup C, C\\cup D, B\\supset D, 2N, 4A$']],\
                            [['a', 'n', 'a', 'a', 'n', 'a', 'n', 'n'], ['$B\\cup C, C\\sqcup D, B\\supset D, 2N$']],\
                            [['a', 'n', 'a', 'n', 'n', 'a', 'n', 'a'], ['$B\\cup C, C\\cup D, B\\cap D$']],\
                            [['a', 'n', 'a', 'n', 'n', 'a', 'n', 'n'], ['$B\\sqcup C, C\\sqcup D, B\\cap D$']],\
                            [['a', 'n', 'a', 'a', 'n', 'n', 'n', 'a'], ['$B\\subset C, C\\supset D, B\\supset D$']],\
                            [['a', 'n', 'a', 'a', 'n', 'n', 'n', 'n'], ['$B\\subset C, C\\sqsupset D, B\\sqsupset D$']],\
                            [['a', 'n', 'a', 'n', 'n', 'n', 'n', 'a'], ['$B\\subset C, C\\supset D, B\\cap D$']],\
                            [['a', 'n', 'a', 'n', 'n', 'n', 'n', 'n'], ['$B\\sqsubset C, C\\sqsupset D, B\\sqcap D$']],\
                            [['a', 'a', 'n', 'a', 'n', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 97']],\
                            [['a', 'a', 'n', 'a', 'n', 'a', 'a', 'n'], ['$B$\textbullet$C$\textbullet$D$ 98']],\
                            [['a', 'a', 'n', 'n', 'n', 'a', 'a', 'a'], ['$B\\cup C, C\\subset D, B\\cup D, 5N, 6A$']],\
                            [['a', 'a', 'n', 'n', 'n', 'a', 'a', 'n'], ['$B\\sqcup C, C\\subset D, B\\cup D, 5N$']],\
                            [['a', 'a', 'n', 'a', 'n', 'n', 'a', 'a'], ['$B\\cup C, C\\supset D, B\\cup D, 3N, 4A$']],\
                            [['a', 'a', 'n', 'a', 'n', 'n', 'a', 'n'], ['$B\\cup C, C\\supset D, B\\sqcup D, 3N$']],\
                            [['a', 'a', 'n', 'n', 'n', 'n', 'a', 'a'], ['$B\\cup C, C\\cap D, B\\cup D$']],\
                            [['a', 'a', 'n', 'n', 'n', 'n', 'a', 'n'], ['$B\\sqcup C, C\\cap D, B\\sqcup D$']],\
                            [['a', 'n', 'n', 'a', 'n', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 105']],\
                            [['a', 'n', 'n', 'a', 'n', 'a', 'a', 'n'], ['$B$\textbullet$C$\textbullet$D$ 106']],\
                            [['a', 'n', 'n', 'n', 'n', 'a', 'a', 'a'], ['$B\\cup C, C\\subset D, B\\subset D, 5N$']],\
                            [['a', 'n', 'n', 'n', 'n', 'a', 'a', 'n'], ['$B\\sqcup C, C\\subset D, B\\subset D, 5N$']],\
                            [['a', 'n', 'n', 'a', 'n', 'n', 'a', 'a'], ['$B\\subset C, C\\supset D, B\\cup D, 3N$']],\
                            [['a', 'n', 'n', 'a', 'n', 'n', 'a', 'n'], ['$B\\subset C, C\\supset D, B\\sqcup D, 3N$']],\
                            [['a', 'n', 'n', 'n', 'n', 'n', 'a', 'a'], ['$B\\subset C, C\\cap D, B\\subset D$']],\
                            [['a', 'n', 'n', 'n', 'n', 'n', 'a', 'n'], ['$B\\sqsubset C, C\\cap D, B\\sqsubset D$']],\
                            [['a', 'a', 'n', 'a', 'n', 'a', 'n', 'a'], ['$B\\supset C, C\\cup D, B\\supset D, 2A$']],\
                            [['a', 'a', 'n', 'a', 'n', 'a', 'n', 'n'], ['$B\\supset C, C\\sqcup D, B\\supset D, 2A$']],\
                            [['a', 'a', 'n', 'n', 'n', 'a', 'n', 'a'], ['$B\\supset C, C\\subset D, B\\supset D$']],\
                            [['a', 'a', 'n', 'n', 'n', 'a', 'n', 'n'], ['$B\\sqsupset C, C\\sqsubset D, B\\supset D$']],\
                            [['a', 'a', 'n', 'a', 'n', 'n', 'n', 'a'], ['$B\\supset C, C\\supset D, B\\supset D$']],\
                            [['a', 'a', 'n', 'a', 'n', 'n', 'n', 'n'], ['$B\\supset C, C\\sqsupset D, B\\sqsupset D$']],\
                            [['a', 'a', 'n', 'n', 'n', 'n', 'n', 'a'], ['$B\\supset C, C\\cap D, B\\supset D$']],\
                            [['a', 'a', 'n', 'n', 'n', 'n', 'n', 'n'], ['$B\\sqsupset C, C\\sqcap D, B\\sqsupset D$']],\
                            [['a', 'n', 'n', 'a', 'n', 'a', 'n', 'a'], ['$B\\supset C, C\\cup D, B\\supset D, 2N$']],\
                            [['a', 'n', 'n', 'a', 'n', 'a', 'n', 'n'], ['$B\\supset C, C\\sqcup D, B\\supset D, 2N$']],\
                            [['a', 'n', 'n', 'n', 'n', 'a', 'n', 'a'], ['$B\\supset C, C\\subset D, B\\cap D$']],\
                            [['a', 'n', 'n', 'n', 'n', 'a', 'n', 'n'], ['$B\\sqsupset C, C\\sqsubset D, B\\cap D$']],\
                            [['a', 'n', 'n', 'a', 'n', 'n', 'n', 'a'], ['$B\\cap C, C\\supset D, B\\supset D$']],\
                            [['a', 'n', 'n', 'a', 'n', 'n', 'n', 'n'], ['$B\\cap C, C\\sqsupset D, B\\sqsupset D$']],\
                            [['a', 'n', 'n', 'n', 'n', 'n', 'n', 'a'], ['$B\\cap C, C\\cap D, B\\cap D$']],\
                            [['a', 'n', 'n', 'n', 'n', 'n', 'n', 'n'], ['$B\\sqcap C, C\\sqcap D, B\\sqcap D$']],\
                            [['n', 'a', 'a', 'a', 'a', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 129']],\
                            [['n', 'a', 'a', 'a', 'a', 'a', 'a', 'n'], ['$B$\textbullet$C$\textbullet$D$ 130']],\
                            [['n', 'a', 'a', 'n', 'a', 'a', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 131']],\
                            [['n', 'a', 'a', 'n', 'a', 'a', 'a', 'n'], ['$B\\sqcup C, C\\cup D, B\\cup D, 1N, 5A$']],\
                            [['n', 'a', 'a', 'a', 'a', 'n', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 133']],\
                            [['n', 'a', 'a', 'a', 'a', 'n', 'a', 'n'], ['$B\\cup C, C\\cup D, B\\sqcup D, 1N, 3A$']],\
                            [['n', 'a', 'a', 'n', 'a', 'n', 'a', 'a'], ['$B$\textbullet$C$\textbullet$D$ 135']],\
                            [['n', 'a', 'a', 'n', 'a', 'n', 'a', 'n'], ['$B\\sqcup C, C\\cup D, B\\sqcup D, 1N$']],\
                            [['n', 'n', 'a', 'a', 'a', 'a', 'a', 'a'], ["$B\\cup C, C\\sqcap 'D, B\\cup D, 7A, 8A$"]],\
                            [['n', 'n', 'a', 'a', 'a', 'a', 'a', 'n'], ["$B\\cup C, C\\sqcap 'D, B\\cup D, 7A, 8N$"]],\
                            [['n', 'n', 'a', 'n', 'a', 'a', 'a', 'a'], ["$B\\cup C, C\\sqcap 'D, B\\subset D, 7A$"]],\
                            [['n', 'n', 'a', 'n', 'a', 'a', 'a', 'n'], ["$B\\sqcup C, C\\sqcap 'D, B\\subset D$"]],\
                            [['n', 'n', 'a', 'a', 'a', 'n', 'a', 'a'], ["$B\\subset C, C\\sqcap 'D, B\\cup D, 7A$"]],\
                            [['n', 'n', 'a', 'a', 'a', 'n', 'a', 'n'], ["$B\\subset C, C\\sqcap 'D, B\\sqcup D$"]],\
                            [['n', 'n', 'a', 'n', 'a', 'n', 'a', 'a'], ["$B\\subset C, C\\sqcap 'D, B\\subset D, 7A$"]],\
                            [['n', 'n', 'a', 'n', 'a', 'n', 'a', 'n'], ["$B\\sqsubset C, C\\sqcap 'D, B\\sqsubset D$"]],\
                            [['n', 'a', 'a', 'a', 'a', 'a', 'n', 'a'], ['$B$\textbullet$C$\textbullet$D$ 145']],\
                            [['n', 'a', 'a', 'a', 'a', 'a', 'n', 'n'], ['$B\\cup C, C\\sqcup D, B\\cup D, 1N, 2A$']],\
                            [['n', 'a', 'a', 'n', 'a', 'a', 'n', 'a'], ['$B$\textbullet$C$\textbullet$D$ 147']],\
                            [['n', 'a', 'a', 'n', 'a', 'a', 'n', 'n'], ['$B\\sqcup C, C\\sqcup D, B\\cup D, 1N$']],\
                            [['n', 'a', 'a', 'a', 'a', 'n', 'n', 'a'], ['$B$\textbullet$C$\textbullet$D$ 149']],\
                            [['n', 'a', 'a', 'a', 'a', 'n', 'n', 'n'], ['$B\\cup C, C\\sqcup D, B\\sqcup D, 1N$']],\
                            [['n', 'a', 'a', 'n', 'a', 'n', 'n', 'a'], ['$B$\textbullet$C$\textbullet$D$ 151']],\
                            [['n', 'a', 'a', 'n', 'a', 'n', 'n', 'n'], ['$B\\sqcup C, C\\sqcup D, B\\sqcup D, 1N$']],\
                            [['n', 'n', 'a', 'a', 'a', 'a', 'n', 'a'], ["$B\\cup C, C\\sqcap 'D, B\\cup D, 7N, 8A$"]],\
                            [['n', 'n', 'a', 'a', 'a', 'a', 'n', 'n'], ["$B\\cup C, C\\cap 'D, B\\cup D$"]],\
                            [['n', 'n', 'a', 'n', 'a', 'a', 'n', 'a'], ["$B\\cup C, C\\sqcap 'D, B\\subset D, 7N$"]],\
                            [['n', 'n', 'a', 'n', 'a', 'a', 'n', 'n'], ["$B\\sqcup C, C\\cap 'D, B\\subset D$"]],\
                            [['n', 'n', 'a', 'a', 'a', 'n', 'n', 'a'], ["$B\\subset C, C\\sqcap 'D, B\\cup D, 7N$"]],\
                            [['n', 'n', 'a', 'a', 'a', 'n', 'n', 'n'], ["$B\\subset C, C\\cap 'D, B\\sqcup D$"]],\
                            [['n', 'n', 'a', 'n', 'a', 'n', 'n', 'a'], ["$B\\subset C, C\\sqcap 'D, B\\subset D, 7N$"]],\
                            [['n', 'n', 'a', 'n', 'a', 'n', 'n', 'n'], ["$B\\sqsubset C, C\\cap 'D, B\\sqsubset D$"]],\
                            [['n', 'a', 'n', 'a', 'a', 'a', 'a', 'a'], ["$B\\cup C, C\\cup D, B\\sqcap 'D, 6A, 8A$"]],\
                            [['n', 'a', 'n', 'a', 'a', 'a', 'a', 'n'], ["$B\\cup C, C\\cup D, B\\sqcap 'D, 6A, 8N$"]],\
                            [['n', 'a', 'n', 'n', 'a', 'a', 'a', 'a'], ["$B\\cup C, C\\subset D, B\\sqcap 'D, 6A$"]],\
                            [['n', 'a', 'n', 'n', 'a', 'a', 'a', 'n'], ["$B\\sqcup C, C\\subset D, B\\sqcap 'D$"]],\
                            [['n', 'a', 'n', 'a', 'a', 'n', 'a', 'a'], ["$B\\cup C, C\\cup D, B\\sqcap 'D, 6N, 8A$"]],\
                            [['n', 'a', 'n', 'a', 'a', 'n', 'a', 'n'], ["$B\\cup C, C\\cup D, B\\cap 'D$"]],\
                            [['n', 'a', 'n', 'n', 'a', 'n', 'a', 'a'], ["$B\\cup C, C\\subset D, B\\sqcap 'D, 6N$"]],\
                            [['n', 'a', 'n', 'n', 'a', 'n', 'a', 'n'], ["$B\\sqcup C, C\\subset D, B\\cap 'D$"]],\
                            [['n', 'n', 'n', 'a', 'a', 'a', 'a', 'a'], ["$B\\cup C, C\\sqcap 'D, B\\sqcap 'D, 8A$"]],\
                            [['n', 'n', 'n', 'a', 'a', 'a', 'a', 'n'], ["$B\\cup C, C\\sqcap 'D, B\\sqcap 'D, 8N$"]],\
                            [['n', 'n', 'n', 'n', 'a', 'a', 'a', 'a'], ["$B\\cup C, C\\sqsupset 'D, B\\sqsupset 'D$"]],\
                            [['n', 'n', 'n', 'n', 'a', 'a', 'a', 'n'], ["$B\\sqcup C, C\\sqsupset 'D, B\\sqsupset 'D$"]],\
                            [['n', 'n', 'n', 'a', 'a', 'n', 'a', 'a'], ["$B\\subset C, C\\sqcap 'D, B\\sqcap 'D$"]],\
                            [['n', 'n', 'n', 'a', 'a', 'n', 'a', 'n'], ["$B\\subset C, C\\sqcap 'D, B\\cap 'D$"]],\
                            [['n', 'n', 'n', 'n', 'a', 'n', 'a', 'a'], ["$B\\subset C, C\\sqsupset 'D, B\\sqsupset 'D$"]],\
                            [['n', 'n', 'n', 'n', 'a', 'n', 'a', 'n'], ["$B\\sqsubset C, C\\sqsupset 'D, B\\supset 'D$"]],\
                            [['n', 'a', 'n', 'a', 'a', 'a', 'n', 'a'], ["$B\\supset C, C\\cup D, B\\sqcap 'D, 6A$"]],\
                            [['n', 'a', 'n', 'a', 'a', 'a', 'n', 'n'], ["$B\\supset C, C\\sqcup D, B\\sqcap 'D$"]],\
                            [['n', 'a', 'n', 'n', 'a', 'a', 'n', 'a'], ["$B\\supset C, C\\subset D, B\\sqcap 'D, 6A$"]],\
                            [['n', 'a', 'n', 'n', 'a', 'a', 'n', 'n'], ["$B\\sqsupset C, C\\sqsubset D, B\\sqcap 'D$"]],\
                            [['n', 'a', 'n', 'a', 'a', 'n', 'n', 'a'], ["$B\\supset C, C\\cup D, B\\sqcap 'D, 6N$"]],\
                            [['n', 'a', 'n', 'a', 'a', 'n', 'n', 'n'], ["$B\\supset C, C\\sqcup D, B\\cap 'D$"]],\
                            [['n', 'a', 'n', 'n', 'a', 'n', 'n', 'a'], ["$B\\supset C, C\\subset D, B\\sqcap 'D, 6N$"]],\
                            [['n', 'a', 'n', 'n', 'a', 'n', 'n', 'n'], ["$B\\sqsupset C, C\\sqsubset D, B\\cap 'D$"]],\
                            [['n', 'n', 'n', 'a', 'a', 'a', 'n', 'a'], ["$B\\supset C, C\\sqcap 'D, B\\sqcap 'D$"]],\
                            [['n', 'n', 'n', 'a', 'a', 'a', 'n', 'n'], ["$B\\supset C, C\\cap 'D, B\\sqcap 'D$"]],\
                            [['n', 'n', 'n', 'n', 'a', 'a', 'n', 'a'], ["$B\\supset C, C\\sqsupset 'D, B\\sqsupset 'D$"]],\
                            [['n', 'n', 'n', 'n', 'a', 'a', 'n', 'n'], ["$B\\sqsupset C, C\\supset 'D, B\\sqsupset 'D$"]],\
                            [['n', 'n', 'n', 'a', 'a', 'n', 'n', 'a'], ["$B\\cap C, C\\sqcap 'D, B\\sqcap 'D$"]],\
                            [['n', 'n', 'n', 'a', 'a', 'n', 'n', 'n'], ["$B\\cap C, C\\cap 'D, B\\cap 'D$"]],\
                            [['n', 'n', 'n', 'n', 'a', 'n', 'n', 'a'], ["$B\\cap C, C\\sqsupset 'D, B\\sqsupset 'D$"]],\
                            [['n', 'n', 'n', 'n', 'a', 'n', 'n', 'n'], ["$B\\sqcap C, C\\supset 'D, B\\supset 'D$"]],\
                            [['n', 'a', 'a', 'a', 'n', 'a', 'a', 'a'], ["$B\\sqcap 'C, C\\cup D, B\\cup D, 4A, 8A$"]],\
                            [['n', 'a', 'a', 'a', 'n', 'a', 'a', 'n'], ["$B\\sqcap 'C, C\\cup D, B\\cup D, 4A, 8N$"]],\
                            [['n', 'a', 'a', 'n', 'n', 'a', 'a', 'a'], ["$B\\sqcap 'C, C\\cup D, B\\cup D, 4N, 8A$"]],\
                            [['n', 'a', 'a', 'n', 'n', 'a', 'a', 'n'], ["$B\\cap 'C, C\\cup D, B\\cup D$"]],\
                            [['n', 'a', 'a', 'a', 'n', 'n', 'a', 'a'], ["$B\\sqcap 'C, C\\supset D, B\\cup D, 4A$"]],\
                            [['n', 'a', 'a', 'a', 'n', 'n', 'a', 'n'], ["$B\\sqcap 'C, C\\supset D, B\\sqcup D$"]],\
                            [['n', 'a', 'a', 'n', 'n', 'n', 'a', 'a'], ["$B\\sqcap 'C, C\\supset D, B\\cup D, 4N$"]],\
                            [['n', 'a', 'a', 'n', 'n', 'n', 'a', 'n'], ["$B\\cap 'C, C\\supset D, B\\sqcup D$"]],\
                            [['n', 'n', 'a', 'a', 'n', 'a', 'a', 'a'], ["$B\\sqcap 'C, C\\sqcap 'D, B\\cup D, 8A$"]],\
                            [['n', 'n', 'a', 'a', 'n', 'a', 'a', 'n'], ["$B\\sqcap 'C, C\\sqcap 'D, B\\cup D, 8N$"]],\
                            [['n', 'n', 'a', 'n', 'n', 'a', 'a', 'a'], ["$B\\sqcap 'C, C\\sqcap 'D, B\\subset D$"]],\
                            [['n', 'n', 'a', 'n', 'n', 'a', 'a', 'n'], ["$B\\cap 'C, C\\sqcap 'D, B\\subset D$"]],\
                            [['n', 'n', 'a', 'a', 'n', 'n', 'a', 'a'], ["$B\\sqsupset 'C, C\\sqsubset 'D, B\\cup D$"]],\
                            [['n', 'n', 'a', 'a', 'n', 'n', 'a', 'n'], ["$B\\sqsupset 'C, C\\sqsubset 'D, B\\sqcup D$"]],\
                            [['n', 'n', 'a', 'n', 'n', 'n', 'a', 'a'], ["$B\\sqsupset 'C, C\\sqsubset 'D, B\\subset D$"]],\
                            [['n', 'n', 'a', 'n', 'n', 'n', 'a', 'n'], ["$B\\supset 'C, C\\sqsubset 'D, B\\sqsubset D$"]],\
                            [['n', 'a', 'a', 'a', 'n', 'a', 'n', 'a'], ["$B\\sqcap 'C, C\\cup D, B\\supset D, 4A$"]],\
                            [['n', 'a', 'a', 'a', 'n', 'a', 'n', 'n'], ["$B\\sqcap 'C, C\\sqcup D, B\\supset D$"]],\
                            [['n', 'a', 'a', 'n', 'n', 'a', 'n', 'a'], ["$B\\sqcap 'C, C\\cup D, B\\supset D, 4N$"]],\
                            [['n', 'a', 'a', 'n', 'n', 'a', 'n', 'n'], ["$B\\cap 'C, C\\sqcup D, B\\supset D$"]],\
                            [['n', 'a', 'a', 'a', 'n', 'n', 'n', 'a'], ["$B\\sqcap 'C, C\\supset D, B\\supset D, 4A$"]],\
                            [['n', 'a', 'a', 'a', 'n', 'n', 'n', 'n'], ["$B\\sqcap 'C, C\\sqsupset D, B\\sqsupset D$"]],\
                            [['n', 'a', 'a', 'n', 'n', 'n', 'n', 'a'], ["$B\\sqcap 'C, C\\supset D, B\\supset D, 4N$"]],\
                            [['n', 'a', 'a', 'n', 'n', 'n', 'n', 'n'], ["$B\\cap 'C, C\\sqsupset D, B\\sqsupset D$"]],\
                            [['n', 'n', 'a', 'a', 'n', 'a', 'n', 'a'], ["$B\\sqcap 'C, C\\sqcap 'D, B\\supset D$"]],\
                            [['n', 'n', 'a', 'a', 'n', 'a', 'n', 'n'], ["$B\\sqcap 'C, C\\cap 'D, B\\supset D$"]],\
                            [['n', 'n', 'a', 'n', 'n', 'a', 'n', 'a'], ["$B\\sqcap 'C, C\\sqcap 'D, B\\cap D$"]],\
                            [['n', 'n', 'a', 'n', 'n', 'a', 'n', 'n'], ["$B\\cap 'C, C\\cap 'D, B\\cap D$"]],\
                            [['n', 'n', 'a', 'a', 'n', 'n', 'n', 'a'], ["$B\\sqsupset 'C, C\\sqsubset 'D, B\\supset D$"]],\
                            [['n', 'n', 'a', 'a', 'n', 'n', 'n', 'n'], ["$B\\sqsupset 'C, C\\subset 'D, B\\sqsupset D$"]],\
                            [['n', 'n', 'a', 'n', 'n', 'n', 'n', 'a'], ["$B\\sqsupset 'C, C\\sqsubset 'D, B\\cap D$"]],\
                            [['n', 'n', 'a', 'n', 'n', 'n', 'n', 'n'], ["$B\\supset 'C, C\\subset 'D, B\\sqcap D$"]],\
                            [['n', 'a', 'n', 'a', 'n', 'a', 'a', 'a'], ["$B\\sqcap 'C, C\\cup D, B\\sqcap 'D, 8A$"]],\
                            [['n', 'a', 'n', 'a', 'n', 'a', 'a', 'n'], ["$B\\sqcap 'C, C\\cup D, B\\sqcap 'D, 8N$"]],\
                            [['n', 'a', 'n', 'n', 'n', 'a', 'a', 'a'], ["$B\\sqcap 'C, C\\subset D, B\\sqcap 'D$"]],\
                            [['n', 'a', 'n', 'n', 'n', 'a', 'a', 'n'], ["$B\\cap' C, C\\subset D, B\\sqcap 'D$"]],\
                            [['n', 'a', 'n', 'a', 'n', 'n', 'a', 'a'], ["$B\\sqcap 'C, C\\supset D, B\\sqcap 'D$"]],\
                            [['n', 'a', 'n', 'a', 'n', 'n', 'a', 'n'], ["$B\\sqcap 'C, C\\supset D, B\\cap 'D$"]],\
                            [['n', 'a', 'n', 'n', 'n', 'n', 'a', 'a'], ["$B\\sqcap 'C, C\\cap D, B\\sqcap 'D$"]],\
                            [['n', 'a', 'n', 'n', 'n', 'n', 'a', 'n'], ["$B\\cap 'C, C\\cap D, B\\cap 'D$"]],\
                            [['n', 'n', 'n', 'a', 'n', 'a', 'a', 'a'], ["$B\\sqcap 'C, C\\sqcap 'D B\\sqcap 'D, 8A$"]],\
                            [['n', 'n', 'n', 'a', 'n', 'a', 'a', 'n'], ["$B\\sqcap 'C, C\\sqcap 'D B\\sqcap 'D, 8N$"]],\
                            [['n', 'n', 'n', 'n', 'n', 'a', 'a', 'a'], ["$B\\sqcap 'C, C\\sqsupset 'D, B\\sqsupset 'D$"]],\
                            [['n', 'n', 'n', 'n', 'n', 'a', 'a', 'n'], ["$B\\cap 'C, C\\sqsupset 'D, B\\sqsupset 'D$"]],\
                            [['n', 'n', 'n', 'a', 'n', 'n', 'a', 'a'], ["$B\\sqsupset 'C, C\\sqsubset 'D, B\\sqcap 'D$"]],\
                            [['n', 'n', 'n', 'a', 'n', 'n', 'a', 'n'], ["$B\\sqsupset 'C, C\\sqsubset 'D, B\\cap 'D$"]],\
                            [['n', 'n', 'n', 'n', 'n', 'n', 'a', 'a'], ["$B\\sqsupset 'C, C\\sqcup 'D, B\\sqsupset 'D$"]],\
                            [['n', 'n', 'n', 'n', 'n', 'n', 'a', 'n'], ["$B\\supset 'C, C\\sqcup 'D, B\\supset 'D$"]],\
                            [['n', 'a', 'n', 'a', 'n', 'a', 'n', 'a'], ["$B\\sqsubset 'C, C\\cup D, B\\sqsubset 'D$"]],\
                            [['n', 'a', 'n', 'a', 'n', 'a', 'n', 'n'], ["$B\\sqsubset 'C, C\\sqcup D, B\\sqsubset 'D$"]],\
                            [['n', 'a', 'n', 'n', 'n', 'a', 'n', 'a'], ["$B\\sqsubset 'C, C\\subset D, B\\sqsubset 'D$"]],\
                            [['n', 'a', 'n', 'n', 'n', 'a', 'n', 'n'], ["$B\\subset 'C, C\\sqsubset D, B\\sqsubset 'D$"]],\
                            [['n', 'a', 'n', 'a', 'n', 'n', 'n', 'a'], ["$B\\sqsubset 'C, C\\supset D, B\\sqsubset 'D$"]],\
                            [['n', 'a', 'n', 'a', 'n', 'n', 'n', 'n'], ["$B\\sqsubset 'C, C\\sqsupset D, B\\subset 'D$"]],\
                            [['n', 'a', 'n', 'n', 'n', 'n', 'n', 'a'], ["$B\\sqsubset 'C, C\\cap D, B\\sqsubset 'D$"]],\
                            [['n', 'a', 'n', 'n', 'n', 'n', 'n', 'n'], ["$B\\subset 'C, C\\sqcap D, B\\subset 'D$"]],\
                            [['n', 'n', 'n', 'a', 'n', 'a', 'n', 'a'], ["$B\\sqsubset 'C, C\\sqcap 'D, B\\sqsubset 'D$"]],\
                            [['n', 'n', 'n', 'a', 'n', 'a', 'n', 'n'], ["$B\\sqsubset 'C, C\\cap 'D, B\\sqsubset 'D$"]],\
                            [['n', 'n', 'n', 'n', 'n', 'a', 'n', 'a'], ["$B\\sqsubset 'C, C\\sqsupset 'D, B\\sqcup 'D$"]],\
                            [['n', 'n', 'n', 'n', 'n', 'a', 'n', 'n'], ["$B\\subset 'C, C\\supset 'D, B\\sqcup 'D$"]],\
                            [['n', 'n', 'n', 'a', 'n', 'n', 'n', 'a'], ["$B\\sqcup 'C, C\\sqsubset 'D, B\\sqsubset 'D$"]],\
                            [['n', 'n', 'n', 'a', 'n', 'n', 'n', 'n'], ["$B\\sqcup 'C, C\\subset 'D, B\\subset 'D$"]],\
                            [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'a'], ["$B\\sqcup 'C, C\\sqcup 'D, B\\sqcup 'D$"]],\
                            [['n', 'n', 'n', 'n', 'n', 'n', 'n', 'n'], ["$B\\cup 'C, C\\cup 'D, B\\cup 'D$"]]]

    for formulas_names in list_formulas_names:
        if formulas_names[0] == formula:
            #print(formula_list_name[0])
            if index_premis_circumstance == 2:
                new_formula_A = formulas_names[1][0][:].replace("B", "X")
                new_formula_2 = new_formula_A.replace("D", "E")
                new_formula_3 = new_formula_2.replace("C", "D")
                new_formula_4 = new_formula_3.replace("X", "C")
                return [new_formula_4]
            #"$C$\textbullet$D$\textbullet$E$"
            elif index_premis_circumstance == 1:
                new_formula_B = formulas_names[1][0][:].replace("D", "E")
                return [new_formula_B]
            #"$B$\textbullet$C$\textbullet$E$"
            elif index_premis_circumstance == 3:
                new_formula_C = formulas_names[1][0][:].replace("D", "E")
                new_formula_2 = new_formula_C.replace("C", "D")
                return [new_formula_2]
            #"$B$\textbullet$D$\textbullet$E$"
            elif index_premis_circumstance == 4:
                return [formulas_names[1][0]]
            #"$B$\textbullet$C$\textbullet$D$"

"""def replace_total_formulas_fn( total_formula_old, *args):


    for j in range(8):
        if total_formula_old[j] == 'u':
            total_formula_old[j] = 'a'    
            total_formula_new_A = total_formula_old[:]
            total_formula_old[j] = 'n'
            total_formula_new_N = total_formula_old[:]
            
            return(total_formula_new_A, total_formula_new_N, j+1)
    
    return(0)"""


                                        
def deduction_of_tetradic_total_formulas_from_triadic_level( *args):
    #~4 billion Possibilitys from triadic possibilitys to tetradic possibilitys:
    #21 places = 12 sec
    #22 places = 24 sec
    #32 places = 6.8 h (calculated approximatly)
    #BEGIN: 2025-02-06 22:46:15.554045
    #END: 2025-02-07 05:24:23.855997

    with open('file.csv', 'w') as file:
        writer = csv.writer(file)
        
        list_third_level_input = []
        count = 0

        #count_x = 0

        list_of_total_formulas_edited = []
        
        dummy_list = []
        
        begin_now = datetime.now()
        print("BEGIN:", begin_now)
        
        for i in range(2**32):
            ones_and_zeros = '{:032b}'.format(i)
            list_ones_and_zeros = list(ones_and_zeros)
            
            for j in range(32):
                if list_ones_and_zeros[j] == "1":
                    list_ones_and_zeros[j] = "n"
                if list_ones_and_zeros[j] == "0":
                    list_ones_and_zeros[j] = "a"
                                                                                                                                            
            
            first_formula_tri = list_ones_and_zeros[0:8]
            second_formula_tri =  list_ones_and_zeros[8:16]
            third_formula_tri = list_ones_and_zeros[16:24]
            fourth_formula_tri = list_ones_and_zeros[24:32]
            #print(first_formula_tri)
            #print(second_formula_tri)
            #print(third_formula_tri)
            #print(fourth_formula_tri)
        

        
        
            solution_and_contradiction_test = syllogism_contradiction_test_tet(first_formula_tri, second_formula_tri, third_formula_tri, fourth_formula_tri)
                        #solution_and_contradiction_test[0].count('u') == 1 --> one 'u' in total-formula
                        #len(error_number) == 0 --> no contradiction
                                                            
                        #if len(error_number) != 0:
                        #    count_x = count_x + 1
                        #    print(error_number)                        
            #print(solution_and_contradiction_test)
            if (solution_and_contradiction_test[0] != 'W'):
                                                                                                                                                        
                first_formula = triadic_name_fn(first_formula_tri, 2)
                second_formula = triadic_name_fn(second_formula_tri, 1)
                third_formula = triadic_name_fn(third_formula_tri, 3)
                fourth_formula = triadic_name_fn(fourth_formula_tri, 4)
                
                writer.writerow([solution_and_contradiction_test[0], [[fourth_formula, fourth_formula_tri], [second_formula, second_formula_tri], [first_formula, first_formula_tri], [third_formula, third_formula_tri]]])
                
        file.close()    
                                                                                                                                          
    end_now = datetime.now()
    print("END:", end_now)



deduction_of_tetradic_total_formulas_from_triadic_level()

