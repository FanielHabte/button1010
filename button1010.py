# import tikinter
import tkinter as tk


#define button
def button_click():
    print("Button  clicked")

#creat the rooth window
root = tk.Tk()
root.title("Button example")

  #crate botton object 
button = tk.Button(root,text="Click Me!",command=button_click)
button.pack()  

#creat the mainloop that keeps the root window visible
root.mainloop() 