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
    shellz = []
    oes = []
    for row in readCSV:
        symbz.append(row[1])
        names.append(row[2])
        shellz.append(row[3])
        oes.append(row[4])

exp = ['\u2070', '\u00b9','\u00b2','\u00b3','\u2074','\u2075','\u2076','\u2077','\u2078','\u2079','\u00b9\u2070','\u00b9\u00b9','\u00b9\u00b2','\u00b9\u00b3','\u00b9\u2074']

def welcome():
    print ('Welcome to the periodic table learning tool!')
    time.sleep (1)
    print ('You will learn about the electron configuration!')
    time.sleep (1)
    
def ecf():

    enum = int(num)
    configurat = ''
    for i in range(19):
        if (enum > maxe[i]):
            configurat = configurat + shells[i] + exp[maxe[i]]
            enum = enum - maxe[i]
        else:
            configurat = configurat + shells[i] + exp[enum]
            break
    print(configurat)


def outmost(number):
    print (elem, 'has',number,'electrons in its outmost',shell,'orbital.')
    time.sleep (1)
    
shells = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f', '6d', '7p']
maxe = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]

def inner():
    shellnum = shells.index(shell)
    innershell = ''
    for i in range(shellnum):
        if (i == 0):
            innershell = innershell + str(shells[i])
        elif (i == shellnum - 1):
            innershell = innershell + ', and ' + str(shells[i])
        else:
            innershell = innershell + ', ' + str(shells[i])
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
    choose = input('Now type in the chemical symbol of the element you would like to explore.')
   
    #Database
    global elem
    global num
    global shell

    if (choose in symbz):
        num = symbz.index(choose)
        elem = names[num]
        shell = shellz[num]
    
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
        ecf()
    elif num == 2:
        print ('Helium has two electrons, exactly filling the 1s orbital. So, it is a happy noble gas!')
        config ()
        ecf()
    else:
        outmost(oes[num])
        inner()
        config()
        ecf()
       
# operation area
def run():
    welcome()
    ask()

#Here we go!   
        
run()