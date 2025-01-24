from datetime import datetime
import csv

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
    if first_formula[3] == "a" and second_formula[4] == "n":  # calculates potential "a"-values of seventh value
        return ("a")
    elif first_formula[3] == "a" and third_formula[4] == "n":
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
        return ('W')
    conclusion[2] = tet_syllogism_deduction_second_value_n(first_formula, second_formula, third_formula)
    conclusion[3] = tet_syllogism_deduction_second_value_a(first_formula, second_formula, third_formula)
    if conclusion[2] == 'n' and conclusion[3] == 'a':
        return ('W')
    conclusion[4] = tet_syllogism_deduction_third_value_n(first_formula, second_formula, third_formula)
    conclusion[5] = tet_syllogism_deduction_third_value_a(first_formula, second_formula, third_formula)
    if conclusion[4] == 'n' and conclusion[5] == 'a':
        return ('W')
    conclusion[6] = tet_syllogism_deduction_fourth_value_n(first_formula, second_formula, third_formula)
    conclusion[7] = tet_syllogism_deduction_fourth_value_a(first_formula, second_formula, third_formula)
    if conclusion[6] == 'n' and conclusion[7] == 'a':
        return ('W')
    conclusion[8] = tet_syllogism_deduction_fifth_value_n(first_formula, second_formula, third_formula)
    conclusion[9] = tet_syllogism_deduction_fifth_value_a(first_formula, second_formula, third_formula)
    if conclusion[8] == 'n' and conclusion[9] == 'a':
        return ('W')
    conclusion[10] = tet_syllogism_deduction_sixth_value_n(first_formula, second_formula, third_formula)
    conclusion[11] = tet_syllogism_deduction_sixth_value_a(first_formula, second_formula, third_formula)
    if conclusion[10] == 'n' and conclusion[11] == 'a':
        return ('W')
    conclusion[12] = tet_syllogism_deduction_seventh_value_n(first_formula, second_formula, third_formula)
    conclusion[13] = tet_syllogism_deduction_seventh_value_a(first_formula, second_formula, third_formula)
    if conclusion[12] == 'n' and conclusion[13] == 'a':
        return ('W')
    conclusion[14] = tet_syllogism_deduction_eighth_value_n(first_formula, second_formula, third_formula)
    conclusion[15] = tet_syllogism_deduction_eighth_value_a(first_formula, second_formula, third_formula)
    if conclusion[14] == 'n' and conclusion[15] == 'a':
        return ('W')

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

def triadic_name_fn( formula, index_premis_circumstance):
    list_third_level = []
    list_third_level_list = []

    count_2 = 0
    for l in range(2):
        for m in range(2):
            for n in range(2):
                for o in range(2):
                    for p in range(2):
                        for q in range(2):
                            for r in range(2):
                                for s in range(2):
                                    if l == 0:
                                        list_third_level.append('a')
                                    elif l == 1:
                                        list_third_level.append('n')
                                    if m == 0:
                                        list_third_level.append('a')
                                    elif m == 1:
                                        list_third_level.append('n')
                                    if n == 0:
                                        list_third_level.append('a')
                                    elif n == 1:
                                        list_third_level.append('n')
                                    if o == 0:
                                        list_third_level.append('a')
                                    elif o == 1:
                                        list_third_level.append('n')
                                    if p == 0:
                                        list_third_level.append('a')
                                    elif p == 1:
                                        list_third_level.append('n')
                                    if q == 0:
                                        list_third_level.append('a')
                                    elif q == 1:
                                        list_third_level.append('n')
                                    if r == 0:
                                        list_third_level.append('a')
                                    elif r == 1:
                                        list_third_level.append('n')
                                    if s == 0:
                                        list_third_level.append('a')
                                    elif s == 1:
                                        list_third_level.append('n')
                                    if len(list_third_level) == 8:
                                        count_2 = count_2 + 1
                                        
                                        list_third_level_list.append([list_third_level[:]])
                                        #for t in range(len(list_removed_double_formulas_list)):
                                            #if list_third_level == list_removed_double_formulas_list[t][0]:
                                                #list_third_level_list.remove([list_third_level, 0])
                                                #list_third_level_list.append([list_removed_double_formulas_list[t][0], list_removed_double_formulas_list[t][1], list_removed_double_formulas_list[t][2]])
                                    list_third_level.clear()

    triadic_level_formulas_names_list = [\
        ["$B$\textbullet$C$\textbullet$D$ 1"],\
        ["$B$\textbullet$C$\textbullet$D$ 2"],\
        ["$B$\textbullet$C$\textbullet$D$ 3"],\
        ["$B\sqcup C, C\cup D, B\cup D, 1A, 5A$"],\
        ["$B$\textbullet$C$\textbullet$D$ 5"],\
        ["$B\cup C, C\cup D, B\sqcup D, 1A, 3A$"],\
        ["$B$\textbullet$C$\textbullet$D$ 7"],\
        ["$B\sqcup C, C\cup D, B\sqcup D, 1A$"],\
        ["$B$\textbullet$C$\textbullet$D$ 9"],\
        ["$B$\textbullet$C$\textbullet$D$ 10"],\
        ["$B\cup C, C\cup D, B\subset D, 5A, 7A$"],\
        ["$B\sqcup C, C\cup D, B\subset D, 5A$"],\
        ["$B\subset C, C\cup D, B\cup D, 3A, 7A$"],\
        ["$B\subset C, C\cup D, B\sqcup D, 3A$"],\
        ["$B\subset C, C\cup D, B\subset D, 7A$"],\
        ["$B\sqsubset C, C\cup D, B\sqsubset D$"],\
        ["$B$\textbullet$C$\textbullet$D$ 17"],\
        ["$B\cup C, C\sqcup D, B\cup D, 1A, 2A$"],\
        ["$B$\textbullet$C$\textbullet$D$ 19"],\
        ["$B\sqcup C, C\sqcup D, B\cup D, 1A$"],\
        ["$B$\textbullet$C$\textbullet$D$ 21"],\
        ["$B\cup C, C\sqcup D, B\sqcup D, 1A$"],\
        ["$B$\textbullet$C$\textbullet$D$ 23"],\
        ["$B\sqcup C, C\sqcup D, B\sqcup D, 1A$"],\
        ["$B$\textbullet$C$\textbullet$D$ 25"],\
        ["$B\cup C, C\sqcup D, B\cup D, 1A, 2N$"],\
        ["$B\cup C, C\cup D, B\subset D, 5A, 7N$"],\
        ["$B\sqcup C, C\sqcup D, B\subset D$"],\
        ["$B\subset C, C\cup D, B\cup D, 3A, 7N$"],\
        ["$B\subset C, C\sqcup D, B\sqcup D$"],\
        ["$B\subset C, C\cup D, B\subset D, 7N$"],\
        ["$B\sqsubset C, C\sqcup D, B\sqsubset D$"],\
        ["$B$\textbullet$C$\textbullet$D$ 33"],\
        ["$B$\textbullet$C$\textbullet$D$ 34"],\
        ["$B\cup C, C\subset D, B\cup D, 5A, 6A$"],\
        ["$B\sqcup C, C\subset D, B\cup D, 5A$"],\
        ["$B$\textbullet$C$\textbullet$D$ 37"],\
        ["$B\cup C, C\cup D, B\sqcup D, 1A, 3N$"],\
        ["$B\cup C, C\subset D, B\cup D, 5A, 6N$"],\
        ["$B\sqcup C, C\subset D, B\sqcup D$"],\
        ["$B$\textbullet$C$\textbullet$D$ 41"],\
        ["$B$\textbullet$C$\textbullet$D$ 42"],\
        ["$B\cup C, C\subset D, B\subset D, 5A$"],\
        ["$B\sqcup C, C\subset D, B\subset D, 5A$"],\
        ["$B\subset C, C\cup D, B\cup D, 3N, 7A$"],\
        ["$B\subset C, C\cup D, B\sqcup D, 3N$"],\
        ["$B\subset C, C\subset D, B\subset D$"],\
        ["$B\sqsubset C, C\subset D, B\sqsubset D$"],\
        ["$B\supset C, C\cup D, B\cup D, 2A, 6A$"],\
        ["$B\supset C, C\sqcup D, B\cup D, 2A$"],\
        ["$B\supset C, C\subset D, B\cup D, 6A$"],\
        ["$B\sqsupset C, C\sqsubset D, B\cup D$"],\
        ["$B\supset C, C\cup D, B\cup D, 2A, 6N$"],\
        ["$B\supset C, C\sqcup D, B\sqcup D$"],\
        ["$B\supset C, C\subset D, B\cup D, 6N$"],\
        ["$B\sqsupset C, C\sqsubset D, B\sqcup D$"],\
        ["$B\supset C, C\cup D, B\cup D, 2N, 6A$"],\
        ["$B\supset C, C\sqcup D, B\cup D, 2N$"],\
        ["$B\supset C, C\subset D, B\subset D$"],\
        ["$B\sqsupset C, C\sqsubset D, B\subset D$"],\
        ["$B\cap C, C\cup D, B\cup D$"],\
        ["$B\cap C, C\sqcup D, B\sqcup D$"],\
        ["$B\cap C, C\subset D, B\subset D$"],\
        ["$B\sqcap C, C\sqsubset D, B\sqsubset D$"],\
        ["$B$\textbullet$C$\textbullet$D$ 65"],\
        ["$B$\textbullet$C$\textbullet$D$ 66"],\
        ["$B$\textbullet$C$\textbullet$D$ 67"],\
        ["$B\sqcup C, C\cup D, B\cup D, 1A, 5N$"],\
        ["$B\cup C, C\supset D, B\cup D, 3A, 4A$"],\
        ["$B\cup C, C\supset D, B\sqcup D, 3A$"],\
        ["$B\cup C, C\supset D, B\cup D, 3A, 4N$"],\
        ["$B\sqcup C, C\supset D, B\sqcup D$"],\
        ["$B$\textbullet$C$\textbullet$D$ 73"],\
        ["$B$\textbullet$C$\textbullet$D$ 74"],\
        ["$B\cup C, C\cup D, B\subset D, 5N, 7A$"],\
        ["$B\sqcup C, C\cup D, B\subset D, 5N$"],\
        ["$B\subset C, C\supset D, B\cup D, 3A$"],\
        ["$B\subset C, C\supset D, B\sqcup D, 3A$"],\
        ["$B\subset C, C\supset D, B\subset D$"],\
        ["$B\sqsubset C, C\supset D, B\sqsubset D$"],\
        ["$B\cup C, C\cup D, B\supset D, 2A, 4A$"],\
        ["$B\cup C, C\sqcup D, B\supset D, 2A$"],\
        ["$B\cup C, C\cup D, B\supset D, 2A, 4N$"],\
        ["$B\sqcup C, C\sqcup D, B\supset D$"],\
        ["$B\cup C, C\supset D, B\supset D, 4A$"],\
        ["$B\cup C, C\sqsupset D, B\sqsupset D$"],\
        ["$B\cup C, C\supset D, B\supset D, 4N$"],\
        ["$B\sqcup C, C\sqsupset D, B\sqsupset D$"],\
        ["$B\cup C, C\cup D, B\supset D, 2N, 4A$"],\
        ["$B\cup C, C\sqcup D, B\supset D, 2N$"],\
        ["$B\cup C, C\cup D, B\cap D$"],\
        ["$B\sqcup C, C\sqcup D, B\cap D$"],\
        ["$B\subset C, C\supset D, B\supset D$"],\
        ["$B\subset C, C\sqsupset D, B\sqsupset D$"],\
        ["$B\subset C, C\supset D, B\cap D$"],\
        ["$B\sqsubset C, C\sqsupset D, B\sqcap D$"],\
        ["$B$\textbullet$C$\textbullet$D$ 97"],\
        ["$B$\textbullet$C$\textbullet$D$ 98"],\
        ["$B\cup C, C\subset D, B\cup D, 5N, 6A$"],\
        ["$B\sqcup C, C\subset D, B\cup D, 5N$"],\
        ["$B\cup C, C\supset D, B\cup D, 3N, 4A$"],\
        ["$B\cup C, C\supset D, B\sqcup D, 3N$"],\
        ["$B\cup C, C\cap D, B\cup D$"],\
        ["$B\sqcup C, C\cap D, B\sqcup D$"],\
        ["$B$\textbullet$C$\textbullet$D$ 105"],\
        ["$B$\textbullet$C$\textbullet$D$ 106"],\
        ["$B\cup C, C\subset D, B\subset D, 5N$"],\
        ["$B\sqcup C, C\subset D, B\subset D, 5N$"],\
        ["$B\subset C, C\supset D, B\cup D, 3N$"],\
        ["$B\subset C, C\supset D, B\sqcup D, 3N$"],\
        ["$B\subset C, C\cap D, B\subset D$"],\
        ["$B\sqsubset C, C\cap D, B\sqsubset D$"],\
        ["$B\supset C, C\cup D, B\supset D, 2A$"],\
        ["$B\supset C, C\sqcup D, B\supset D, 2A$"],\
        ["$B\supset C, C\subset D, B\supset D$"],\
        ["$B\sqsupset C, C\sqsubset D, B\supset D$"],\
        ["$B\supset C, C\supset D, B\supset D$"],\
        ["$B\supset C, C\sqsupset D, B\sqsupset D$"],\
        ["$B\supset C, C\cap D, B\supset D$"],\
        ["$B\sqsupset C, C\sqcap D, B\sqsupset D$"],\
        ["$B\supset C, C\cup D, B\supset D, 2N$"],\
        ["$B\supset C, C\sqcup D, B\supset D, 2N$"],\
        ["$B\supset C, C\subset D, B\cap D$"],\
        ["$B\sqsupset C, C\sqsubset D, B\cap D$"],\
        ["$B\cap C, C\supset D, B\supset D$"],\
        ["$B\cap C, C\sqsupset D, B\sqsupset D$"],\
        ["$B\cap C, C\cap D, B\cap D$"],\
        ["$B\sqcap C, C\sqcap D, B\sqcap D$"],\
        ["$B$\textbullet$C$\textbullet$D$ 129"],\
        ["$B$\textbullet$C$\textbullet$D$ 130"],\
        ["$B$\textbullet$C$\textbullet$D$ 131"],\
        ["$B\sqcup C, C\cup D, B\cup D, 1N, 5A$"],\
        ["$B$\textbullet$C$\textbullet$D$ 133"],\
        ["$B\cup C, C\cup D, B\sqcup D, 1N, 3A$"],\
        ["$B$\textbullet$C$\textbullet$D$ 135"],\
        ["$B\sqcup C, C\cup D, B\sqcup D, 1N$"],\
        ["$B\cup C, C\sqcap 'D, B\cup D, 7A, 8A$"],\
        ["$B\cup C, C\sqcap 'D, B\cup D, 7A, 8N$"],\
        ["$B\cup C, C\sqcap 'D, B\subset D, 7A$"],\
        ["$B\sqcup C, C\sqcap 'D, B\subset D$"],\
        ["$B\subset C, C\sqcap 'D, B\cup D, 7A$"],\
        ["$B\subset C, C\sqcap 'D, B\sqcup D$"],\
        ["$B\subset C, C\sqcap 'D, B\subset D, 7A$"],\
        ["$B\sqsubset C, C\sqcap 'D, B\sqsubset D$"],\
        ["$B$\textbullet$C$\textbullet$D$ 145"],\
        ["$B\cup C, C\sqcup D, B\cup D, 1N, 2A$"],\
        ["$B$\textbullet$C$\textbullet$D$ 147"],\
        ["$B\sqcup C, C\sqcup D, B\cup D, 1N$"],\
        ["$B$\textbullet$C$\textbullet$D$ 149"],\
        ["$B\cup C, C\sqcup D, B\sqcup D, 1N$"],\
        ["$B$\textbullet$C$\textbullet$D$ 151"],\
        ["$B\sqcup C, C\sqcup D, B\sqcup D, 1N$"],\
        ["$B\cup C, C\sqcap 'D, B\cup D, 7N, 8A$"],\
        ["$B\cup C, C\cap 'D, B\cup D$"],\
        ["$B\cup C, C\sqcap 'D, B\subset D, 7N$"],\
        ["$B\sqcup C, C\cap 'D, B\subset D$"],\
        ["$B\subset C, C\sqcap 'D, B\cup D, 7N$"],\
        ["$B\subset C, C\cap 'D, B\sqcup D$"],\
        ["$B\subset C, C\sqcap 'D, B\subset D, 7N$"],\
        ["$B\sqsubset C, C\cap 'D, B\sqsubset D$"],\
        ["$B\cup C, C\cup D, B\sqcap 'D, 6A, 8A$"],\
        ["$B\cup C, C\cup D, B\sqcap 'D, 6A, 8N$"],\
        ["$B\cup C, C\subset D, B\sqcap 'D, 6A$"],\
        ["$B\sqcup C, C\subset D, B\sqcap 'D$"],\
        ["$B\cup C, C\cup D, B\sqcap 'D, 6N, 8A$"],\
        ["$B\cup C, C\cup D, B\cap 'D$"],\
        ["$B\cup C, C\subset D, B\sqcap 'D, 6N$"],\
        ["$B\sqcup C, C\subset D, B\cap 'D$"],\
        ["$B\cup C, C\sqcap 'D, B\sqcap 'D, 8A$"],\
        ["$B\cup C, C\sqcap 'D, B\sqcap 'D, 8N$"],\
        ["$B\cup C, C\sqsupset 'D, B\sqsupset 'D$"],\
        ["$B\sqcup C, C\sqsupset 'D, B\sqsupset 'D$"],\
        ["$B\subset C, C\sqcap 'D, B\sqcap 'D$"],\
        ["$B\subset C, C\sqcap 'D, B\cap 'D$"],\
        ["$B\subset C, C\sqsupset 'D, B\sqsupset 'D$"],\
        ["$B\sqsubset C, C\sqsupset 'D, B\supset 'D$"],\
        ["$B\supset C, C\cup D, B\sqcap 'D, 6A$"],\
        ["$B\supset C, C\sqcup D, B\sqcap 'D$"],\
        ["$B\supset C, C\subset D, B\sqcap 'D, 6A$"],\
        ["$B\sqsupset C, C\sqsubset D, B\sqcap 'D$"],\
        ["$B\supset C, C\cup D, B\sqcap 'D, 6N$"],\
        ["$B\supset C, C\sqcup D, B\cap 'D$"],\
        ["$B\supset C, C\subset D, B\sqcap 'D, 6N$"],\
        ["$B\sqsupset C, C\sqsubset D, B\cap 'D$"],\
        ["$B\supset C, C\sqcap 'D, B\sqcap 'D$"],\
        ["$B\supset C, C\cap 'D, B\sqcap 'D$"],\
        ["$B\supset C, C\sqsupset 'D, B\sqsupset 'D$"],\
        ["$B\sqsupset C, C\supset 'D, B\sqsupset 'D$"],\
        ["$B\cap C, C\sqcap 'D, B\sqcap 'D$"],\
        ["$B\cap C, C\cap 'D, B\cap 'D$"],\
        ["$B\cap C, C\sqsupset 'D, B\sqsupset 'D$"],\
        ["$B\sqcap C, C\supset 'D, B\supset 'D$"],\
        ["$B\sqcap 'C, C\cup D, B\cup D, 4A, 8A$"],\
        ["$B\sqcap 'C, C\cup D, B\cup D, 4A, 8N$"],\
        ["$B\sqcap 'C, C\cup D, B\cup D, 4N, 8A$"],\
        ["$B\cap 'C, C\cup D, B\cup D$"],\
        ["$B\sqcap 'C, C\supset D, B\cup D, 4A$"],\
        ["$B\sqcap 'C, C\supset D, B\sqcup D$"],\
        ["$B\sqcap 'C, C\supset D, B\cup D, 4N$"],\
        ["$B\cap 'C, C\supset D, B\sqcup D$"],\
        ["$B\sqcap 'C, C\sqcap 'D, B\cup D, 8A$"],\
        ["$B\sqcap 'C, C\sqcap 'D, B\cup D, 8N$"],\
        ["$B\sqcap 'C, C\sqcap 'D, B\subset D$"],\
        ["$B\cap 'C, C\sqcap 'D, B\subset D$"],\
        ["$B\sqsupset 'C, C\sqsubset 'D, B\cup D$"],\
        ["$B\sqsupset 'C, C\sqsubset 'D, B\sqcup D$"],\
        ["$B\sqsupset 'C, C\sqsubset 'D, B\subset D$"],\
        ["$B\supset 'C, C\sqsubset 'D, B\sqsubset D$"],\
        ["$B\sqcap 'C, C\cup D, B\supset D, 4A$"],\
        ["$B\sqcap 'C, C\sqcup D, B\supset D$"],\
        ["$B\sqcap 'C, C\cup D, B\supset D, 4N$"],\
        ["$B\cap 'C, C\sqcup D, B\supset D$"],\
        ["$B\sqcap 'C, C\supset D, B\supset D, 4A$"],\
        ["$B\sqcap 'C, C\sqsupset D, B\sqsupset D$"],\
        ["$B\sqcap 'C, C\supset D, B\supset D, 4N$"],\
        ["$B\cap 'C, C\sqsupset D, B\sqsupset D$"],\
        ["$B\sqcap 'C, C\sqcap 'D, B\supset D$"],\
        ["$B\sqcap 'C, C\cap 'D, B\supset D$"],\
        ["$B\sqcap 'C, C\sqcap 'D, B\cap D$"],\
        ["$B\cap 'C, C\cap 'D, B\cap D$"],\
        ["$B\sqsupset 'C, C\sqsubset 'D, B\supset D$"],\
        ["$B\sqsupset 'C, C\subset 'D, B\sqsupset D$"],\
        ["$B\sqsupset 'C, C\sqsubset 'D, B\cap D$"],\
        ["$B\supset 'C, C\subset 'D, B\sqcap D$"],\
        ["$B\sqcap 'C, C\cup D, B\sqcap 'D, 8A$"],\
        ["$B\sqcap 'C, C\cup D, B\sqcap 'D, 8N$"],\
        ["$B\sqcap 'C, C\subset D, B\sqcap 'D$"],\
        ["$B\cap' C, C\subset D, B\sqcap 'D$"],\
        ["$B\sqcap 'C, C\supset D, B\sqcap 'D$"],\
        ["$B\sqcap 'C, C\supset D, B\cap 'D$"],\
        ["$B\sqcap 'C, C\cap D, B\sqcap 'D$"],\
        ["$B\cap 'C, C\cap D, B\cap 'D$"],\
        ["$B\sqcap 'C, C\sqcap 'D B\sqcap 'D, 8A$"],\
        ["$B\sqcap 'C, C\sqcap 'D B\sqcap 'D, 8N$"],\
        ["$B\sqcap 'C, C\sqsupset 'D, B\sqsupset 'D$"],\
        ["$B\cap 'C, C\sqsupset 'D, B\sqsupset 'D$"],\
        ["$B\sqsupset 'C, C\sqsubset 'D, B\sqcap 'D$"],\
        ["$B\sqsupset 'C, C\sqsubset 'D, B\cap 'D$"],\
        ["$B\sqsupset 'C, C\sqcup 'D, B\sqsupset 'D$"],\
        ["$B\supset 'C, C\sqcup 'D, B\supset 'D$"],\
        ["$B\sqsubset 'C, C\cup D, B\sqsubset 'D$"],\
        ["$B\sqsubset 'C, C\sqcup D, B\sqsubset 'D$"],\
        ["$B\sqsubset 'C, C\subset D, B\sqsubset 'D$"],\
        ["$B\subset 'C, C\sqsubset D, B\sqsubset 'D$"],\
        ["$B\sqsubset 'C, C\supset D, B\sqsubset 'D$"],\
        ["$B\sqsubset 'C, C\sqsupset D, B\subset 'D$"],\
        ["$B\sqsubset 'C, C\cap D, B\sqsubset 'D$"],\
        ["$B\subset 'C, C\sqcap D, B\subset 'D$"],\
        ["$B\sqsubset 'C, C\sqcap 'D, B\sqsubset 'D$"],\
        ["$B\sqsubset 'C, C\cap 'D, B\sqsubset 'D$"],\
        ["$B\sqsubset 'C, C\sqsupset 'D, B\sqcup 'D$"],\
        ["$B\subset 'C, C\supset 'D, B\sqcup 'D$"],\
        ["$B\sqcup 'C, C\sqsubset 'D, B\sqsubset 'D$"],\
        ["$B\sqcup 'C, C\subset 'D, B\subset 'D$"],\
        ["$B\sqcup 'C, C\sqcup 'D, B\sqcup 'D$"],\
        ["$B\cup 'C, C\cup 'D, B\cup 'D$"]\
    ]

    for i, formula_list_A_N in enumerate(list_third_level_list):
        for formula_list_name in triadic_level_formulas_names_list:
            if formula_list_A_N[0] == formula:
                #print(formula_list_name[0])
                if index_premis_circumstance == 2:
                    new_formula_A = triadic_level_formulas_names_list[i][0][:].replace("B", "X")
                    new_formula_2 = new_formula_A.replace("D", "E")
                    new_formula_3 = new_formula_2.replace("C", "D")
                    new_formula_4 = new_formula_3.replace("X", "C")
                    return [new_formula_4]
                #"$C$\textbullet$D$\textbullet$E$"
                elif index_premis_circumstance == 1:
                    new_formula_B = triadic_level_formulas_names_list[i][0][:].replace("D", "E")
                    return [new_formula_B]
                #"$B$\textbullet$C$\textbullet$E$"
                elif index_premis_circumstance == 3:
                    new_formula_C = triadic_level_formulas_names_list[i][0][:].replace("D", "E")
                    new_formula_2 = new_formula_C.replace("C", "D")
                    return [new_formula_2]
                #"$B$\textbullet$D$\textbullet$E$"
                elif index_premis_circumstance == 4:
                    return [triadic_level_formulas_names_list[i][0]]
                #"$B$\textbullet$C$\textbullet$D$"

def enlonged_fn(*args):

    #calculate from enlonged triadic formulas to fourth enlonged tetradic formula
    #needs about 32 minutes to calculate
    with open('main_output_innerhalb_der_Stufe (1. Schritt).csv', 'w') as file:
        writer = csv.writer(file)
        
        list_third_level_input = []
        count = 0

        #count_x = 0

        list_of_total_formulas_edited = []
        
        dummy_list = []
        
        begin_now = datetime.now()
        print("BEGIN:", begin_now)
        
        for i in range(2**24):
            ones_and_zeros = '{:024b}'.format(i)
            list_ones_and_zeros = list(ones_and_zeros)
            
            for j in range(24):
                if list_ones_and_zeros[j] == "1":
                    list_ones_and_zeros[j] = "n"
                if list_ones_and_zeros[j] == "0":
                    list_ones_and_zeros[j] = "a"

            first_formula_tri = list_ones_and_zeros[0:8]
            second_formula_tri =  list_ones_and_zeros[8:16]
            third_formula_tri = list_ones_and_zeros[16:24]
                                                                                                                                            
            
            syllogism_solution_tet = syllogism_contradiction_test_tet(first_formula_tri, second_formula_tri, third_formula_tri)

            if (syllogism_solution_tet[0] != 'W'):
                                                                                                                                                        
                first_formula = triadic_name_fn(first_formula_tri, 1)
                second_formula = triadic_name_fn(second_formula_tri, 2)
                third_formula = triadic_name_fn(third_formula_tri, 3)
                
                fourth_formula_tri = syllogism_solution_tet[0]
                if syllogism_solution_tet[0].count('u') == 0:
                    fourth_formula = triadic_name_fn(fourth_formula_tri, 4)
                else:
                    fourth_formula = 'u. k.'
                writer.writerow([syllogism_solution_tet[0], [[first_formula, second_formula, third_formula], [fourth_formula]]])
                
        file.close()    
                                                                                                                                          
    end_now = datetime.now()
    print("END:", end_now)

enlonged_fn()