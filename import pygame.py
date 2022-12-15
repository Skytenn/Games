import tkinter as tk

def main():
    window= tk.Tk()
    window.title(" Kilometer to Miles Converter")
    window.geometry("375x200")
    

    label1 = tk.Label(window, text="Enter Kilometer:")
    label2 = tk.Label(window, text="Miles:")
    label1.place(x=50,y=30)
    
    textbox1 = tk.Entry(window, width=12)
    textbox1.place(x=200,y=35)
    label2.place(x=50,y=100)
    label3 = tk.Label(window, text=" ")
    label3.place(x=180,y=100)

    con=0.621371
         
    def btn1_click():
        Miles =(float(textbox1.get()) * con)
        label3.configure(text = float(Miles))
    btn1 = tk.Button(window, text="              Convert             ", command=btn1_click)
    btn1.place(x=90,y=150)
    window.mainloop()
    

main()