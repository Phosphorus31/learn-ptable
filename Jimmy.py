import random
import numpy as np 
import time 
import sys

import csv

#define functions
row1 = [1,2]
row2 = np.arange(8) + 3
row3 = np.arange(8) + 11
row4 = [19,20]

with open('Elements.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    symbz = []
    names = []
    for row in readCSV:
        symbz.append(row[1])
        names.append(row[2])

exp = ['\u00b9','\u00b2','\u00b3','\u2074','\u2075','\u2076',]

def welcome():
    print ('Welcome to the periodic table learning tool!')
    time.sleep (1)
    print ('You will learn about the electron configuration!')
    time.sleep (1)
    
def ecf(s1,s2,p2,s3,p3,s4):
    if s2 == -1:
        print ('1s',exp[1])
    elif p2 == -1:
        print ('1s',exp[1],'2s',exp[num-3])
    elif s3 == -1:
        print ('1s',exp[1],'2s',exp[1],'2p',exp[num-5])
    elif p3 == -1:
        print ('1s',exp[1],'2s',exp[1],'2p',exp[5],'3s',exp[num-11])
    elif s4 == -1:
        print ('1s',exp[1],'2s',exp[1],'2p',exp[5],'3sj',exp[1],'3p',exp[num-13])
    else:
        print ('1s',exp[1],'2s',exp[1],'2p',exp[5],'3s',exp[1],'3p',exp[5],'4s',exp[num-19])
        
def outmost(number):
    print (elem, 'has',number,'electrons in its outmost',shell,'orbital.')
    time.sleep (1)
    
def inner():
    if shell == '2s':
        innershell = '1s'
    elif shell == '2p':
        innershell = '1s and 2s'
    elif shell == '3s':
        innershell = '1s, 2s and 2p'
    elif shell == '3p':
        innershell = '1s, 2s, 2p, and 3s'
    else:
        innershell = '1s, 2s, 2p, 3s, and 3p'
    print ('It also has the full',innershell,'orbitals.')
    time.sleep (1)
    
def AR (area):
    print (elem,'falls into the',area,'area.')
    time.sleep (1)
    
def config():
    time.sleep (1)
    print ('The electron configuration of',elem,'is:')
    time.sleep (1)
    
    
#Interactive system 
def ask():
    choose = input('Now type in the chemical symbol of the element you would like to explore.  ')
   
    #Database
    global elem
    global num

    if (choose in symbz):
        num = symbz.index(choose)
        elem = names[num]
        
    global shell
    if num <= 2:
        shell = '1s'
    elif num <= 4:
        shell = '2s'
    elif num <= 10:
        shell = '2p'
    elif num <= 12:
        shell = '3s'
    elif num <= 18:
        shell = '3p'
    else:
        shell = '4s'
    
    #General response
    print ('You have chosen the element:', elem)
    time.sleep (1.5)
    print ('The outmost orbital is decided by which area the element falls on the periodic table.')
    time.sleep (1.5)
    AR(shell)
    
    #Specific response
    if num == 1:
        print ('Because hydrogen only has one electron orbitting around the nucleus, it has a half-empty 1s orbital.')
        config()
        print(shell,exp[0])
    elif num == 2:
        print ('Helium has two electrons, exactly filling the 1s orbital. So, it is a happy noble gas!')
        config ()
        print(shell,exp[1])
    elif num == 3 or num == 4:
        outmost(num-2)
        inner()
        config()
        ecf(2,99,-1,-1,-1,-1)
    elif num <= 10:
        outmost(num-4)
        inner()
        config()
        ecf(2,2,num-4,-1,-1,-1)
    elif num == 11 or num == 12:
        outmost(num-10)
        inner()
        config()
        ecf(2,2,6,99,-1,-1)
    elif num <= 18:
        outmost(num-12)
        inner()
        config()
        ecf(2,2,6,2,99,-1)
    else:
        outmost (num-18)
        inner()
        config()
        ecf(2,2,6,2,6,99)
    
        
# operation area
def run():
    welcome()
    ask()

        
        
#Here we go!   
        
run()
