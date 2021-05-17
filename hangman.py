from tkinter import *
import random
from tkinter import messagebox


lista_palavras = ['cat', 'whale', 'run', 'ocean', 'boat']
word = random.choice(lista_palavras)
word = word.upper()
tries = 6
word_completion = '_' * len(word)
guessed_letters = []
guessed = False


def play():
    global word_completion
    global word
    global tries
    global guessed_letters
    global guessed
    global rootlb

    rootlb.destroy()
    guess = input1.get().upper()
    input1.delete(0, END)
    while not guessed and tries > 0:
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                rootlb = Label(root, text=f'You already tried {guess}', font=('arial', 20, 'bold'), bg='white')
                rootlb.place(x=145, y=70)
                masterlb.set(rootlb)

            elif guess not in word:
                rootlb = Label(root, text=f'{guess} wrong', font=('arial', 20, 'bold'), bg='white')
                rootlb.place(x=200, y=70)
                masterlb.set(rootlb)
                tries -= 1
                guessed_letters.append(guess)

            else:
                rootlb = Label(root, text=f'{guess}, it is in the word', font=('arial', 20, 'bold'), bg='white')
                rootlb.place(x=145, y=70)
                masterlb.set(rootlb)
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)


        else:
            messagebox.showinfo('Error', 'Incorrect value!')
        showimage(gmlb1, tries)
        try_lab = Label(root, text=f'Tries: {display_hangman(tries)}', font=('arial', 15, 'bold'), bg='white')
        try_lab.place(x=15, y=20)
        masterlb.set(try_lab)
        wc_lab = Label(root, text=f'{word_completion}', font=('arial', 30, 'bold'), bg='white')
        wc_lab.place(x=200, y=330)
        masterlb.set(wc_lab)
        break
    if '_' not in word_completion:
        win(root, word)
    if int(display_hangman(tries)) > 6:
        lose(root, word)


def display_hangman(tries):
    stages = [7, 6, 5, 4, 3, 2, 1]
    return f'{stages[-tries]}'


def showimage(gmlb1, tries):
    if tries == 6:
        img = PhotoImage(file='p2.gif')
        gmlb1.configure(image=img)
        gmlb1.image = img
    if tries == 5:
        img = PhotoImage(file='p3.gif')
        gmlb1.configure(image=img)
        gmlb1.image = img
    if tries == 4:
        img = PhotoImage(file='p4.gif')
        gmlb1.configure(image=img)
        gmlb1.image = img
    if tries == 3:
        img = PhotoImage(file='p5.gif')
        gmlb1.configure(image=img)
        gmlb1.image = img
    if tries == 2:
        img = PhotoImage(file='p6.gif')
        gmlb1.configure(image=img)
        gmlb1.image = img
    if tries == 1:
        img = PhotoImage(file='p7.gif')
        gmlb1.configure(image=img)
        gmlb1.image = img
    if tries == 0:
        img = PhotoImage(file='p8.gif')
        gmlb1.configure(image=img)
        gmlb1.image = img


def win(root, word):
    messagebox.showinfo('Winner', 'You WON! The word was' + word + '!')
    root.withdraw()


def lose(root, word):
    messagebox.showinfo('Loser', 'You LOST! The word was ' + word + '!')
    root.withdraw()


root = Tk()
root.geometry('550x600')
root.configure(bg='white')
root.title('Hang man game')
# ------------------------------------------------ Labels

intlabel = Label(root, text='Hangman Game', font=('Times', 35, 'bold'), bg='white')
intlabel.place(x=100, y=0)
first_n = Label(root, text='Guess the word: ', font=('arial', 18, 'bold'), bg='white')
first_n.place(x=80, y=444)

masterlb = StringVar()
rootlb = Label(root, textvariable=masterlb)

gallow = PhotoImage(file='p2.gif')
gmlb1 = Label(root, image=gallow)
gmlb1.image = gallow
gmlb1.place(x=90, y=120)

g_lab = Label(root, text=f'Guess: {len(word)} letters!', font=('arial', 18, 'bold'), bg='white')
g_lab.place(x=160, y=400)
masterlb.set(g_lab)
try_lab = Label(root, text=f'Tries: {display_hangman(tries)}', font=('arial', 15, 'bold'), bg='white')
try_lab.place(x=15, y=20)
masterlb.set(try_lab)
wc_lab = Label(root, text=f'{word_completion}', font=('arial', 30, 'bold'), bg='white')
wc_lab.place(x=200, y=330)
masterlb.set(wc_lab)

# ------------------------------------------------- Entry box

input1 = Entry(root, font=('arial', 12, 'bold'), relief=SUNKEN, bd=2, bg='grey', width=13, justify='center')
input1.pack()
input1.place(x=290, y=450)
input1.focus_set()

# ------------------------------------------------- Button

b2 = Button(root, text='Play', font=('arial', 14, 'bold'), width=8, bd=5, bg='white', activebackground='grey',
            activeforeground='white', command=play)
b2.place(x=205, y=500)


root.mainloop()
