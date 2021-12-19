import sys
import pandas as pd
import csv

file =open('predictions_INB_LR.csv')
csvreader = list(csv.reader(file))

# val3 = csvreader[-2][-1]
# print(val3)



def helloworld(out):
    val1 = csvreader[2][-1]
    
    
    
    
    out.write(val1)
    
def val_2(out):
    val2 = csvreader[100][-1]
    out.write(val2)
    
def val_3(out):
    val3 = csvreader[-2][-1]
    out.write(val3)

def val_4(out):
    val4 = csvreader[1500][-1]
    out.write(val4)
    
