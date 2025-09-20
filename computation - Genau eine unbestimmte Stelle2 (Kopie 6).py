from datetime import datetime
import csv
import ast

begin_now = datetime.now()
print("BEGIN:", begin_now)


csv.register_dialect('myDialect', delimiter=' ', doublequote=True,
                         quoting=csv.QUOTE_NONE, skipinitialspace=True)

with open('file_innerhalb_mit_geltungswertformeln_1_2_3.csv') as orders_file_1:
    reader = csv.reader(orders_file_1, delimiter=',')
    


    innerhalb = list(reader)


    innerhalb_copy = innerhalb[:]
        
    for k in range(len(innerhalb_copy)):
        if innerhalb_copy[k] == []:
            innerhalb.remove(innerhalb_copy[k])

    count_a = 0

    deleted_doubles_1 = []
    #for order in deducable_tetradic_formula_list:
        #if order[0] not in deleted_doubles_1:
            #deleted_doubles_1.append(order)
            #count_a = count_a + 1

    print(count_a)
    
    count_all = 0
    

    for formula in innerhalb:
        formula[0] = eval(formula[0])
        formula[1] = eval(formula[1])

        count_all = count_all + 1
orders_file_1.close()

with open('output_step_13_(last_step)_file_20.05.2025 (Kopieren).csv') as orders_file:
    reader = csv.reader(orders_file, delimiter=',')
    


    deducable_tetradic_formula_list = list(reader)

orders_file.close()

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

count_all = 0


for formula in deducable_tetradic_formula_list:
    formula[0] = eval(formula[0])
    formula[1] = eval(formula[1])
    if len(formula) == 3:
        formula[2] = eval(formula[2])
    if len(formula) == 4:
        formula[2] = eval(formula[2])
        formula[3] = eval(formula[3])
    if len(formula) == 5:
        formula[2] = eval(formula[2])
        formula[3] = eval(formula[3])
        formula[4] = eval(formula[4])
    if len(formula) == 6:
        formula[2] = eval(formula[2])
        formula[3] = eval(formula[3])
        formula[4] = eval(formula[4])
        formula[5] = eval(formula[5])
    if len(formula) == 7:
        formula[2] = eval(formula[2])
        formula[3] = eval(formula[3])
        formula[4] = eval(formula[4])
        formula[5] = eval(formula[5])
        formula[6] = eval(formula[6])
    if len(formula) == 8:
        formula[2] = eval(formula[2])
        formula[3] = eval(formula[3])
        formula[4] = eval(formula[4])
        formula[5] = eval(formula[5])
        formula[6] = eval(formula[6])
        formula[7] = eval(formula[7])
    if len(formula) == 9:
        formula[2] = eval(formula[2])
        formula[3] = eval(formula[3])
        formula[4] = eval(formula[4])
        formula[5] = eval(formula[5])
        formula[6] = eval(formula[6])
        formula[7] = eval(formula[7])
        formula[8] = eval(formula[8])
    if len(formula) == 10:
        formula[2] = eval(formula[2])
        formula[3] = eval(formula[3])
        formula[4] = eval(formula[4])
        formula[5] = eval(formula[5])
        formula[6] = eval(formula[6])
        formula[7] = eval(formula[7])
        formula[8] = eval(formula[8])
        formula[9] = eval(formula[9])

    count_all = count_all + 1

print(count_all)

count_ein_u = 0
count_zwei_u = 0
count_ohne_u = 0

count_8u = 0
count_7u = 0
count_6u = 0
count_5u = 0
count_4u = 0
count_3u = 0
count_2u = 0
count_1u = 0

gewichtet_8u = 1 # 6* 341.33
gewichtet_7u = 7/8
gewichtet_6u = (3/4) #65536/(192=16*12) =341.33
gewichtet_5u = (2/3) #65536/(192=16*12) =341.33 -1.33
gewichtet_4u = (1/2) #192.66+341.33
gewichtet_3u = (1/3) #48*37
gewichtet_2u = (1/4) #112 (= 2.4*46.66) *37
gewichtet_1u = (1/8) #192*65

gewicht_2_count_8u = 1/2

gewicht_2_count_6u = 3/8
gewicht_2_count_5u = 2/6
gewicht_2_count_4u = 1/4
gewicht_2_count_3u = 1/6
gewicht_2_count_2u = 1/8
gewicht_2_count_1u = 1/32

gewicht_2_count_0u = 0


count_0u = 0

print("---------------------------")

count_2u = 0

for formula_innerhalb in innerhalb:
    for total_formula in deducable_tetradic_formula_list:
        if len(total_formula[0]) != 1:
            if formula_innerhalb[1][0][0] == total_formula[1][1][1] and \
               formula_innerhalb[1][0][1] == total_formula[1][2][1] and \
               formula_innerhalb[1][0][2] == total_formula[1][3][1]:
                if formula_innerhalb[0].count("u") == 0:
                    if len(total_formula) == 2:
                        count_0u = count_0u + gewicht_2_count_0u
                    if len(total_formula) == 3:
                        count_0u = count_0u + gewicht_2_count_1u
                    if len(total_formula) == 4:
                        count_0u = count_0u + gewicht_2_count_2u
                    if len(total_formula) == 5:
                        count_0u = count_0u + gewicht_2_count_3u
                    if len(total_formula) == 6:
                        count_0u = count_0u + gewicht_2_count_4u
                    if len(total_formula) == 7:
                        count_0u = count_0u + gewicht_2_count_5u
                    if len(total_formula) == 8:
                        count_0u = count_0u + gewicht_2_count_6u
                    if len(total_formula) == 10:
                        count_0u = count_0u + gewicht_2_count_8u
                if formula_innerhalb[0].count("u") == 1:
                    if len(total_formula) == 2:
                        count_1u = count_1u + gewicht_2_count_0u
                    if len(total_formula) == 3:
                        count_1u = count_1u + gewicht_2_count_1u
                    if len(total_formula) == 4:
                        count_1u = count_1u + gewicht_2_count_2u
                    if len(total_formula) == 5:
                        count_1u = count_1u + gewicht_2_count_3u
                    if len(total_formula) == 6:
                        count_1u = count_1u + gewicht_2_count_4u
                    if len(total_formula) == 7:
                        count_1u = count_1u + gewicht_2_count_5u
                    if len(total_formula) == 8:
                        count_1u = count_1u + gewicht_2_count_6u
                    if len(total_formula) == 10:
                        count_1u = count_1u + gewicht_2_count_8u
  
                if formula_innerhalb[0].count("u") == 2:
                    if len(total_formula) == 2:
                        count_2u = count_2u + gewicht_2_count_0u
                    if len(total_formula) == 3:
                        count_2u = count_2u + gewicht_2_count_1u
                    if len(total_formula) == 4:
                        count_2u = count_2u + gewicht_2_count_2u
                    if len(total_formula) == 5:
                        count_2u = count_2u + gewicht_2_count_3u
                    if len(total_formula) == 6:
                        count_2u = count_2u + gewicht_2_count_4u
                    if len(total_formula) == 7:
                        count_2u = count_2u + gewicht_2_count_5u
                    if len(total_formula) == 8:
                        count_2u = count_2u + gewicht_2_count_6u
                    if len(total_formula) == 10:
                        count_2u = count_2u + gewicht_2_count_8u

                if formula_innerhalb[0].count("u") == 3:
                    if len(total_formula) == 2:
                        count_3u = count_3u + gewicht_2_count_0u
                    if len(total_formula) == 3:
                        count_3u = count_3u + gewicht_2_count_1u
                    if len(total_formula) == 4:
                        count_3u = count_3u + gewicht_2_count_2u
                    if len(total_formula) == 5:
                        count_3u = count_3u + gewicht_2_count_3u
                    if len(total_formula) == 6:
                        count_3u = count_3u + gewicht_2_count_4u
                    if len(total_formula) == 7:
                        count_3u = count_3u + gewicht_2_count_5u
                    if len(total_formula) == 8:
                        count_3u = count_3u + gewicht_2_count_6u
                    if len(total_formula) == 10:
                        count_3u = count_3u + gewicht_2_count_8u
                if formula_innerhalb[0].count("u") == 4:
                    if len(total_formula) == 2:
                        count_4u = count_4u + gewicht_2_count_0u
                    if len(total_formula) == 3:
                        count_4u = count_4u + gewicht_2_count_1u
                    if len(total_formula) == 4:
                        count_4u = count_4u + gewicht_2_count_2u
                    if len(total_formula) == 5:
                        count_4u = count_4u + gewicht_2_count_3u
                    if len(total_formula) == 6:
                        count_4u = count_4u + gewicht_2_count_4u
                    if len(total_formula) == 7:
                        count_4u = count_4u + gewicht_2_count_5u
                    if len(total_formula) == 8:
                        count_4u = count_4u + gewicht_2_count_6u
                    if len(total_formula) == 10:
                        count_4u = count_4u + gewicht_2_count_8u
                if formula_innerhalb[0].count("u") == 5:
                    if len(total_formula) == 2:
                        count_5u = count_5u + gewicht_2_count_0u
                    if len(total_formula) == 3:
                        count_5u = count_5u + gewicht_2_count_1u
                    if len(total_formula) == 4:
                        count_5u = count_5u + gewicht_2_count_2u
                    if len(total_formula) == 5:
                        count_5u = count_5u + gewicht_2_count_3u
                    if len(total_formula) == 6:
                        count_5u = count_5u + gewicht_2_count_4u
                    if len(total_formula) == 7:
                        count_5u = count_5u + gewicht_2_count_5u
                    if len(total_formula) == 8:
                        count_5u = count_5u + gewicht_2_count_6u
                    if len(total_formula) == 10:
                        count_5u = count_5u + gewicht_2_count_8u
                if formula_innerhalb[0].count("u") == 6:
                    if len(total_formula) == 2:
                        count_6u = count_6u + gewicht_2_count_0u
                    if len(total_formula) == 3:
                        count_6u = count_6u + gewicht_2_count_1u
                    if len(total_formula) == 4:
                        count_6u = count_6u + gewicht_2_count_2u
                    if len(total_formula) == 5:
                        count_6u = count_6u + gewicht_2_count_3u
                    if len(total_formula) == 6:
                        count_6u = count_6u + gewicht_2_count_4u
                    if len(total_formula) == 7:
                        count_6u = count_6u + gewicht_2_count_5u
                    if len(total_formula) == 8:
                        count_6u = count_6u + gewicht_2_count_6u
                    if len(total_formula) == 10:
                        count_6u = count_6u + gewicht_2_count_8u
                if formula_innerhalb[0].count("u") == 7:
                    if len(total_formula) == 2:
                        count_7u = count_7u + gewicht_2_count_0u
                    if len(total_formula) == 3:
                        count_7u = count_7u + gewicht_2_count_1u
                    if len(total_formula) == 4:
                        count_7u = count_7u + gewicht_2_count_2u
                    if len(total_formula) == 5:
                        count_7u = count_7u + gewicht_2_count_3u
                    if len(total_formula) == 6:
                        count_7u = count_7u + gewicht_2_count_4u
                    if len(total_formula) == 7:
                        count_7u = count_7u + gewicht_2_count_5u
                    if len(total_formula) == 8:
                        count_7u = count_7u + gewicht_2_count_6u
                    if len(total_formula) == 10:
                        count_7u = count_7u + gewicht_2_count_8u
                if formula_innerhalb[0].count("u") == 8:
                    if len(total_formula) == 2:
                        count_8u = count_8u + gewicht_2_count_0u
                    if len(total_formula) == 3:
                        count_8u = count_8u + gewicht_2_count_1u
                    if len(total_formula) == 4:
                        count_8u = count_8u + gewicht_2_count_2u
                    if len(total_formula) == 5:
                        count_8u = count_8u + gewicht_2_count_3u
                    if len(total_formula) == 6:
                        count_8u = count_8u + gewicht_2_count_4u
                    if len(total_formula) == 7:
                        count_8u = count_8u + gewicht_2_count_5u
                    if len(total_formula) == 8:
                        count_8u = count_8u + gewicht_2_count_6u
                    if len(total_formula) == 10:
                        count_8u = count_8u + gewicht_2_count_8u


print('ohne us: ', count_0u)

print('8u: ', count_8u,'gewichtet: ', gewichtet_8u)

print('7u: ', count_7u,'gewichtet: ',  gewichtet_7u)
print('6u: ', count_6u,'gewichtet: ',  gewichtet_6u)
print('5u: ', count_5u,'gewichtet: ',  gewichtet_5u)
print('4u: ', count_4u,'gewichtet: ',  gewichtet_4u)
print('3u: ', count_3u,'gewichtet: ',  gewichtet_3u)
print('2u: ', count_2u,'gewichtet: ',  gewichtet_2u)
print('1u: ', count_1u,'gewichtet: ',  gewichtet_1u)
print('0u: ', count_0u)


print("-----------------------")

x = gewichtet_8u + gewichtet_7u + gewichtet_6u + gewichtet_5u + gewichtet_4u + gewichtet_3u + gewichtet_2u + gewichtet_1u + 743

print('------------')
print(x)
z = count_1u+count_2u+count_3u+count_4u+count_5u+count_6u+count_7u+count_8u
print('------------')
print(z)
print("743+z: ", z+743)


end_now = datetime.now()
print("END:", end_now)

