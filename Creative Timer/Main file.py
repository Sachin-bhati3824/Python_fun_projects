import tkinter as tk 
root = tk.Tk()
root.geometry("250x123")
root.title("Creative Timer")
current_time = 0 
def update_time():
    global current_time
    current_time += 1 
    label.config(text = current_time)
    root.after(1000,update_time)

label = tk.Label(root,text= "", font = ("Arial",14))
label.pack(pady=20 )
update_time()
root.resizable(False,False)
root.mainloop()