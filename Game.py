import tkinter 
def settile(row,column):
    pass

playerx='X'
playerO='O'
curr_player=playerx
board=[[0,0,0],
       [0,0,0],
       [0,0,0]]
color_blue="blue"
color_yellow="yellow"
color_gray="gray"

window=tkinter.Tk()
window.title("tic tac toe")
window.resizable(False,False)

frame=tkinter.Frame(window)
label=tkinter.Label(frame,text=curr_player+"'s turn",foreground="black",font=("Consolas",20))

label.grid(row=0,column=0,columnspan=3,sticky="we")
for row in range(3):
    for column in range(3):
        board[row][column] = tkinter.Button(frame,text="",font=("Consolas",50,"bold"),
                                         background=color_gray,foreground=color_blue,width=4,height=1,
                                         command=lambda row=row,column=column:settile(row,column))
        board[row][column].grid(row=row+1,column=column)

frame.pack()    

window.mainloop()