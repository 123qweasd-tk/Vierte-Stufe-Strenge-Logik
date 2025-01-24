from datetime import datetime
import csv

begin_now = datetime.now()
print("BEGIN:", begin_now)


csv.register_dialect('myDialect', delimiter=' ', doublequote=True,
                         quoting=csv.QUOTE_NONE, skipinitialspace=True)

with open('main_output (4. Schritt).csv') as orders_file:
    reader = csv.reader(orders_file, delimiter=',')
    
    with open('main_output (5. Schritt).csv', 'wt') as output_file:
        writer = csv.writer(output_file)

        deducable_tetradic_formula_list = list(reader)


        deducable_tetradic_formula_copy = deducable_tetradic_formula_list[:]
        
        for k in range(len(deducable_tetradic_formula_copy)):
            if deducable_tetradic_formula_copy[k] == []:
                deducable_tetradic_formula_list.remove(deducable_tetradic_formula_copy[k])

        tetradic_level_formulas_list = []
        
        for i in range(2**16):
            ones_and_zeros = '{:016b}'.format(i)
            list_ones_and_zeros = list(ones_and_zeros)
            
                
            for j in range(16):
                if list_ones_and_zeros[j] == "1":
                    list_ones_and_zeros[j] = "n"
                if list_ones_and_zeros[j] == "0":
                    list_ones_and_zeros[j] = "a"
            
            total_formula_list_entry = list_ones_and_zeros[0:16]
                
            tetradic_level_formulas_list.append([total_formula_list_entry])
            
        tetradic_level_formulas_list_copy = tetradic_level_formulas_list[:]


        for tetradic_level_formula in tetradic_level_formulas_list_copy:
            for deducable_tetradic_formula in deducable_tetradic_formula_list:
                #print(str(tetradic_level_formula[0]), str(deducable_tetradic_formula[0]))
                if str(tetradic_level_formula[0]) == str(deducable_tetradic_formula[0]):
                    #print('test')
                    tetradic_level_formulas_list.remove(tetradic_level_formula)
                    tetradic_level_formulas_list.append(deducable_tetradic_formula)

        #tetradic_level_formulas_list_sorted = sorted(tetradic_level_formulas_list, key=lambda x: (x!=('a'), (x[0][0], x[0][8], x[0][4], x[0][12], x[0][2], x[0][10], x[0][6], x[0][14], x[0][1], x[0][9], x[0][5], x[0][13], x[0][3], x[0][11], x[0][7], x[0][15])))

        for formula in tetradic_level_formulas_list_sorted:
            writer.writerow(formula)


        


    output_file.close()
orders_file.close()


end_now = datetime.now()
print("END:", end_now)

