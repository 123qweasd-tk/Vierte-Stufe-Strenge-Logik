from datetime import datetime
import csv
import ast


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

    for e, count_complete_conclusions_and_elementary_particle_premisis in enumerate(all_set):
        count_e.append([count_complete_conclusions_and_elementary_particle_premisis, 0, e])
        
    for formula in deducable_tetradic_formula_list:
        count_overall = 0

        count_1 = 0
        count_2 = 0
        count_3 = 0
        count_4 = 0
        count_1qu = 0
        count_2qu = 0
        count_3qu = 0
        count_4qu = 0
        count_x = 0
        count_y = 0
        count_z = 0
        count_z2 = 0
        
        

        if len(formula) >= 3:
            name_function_prem_4 = function_number_to_name(formula[1][3][0], 3)


            name_function_prem_1 = function_number_to_name(formula[1][0][0], 4)

            name_function_prem_2 = function_number_to_name(formula[1][1][0], 2)

            name_function_prem_3 = function_number_to_name(formula[1][2][0], 1)


            number_premisis_list = [name_function_prem_1, name_function_prem_2, name_function_prem_3, name_function_prem_4]
            
            for o in gluons_and_quarks:
                
                
                if (name_function_prem_1+1) == o:
                    count_1 = count_1 + 1
                if (name_function_prem_2+1) == o:
                    count_2 = count_2 + 1
                if (name_function_prem_3+1) == o:
                    count_3 = count_3 + 1
                if (name_function_prem_4+1) == o:
                    count_4 = count_4 + 1
                    
            
            
            if (count_1 + count_2 + count_3 + count_4) >= 1:
                count_overall = count_overall + 1


            for o in rest:
                
                if (name_function_prem_1+1) == o:
                    count_1qu = count_1qu + 1
                if (name_function_prem_2+1) == o:
                    count_2qu = count_2qu + 1
                if (name_function_prem_3+1) == o:
                    count_3qu = count_3qu + 1
                if (name_function_prem_4+1) == o:
                    count_4qu = count_4qu + 1
                    
            for s in all_set:
                
                if (name_function_prem_1+1) == s:
                    count_x = count_x + 1
                if (name_function_prem_2+1) == s:
                    count_y = count_y + 1
                if (name_function_prem_3+1) == s:
                    count_z = count_z + 1
                if (name_function_prem_3+1) == s:
                    count_z2 = count_z2 + 1

#count_overall == 1 and
# and (count_1qu + count_2qu + count_3qu + count_4qu) == 0
                    
            if   (count_x + count_y + count_z + count_z2) == 4:
                
                #print('Ein Gl und zwei Qu:')
                #print(formula[0])
                #print(formula[1])
                #print(name_function_prem_1)
                #print(name_function_prem_2)
                #print(name_function_prem_3)
                
                count_formulas = count_formulas + 1

                if len(formula) == 3:
                    count_partition = count_partition + 1/12480
                elif len(formula) == 4:
                    count_partition = count_partition + 1/8288
                elif len(formula) == 5:
                    count_partition = count_partition + 1/3552
                elif len(formula) == 6:
                    count_partition = count_partition + 1/2136
                elif len(formula) == 7:
                    count_partition = count_partition + 1/1360
                elif len(formula) == 8:
                    count_partition = count_partition + 1/2112
                elif len(formula) == 10:
                    count_partition = count_partition + 1/32

                for count_complete_conclusion_elementary_partical in count_e:
                    if (name_function_prem_4+1) == count_complete_conclusion_elementary_partical[0]:
                        count_complete_conclusion_elementary_partical[1] = count_complete_conclusion_elementary_partical[1] + 1
                
        
    all_conclusions = 0
    
    counting_list = []


    for p, counting in enumerate(count_e):
        for o in gluons:
            if counting[0] == o:
                counting.append(['gluon'])
        for i in quarks:
            if counting[0] == i:
                counting.append(['quark'])
        for r in rest:
            if counting[0] == r:
                counting.append(['rest'])
        #print(counting)
        counting_list.append(0)
        all_conclusions = all_conclusions + counting[1]
        
    for p, counting in enumerate(count_e):
        for counting_2 in count_e:
            if counting[1] == counting_2[1] and counting[3] == counting_2[3]:
                counting_list[p] = counting_list[p] + 1
                
    for u, counting in enumerate(count_e):
        counting.append(counting_list[u])
    
    print('----------')
    
    for i, row in enumerate(count_e):
        print(' '+str(row[1])+' & ('+str(row[4])+') \\\ \hline')
        
    print('----------')
    
    final_count_rest = 0
    final_count_quark = 0
    final_count_gluon = 0
    
    for z, counting in enumerate(count_e):
        if counting[3][0] == 'rest':
            final_count_rest = final_count_rest + counting[1]
        if counting[3][0] == 'quark':
            final_count_quark = final_count_quark + counting[1]
        if counting[3][0] == 'gluon':
            final_count_gluon = final_count_gluon + counting[1]
    
    print(final_count_rest)
    print(final_count_quark)
    print(final_count_gluon)
    
    count_one = 0
    count_two = 0
    count_three = 0
    count_five = 0
    count_fiftheen = 0
    count_sixtheen = 0

    count_four = 0
    count_six = 0
    count_seven = 0
    count_eight = 0
    count_nine = 0
    count_ten = 0
    count_eleven = 0
    count_twelve = 0
    count_thirdteen = 0
    
    for counting in counting_list:
        if counting == 1:
            count_one = count_one + 1
        elif counting == 2:
            count_two = count_two + 1
        elif counting == 3:
            count_three = count_three + 1
        elif counting == 4:
            count_four = count_four + 1
        elif counting == 5:
            count_five = count_five + 1
        elif counting == 6:
            count_six = count_six + 1
        elif counting == 7:
            count_seven = count_seven + 1
        elif counting == 8:
            count_eight = count_eight + 1
        elif counting == 9:
            count_nine = count_nine + 1
        elif counting == 10:
            count_ten = count_ten + 1
        elif counting == 11:
            count_eleven = count_eleven + 1
        elif counting == 12:
            count_twelve = count_twelve + 1
        elif counting == 13:
            count_thirdteen = count_thirdteen + 1
        elif counting == 15:
            count_fiftheen = count_fiftheen + 1
        elif counting == 16:
            count_sixtheen = count_sixtheen + 1
        else:
            print('missing', counting)
        #print(counting)
    
    
    count_whole_shit = count_one + count_two/2 + count_three/3 + count_four/4 + count_five/5 + \
                       count_six/6 + count_seven/7 + count_eight/8 + count_nine/9 + count_ten/10 +\
                       count_eleven/11 + count_twelve/12 + count_thirdteen/13 + count_fiftheen/15 + count_sixtheen/16
    
    print(count_whole_shit)
    print(all_conclusions)
    
    print(count_partition)
    print(count_formulas)
    
orders_file.close()


end_now = datetime.now()
print("END:", end_now)

