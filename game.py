from doctest import master
from logging import root
from tkinter import *
import random
from turtle import color

master = Tk()
body= Frame(master, bg="#add8e6")
body.place(relx=0.1, rely=0.12, relwidth=0.8, relheight=0.85)
body.grid(row=0,column=0)
master.title("The Rock Paper Scissors Game")
#/////////////////////HEADER///////////////////
headeryazi= Label(body,bg="#add8e6", anchor=CENTER, text="The Rock Paper Scissors Game", font="Verdana 12 bold").grid(row=1,column=2)
temp= Label(body, bg="#add8e6", anchor=CENTER,font="Verdana 12 bold").grid(row=2,column=2)
temp= Label(body, bg="#add8e6", anchor=CENTER,font="Verdana 12 bold").grid(row=3,column=2)
#/////////////////////BODY///////////////////
secim= ["ROCK","PAPER","SCISSORS"]

def updateChoice(x):
#for bot
   bot= random.choice(secim)
   msgbot.configure(text="BOT CHOOSE "+bot)
   msg.configure(text="YOU CHOOSE "+x)
#if you win
   if bot == x :
      winlose.configure(text="ITS A TIE \n")
   elif bot == secim[0] and x == secim[1]:
      winlose.configure(text="YOU WIN! Paper Beats Rock \n")
   elif bot == secim[1] and x == secim[2]:
      winlose.configure(text="YOU WIN! Scissors Beats Paper \n")
   elif bot == secim[2] and x == secim[0]:
      winlose.configure(text="YOU WIN! Rock Beats Scissors \n")
#if you lose
   elif bot == secim[1] and x == secim[0]:
      winlose.configure(text="You Lose. Paper Beats Rock \n")
   elif bot == secim[2] and x == secim[1]:
      winlose.configure(text="You Lose. Scissors Beats Paper \n")
   elif bot == secim[0] and x == secim[2]:
      winlose.configure(text="You Lose. Rock Beats Scissors \n")

rock= Button(body,anchor=CENTER,width=20,height=2,text="ROCK", command= lambda:updateChoice("ROCK")).grid(row=5,column=1)
paper= Button(body,anchor=CENTER,width=20,height=2,text="PAPER", command= lambda:updateChoice("PAPER")).grid(row=5,column=2)
scissors= Button(body,anchor=CENTER,width=20,height=2,text="SCISSORS", command= lambda:updateChoice("SCISSORS")).grid(row=5,column=3)

msg= Label(body,anchor=CENTER,width=20,font="Verdana 10 bold",bg="#add8e6")
msg.grid(row=7,column=1)
msgbot= Label(body,anchor=CENTER,width=20,font="Verdana 10 bold",bg="#add8e6")
msgbot.grid(row=7,column=3)
temp= Label(body,anchor=CENTER,bg="#add8e6", font="Verdana 12 bold").grid(row=6,column=2)
winlose= Label(body,anchor=CENTER,width=30,font="Verdana 10 bold",bg="#add8e6")
winlose.grid(row=8,column=2)
master.mainloop()