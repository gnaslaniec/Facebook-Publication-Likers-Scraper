import csv
import os


def gravador_csv(col, arquivo):
    if not os.path.exists('Arquivos'):
        os.makedirs('Arquivos')

    with open(r'Arquivos/{}_Likers.csv'.format(arquivo),
              'a', encoding='utf8', newline='') as file:
        print('\nGravando!')
        gravador = csv.writer(file)
        gravador.writerow([col])
    file.close()
