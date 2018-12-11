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


        button=Button(self.frame, text="Exit",relief="sunken", height="6",
                         width="9", bg="#FF0000", command="exit")
        
        self.frame2=Frame(self.frame)
        info=Text(self.frame2,height=30,width=122)

        wc.grid(row=0,column=0,sticky=W )
        info.grid(row=0,column=0)
        self.frame2.grid(row=1,column=0,columnspan=2)
        self.frame1.grid(row=0,column=0,sticky=W)
        self.frame.grid(row=0,column=0)
        button.grid(row=0,column=1,sticky=W)
        self.top.mainloop()
a=hangman()
a.maingui()