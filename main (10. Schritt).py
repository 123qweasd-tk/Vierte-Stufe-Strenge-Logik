from datetime import datetime
import csv



def replace_n_times_fn(list_tetradic_level_raw, writer, *args):
    #print(list_tetradic_level_raw[0])
    if list_tetradic_level_raw[0].count('u') == 0:
                        
        writer.writerow(list_tetradic_level_raw)
                
    return(0)

begin_now = datetime.now()
print("BEGIN:", begin_now)


csv.register_dialect('myDialect', delimiter=' ', doublequote=True,
                         quoting=csv.QUOTE_NONE, skipinitialspace='True')

input_file = open("main_output (9. Schritt) _ alle us und 8u.csv", 'r')
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
