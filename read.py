import csv
import numpy as np
def readFile(name):
    dataset = []
    with open(name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
           aux2 = []
           for i in range(0,len(row)):
               aux2.append(float(row[i]))
               if(i == len(row)-1):
                 aux2.append(int(row[i]))
           dataset.append(aux2)
    return dataset

    

