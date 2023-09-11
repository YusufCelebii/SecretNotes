import tkinter as tk
from tkinter import messagebox
import base64


window = tk.Tk()
w = 400
h = 600
# initialize screen
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width / 2) - (w / 2)
y_coordinate = (screen_height / 2) - (h / 2)
window.geometry("%dx%d+%d+%d" % (w, h,x_coordinate,y_coordinate))


def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

def save_and_encrypt():
    master_key_input = master_key.get()
    title = title1.get()
    if master_key_input == "" or title=="" or text1=="":
        messagebox.showinfo("Form",
                            "Please enter blanks",
                            icon='info')
    else:

        encrypted_message=encode(master_key_input,text1.get("1.0","end"))
        combined_text = title + ":\n" + encrypted_message + "\n"
        try:
            with open("My Secrets.txt", "a") as file:
                file.write(combined_text)
        except Exception as e:
            with open("My Secrets.txt","w") as file:
                file.write(combined_text)
        finally:
            title1.delete(0,"end")
            text1.delete("1.0","end")
            master_key.delete(0,"end")
            window.update()

def decrypt_text():
    master_key_input=master_key.get()
    message_encrypted=text1.get("1.0","end")
    if master_key_input == "" or text1 == "":
        messagebox.showinfo("Form",
                            "Please enter blanks",
                            icon='info')
    else:
        try:
            decrpted_message=decode(master_key_input,message_encrypted)
            text1.delete("1.0","end")
            text1.insert("1.0",decrpted_message)
        except:
            messagebox.showinfo("Form",
                                "Please enter encrypted message",
                                icon='info')




# put the "SECRETS"
label1 = tk.Label(text="My Secrets", font=("Arial", 30, "bold"), fg="dark slate blue")
label1.place(x=200, y=30, anchor="center")

# put the title
label2 = tk.Label(text="Enter your title", font=("Times New Roman", 15, "bold"))
label2.place(x=200, y=100, anchor="center")
title1 = tk.Entry(bg="light blue", width=30, font=("Times", 12, "normal"))
title1.place(x=200, y=120, anchor="center")

# put the text
label3 = tk.Label(text="Enter your secrets", font=("Times New Roman", 15, "bold"))
label3.place(x=200, y=160, anchor="center")
text1 = tk.Text(bg="light blue", width=40, font=("Times", 11, "normal"))
text1.place(x=200, y=170, anchor="n", width=300, height=300)

# masterkey label and entry
label4 = tk.Label(text="Enter your master key", font=("Times New Roman", 12, "bold"))
label4.place(x=200, y=500, anchor="center")
master_key = tk.Entry(bg="light blue", width=30, font=("Times", 10, "normal"))
master_key.place(x=200, y=520, anchor="center")

# Encrypte and Save button
save_button = tk.Button(text="Encrypte & Save", font=("Arial", 10, "bold"), bg="gray56",command=save_and_encrypt)
save_button.place(x=200, y=545, anchor="center")

# Decrypte Button
decrypte_button = tk.Button(text="Decrypte", font=("Arial Black", 8, "bold"), bg="gray56",command=decrypt_text)
decrypte_button.place(x=200, y=580, anchor="center")

window.mainloop()




