from datetime import datetime
import csv
import ast

begin_now = datetime.now()
print("BEGIN:", begin_now)


csv.register_dialect('myDialect', delimiter=' ', doublequote=True,
                         quoting=csv.QUOTE_NONE, skipinitialspace=True)

with open('main_output (9. Schritt) _ alle us und 8u.csv') as orders_file:
    reader = csv.reader(orders_file, delimiter=',')
    
    with open('main_output (10. Schritt) _ alle us und 8u.csv', 'wt') as output_file:

        writer = csv.writer(output_file)
        
        

        deducable_tetradic_formula_list = list(reader)


        deducable_tetradic_formula_copy = deducable_tetradic_formula_list[:]
            
        for k in range(len(deducable_tetradic_formula_copy)):
            if deducable_tetradic_formula_copy[k] == []:
                deducable_tetradic_formula_list.remove(deducable_tetradic_formula_copy[k])

        count_a = 0

        deducable_tetradic_formula_list = sorted(deducable_tetradic_formula_list, key=len)

        deleted_doubles_1 = []
        for order in deducable_tetradic_formula_list:
            if order[0] not in deleted_doubles_1:
                deleted_doubles_1.append(order)
                count_a = count_a + 1

        print(count_a)
        
        count_all = 0
        

        for formula in deducable_tetradic_formula_list:
            formula[0] = eval(formula[0])
            formula[1] = eval(formula[1])
            if len(formula) == 3:
                formula[2] = eval(formula[2])
            count_all = count_all + 1

        print(count_all)
        
        count_ein_u = 0
        count_ein_u_2 = 0
        count_ein_u_3 = 0
        count_zwei_u = 0
        count_zwei_u_2 = 0
        count_zwei_u_3 = 0
        count_ohne_u = 0
        count_ohne_u_2 = 0
        count_ohne_u_3 = 0
        
        count_drei_u = 0
        
        count_vier_u = 0
        count_fünf_u = 0
        count_sechs_u = 0
        count_sieben_u = 0
        count_acht_u = 0
        
        double_formulas = []
        
        count_x = 0
        
        deleted_doubles_x = []
        for formula in deducable_tetradic_formula_list:
            if formula[0] not in deleted_doubles_x:
                deleted_doubles_x.append(formula[0])
                writer.writerow(formula)
                double_formulas.append(formula)
                count_x = count_x + 1
                
        for formula in double_formulas:
            if len(formula) == 2:
                count_ohne_u = count_ohne_u + 1
            elif len(formula) == 3:
                count_ein_u = count_ein_u + 1
            elif len(formula) == 4:
                count_zwei_u = count_zwei_u + 1
            elif len(formula) == 5:
                count_drei_u = count_drei_u + 1
            elif len(formula) == 6:
                count_vier_u = count_vier_u + 1
            elif len(formula) == 7:
                count_fünf_u = count_fünf_u + 1
            elif len(formula) == 8:
                count_sechs_u = count_sechs_u + 1
            elif len(formula) == 9:
                count_sieben_u = count_sieben_u + 1
            elif len(formula) == 10:
                count_acht_u = count_acht_u + 1
                
        print(count_ohne_u, 'ohne: ', '0')
        print(count_ein_u, ':1 ')
        print(count_zwei_u, ':2 ')
        print(count_drei_u, ':3 ')
        print(count_vier_u, ':4 ')
        print(count_fünf_u, ':5 ')
        print(count_sechs_u, ':6 ')
        print(count_sieben_u, ':7 ')
        print(count_acht_u, ':8 ')


"""

BEGIN: 2025-02-06 15:41:26.401139
81553
81553
33489 ohne:  0
12480 :1 
8288 :2 
3552 :3 
2136 :4 
1360 :5 
2112 :6 
0 :7 
1376 :8 
END: 2025-02-06 15:46:51.589750
"""
    
output_file.close()
orders_file.close()


end_now = datetime.now()
print("END:", end_now)

