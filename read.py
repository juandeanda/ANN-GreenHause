import csv
import numpy as np
def readFile(name):
    dataset = []
    with open(name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
           aux = np.zeros(len(row))
           for i in range(0,len(row)):
               aux[i] = row[i]
           dataset.append(aux)
    return dataset

    

