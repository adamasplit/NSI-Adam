import sqlite3

base = sqlite3.connect('comptes_eleves_python_2017.db')

with base:
    c = base.cursor()
    c.execute("SELECT Nom,Prenom,classe FROM eleve ")
    rows = c.fetchall()
i = 0
for row in rows:
    print(row)
    i = i + 1
print("il y a % d élèves dans le lycée" % (i))