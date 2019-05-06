import time
import csv

shell_e = [2, 2, 6, 2, 6, 2, 10, 6, 2, 10, 6, 2, 14, 10, 6, 2, 14, 10, 6]
e_orbitals = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f', '6d', '7p']
exp = ['\u2070', '\u00b9','\u00b2','\u00b3','\u2074','\u2075','\u2076','\u2077','\u2078','\u2079','\u00b9\u2070','\u00b9\u00b9','\u00b9\u00b2','\u00b9\u00b3','\u00b9\u2074']

def run():
    welcome()
    ask_cycle()
    ask_again()

def welcome():
    print('Welcome to the periodic table learning tool!')
    time.sleep(1)
    print('You can learn about the electron configurations of different neutral elements!')
    time.sleep(1)

with open('Elements.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter = ',')
    symbols = []
    names = []
    o_shells = []
    for row in readCSV:
        symbols.append(row[1])
        names.append(row[2])
        o_shells.append(row[3])

def ask():
    choose = input('Please enter the chemical symbol or the name of the element that you would like to explore: ')

    global num
    global elem
    global o_shell

    while (not(choose in symbols) and not(choose in names)):
        print('The name you entered does not exist in our database; please confirm your spelling and try again.')
        time.sleep(1)
        choose = input('In order for this database to work, please capitalize the first letter and leave the rest un-capitalized: ')

    if (choose in symbols):
        num = symbols.index(choose)
        elem = names[num]
        o_shell = o_shells[num]
    elif (choose in names):
        num = names.index(choose)
        elem = choose
        o_shell = o_shells[num]

    print('You have chosen element ' + str(num) + ': ' + elem)
    time.sleep(1)

def o_orbital(a_num, outmost_shell):
    print('The area on which the element falls on the periodic table is dictated by the highest-energy orbital of that element.')
    time.sleep(1)
    print(names[a_num] + ' falls in the ' + outmost_shell + ' area, meaning that the highest energy orbital it contains is ' + outmost_shell + '.')
    time.sleep(1)

def e_config(a_num):
    electron_num = int(a_num)
    global config
    global outer_e
    config = ''
    for i in range(19):
        if (electron_num > shell_e[i]):
            config = config + e_orbitals[i] + exp[shell_e[i]]
            electron_num = electron_num - shell_e[i]
        else:
            config = config + e_orbitals[i] + exp[electron_num]
            outer_e = electron_num
            break

def o_elec(a_num, outer_num, outmost_shell):
    if (outer_num == 1):
        print(names[a_num] + ' has 1 electron in its highest energy ' + outmost_shell + ' orbital.')
    else:
        print(names[a_num] + ' has ' + str(outer_num) + ' electrons in its highest energy ' + outmost_shell + ' orbital.')
    time.sleep(1)

def i_shells(a_num, outmost_shell):
    if (a_num > 2):
        innershells = ''
        for i in range(e_orbitals.index(o_shell)):
            if (i == 0):
                innershells = innershells + str(e_orbitals[i])
            elif (i == e_orbitals.index(o_shell) - 1):
                innershells = innershells + ', and ' + str(e_orbitals[i])
            else:
                innershells = innershells + ', ' + str(e_orbitals[i])
        print('It also has full ' + innershells + ' orbitals, filled with electrons.')
        time.sleep(1)

def print_config(a_num, elec_c):
    print('The electron configuration of neutral ' + str(names[a_num]).lower() + ' is:')
    time.sleep(1)
    print(elec_c)
    time.sleep(1)
    shorthand(a_num, elec_c)

def shorthand(atomic_number, electron_configuration):
    if (atomic_number <= 2):
        print('The electron configuration of ' + str(names[atomic_number]).lower() + ' has no shorthand notation.')
        time.sleep(1)
    else:
        print('The shorthand notation for ' + str(names[atomic_number]).lower() + '\'s electron configuration is:')
        time.sleep(1)
        if ('7s' in electron_configuration):
            print('[Rn]' + electron_configuration[49:])
        elif ('6s' in electron_configuration):
            print('[Xe]' + electron_configuration[35:])
        elif ('5s' in electron_configuration):
            print('[Kr]' + electron_configuration[25:])
        elif ('4s' in electron_configuration):
            print('[Ar]' + electron_configuration[15:])
        elif ('3s' in electron_configuration):
            print('[Ar]' + electron_configuration[9:])
        elif ('2s' in electron_configuration):
            print('[Ar]' + electron_configuration[6:])
        time.sleep(1)

def ask_cycle():
    ask()
    o_orbital(num, o_shell)
    e_config(num)
    o_elec(num, outer_e, o_shell)
    i_shells(num, o_shell)
    print_config(num, config)

def ask_again():
    state = input('Would you like to learn about another type of element? (Yes/No) ')
    if ((state == 'Yes') or (state == 'yes')):
        ask_cycle()
    elif ((state == 'No') or (state == 'no')):
        print('Thank you for using the periodic table learning tool!')
        time.sleep(1)
        print('We hope to see you again soon :)')
    else:
        print('I\'m not sure I understand what you mean, please try again.')
        time.sleep(1)
<<<<<<< HEAD
        ask_again()
=======
        ask_again()
>>>>>>> dfaf92dbae856d51c6c3d8b7cb864ca7d66b3dc9
