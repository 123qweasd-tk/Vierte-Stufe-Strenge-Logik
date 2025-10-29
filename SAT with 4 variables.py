###needs about 1.5 minutes

from datetime import datetime
import csv

import itertools
#from normal_form import cnf
#from normal_form import sat
from pysat.formula import CNF

from pysat.formula import WCNF

from pysat.formula import *

from pysat.examples.rc2 import RC2

from pprint import pprint
import cnfgen

def latex_fn(*args):
    
    
    F = cnfgen.CNF()
    with open('LATEX.csv', 'a') as file_2:
        
        writer = csv.writer(file_2)
        
        for lolo in args:
            F.add_clause(lolo)
        writer.writerow([F.to_latex()])
        file_2.close()
        
def sat_fn(*args):
    
    
    wcnf = WCNF()
    with open('file_Np_p_latex_formulas.txt', 'a') as file_2:
        
        writer = csv.writer(file_2)
        
        for lolo in args:
            wcnf.append(lolo)
        with RC2(wcnf) as rc2:

            for count_sat, m in enumerate(rc2.enumerate()):
                
                pass
        
        writer.writerow([count_sat+1])
        file_2.close()
        

begin_now = datetime.now()
print("BEGIN:", begin_now)

list_1 =    [[1, 2, 3, 4] , \
            [1, 2, 3, -4] , \
            [1, 2, -3, 4] , \
            [1, 2, -3, -4] , \
            [1, -2, 3, 4] , \
            [1, -2, 3, -4] , \
            [1, -2, -3, 4] , \
            [1, -2, -3, -4] , \
            [-1, 2, 3, 4] , \
            [-1, 2, 3, -4] , \
            [-1, 2, -3, 4] , \
            [-1, 2, -3, -4] , \
            [-1, -2, 3, 4] , \
            [-1, -2, 3, -4] , \
            [-1, -2, -3, 4] , \
            [-1, -2, -3, -4]]
count = 0
count_2 = 0
count_3= 0
count_4 = 0
count_5 = 0
count_6 = 0
count_7 = 0
count_8 = 0
count_9 = 0
count_10 = 0
count_11 = 0
count_12 = 0
count_13 = 0
count_14 = 0
count_15 = 0
#for x in range(list_1):

with open('LATEX.csv', 'w') as file:
    writer = csv.writer(file)
    file.close() 

for o in list_1:
    #print(o)
    count_2 = count_2 +1
    latex_fn(o)
    for i, j in itertools.combinations((list_1), 2):
        if o==j:
            #print(i,j)
            count_3= count_3+1
            latex_fn(i,j)
            #print(F.to_latex())
            for k, l, m in itertools.combinations((list_1), 3):

                if i == l and j==m:

                    count=count+1
                    #print(k,l,m)
                    latex_fn(k,l,m)
                    for n, p, q, r in itertools.combinations((list_1), 4):
                        if q == l and p == k and m==r:
                            
                            count_4=count_4+1
                            #print(n,p,q,r)
                            latex_fn(n,p,q,r)
                            for a1, a2, a3, a4, a5 in itertools.combinations((list_1), 5):
                                if a5 ==r and a4 == q and a3==p and a2==n:
                                    
                                    count_5=count_5+1
                                    #print(a1, a2, a3, a4, a5)
                                    latex_fn(a1, a2, a3, a4, a5)
                                    for b1, b2, b3, b4, b5, b6 in itertools.combinations((list_1), 6):
                                        if a5 ==b6 and a4 == b5 and a3==b4 and a2==b3 and a1 ==b2 :
                                            
                                            count_6=count_6+1
                                            #print(b1, b2, b3, b4, b5, b6)
                                            
                                            latex_fn(b1, b2, b3, b4, b5, b6)
                                            for c1, c2, c3, c4, c5, c6, c7 in itertools.combinations((list_1), 7):
                                                if c7 ==b6 and c6 == b5 and c5==b4 and c4==b3 and c3 ==b2 and c2==b1:
                                                    
                                                    count_7=count_7+1
                                                    #print(c1, c2, c3, c4, c5, c6, c7)
                                                    latex_fn(c1, c2, c3, c4, c5, c6, c7)
                                                    for d1, d2, d3, d4, d5, d6, d7, d8 in itertools.combinations((list_1), 8):
                                                        if c7 ==d8 and c6 == d7 and c5==d6 and c4==d5 and c3 ==d4 and c2==d3 and c1==d2:
                                                            
                                                            count_8=count_8+1
                                                            #print(d1, d2, d3, d4, d5, d6, d7, d8)
                                                            latex_fn(d1, d2, d3, d4, d5, d6, d7, d8)
                                                            for e1, e2, e3, e4, e5, e6, e7, e8, e9 in itertools.combinations((list_1), 9):
                                                                if e9 ==d8 and e8 == d7 and e7==d6 and e6==d5 and e5 ==d4 and e4==d3 and e3==d2 and e2==d1:
                                                                    
                                                                    count_9=count_9+1
                                                                    latex_fn(e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                                                    #print(e1, e2, e3, e4, e5, e6, e7, e8, e9)
                                                                    for f1, f2, f3, f4, f5, f6, f7, f8, f9, f10 in itertools.combinations((list_1), 10):
                                                                        if e9 ==f10 and e8 == f9 and e7==f8 and e6==f7 and \
                                                                           e5 ==f6 and e4==f5 and e3==f4 and e2==f3 and e1==f2:
                                                                            
                                                                            count_10=count_10+1
                                                                            latex_fn(f1, f2, f3, f4, f5, f6, f7, f8, f9, f1)
                                                                            #print(f1, f2, f3, f4, f5, f6, f7, f8, f9, f10)
                                                                            for g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11 in itertools.combinations((list_1), 11):
                                                                                if g11 ==f10 and g10 == f9 and g9==f8 and g8==f7 and \
                                                                                   g7 ==f6 and g6==f5 and g5==f4 and g4==f3 and g3==f2 and g2==f1:
                                                                                    
                                                                                    count_11=count_11+1
                                                                                    latex_fn(g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11)
                                                                                    #print(g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11)
                                                                                    for h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12 in itertools.combinations((list_1), 12):
                                                                                        if g11 ==h12 and g10 == h11 and g9==h10 and g8==h9 and \
                                                                                           g7 ==h8 and g6==h7 and g5==h6 and g4==h5 and g3==h4 and \
                                                                                           g2==h3 and g1==h2:
                                                                                            
                                                                                            count_12=count_12+1
                                                                                            latex_fn(h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12)
                                                                                            #print(h1, h2, h3, h4, h5, h6, h7, h8, h9, h10, h11, h12)
                                                                                            for i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13 in itertools.combinations((list_1), 13):
                                                                                                if i13 ==h12 and i12 == h11 and i11==h10 and i10==h9 and \
                                                                                                   i9 ==h8 and i8==h7 and i7==h6 and i6==h5 and i5==h4 and \
                                                                                                   i4==h3 and i3==h2 and i2==h1:
                                                                                                    
                                                                                                    count_13=count_13+1
                                                                                                    latex_fn(i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13)
                                                                                                    #print(i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13)
                                                                                                    
                                                                                                    for j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14 in itertools.combinations((list_1), 14):
                                                                                                        if i13 ==j14 and i12 == j13 and i11==j12 and i10==j11 and \
                                                                                                           i9 ==j10 and i8==j9 and i7==j8 and i6==j7 and i5==j6 and \
                                                                                                           i4==j5 and i3==j4 and i2==j3 and i1==j2:
                                                                                                            
                                                                                                            count_14=count_14+1
                                                                                                            latex_fn(j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14)
                                                                                                            #print(j1, j2, j3, j4, j5, j6, j7, j8, j9, j10, j11, j12, j13, j14)
                                                                                                            for k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14, k15 in itertools.combinations((list_1), 15):
                                                                                                                if k15 ==j14 and k14 == j13 and k13==j12 and k12==j11 and \
                                                                                                                   k11 ==j10 and k10==j9 and k9==j8 and k8==j7 and k7==j6 and \
                                                                                                                   k6==j5 and k5==j4 and k4==j3 and k3==j2 and k2==j1:
                                                                                                                    
                                                                                                                    count_15=count_15+1
                                                                                                                    latex_fn(k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14, k15)
                                                                                                                    #print(k1, k2, k3, k4, k5, k6, k7, k8, k9, k10, k11, k12, k13, k14, k15)
    
                    

print(count_2)
print(count_3)
print(count)
print(count_4)
print(count_5)
print(count_6)
print(count_7)
print(count_8)
print(count_9)
print(count_10)
print(count_11)
print(count_12)
print(count_13)
print(count_14)
print(count_15)
print("---------")
print(count+count_2+count_3+count_4+count_5+count_6+count_7+count_8+count_9+count_10+\
      count_11+count_12+count_13+count_14+count_15)

end_now = datetime.now()
print("END:", end_now)