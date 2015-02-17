# yes/no
#by me
#loops as long as the user wants

#import statements
import random
from tkinter import *
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox

#create message box
root = Tk()
w = Label(root, text="Rock Paper Scissors")
w.pack()

#sentinel variable
answer = "y"

messagebox.showinfo("Welcome","Welcome to Rock Paper Scissors. I must warn you that the explanation of this game is ONLY for complete idiots.")
messagebox.showinfo("instructions","For those of you who are, here is how you play; I pick either Rock, Paper, or Scissors, then you pick from the same.")
messagebox.showinfo("Key to Win","Rock smashes Scissors, Scissors cut Paper to shreds, and Paper completely envelopes Rock. Here we go, ready or not.")

while answer == "y":
    #pick a random number
    number = random.randint (1,3)
    compchoice = 0

    #translate computer's choice of number to a game value
    if number == 1:
        compchoice = "r"
    elif number == 2:
        compchoice = "p"
    else:
        compchoice = "s"
    playchoice = simpledialog.askstring("Your Choice","Now, which one will you choose?").strip().lower()[0]
    if playchoice == "r" and compchoice == "r":
        messagebox.showinfo("Rock V Rock","It..... is ..... a..... TIE!")
    elif playchoice == "r" and compchoice == "p":
       messagebox.showinfo("Rock V Paper","Unfortunately, you lost, I chose paper.")
    elif playchoice == "r" and compchoice == "s":
       messagebox.showinfo("Rock V Scissors","YOU WON!!!!!! HOORAY FOR YOU!!!!!")
    elif playchoice == "p" and compchoice == "r":
       messagebox.showinfo("Paper V Rock","YOU WON!!!! I chose Rock.")
    elif playchoice == "p" and compchoice == "p":
       messagebox.showinfo("Paper V Paper","HM.... That's interesting, I was sure you would choose Rock.     Well, anyways, we tied.")
    elif playchoice == "p" and compchoice == "s":
       messagebox.showinfo("Paper V Scissors","I won. I chose Scissors.")
    elif playchoice == "s" and compchoice == "r":
       messagebox.showinfo("Scissors V Rock","I won. I chose Rock")
    elif playchoice == "s" and compchoice == "p":
       messagebox.showinfo("Scissors v Paper","You won. Congratulations.")
    else:
       messagebox.showinfo("Scissors V Scissors","AAANNNDDD..... IIITTT..... IIISSS..... AAA, drumroll please, IT IS A TIE")
    

    answer = simpledialog.askstring("Play Again?","Do you want to play again? ").strip().lower()[0]
    
