from datetime import datetime
import csv
import ast

global formula_between_global_variable
formula_between_global_variable = 0

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
                return i
            #"$C$\textbullet$D$\textbullet$E$"
    elif index_premis_circumstance == 1:
        new_formula_B = formula.replace("E", "D")
        for i, formulas_names in enumerate(list_formulas_names):
            if formulas_names[1][0] == new_formula_B:
                return i
    #"$B$\textbullet$C$\textbullet$E$"
    elif index_premis_circumstance == 3:
        new_formula_C = formula.replace("D", "C")
        new_formula_2 = new_formula_C.replace("E", "D")
        for i, formulas_names in enumerate(list_formulas_names):
            if formulas_names[1][0] == new_formula_2:
                return i
    #"$B$\textbullet$D$\textbullet$E$"
    elif index_premis_circumstance == 4:
        for i, formulas_names in enumerate(list_formulas_names):
            if formulas_names[1][0] == formula:
                return i
    #"$B$\textbullet$C$\textbullet$D$"

def triadic_name_fn_between( formula, index_premis_circumstance):
    
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
                return i
            #"$C$\textbullet$D$\textbullet$E$"
    elif index_premis_circumstance == 1:
        new_formula_B = formula.replace("E", "D")
        for i, formulas_names in enumerate(list_formulas_names):
            if formulas_names[1][0] == new_formula_B:
                return i
    #"$B$\textbullet$C$\textbullet$E$"
    elif index_premis_circumstance == 3:
        new_formula_C = formula.replace("D", "C")
        new_formula_2 = new_formula_C.replace("E", "D")
        for i, formulas_names in enumerate(list_formulas_names):
            if formulas_names[1][0] == new_formula_2:
                return i
    #"$B$\textbullet$D$\textbullet$E$"
    elif index_premis_circumstance == 4:
        for i, formulas_names in enumerate(list_formulas_names):
            if formulas_names[1][0] == formula:
                return i
    #"$B$\textbullet$C$\textbullet$D$"

def function_number_to_name_between(name, number):
    i = triadic_name_fn_between(name, number)

    return i

def function_number_to_name(name, number):
    i = triadic_name_fn(name, number)

    return i

begin_now = datetime.now()
print("BEGIN:", begin_now)


csv.register_dialect('myDialect', delimiter=' ', doublequote=True,
                         quoting=csv.QUOTE_NONE, skipinitialspace=True)

with open('main_output (10. Schritt) _ alle us und 8u.csv') as orders_file:
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

with open('main_innerhalb_der_Stufe output.csv') as orders_file_between:
    reader_between = csv.reader(orders_file_between, delimiter=',')
    


    deducable_tetradic_formula_list_between = list(reader_between)


    deducable_tetradic_formula_copy_between = deducable_tetradic_formula_list_between[:]
        
    for k in range(len(deducable_tetradic_formula_copy_between)):
        if deducable_tetradic_formula_copy_between[k] == []:
            deducable_tetradic_formula_list_between.remove(deducable_tetradic_formula_copy_between[k])


    for formula in deducable_tetradic_formula_list_between:
        formula[0] = eval(formula[0])
        formula[1] = eval(formula[1])

orders_file_between.close()

############## Useful, if you interrupted
"""with open('new_attempt_old (input).csv') as file_new_attempt_old:
    reader_numbers_to_delete = csv.reader(file_new_attempt_old, delimiter=',')
    


    list_numbers_to_delete = list(reader_numbers_to_delete)


    list_numbers_to_delete_copy = list_numbers_to_delete[:]
        
    for k in range(len(list_numbers_to_delete_copy)):
        if list_numbers_to_delete_copy[k] == []:
            list_numbers_to_delete.remove(list_numbers_to_delete_copy[k])


    for formula in list_numbers_to_delete:
        formula[0] = eval(formula[0])
        formula[1] = eval(formula[1])

orders_file_between.close()

list_numbers_to_delete_copy = list_numbers_to_delete[:]


remove_deducable_tetradic_formula_list = deducable_tetradic_formula_list[:]


for index, number in enumerate(list_numbers_to_delete):
    for index_2, formula in enumerate(remove_deducable_tetradic_formula_list):
        if number[1]-1 == index_2:
            remove_deducable_tetradic_formula_list.remove(remove_deducable_tetradic_formula_list[number[1]-1])

mid_now = datetime.now()
print("MID:", mid_now)
"""

dictionaries = {}
for d in range(len(deducable_tetradic_formula_list)):
    dictionaries['X'+str(d)] = {"formula": " ", "count" : 0}


remove_deducable_tetradic_formula_list = deducable_tetradic_formula_list[:]

### IF YOU INTERRUPTED BEGIN WITH: for d, formula in enumerate(deducable_tetradic_formula_list[NUMBERINTERRUPTED:], NUMBERINTERRUPTED):

for d, formula in enumerate(deducable_tetradic_formula_list):
    for e, formula_2 in enumerate(remove_deducable_tetradic_formula_list):

        if (formula[1][0][0] == formula_2[1][0][0] and \
           formula[1][1][0] == formula_2[1][1][0] and \
           formula[1][2][0] == formula_2[1][2][0]):
            
            dictionaries['X'+str(d)]["count"] = dictionaries['X'+str(d)]["count"] + 1
            
            count_dummy_for_loop = dictionaries['X'+str(d)]["count"]
            
            if count_dummy_for_loop == 1:
            
                for f, formula_between in enumerate(deducable_tetradic_formula_list_between):
                
                    prem_2 = function_number_to_name(formula_2[1][1][0], 2)
                    prem_2_between = function_number_to_name_between(formula_between[1][0][1][0], 2)
                    prem_1 = function_number_to_name(formula_2[1][0][0], 4)
                    prem_1_between = function_number_to_name_between(formula_between[1][0][0][0], 1)
                    prem_3 = function_number_to_name(formula_2[1][2][0], 1)
                    prem_3_between = function_number_to_name_between(formula_between[1][0][2][0], 3)
                    
                    if prem_2_between == prem_2 and prem_1_between == prem_1 and prem_3_between == prem_3:
                
                        dictionaries['X'+str(d)]["formula"] = formula_between[0]
                        formula_between_global_variable = formula_between[0]

                        with open('new_attempt.csv', 'a') as file:
                            writer = csv.writer(file)
                        
                            writer.writerow([d+1, e+1, dictionaries['X'+str(d)]])
                        
                        file.close()
                        
                        remove_deducable_tetradic_formula_list.remove(formula_2)
            else:
                dictionaries['X'+str(d)]["formula"] = formula_between_global_variable

                with open('new_attempt.csv', 'a') as file:
                    writer = csv.writer(file)
                
                    writer.writerow([d+1, e+1, dictionaries['X'+str(d)]])
                
                file.close()
                
                remove_deducable_tetradic_formula_list.remove(formula_2)
        
                    #print(dictionaries['X'+str(d)])
        #name_function_prem_2 = function_number_to_name(formula_between[1][1][0], 2)

        #name_function_prem_3 = function_number_to_name(formula_between[1][2][0], 1)


            #name_function_prem_4 = function_number_to_name(formula[1][1][0][0], 4)

            #name_function_prem_1 = function_number_to_name(formula[1][0][0][0], 1)
            #name_function_prem_2 = function_number_to_name(formula[1][0][1][0], 2)
            #)

#IF YOU INTERRUPTNEXT CODE MEANINGLESS
with open('new_attempt_finished.csv', 'w') as file:
    writer = csv.writer(file)
    for d, (key, value) in enumerate(dictionaries.items()):
        writer.writerow([d+1, [key, value]])

file.close()


##################################################




end_now = datetime.now()
print("END:", end_now)

