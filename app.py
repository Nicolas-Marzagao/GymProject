from os import system
import math

def weightCalc():
        while True:
                print('\nSelect the conversion:\n[ 1 ] - Lbs to Kgs\n[ 2 ] - Kgs to Lbs\n[ 3 ] - Back\n')

                sel = int(input('> '))

                if sel == 1:
                        print('Enter the Weight(lbs):')
                        w = float(input('> '))

                        rw = w / 2.205

                        print(f'{w} in kgs is {rw:.2f}')
                elif sel == 2:
                        print('Enter the Weight(kgs):')
                        w = float(input('> '))

                        rw = w * 2.205

                        print(f'{w} in lbs is {rw:.2f}')
                else: break


def rpmCalc():
        while True:
                print('Enter a weight you can lift for more then 6 reps in this exercise:')
                print('Note: it does work with lower rep ranges but a number higher then 6 is recomended.')
                w = float(input('> '))

                print('Enter the number of reps with that weight: ')
                r = int(input('> '))

                res = w * pow(r,0.10)

                print(f'Your 1 rep max in this exercise is: {res:.2f}')

                input('Press enter to return to the main menu')
                break


def rotineGen():
        while True:
                monday = [' '] * 5
                print('Enter the first exercise')
                f = open('exerc.txt', 'w')

                for i in range(5):
                        monday[i] = input('exercise: ')
                        f.write(monday[i] + '\n')
                        print(monday)
                input()
                break


while True:
        system('clear')
        print('''
***********************
**** Gym Rat Tools ****
***********************

[ 1 ] - Weight calculator, from lbs to kgs and back.
[ 2 ] - One Rep Max calculator.
[ 3 ] - Workout Rotine Generator.
[ 4 ] - Exit.''')

        op = int(input('\n> '))

        if op == 1:
                weightCalc()

        elif op == 2:
                rpmCalc()

        elif op == 3:
                rotineGen()

        elif op == 4:
                print('Exiting...')
                break
        else: break
