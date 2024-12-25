# Vierte-Stufe-Strenge-Logik
Vierte Stufe - Strenge Logik

Dies ist ein Projekt zur Bestimmung von Elementar-elementar-Entitäten mithilfe der vierten Stufe, wie sie Walther Brüning in seinem 1996 erschienen Buch "Grundlagen der Strengen Logik" begründet.

"main.py" - beinhaltet einen Programmiercode, der die beiden Ableitungsregeln von der verlängerten triadischen Stufe zur tetradischen Stufe festlegt und alle Kombinationen (2**32 = 4 294 967 296) durch-iteriert und in eine neu erstellte .csv-Datei ausgibt.

"Vierte_Stufe_20.536 Formeln_noch_mit_unbestimmten_Stellen.csv" - beinhaltet eine Liste mit einem ersten Element, der die resultierende Geltungswertformel (der vierten Stufe) angibt und einem zweiten Element der Liste die vier Prämissen (der dritten verlängerten Stufe) dazu angibt.

Ziel des Projekts ist es, analog zu:
https://github.com/123qweasd-tk/Syllogistik-App/blob/main/Logische_Grundlagen_der_Quantenphysik_Thomas_K%C3%A4fer.pdf
die unbestimmten Parameter der vierten Stufe, die nicht aus der dritten verlängerten Stufe gewonnen werden können, als eine Zahl darstellen zu können in Bezug auf die 65 536 möglichen Formeln der vierten Stufe.

Ad "Vierte_Stufe_20.536 Formeln_noch_mit_unbestimmten_Stellen.csv":
Die Prämissen sind in Latex-Code geschrieben. (\usepackage{latexsym} - nicht vergessen)
Warnung: Die Namen der Prämissen sind handgeschrieben und können fehlerhaft sein.

Ad "main.py":
Dieses Programm braucht für einen Durchlauf ca. 6,8 Stunden.

Anmerkung:
Es fehlt noch die Festsetzung der unbestimmten Geltungswertstellen in potentielle Ganzformeln, die Liste der möglichen Formeln auf tetradischer Stufe und eine Zuordnung ersteres zu letzterem, mit vorheriger Streichung von Formeln, die weniger Informationen (mehr unbestimmte Stellen) enthalten und sonst doppelt oder öfter erscheinen und gezählt würden.
Zweitens fehlt eine Analyse der triadischen Stufe innerhalb. Es wird sich eine Anzahl ergeben, die nur vollständige (ohne unbestimmte Stellen) Konklusionen ergeben.
