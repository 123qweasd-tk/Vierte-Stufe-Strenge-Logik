from datetime import datetime
import csv
import ast

global formula_between_global_variable
formula_between_global_variable = 0

def tet_syllogism_deduction_first_value_n(first_formula, second_formula, third_formula):
    if first_formula[0] == "n" and first_formula[4] == "n":  # caluculates potential "n"-values of first value
        return ("n")
    elif second_formula[0] == "n" and second_formula[4] == "n":
        return ("n")
    elif third_formula[0] == "n" and third_formula[4] == "n":
        return ("n")

    elif first_formula[0] == "n" and second_formula[4] == "n":
        return ("n")
    elif second_formula[0] == "n" and first_formula[4] == "n":
        return ("n")

    elif first_formula[0] == "n" and third_formula[4] == "n":
        return ("n")        
    elif third_formula[0] == "n" and first_formula[4] == "n":
        return ("n")

    elif second_formula[0] == "n" and third_formula[4] == "n":
        return ("n")        
    elif third_formula[0] == "n" and second_formula[4] == "n":
        return ("n")

    
    else:  # calculates potential "u"-values of first value
        return ("u")

def tet_syllogism_deduction_first_value_a(first_formula, second_formula, third_formula):
    if first_formula[0] == "a" and second_formula[1] == "n":  # calculates potential "a"-values of first value
        return ("a")
    elif first_formula[0] == "a" and third_formula[1] == "n":
        return ("a")
    elif first_formula[4] == "a" and second_formula[5] == "n":
        return ("a")
    elif first_formula[4] == "a" and third_formula[5] == "n":
        return ("a")
    elif second_formula[0] == "a" and first_formula[2] == "n":
        return ("a")
    elif second_formula[0] == "a" and third_formula[2] == "n":
        return ("a")
    elif second_formula[4] == "a" and first_formula[6] == "n":
        return ("a")
    elif second_formula[4] == "a" and third_formula[6] == "n":
        return ("a")
    elif third_formula[0] == "a" and first_formula[1] == "n":
        return ("a")
    elif third_formula[0] == "a" and second_formula[2] == "n":
        return ("a")
    elif third_formula[4] == "a" and first_formula[5] == "n":
        return ("a")
    elif third_formula[4] == "a" and second_formula[6] == "n":
        return ("a")
    else:  # calculates potential "u"-values of first value
        return ("u")

def tet_syllogism_deduction_second_value_n(first_formula, second_formula, third_formula):
    if first_formula[0] == "n" and first_formula[4] == "n":  # caluculates potential "n"-values of second value
        return ("n")
    elif second_formula[1] == "n" and second_formula[5] == "n":
        return ("n")
    elif third_formula[1] == "n" and third_formula[5] == "n":
        return ("n")

    elif first_formula[0] == "n" and second_formula[5] == "n":
        return ("n")
    elif second_formula[1] == "n" and first_formula[4] == "n":
        return ("n")

    elif first_formula[0] == "n" and third_formula[5] == "n":
        return ("n")        
    elif third_formula[1] == "n" and first_formula[4] == "n":
        return ("n")

    elif second_formula[1] == "n" and third_formula[5] == "n":
        return ("n")        
    elif third_formula[1] == "n" and second_formula[5] == "n":
        return ("n")

    
    else:  # calculates potential "u"-values of first value
        return ("u")

def tet_syllogism_deduction_second_value_a(first_formula, second_formula, third_formula):
    if first_formula[0] == "a" and second_formula[0] == "n":  # calculates potential "a"-values of second value
        return ("a")
    elif first_formula[0] == "a" and third_formula[0] == "n":
        return ("a")
    elif first_formula[4] == "a" and second_formula[4] == "n":
        return ("a")
    elif first_formula[4] == "a" and third_formula[4] == "n":
        return ("a")
    elif second_formula[1] == "a" and first_formula[2] == "n":
        return ("a")
    elif second_formula[1] == "a" and third_formula[3] == "n":
        return ("a")
    elif second_formula[5] == "a" and first_formula[6] == "n":
        return ("a")
    elif second_formula[5] == "a" and third_formula[7] == "n":
        return ("a")
    elif third_formula[1] == "a" and first_formula[1] == "n":
        return ("a")
    elif third_formula[1] == "a" and second_formula[3] == "n":
        return ("a")
    elif third_formula[5] == "a" and first_formula[5] == "n":
        return ("a")
    elif third_formula[5] == "a" and second_formula[7] == "n":
        return ("a")
    else:  # calculates potential "u"-values of second value
        return ("u")

def tet_syllogism_deduction_third_value_n(first_formula, second_formula, third_formula):
    if first_formula[1] == "n" and first_formula[5] == "n":  # caluculates potential "n"-values of third value
        return ("n")
    elif second_formula[2] == "n" and second_formula[6] == "n":
        return ("n")
    elif third_formula[0] == "n" and third_formula[4] == "n":
        return ("n")

    elif first_formula[1] == "n" and second_formula[6] == "n":
        return ("n")
    elif second_formula[2] == "n" and first_formula[5] == "n":
        return ("n")

    elif first_formula[1] == "n" and third_formula[4] == "n":
        return ("n")        
    elif third_formula[0] == "n" and first_formula[5] == "n":
        return ("n")

    elif second_formula[2] == "n" and third_formula[4] == "n":
        return ("n")        
    elif third_formula[0] == "n" and second_formula[6] == "n":
        return ("n")

    
    else:  # calculates potential "u"-values of third value
        return ("u")

def tet_syllogism_deduction_third_value_a(first_formula, second_formula, third_formula):
    if first_formula[1] == "a" and second_formula[3] == "n":  # calculates potential "a"-values of third value
        return ("a")
    elif first_formula[1] == "a" and third_formula[1] == "n":
        return ("a")
    elif first_formula[5] == "a" and second_formula[7] == "n":
        return ("a")
    elif first_formula[5] == "a" and third_formula[5] == "n":
        return ("a")
    elif second_formula[2] == "a" and first_formula[3] == "n":
        return ("a")
    elif second_formula[2] == "a" and third_formula[2] == "n":
        return ("a")
    elif second_formula[6] == "a" and first_formula[7] == "n":
        return ("a")
    elif second_formula[6] == "a" and third_formula[6] == "n":
        return ("a")
    elif third_formula[0] == "a" and first_formula[0] == "n":
        return ("a")
    elif third_formula[0] == "a" and second_formula[0] == "n":
        return ("a")
    elif third_formula[4] == "a" and first_formula[4] == "n":
        return ("a")
    elif third_formula[4] == "a" and second_formula[4] == "n":
        return ("a")
    else:  # calculates potential "u"-values of third value
        return ("u")

def tet_syllogism_deduction_fourth_value_n(first_formula, second_formula, third_formula):
    if first_formula[1] == "n" and first_formula[5] == "n":  # caluculates potential "n"-values of fourth value
        return ("n")
    elif second_formula[3] == "n" and second_formula[7] == "n":
        return ("n")
    elif third_formula[1] == "n" and third_formula[5] == "n":
        return ("n")

    elif first_formula[1] == "n" and second_formula[7] == "n":
        return ("n")
    elif second_formula[3] == "n" and first_formula[5] == "n":
        return ("n")

    elif first_formula[1] == "n" and third_formula[5] == "n":
        return ("n")        
    elif third_formula[1] == "n" and first_formula[5] == "n":
        return ("n")

    elif second_formula[3] == "n" and third_formula[5] == "n":
        return ("n")        
    elif third_formula[1] == "n" and second_formula[7] == "n":
        return ("n")

    
    else:  # calculates potential "u"-values of fourth value
        return ("u")

def tet_syllogism_deduction_fourth_value_a(first_formula, second_formula, third_formula):
    if first_formula[1] == "a" and second_formula[2] == "n":  # calculates potential "a"-values of fourth value
        return ("a")
    elif first_formula[1] == "a" and third_formula[0] == "n":
        return ("a")
    elif first_formula[5] == "a" and second_formula[6] == "n":
        return ("a")
    elif first_formula[5] == "a" and third_formula[4] == "n":
        return ("a")
    elif second_formula[3] == "a" and first_formula[3] == "n":
        return ("a")
    elif second_formula[3] == "a" and third_formula[3] == "n":
        return ("a")
    elif second_formula[7] == "a" and first_formula[7] == "n":
        return ("a")
    elif second_formula[7] == "a" and third_formula[7] == "n":
        return ("a")
    elif third_formula[1] == "a" and first_formula[0] == "n":
        return ("a")
    elif third_formula[1] == "a" and second_formula[1] == "n":
        return ("a")
    elif third_formula[5] == "a" and first_formula[4] == "n":
        return ("a")
    elif third_formula[5] == "a" and second_formula[5] == "n":
        return ("a")
    else:  # calculates potential "u"-values of fourth value
        return ("u")
    
def tet_syllogism_deduction_fifth_value_n(first_formula, second_formula, third_formula):
    if first_formula[2] == "n" and first_formula[6] == "n":  # caluculates potential "n"-values of fifth value
        return ("n")
    elif second_formula[0] == "n" and second_formula[4] == "n":
        return ("n")
    elif third_formula[2] == "n" and third_formula[6] == "n":
        return ("n")

    elif first_formula[2] == "n" and second_formula[4] == "n":
        return ("n")
    elif second_formula[0] == "n" and first_formula[6] == "n":
        return ("n")

    elif first_formula[2] == "n" and third_formula[6] == "n":
        return ("n")        
    elif third_formula[2] == "n" and first_formula[6] == "n":
        return ("n")

    elif second_formula[0] == "n" and third_formula[6] == "n":
        return ("n")        
    elif third_formula[2] == "n" and second_formula[4] == "n":
        return ("n")

    
    else:  # calculates potential "u"-values of fifth value
        return ("u")

def tet_syllogism_deduction_fifth_value_a(first_formula, second_formula, third_formula):
    if first_formula[2] == "a" and second_formula[1] == "n":  # calculates potential "a"-values of fifth value
        return ("a")
    elif first_formula[2] == "a" and third_formula[3] == "n":
        return ("a")
    elif first_formula[6] == "a" and second_formula[5] == "n":
        return ("a")
    elif first_formula[6] == "a" and third_formula[7] == "n":
        return ("a")
    elif second_formula[0] == "a" and first_formula[0] == "n":
        return ("a")
    elif second_formula[0] == "a" and third_formula[0] == "n":
        return ("a")
    elif second_formula[4] == "a" and first_formula[4] == "n":
        return ("a")
    elif second_formula[4] == "a" and third_formula[4] == "n":
        return ("a")
    elif third_formula[2] == "a" and first_formula[3] == "n":
        return ("a")
    elif third_formula[2] == "a" and second_formula[2] == "n":
        return ("a")
    elif third_formula[6] == "a" and first_formula[7] == "n":
        return ("a")
    elif third_formula[6] == "a" and second_formula[6] == "n":
        return ("a")
    else:  # calculates potential "u"-values of fifth value
        return ("u")

def tet_syllogism_deduction_sixth_value_n(first_formula, second_formula, third_formula):
    if first_formula[2] == "n" and first_formula[6] == "n":  # caluculates potential "n"-values of sixth value
        return ("n")
    elif second_formula[1] == "n" and second_formula[5] == "n":
        return ("n")
    elif third_formula[3] == "n" and third_formula[7] == "n":
        return ("n")

    elif first_formula[2] == "n" and second_formula[5] == "n":
        return ("n")
    elif second_formula[1] == "n" and first_formula[6] == "n":
        return ("n")

    elif first_formula[2] == "n" and third_formula[7] == "n":
        return ("n")        
    elif third_formula[3] == "n" and first_formula[6] == "n":
        return ("n")

    elif second_formula[1] == "n" and third_formula[7] == "n":
        return ("n")        
    elif third_formula[3] == "n" and second_formula[5] == "n":
        return ("n")

    
    else:  # calculates potential "u"-values of sixth value
        return ("u")

def tet_syllogism_deduction_sixth_value_a(first_formula, second_formula, third_formula):
    if first_formula[2] == "a" and second_formula[0] == "n":  # calculates potential "a"-values of sixth value
        return ("a")
    elif first_formula[2] == "a" and third_formula[2] == "n":
        return ("a")
    elif first_formula[6] == "a" and second_formula[4] == "n":
        return ("a")
    elif first_formula[6] == "a" and third_formula[6] == "n":
        return ("a")
    elif second_formula[1] == "a" and first_formula[0] == "n":
        return ("a")
    elif second_formula[1] == "a" and third_formula[1] == "n":
        return ("a")
    elif second_formula[5] == "a" and first_formula[4] == "n":
        return ("a")
    elif second_formula[5] == "a" and third_formula[5] == "n":
        return ("a")
    elif third_formula[3] == "a" and first_formula[3] == "n":
        return ("a")
    elif third_formula[3] == "a" and second_formula[3] == "n":
        return ("a")
    elif third_formula[7] == "a" and first_formula[7] == "n":
        return ("a")
    elif third_formula[7] == "a" and second_formula[7] == "n":
        return ("a")
    else:  # calculates potential "u"-values of sixth value
        return ("u")
    
def tet_syllogism_deduction_seventh_value_n(first_formula, second_formula, third_formula):
    if first_formula[3] == "n" and first_formula[7] == "n":  # caluculates potential "n"-values of seventh value
        return ("n")
    elif second_formula[2] == "n" and second_formula[6] == "n":
        return ("n")
    elif third_formula[2] == "n" and third_formula[6] == "n":
        return ("n")

    elif first_formula[3] == "n" and second_formula[6] == "n":
        return ("n")
    elif second_formula[2] == "n" and first_formula[7] == "n":
        return ("n")

    elif first_formula[3] == "n" and third_formula[6] == "n":
        return ("n")        
    elif third_formula[2] == "n" and first_formula[7] == "n":
        return ("n")

    elif second_formula[2] == "n" and third_formula[6] == "n":
        return ("n")        
    elif third_formula[2] == "n" and second_formula[6] == "n":
        return ("n")

    
    else:  # calculates potential "u"-values of seventh value
        return ("u")

def tet_syllogism_deduction_seventh_value_a(first_formula, second_formula, third_formula):
    if first_formula[3] == "a" and second_formula[3] == "n":  # calculates potential "a"-values of seventh value
        return ("a")
    elif first_formula[3] == "a" and third_formula[3] == "n":
        return ("a")
    elif first_formula[7] == "a" and second_formula[7] == "n":
        return ("a")
    elif first_formula[7] == "a" and third_formula[7] == "n":
        return ("a")
    elif second_formula[2] == "a" and first_formula[1] == "n":
        return ("a")
    elif second_formula[2] == "a" and third_formula[0] == "n":
        return ("a")
    elif second_formula[6] == "a" and first_formula[5] == "n":
        return ("a")
    elif second_formula[6] == "a" and third_formula[4] == "n":
        return ("a")
    elif third_formula[2] == "a" and first_formula[2] == "n":
        return ("a")
    elif third_formula[2] == "a" and second_formula[0] == "n":
        return ("a")
    elif third_formula[6] == "a" and first_formula[6] == "n":
        return ("a")
    elif third_formula[6] == "a" and second_formula[4] == "n":
        return ("a")
    else:  # calculates potential "u"-values of seventh value
        return ("u")

def tet_syllogism_deduction_eighth_value_n(first_formula, second_formula, third_formula):
    if first_formula[3] == "n" and first_formula[7] == "n":  # caluculates potential "n"-values of eighth value
        return ("n")
    elif second_formula[3] == "n" and second_formula[7] == "n":
        return ("n")
    elif third_formula[3] == "n" and third_formula[7] == "n":
        return ("n")

    elif first_formula[3] == "n" and second_formula[7] == "n":
        return ("n")
    elif second_formula[3] == "n" and first_formula[7] == "n":
        return ("n")

    elif first_formula[3] == "n" and third_formula[7] == "n":
        return ("n")        
    elif third_formula[3] == "n" and first_formula[7] == "n":
        return ("n")

    elif second_formula[3] == "n" and third_formula[7] == "n":
        return ("n")        
    elif third_formula[3] == "n" and second_formula[7] == "n":
        return ("n")

    
    else:  # calculates potential "u"-values of eighth value
        return ("u")

def tet_syllogism_deduction_eighth_value_a(first_formula, second_formula, third_formula):
    if first_formula[3] == "a" and second_formula[2] == "n":  # calculates potential "a"-values of eighth value
        return ("a")
    elif first_formula[3] == "a" and third_formula[2] == "n":
        return ("a")
    elif first_formula[7] == "a" and second_formula[6] == "n":
        return ("a")
    elif first_formula[7] == "a" and third_formula[6] == "n":
        return ("a")
    elif second_formula[3] == "a" and first_formula[1] == "n":
        return ("a")
    elif second_formula[3] == "a" and third_formula[1] == "n":
        return ("a")
    elif second_formula[7] == "a" and first_formula[5] == "n":
        return ("a")
    elif second_formula[7] == "a" and third_formula[5] == "n":
        return ("a")
    elif third_formula[3] == "a" and first_formula[2] == "n":
        return ("a")
    elif third_formula[3] == "a" and second_formula[1] == "n":
        return ("a")
    elif third_formula[7] == "a" and first_formula[6] == "n":
        return ("a")
    elif third_formula[7] == "a" and second_formula[5] == "n":
        return ("a")
    else:  # calculates potential "u"-values of eighth value
        return ("u")

def syllogism_contradiction_test_tet(first_formula, second_formula, third_formula):

    conclusion = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    conclusion[0] = tet_syllogism_deduction_first_value_n(first_formula, second_formula, third_formula)
    conclusion[1] = tet_syllogism_deduction_first_value_a(first_formula, second_formula, third_formula)
    if conclusion[0] == 'n' and conclusion[1] == 'a':
        return (['W1'])
    conclusion[2] = tet_syllogism_deduction_second_value_n(first_formula, second_formula, third_formula)
    conclusion[3] = tet_syllogism_deduction_second_value_a(first_formula, second_formula, third_formula)
    if conclusion[2] == 'n' and conclusion[3] == 'a':
        return (['W2'])
    conclusion[4] = tet_syllogism_deduction_third_value_n(first_formula, second_formula, third_formula)
    conclusion[5] = tet_syllogism_deduction_third_value_a(first_formula, second_formula, third_formula)
    if conclusion[4] == 'n' and conclusion[5] == 'a':
        return (['W3'])
    conclusion[6] = tet_syllogism_deduction_fourth_value_n(first_formula, second_formula, third_formula)
    conclusion[7] = tet_syllogism_deduction_fourth_value_a(first_formula, second_formula, third_formula)
    if conclusion[6] == 'n' and conclusion[7] == 'a':
        return (['W4'])
    conclusion[8] = tet_syllogism_deduction_fifth_value_n(first_formula, second_formula, third_formula)
    conclusion[9] = tet_syllogism_deduction_fifth_value_a(first_formula, second_formula, third_formula)
    if conclusion[8] == 'n' and conclusion[9] == 'a':
        return (['W5'])
    conclusion[10] = tet_syllogism_deduction_sixth_value_n(first_formula, second_formula, third_formula)
    conclusion[11] = tet_syllogism_deduction_sixth_value_a(first_formula, second_formula, third_formula)
    if conclusion[10] == 'n' and conclusion[11] == 'a':
        return (['W6'])
    conclusion[12] = tet_syllogism_deduction_seventh_value_n(first_formula, second_formula, third_formula)
    conclusion[13] = tet_syllogism_deduction_seventh_value_a(first_formula, second_formula, third_formula)
    if conclusion[12] == 'n' and conclusion[13] == 'a':
        return (['W7'])
    conclusion[14] = tet_syllogism_deduction_eighth_value_n(first_formula, second_formula, third_formula)
    conclusion[15] = tet_syllogism_deduction_eighth_value_a(first_formula, second_formula, third_formula)
    if conclusion[14] == 'n' and conclusion[15] == 'a':
        return (['W8'])

    conclusion_solution = [0,0,0,0,0,0,0,0]
        
    for i in range(8):

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

def triadic_name_fn_enlonged( formula, index_premis_circumstance):
    
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

def enlonged_fn(premis_1, premis_2, premis_3):

        #calculate from enlonged triadic formulas to fourth enlonged tetradic formula

    one = premis_1
    two =  premis_2
    three = premis_3
                                                                                                                                    
    #print(premis_1)
    #print(premis_2)
    #print(premis_3)
    
    syllogism_solution_tet = syllogism_contradiction_test_tet(one, two, three)

    if (syllogism_solution_tet[0] != 'W1') and \
       (syllogism_solution_tet[0] != 'W2') and \
       (syllogism_solution_tet[0] != 'W3') and \
       (syllogism_solution_tet[0] != 'W4') and \
       (syllogism_solution_tet[0] != 'W5') and \
       (syllogism_solution_tet[0] != 'W6') and \
       (syllogism_solution_tet[0] != 'W7') and \
       (syllogism_solution_tet[0] != 'W8'):
                                                                                                                                                
      
        fourth_formula_tri = syllogism_solution_tet[0]
        fourth_formula = triadic_name_fn_enlonged(fourth_formula_tri, 4)

        return [fourth_formula_tri, fourth_formula]
    else:
        print(premis_1)
        print(premis_2)
        print(premis_3)
        return print(syllogism_solution_tet)
                                                                                                                                      
end_now = datetime.now()
print("END:", end_now)



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
                            [['a', 'a', 'a', 'a', 'a', 'n', 'n', 'n'], ['$B\\cup C, C\\sqcup D, B\\sqcup D, 1A$'  ]],\
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

    if index_premis_circumstance == 2:
        new_formula_A = formula.replace("C", "X")
        new_formula_2 = new_formula_A.replace("D", "C")
        new_formula_3 = new_formula_2.replace("E", "D")
        new_formula_4 = new_formula_3.replace("X", "B")
        for i, formulas_names in enumerate(list_formulas_names):
            if formulas_names[1][0] == new_formula_4:
                #print(new_formula_4)
                return formulas_names[0]
            #"$C$\textbullet$D$\textbullet$E$"
    elif index_premis_circumstance == 1:
        new_formula_B = formula.replace("E", "D")
        for i, formulas_names in enumerate(list_formulas_names):
            if formulas_names[1][0] == new_formula_B:
                #print(new_formula_B)
                return formulas_names[0]
    #"$B$\textbullet$C$\textbullet$E$"
    elif index_premis_circumstance == 3:
        new_formula_C = formula.replace("D", "C")
        new_formula_2 = new_formula_C.replace("E", "D")
        for i, formulas_names in enumerate(list_formulas_names):
            if formulas_names[1][0] == new_formula_2:
                #print(new_formula_2)
                return formulas_names[0]
    #"$B$\textbullet$D$\textbullet$E$"
    elif index_premis_circumstance == 4:
        for i, formulas_names in enumerate(list_formulas_names):
            if formulas_names[1][0] == formula:
                #print('premis_0: ',formula)
                return formulas_names[0]
    #"$B$\textbullet$C$\textbullet$D$"


begin_now = datetime.now()
print("BEGIN:", begin_now)


csv.register_dialect('myDialect', delimiter=' ', doublequote=True,
                         quoting=csv.QUOTE_NONE, skipinitialspace=True)

with open('output_step_13_(last_step)_file_20.05.2025.csv') as orders_file:
    reader = csv.reader(orders_file, delimiter=',')
    


    deducable_tetradic_formula_list = list(reader)


    deducable_tetradic_formula_copy = deducable_tetradic_formula_list[:]
        
    for k in range(len(deducable_tetradic_formula_copy)):
        if deducable_tetradic_formula_copy[k] == []:
            deducable_tetradic_formula_list.remove(deducable_tetradic_formula_copy[k])

    count_a = 0

    deleted_doubles_1 = []
    #for order in deducable_tetradic_formula_list:
        #if order[0] not in deleted_doubles_1:
            #deleted_doubles_1.append(order)
            #count_a = count_a + 1

    print(count_a)
    
    count_1 = 0
    count_2 = 0
    count_3 = 0
    count_4 = 0
    count_1qu = 0
    count_2qu = 0
    count_3qu = 0
    count_4qu = 0
    
    count_overall = 0
    count_overallqu = 0

    count_x = 0
    count_y = 0
    count_z = 0
    
    count_all = [count_1, count_2, count_3, count_4]
    count_allqu = [count_1qu, count_2qu, count_3qu, count_4qu]

    
    gluons = [8, 12, 14, 15, 20, 22, 24, 31, 36, 43, 44, 46, 50, 51, 55, 58, 70,\
              76, 77, 78, 82, 85, 87, 90, 100, 102, 107, 108, 109, 110, 113,\
              114, 121, 122, 136, 139, 141, 143, 148, 150, 152, 155, 157, 159,\
              163, 167, 169, 170, 177, 179, 181, 183, 197, 199, 201, 202, 209,\
              211, 213, 215, 225, 226, 233, 234]
    quarks = [4, 6, 11, 13, 18, 26, 27, 29, 35, 38, 39, 45, 49, 53, 57, 68,\
              69, 71, 75, 81, 83, 89, 99, 101, 132, 134, 137, 138, 146, 153,\
              161, 162, 165, 193, 194, 195]
    rest = [1, 2, 3, 5, 7, 9, 10, 17, 19, 21, 23, 25, 33, 34, 37, 41, 42, 65, 66,\
            67, 73, 74, 97, 98, 105, 106, 129, 130, 131, 133, 135, 145, 147, 149,\
            151]
    
    gluons_and_rest = gluons + rest
    gluons_and_quarks = gluons + quarks
    
    all_set =     [8, 12, 14, 15, 20, 22, 24, 31, 36, 43, 44, 46, 50, 51, 55, 58, 70,\
              76, 77, 78, 82, 85, 87, 90, 100, 102, 107, 108, 109, 110, 113,\
              114, 121, 122, 136, 139, 141, 143, 148, 150, 152, 155, 157, 159,\
              163, 167, 169, 170, 177, 179, 181, 183, 197, 199, 201, 202, 209,\
              211, 213, 215, 225, 226, 233, 234, 4, 6, 11, 13, 18, 26, 27, 29,\
               35, 38, 39, 45, 49, 53, 57, 68, 69, 71, 75, 81, 83, 89, 99, 101,\
               132, 134, 137, 138, 146, 153, 161, 162, 165, 193, 194, 195, 1,\
               2, 3, 5, 7, 9, 10, 17, 19, 21, 23, 25, 33, 34, 37, 41, 42, 65, 66,\
            67, 73, 74, 97, 98, 105, 106, 129, 130, 131, 133, 135, 145, 147, 149, 151]
    
    all_set.sort()
    gluons_and_rest.sort()

    for formula in deducable_tetradic_formula_list:
        formula[0] = eval(formula[0])
        formula[1] = eval(formula[1])
        if (len(formula)) == 3:
            formula[2] = eval(formula[2])
        elif (len(formula)) == 4:
            formula[2] = eval(formula[2])
            formula[3] = eval(formula[3])
        elif (len(formula)) == 5:
            formula[2] = eval(formula[2])
            formula[3] = eval(formula[3])
            formula[4] = eval(formula[4])
        elif (len(formula)) == 6:
            formula[2] = eval(formula[2])
            formula[3] = eval(formula[3])
            formula[4] = eval(formula[4])
            formula[5] = eval(formula[5])
        elif (len(formula)) == 7:
            formula[2] = eval(formula[2])
            formula[3] = eval(formula[3])
            formula[4] = eval(formula[4])
            formula[5] = eval(formula[5])
            formula[6] = eval(formula[6])
        elif (len(formula)) == 8:
            formula[2] = eval(formula[2])
            formula[3] = eval(formula[3])
            formula[4] = eval(formula[4])
            formula[5] = eval(formula[5])
            formula[6] = eval(formula[6])
            formula[7] = eval(formula[7])
        elif (len(formula)) == 10:
            formula[2] = eval(formula[2])
            formula[3] = eval(formula[3])
            formula[4] = eval(formula[4])
            formula[5] = eval(formula[5])
            formula[6] = eval(formula[6])
            formula[7] = eval(formula[7])
            formula[8] = eval(formula[8])
            formula[9] = eval(formula[9])

        
    count_e = []
    count_formulas = 0
    
    count_partition = 0
    
orders_file.close()


with open('new_attempt.csv', 'w') as file:
    file.close()

dictionaries = {}
for d in range(len(deducable_tetradic_formula_list)):
    dictionaries['X'+str(d)] = {"formula": " ", "formula_name": " ", "count" : 0}

edit_deducable_tetradic_formula_list = deducable_tetradic_formula_list[:]


for d, formula in enumerate(deducable_tetradic_formula_list):
    for e, formula_2 in enumerate(edit_deducable_tetradic_formula_list):
        #print(formula[1])
        if len(formula[0]) != 1 and len(formula_2[0]) != 1:
            #print('Whole: ', formula)
            #print('1: ', formula[1])
            #print('1;0;1: ', formula[1][0][1])
            #print('1;1;1: ', formula[1][1][1])
            #print('1;2;1: ', formula[1][2][1])
            #print('1;3;1: ', formula[1][3][1])
            if (formula[1][2][1] == formula_2[1][2][1] and \
                formula[1][1][1] == formula_2[1][1][1] and \
                formula[1][3][1] == formula_2[1][3][1]):

                dictionaries['X'+str(d)]["count"] = dictionaries['X'+str(d)]["count"] + 1
                
                #count_dummy_for_loop = dictionaries['X'+str(d)]["count"]
                
                if dictionaries['X'+str(d)]["count"] != 0:
                    
                    #print(formula_2[1][0][0][1])
                    #print(formula_2[1][0][2][1])
                    #print(formula_2[1][0][1][1])
                    #print(formula_2[1][0][3][1])
                    
                    #for f, formula_between in enumerate(deducable_tetradic_formula_list_between):
                    prem_1 = formula[1][2][1]
                    prem_2 = formula[1][1][1]
                    prem_3 = formula[1][3][1]
                    #prem_0 = formula[1][0][1]
                    
                    #print('prem_1: ', prem_1)
                    #print('prem_2: ', prem_2)
                    #print('prem_3: ', prem_3)
                    #print('prem_0: ', prem_0)
                    
                    enlonged_result_list = enlonged_fn(prem_1, prem_2, prem_3)
                    #print('formula[0]:', formula[0])
                    #print('formula_2[0]:', formula_2[0])
                    print(d, formula[0])
                    #print(enlonged_result_list)
                    #print([formula[0]])
                    #print('[0]:', formula[1][0][0])
                    #print(formula[1][1][0])
                    #print(formula[1][2][0])
                    #print(formula[1][3][0])
                    dictionaries['X'+str(d)]["formula"] = enlonged_result_list
                    dictionaries['X'+str(d)]["formula_name"] = enlonged_result_list[1]
                    formula_between_global_variable = enlonged_result_list

                    with open('new_attempt.csv', 'a') as file:
                        writer = csv.writer(file)
                    
                        writer.writerow([d+1, e+1, dictionaries['X'+str(d)]])
                    
                    file.close()
                            
                    edit_deducable_tetradic_formula_list[e] = [[],[[[], []], [[],[]], [[],[]], [[],[]]]]

                else:
                    dictionaries['X'+str(d)]["formula"] = formula_between_global_variable[0]
                    dictionaries['X'+str(d)]["formula_name"] = formula_between_global_variable[1]

                    with open('new_attempt.csv', 'a') as file:
                        writer = csv.writer(file)
                    
                        writer.writerow([d+1, e+1, dictionaries['X'+str(d)]])
                    
                    file.close()
                    
                    edit_deducable_tetradic_formula_list[e] = [[],[[[], []], [[],[]], [[],[]], [[],[]]]]     
                        #print(dictionaries['X'+str(d)])
        #name_function_prem_2 = function_number_to_name(formula_between[1][1][0], 2)

        #name_function_prem_3 = function_number_to_name(formula_between[1][2][0], 1)


            #name_function_prem_4 = function_number_to_name(formula[1][1][0][0], 4)

            #name_function_prem_1 = function_number_to_name(formula[1][0][0][0], 1)
            #name_function_prem_2 = function_number_to_name(formula[1][0][1][0], 2)
            #)


##################################################




end_now = datetime.now()
print("END:", end_now)


