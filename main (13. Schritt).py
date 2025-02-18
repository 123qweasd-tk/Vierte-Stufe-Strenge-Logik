from datetime import datetime
import csv
import ast

begin_now = datetime.now()
print("BEGIN:", begin_now)


csv.register_dialect('myDialect', delimiter=' ', doublequote=True,
                         quoting=csv.QUOTE_NONE, skipinitialspace='True')

with open('main_output (5. Schritt).csv') as orders_file:
    reader = csv.reader(orders_file, delimiter=',')
    
    with open('main_output (6. Schritt).csv', 'wt') as output_file:
        writer = csv.writer(output_file)

        orders = list(reader)
        
        print(orders[0])
        print(orders[67048])
        
        print(orders[0][0])
        print(orders[67048][0])
        
        print(orders[0][0][0])
        print(orders[67048][0][0])


        
        copy_oders = orders[:]
        
        for k in range(len(copy_oders)):
            if copy_oders[k] == []:
                orders.remove(copy_oders[k])

        for formula in orders:
            
            formula[0] = ast.literal_eval(formula[0])

        print(orders[0])
        print(orders[33524])
        
        print(orders[0][0])
        print(orders[33524][0])
        
        print(orders[0][0][0])
        print(orders[33524][0][0])

        list_new = sorted(orders, key=lambda x: (x!=('a'), (x[0][0], x[0][8], x[0][4], x[0][12], x[0][2], x[0][10], x[0][6], x[0][14], x[0][1], x[0][9], x[0][5], x[0][13], x[0][3], x[0][11], x[0][7], x[0][15])))
        #print(list_new)            
        
        for w, formula in enumerate(list_new):
            if len(formula) == 1:
                writer.writerow([formula, ['$B$\textbullet$C$\textbullet$D$\textbullet$E$', w+1]])
            else:
                writer.writerow(formula)
    
    
    
    output_file.close()
orders_file.close()


end_now = datetime.now()
print("END:", end_now)
