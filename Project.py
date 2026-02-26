import customtkinter as ct
import sqlite3


app = ct.CTk()

app.title('ED - EasyDatabase')
app.iconbitmap('big.ico')
app.geometry("420x420")

tab = ct.CTkTabview(app)
tab.pack(pady = 1)


tab_1 = tab.add("Welcome")
tab_2 = tab.add("Automatic")
tab_3 = tab.add("Manual")
tab_4 = tab.add("About")

def output_table():
    op =  ct.CTkToplevel(tab_2)
    op.title("Output Table")
    op.geometry("240x240")

btn_1 = ct.CTkButton(tab_2,width=50,height=20,corner_radius=5, command=output_table)
btn_1.pack(pady = 1)

app.mainloop()