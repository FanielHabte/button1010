#import tkinter and ttk from tkinter
import tkinter as tk
from tkinter import ttk


#define on select event 
def on_select (event):
    
     #create an item object that obatines the values of the selectd item.
    selected_item = event.widget.get()
    print("selcted itme:", selected_item)

    #create the root window
root=tk.Tk()
root.title("Combobox Exmaple")
#Create array to popullate the combo box
items = ["item1", "item2","item3","time4","item5"]
#Create a combo box
combo_box = ttk.Combobox(root, values=items)
#Bind the the event to the function 
combo_box.bind("<<ComboboxSelected>>", on_select)
root.mainloop()