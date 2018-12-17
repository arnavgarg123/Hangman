from tkinter import *
import random


class hangman:
    def maingui(self):
        self.top = Tk()  # creating main window
        self.top.geometry("865x630")  # set dimensions for main window
        self.top.title("Hangman")  # title for the main window
        self.frame = Frame(self.top)  # Main Frame which encloses all other frames and widgets
        self.frame1 = Frame(self.frame)  # frame for welcome
        wc = Label(self.frame1, text="WELCOME TO HANGMAN GAME",
                   relief="raised", height="4", width="77", font=("Helvetica", 16))  # Welcome message

        button = Button(self.frame1, text="EXIT", relief="sunken", height="6",
                        width="9", bg="#FF0000", command="exit")  # Exit button

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
        wc.grid(row=0, column=0, sticky=W)
        info.grid(row=0, column=1)
        img.grid(row=0, column=0)
        self.frame2.grid(row=1, column=0, columnspan=2)
        self.frame1.grid(row=0, column=0, sticky=W)
        self.frame.grid(row=0, column=0)
        button.grid(row=0, column=1, sticky=W)
        self.top.mainloop()

    def st(self):  # functionality of start button
        self.frame2.destroy()  # Clearing frame2
        self.hangmang()

    def inpi(self):
        self.inpu = self.inp.get()
        print(self.inpu)
        match = 0
        for j in range(self.l):
            if self.let[j] == self.inpu:
                self.count = self.count+1
                self.letter[j].insert(END, self.let[j])
                match = 1
            if self.count == self.l:
                self.great()
                break
        if match == 0:
            self.err = self.err+1
            img = Text(self.frame2, height=30, width=50)
            diag = PhotoImage(file='proj/hangman5.png')  # Linking the photo of hangman
            diag = diag.subsample(2, 2)  # Setting size of the photo
            img.image_create(END, image=diag)  # Inserting image to text widget

            img.grid(row=5, columnspan=self.l)
        if self.err == 5:
            self.fail()

    def fail(self):
        self.frame2.destroy()
        print("fail")

    def great(self):
        self.frame2.destroy()
        print("success")

    def hangmang(self):
        self.count = 0
        self.err = 0
        fil = open("./proj/words.txt").readlines()
        i = random.randint(0, 58109)
        self.inpu = 0
        self.l = len(fil[i])-1
        self.letter = {}
        self.let = list(fil[i])
        del(self.let[self.l])
        print(self.let, self.l)
        self.frame2 = Frame(self.frame)
        for i in range(self.l):
            self.letter[i] = Text(self.frame2, height=4, width=6, font=("Helvetica", 16))
            self.letter[i].grid(row=2, column=i)
        self.inp = Entry(self.frame2, width=2, font=("Helvetica", 26))
        self.inp.grid(row=3, column=int(self.l/2))
        self.frame2.grid(row=1, column=0, columnspan=self.l)

        def log():
            self.inpi()
        submit = Button(self.frame2, text="ENTER", command=log)
        print(self.inpu)

        submit.grid(row=4, column=int(self.l/2))


a = hangman()  # object of a class
a.maingui()  # function called
