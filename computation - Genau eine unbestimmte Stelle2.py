from datetime import datetime
import csv
import ast

begin_now = datetime.now()
print("BEGIN:", begin_now)


csv.register_dialect('myDialect', delimiter=' ', doublequote=True,
                         quoting=csv.QUOTE_NONE, skipinitialspace=True)

with open('new_attempt_21_5_2025.csv') as orders_file:
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
    
    count_all = 0
    

    for formula in deducable_tetradic_formula_list:
        formula[0] = eval(formula[0])
        formula[1] = eval(formula[1])
        formula[2] = eval(formula[2])

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
    
    count_0u = 0
    
    for formula in deducable_tetradic_formula_list:
        #print(formula[2])
        #print(formula[2]["formula_3of4"][0][0])
        if formula[2]["formula_3of4"][0].count('u') == 0:
            count_0u = count_0u + 1
        
        if formula[2]["formula_3of4"][0].count('u') == 8:
            count_8u = count_8u + 1
        if formula[2]["formula_3of4"][0].count('u') == 7:
            count_7u = count_7u + 1
        if formula[2]["formula_3of4"][0].count('u') == 6:
            count_6u = count_6u + 1
        if formula[2]["formula_3of4"][0].count('u') == 5:
            count_5u = count_5u + 1
        if formula[2]["formula_3of4"][0].count('u') == 4:
            count_4u = count_4u + 1
        if formula[2]["formula_3of4"][0].count('u') == 3:
            count_3u = count_3u + 1
        if formula[2]["formula_3of4"][0].count('u') == 2:
            count_2u = count_2u + 1
        if formula[2]["formula_3of4"][0].count('u') == 1:
            count_1u = count_1u + 1
    
    
    gewichtet_8u = count_8u*0.5
    gewichtet_7u = count_7u*(7/12)
    gewichtet_6u = count_6u*(2/3)
    gewichtet_5u = count_5u*(17/24)
    gewichtet_4u = count_4u*(3/4)
    gewichtet_3u = count_3u*(19/24)
    gewichtet_2u = count_2u*(5/6)
    gewichtet_1u = count_1u*(11/12)
    
    print('ohne us: ', count_0u)
    
    print(count_8u,'gewichtet: ', gewichtet_8u)
    
    print(count_7u,'gewichtet: ',  gewichtet_7u)
    print(count_6u,'gewichtet: ',  gewichtet_6u)
    print(count_5u,'gewichtet: ',  gewichtet_5u)
    print(count_4u,'gewichtet: ',  gewichtet_4u)
    print(count_3u,'gewichtet: ',  gewichtet_3u)
    print(count_2u,'gewichtet: ',  gewichtet_2u)
    print(count_1u,'gewichtet: ',  gewichtet_1u)



    x = gewichtet_8u + gewichtet_7u + gewichtet_6u + gewichtet_5u + gewichtet_4u + gewichtet_3u + gewichtet_2u + gewichtet_1u
    
    print('------------')
    print(x)

    count_0a = 0
    count_7a = 0
    count_6a = 0
    count_5a = 0
    count_4a = 0
    count_3a = 0
    count_2a = 0
    count_1a = 0

    for formula in deducable_tetradic_formula_list:
        if formula[2]["formula_3of4"][0].count('u') >= 1:
            
            if formula[2]["formula_3of4"][0].count('a') == 8:
                count_0a = count_0a + 1
            if formula[2]["formula_3of4"][0].count('a') == 7:
                count_7a = count_7a + 1
            if formula[2]["formula_3of4"][0].count('a') == 6:
                count_6a = count_6a + 1
            if formula[2]["formula_3of4"][0].count('a') == 5:
                count_5a = count_5a + 1
            if formula[2]["formula_3of4"][0].count('a') == 4:
                count_4a = count_4a + 1
            if formula[2]["formula_3of4"][0].count('a') == 3:
                count_3a = count_3a + 1
            if formula[2]["formula_3of4"][0].count('a') == 2:
                count_2a = count_2a + 1
            if formula[2]["formula_3of4"][0].count('a') == 1:
                count_1a = count_1a + 1
            
    gewichtet_0a = count_0a*0.5
    gewichtet_1a = count_1a*(7/12)
    gewichtet_2a = count_2a*(2/3)
    gewichtet_3a = count_3a*(17/24)
    gewichtet_4a = count_4a*(3/4)
    gewichtet_5a = count_5a*(19/24)
    gewichtet_6a = count_6a*(5/6)
    gewichtet_7a = count_7a*(11/12)
    
    print(count_0a,'gewichtet: ', gewichtet_0a)
    
    print(count_7a,'gewichtet: ',  gewichtet_7a)
    print(count_6a,'gewichtet: ',  gewichtet_6a)
    print(count_5a,'gewichtet: ',  gewichtet_5a)
    print(count_4a,'gewichtet: ',  gewichtet_4a)
    print(count_3a,'gewichtet: ',  gewichtet_3a)
    print(count_2a,'gewichtet: ',  gewichtet_2a)
    print(count_1a,'gewichtet: ',  gewichtet_1a)



    y = gewichtet_0a + gewichtet_7a + gewichtet_6a + gewichtet_5a + gewichtet_4a + gewichtet_3a + gewichtet_2a + gewichtet_1a
    
    print('-----------')
    print(y)

    count_set = []
    new_set = []

    for d, formula in enumerate(deducable_tetradic_formula_list):
        for e, formula_2 in enumerate(deducable_tetradic_formula_list):
            if formula[2]["formula_3of4"] not in new_set:
                new_set.append(formula[2]["formula_3of4"])
    
    dictionaries = {}
    
    for e, formula in enumerate(new_set):
        dictionaries['X'+str(e)] = {"count": 0, "formula": formula}

    for d, formula in enumerate(deducable_tetradic_formula_list):
        for e, formula_new_set in enumerate(new_set):
            if formula[2]["formula_3of4"] == dictionaries['X'+str(e)]["formula_3of4"]:
                dictionaries['X'+str(e)]["count"] = dictionaries['X'+str(e)]["count"] + 1
                
orders_file.close()


for x, y in dictionaries.items():
  print(x, y)

with open('Computation_21_05_2025.csv', 'w') as orders_file_2:
    writer = csv.writer(orders_file_2, delimiter=',')
    for x, y in dictionaries.items():
                
        writer.writerow([x, y])
    
orders_file_2.close()


end_now = datetime.now()
print("END:", end_now)


