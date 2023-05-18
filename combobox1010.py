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