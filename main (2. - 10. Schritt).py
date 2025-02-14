from datetime import datetime
import csv

def replace_total_formulas_fn(total_formula_old, *args):
    

    for j in range(16):
        if total_formula_old[j] == 'u':
            total_formula_old[j] = 'a'    
            total_formula_new_A = total_formula_old[:]
            total_formula_old[j] = 'n'
            total_formula_new_N = total_formula_old[:]
        
            return(total_formula_new_A, total_formula_new_N, j+1)
    return(0)
    


def replace_n_times_fn(list_tetradic_level_raw, writer, *args):
    #print(list_tetradic_level_raw[0])
    if list_tetradic_level_raw[0].count('u') != 0:
        both_new_formulas = replace_total_formulas_fn(eval(list_tetradic_level_raw[:][0][:]))
            
        
        fixed_unkown = eval(list_tetradic_level_raw[2])
        fixed_unkown_2 = eval(list_tetradic_level_raw[3])
        fixed_unkown_3 = eval(list_tetradic_level_raw[4])
        fixed_unkown_4 = eval(list_tetradic_level_raw[5])
        fixed_unkown_5 = eval(list_tetradic_level_raw[6])
        fixed_unkown_6 = eval(list_tetradic_level_raw[7])
        fixed_unkown_7 = eval(list_tetradic_level_raw[8])
        
        first_formula = [both_new_formulas[:][0][:], list_tetradic_level_raw[:][1][:], [fixed_unkown[0]], [fixed_unkown_2[0]], [fixed_unkown_3[0]], [fixed_unkown_4[0]], [fixed_unkown_5[0]], [fixed_unkown_6[0]], [fixed_unkown_7[0]], [str(both_new_formulas[2])+'A']]

                
        writer.writerow(first_formula)
                
        second_formula = [both_new_formulas[:][1][:], list_tetradic_level_raw[:][1][:], [fixed_unkown[0]], [fixed_unkown_2[0]], [fixed_unkown_3[0]], [fixed_unkown_4[0]], [fixed_unkown_5[0]], [fixed_unkown_6[0]], [fixed_unkown_7[0]], [str(both_new_formulas[2])+'N']]
                
        writer.writerow(second_formula)
    else:
        writer.writerow(list_tetradic_level_raw)
                
    return(0)

begin_now = datetime.now()
print("BEGIN:", begin_now)


csv.register_dialect('myDialect', delimiter=' ', doublequote=True,
                         quoting=csv.QUOTE_NONE, skipinitialspace='True')

input_file = open("main_output (8. Schritt) _ alle us.csv", 'r')
input_file = input_file.read().replace('“', '').replace('”', '').splitlines()
normal = csv.reader(input_file, dialect='myDialect')
with open('main_output (9. Schritt) _ alle us und 8u.csv', 'wt') as output_file:

    spamreader = csv.reader(input_file, skipinitialspace=True, delimiter=',', quotechar='"')
    writer = csv.writer(output_file)
        
    for row in spamreader:
            
        if row != []:
            #print(row)
            #print(row[0])
            replace_n_times_fn(row,writer)
                


    


        
output_file.close()


end_now = datetime.now()
print("END:", end_now)