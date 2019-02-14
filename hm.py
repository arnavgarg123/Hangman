from tkinter import *
import random
from PIL import Image, ImageTk


class hangman:
    def maingui(self):
        self.top = Tk()  # creating main window
        self.top.geometry("865x630")  # set dimensions for main window
        self.top.title("Hangman")  # title for the main window
        self.frame = Frame(self.top)  # Main Frame which encloses all other frames and widgets
        self.frame1 = Frame(self.frame)  # frame for welcome
        wc = Label(self.frame1, text="WELCOME TO HANGMAN GAME",
                   relief="raised", height="4", width="68", font=("Helvetica", 16))  # Welcome message

        button = Button(self.frame1, text="EXIT", relief="sunken", height="6",
                        width="9", bg="#FF0000", command="exit")  # Exit button

        button1 = Button(self.frame1, text="RETRY", relief="sunken", height="6",
                         width="9", bg="#3f0", command=lambda: self.st())  # retry button

        self.frame2 = Frame(self.frame)  # Frame containing description of the game
        info = Text(self.frame2, height=30, width=72)  # Text widget to display description
        img = Text(self.frame2, height=30, width=50)  # Text field to enclose image of hangman logo
        # Font for the heading of description
        info.tag_configure('big', font=('Verdana', 20, 'bold'))
        info.tag_configure('small', font=('Tempus Sans ITC', 12, 'bold')
                           )  # Font for the body of description
        abouth = "ABOUT HANGMAN GAMES"  # Heaiding
        aboutb = "\n\n\nHangman is used often by teachers to practice spelling, vocabulary and just for fun. The most popular way to play hangman games offline is to draw blank letters for the chosen word on a paper or on the blackboard and let the players guess the letters. For each incorrect guess, another part of the man is drawn. If the picture is complete before the word is revealed the hangman game is lost and the character is hanged, if the word is revealed before the execution the game is won."  # description
        diag = PhotoImage(file='proj/hangman5.png')  # Linking the photo of hangman
        diag = diag.subsample(2, 2)  # Setting size of the photo
        img.image_create(END, image=diag)  # Inserting image to text widget
        info.insert(END, abouth, 'big')  # Inserting and configuring the heading of description
        info.insert(END, aboutb, 'small')  # Inserting and configuring the body of description
        start = Button(self.frame2, text="START", relief="sunken", height="6",
                       width="9", bg="#008000", command=lambda: self.st())  # Start button

        start.grid(row=1, column=0, columnspan=2)
        wc.grid(row=0, column=1, sticky=W)
        button1.grid(row=0, column=0)
        info.grid(row=0, column=1)
        img.grid(row=0, column=0)
        self.frame2.grid(row=1, column=0, columnspan=3)
        self.frame1.grid(row=0, column=0, sticky=W)
        self.frame.grid(row=0, column=0)
        button.grid(row=0, column=2, sticky=W)
        self.top.mainloop()  # mainloop

    def st(self):  # functionality of start button
        self.frame2.destroy()  # Clearing frame2
        self.hangmang()  # calling game start function

    def inpi(self):  # function to read input
        self.inpu = self.inp.get()  # Taking input in entry field
        match = 0
        for j in range(self.l):
            if self.let[j] == self.inpu:  # comparing input with actual letters of the word
                self.count = self.count+1  # counting the number of letters found
                # displaying correct letters in the text field
                self.letter[j].insert(END, self.let[j])
                match = 1  # showing entry letter matches atleast one of the letters in word
            if self.count == self.l:  # checking ending condition where all letters have been found
                self.great()  # calling function on success
                break
        if match == 0:
            self.err = self.err+1  # increacing the number of errors when wrong letter is entered
            # image to be displayed corresponding to the lifeline
            img = PhotoImage(file="proj/hangman%d.png" % self.err)
            img = img.zoom(15)  # resizing the image
            img = img.subsample(32)  # original relative size of image
            panel = Label(self.frame2, image=img)  # label to display the image
            panel.image = img  # local reference to the image
            panel.grid(row=5, columnspan=self.l)

        if self.err == 5:  # checking failing condition
            self.fail()  # calling function on failure

    def fail(self):  # failure function
        self.frame2.destroy()  # destroying frame
        self.frame2 = Frame(self.frame)  # creating frame
        img = PhotoImage(file="proj/hangman5.png")  # linking photo
        img = img.zoom(25)  # resizing image
        img = img.subsample(32)  # original relative size of image
        panel = Label(self.frame2, image=img)  # label to display the image
        panel.image = img  # local reference to image
        panel.grid(row=0)

        pane = Label(self.frame2, text="You have Failed", font=(
            'Verdana', 20, 'bold'))  # label to show fail message
        self.frame2.grid(row=1, column=0)
        pane.grid(row=1)

    def great(self):  # success function
        self.frame2.destroy()  # destroying frame
        self.frame2 = Frame(self.frame)  # creating frame
        img = PhotoImage(file="proj/download.png")  # linking photo
        img = img.zoom(40)  # resizing image
        img = img.subsample(32)  # original relative size of image
        panel = Label(self.frame2, image=img)  # label to display the image
        panel.image = img  # local reference to image
        panel.grid(row=0)

        panel = Label(self.frame2, text="Congratulations You Won", font=(
            'Verdana', 20, 'bold'))  # label to show success message
        self.frame2.grid(row=1, column=0)
        panel.grid(row=1)

    def hangmang(self):  # main game function
        self.count = 0  # variable to count number of variables found
        self.err = 0  # variable to count error
        # opening text file containing all the words to be used in hangman
        fil = open("./proj/words.txt").readlines()
        i = random.randint(0, 58109)  # randomly selecting an integer to choose a word
        self.inpu = 0  # initializing a variable
        self.l = len(fil[i])-1  # length of word choosen
        self.letter = {}  # initializing dictionary
        self.let = list(fil[i])  # list created of all letters in the randomly selected word
        del(self.let[self.l])  # deleting \n from the word
        self.frame2 = Frame(self.frame)  # creating a frame
        for i in range(self.l):
            # creating text widgets to show on screen (equals to number of letters)
            self.letter[i] = Text(self.frame2, height=4, width=6, font=("Helvetica", 16))
            self.letter[i].grid(row=2, column=i)
        self.inp = Entry(self.frame2, width=2, font=("Helvetica", 26))  # entry field to take input
        self.inp.grid(row=3, column=int(self.l/2))
        self.frame2.grid(row=1, column=0, columnspan=self.l)

        def log():  # function for ENTER button
            self.inpi()  # calling outer function for taking entry
        submit = Button(self.frame2, text="ENTER", command=log)  # creating enter button

        submit.grid(row=4, column=int(self.l/2))


a = hangman()  # object of a class
a.maingui()  # function called
