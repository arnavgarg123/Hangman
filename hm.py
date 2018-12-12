from tkinter import *
class hangman:
    def maingui(self):
        self.top=Tk()
        self.top.geometry("865x630")
        self.top.title("Hangman")
        self.frame=Frame(self.top)
        self.frame1=Frame(self.frame)                                                            #frame for welcome
        wc = Label(self.frame1, text="WELCOME TO HANGMAN GAME",
                   relief="raised", height="4", width="77",font=("Helvetica", 16))


        button=Button(self.frame, text="EXIT",relief="sunken", height="6",
                         width="9", bg="#FF0000", command="exit")
        
        self.frame2=Frame(self.frame)
        info=Text(self.frame2,height=30,width=72)
        img=Text(self.frame2,height=30,width=50)
        info.tag_configure('big', font=('Verdana', 20, 'bold'))
        info.tag_configure('small',font=('Tempus Sans ITC', 12, 'bold'))
        abouth="ABOUT HANGMAN GAMES" 
        aboutb="\n\n\nHangman is used often by teachers to practice spelling, vocabulary and just for fun. The most popular way to play hangman games offline is to draw blank letters for the chosen word on a paper or on the blackboard and let the players guess the letters. For each incorrect guess, another part of the man is drawn. If the picture is complete before the word is revealed the hangman game is lost and the character is hanged, if the word is revealed before the execution the game is won."
        diag=PhotoImage(file='proj/hangman5.png')
        diag = diag.subsample(2, 2)
        img.image_create(END, image=diag)
        info.insert(END,abouth,'big')
        info.insert(END,aboutb,'small')
        start=Button(self.frame, text="START",relief="sunken", height="6",
                         width="9", bg="#008000", command="exit")
        
        start.grid(row=2,column=0)
        wc.grid(row=0,column=0,sticky=W )
        info.grid(row=0,column=1)
        img.grid(row=0,column=0)
        self.frame2.grid(row=1,column=0,columnspan=2)
        self.frame1.grid(row=0,column=0,sticky=W)
        self.frame.grid(row=0,column=0)
        button.grid(row=0,column=1,sticky=W)
        self.top.mainloop()
a=hangman()
a.maingui()