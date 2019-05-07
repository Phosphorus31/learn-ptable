import time
import csv
import random

shell_e = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
e_orbitals = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f', '6d', '7p']
exp = ['\u2070', '\u00b9','\u00b2','\u00b3','\u2074','\u2075','\u2076','\u2077','\u2078','\u2079','\u00b9\u2070','\u00b9\u00b9','\u00b9\u00b2','\u00b9\u00b3','\u00b9\u2074']
let = ['A', 'B', 'C', 'D', 'a', 'b', 'c', 'd']

with open('Elements.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    numbers = []
    symbols = []
    names = []
    o_shells = []
    for row in readCSV:
        numbers.append(row[0])
        symbols.append(row[1])
        names.append(row[2])
        o_shells.append(row[3])

def highest_energy_orbital(correct):
    print('What is the highest energy orbital that neutral ' + str(names[correct]).lower() + ' contains?')
    choices = []
    choices.append(e_orbitals.index(o_shells[correct]))
    while (len(choices) < 4):
        x = random.randint(0, 18)
        if (not(x in choices)):
            choices.append(x)
    choices.sort()
    for i in range(4):
        print(let[i] + '. ' + e_orbitals[choices[i]])
    ans = False
    while (not ans):
        choice = input('Answer: ')
        if (choice in let):
            if (choices[let.index(choice) % 4] == e_orbitals.index(o_shells[correct])):
                ans = True
                print('Correct! The highest energy orbital that neutral ' + str(names[correct]).lower() + ' contains is ' + o_shells[correct]  + '!')
            else:
                print('I\'m sorry, that was incorrect. Please try again.')
        else:
            print('I\'m sorry, I don\'t understand what you mean, please try again.')

def configuration(a_num):
    electron_num = int(a_num)
    config = ''
    for i in range(19):
        if ( electron_num > shell_e[i]):
            config = config + e_orbitals[i] + exp[shell_e[i]]
            electron_num = electron_num - shell_e[i]
        else:
            config = config + e_orbitals[i] + exp[electron_num]
            return config

def from_config(correct):
    print('Which of the following is the element whose ground state electron configuration is ' + configuration(correct) + '?')
    choices = []
    choices.append(correct)
    while (len(choices) < 4):
        x = random.randint(0, 117)
        if (not(x in choices)):
            choices.append(x)
    choices.sort()
    for i in range(4):
        print(let[i] + '. ' + names[choices[i]])
    ans = False
    while (not ans):
        choice = input('Answer: ')
        if (choice in let):
            if (choices[let.index(choice) % 4] == correct):
                ans = True
                print('Correct! ' + str(names[correct]) + '\'s ground state electron configuration is ' + configuration(correct)  + '!')
            else:
                print('I\'m sorry, that was incorrect. Please try again.')
        else:
            print('I\'m sorry, I don\'t understand what you mean, please try again.')