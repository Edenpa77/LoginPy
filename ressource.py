import time
from tkinter import *



def calapp() :
    calap = Tk()

    framecalapp = Frame(calap, bg='#1468e8')

    n1 = Label(calap, text='+', font=('Courrier', 40), bg='#1468e8', fg='white')
    n2 = Label(calap, text='-', font=('Courrier', 40), bg='#1468e8', fg='white')
    n3 = Label(calap, text='*', font=('Courrier', 40), bg='#1468e8', fg='white')
    n4 = Label(calap, text='/', font=('Courrier', 40), bg='#1468e8', fg='white')

    while 1:
        reponse = input(">>> ")
        if reponse in ['1', '2', '3', '4']:
            break
        else:
            print("Incorrect choice")

    if reponse == "1":
        note1 = int(input('number 1 : '))
        note2 = int(input('number 2 : '))
        note3 = note1 + note2
        print(str('the result is : {}'.format(note3)))
        time.sleep(5)

    if reponse == "2":
        note1 = int(input('number 1 : '))
        note2 = int(input('number 2 : '))
        note3 = note1 - note2
        print(str('the result is : {}'.format(note3)))
        time.sleep(5)

    if reponse == "3":
        note1 = int(input('number 1 : '))
        note2 = int(input('number 2 : '))
        note3 = note1 * note2
        print(str('the result is : {}'.format(note3)))
        time.sleep(5)

    if reponse == '4':
        note1 = int(input('number 1 : '))
        note2 = int(input('number 2 : '))
        note3 = note1 / note2
        print(str('the result is : {}'.format(note3)))
        time.sleep(5)