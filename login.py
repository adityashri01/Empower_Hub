from customtkinter import*
from PIL import Image
from tkinter import messagebox


def login():
    if userName.get()=='' or userpassword.get()=='':
        messagebox.showerror('Error','All fields cannot be empty')

    elif userName.get()=='Aditya' or userpassword.get()=='Aditya1234':
        messagebox.showinfo('Login Successfull','You are welcome')
        root.destroy()
        import employeemanagementsystem

    else:
        messagebox.showerror('Error','Please use correct informations')

       
    



root=CTk()
root.geometry('930x478')
root.title('Login Page')
root.resizable(0,0)
image=CTkImage(Image.open('backgroundimage.jpeg'),size=(930,478))
imageLabel=CTkLabel(root,image=image,text=" ")
imageLabel.place(x=0,y=0)

headingLabel1=CTkLabel(root,text="Welcome To",bg_color='#090909',text_color='White',font=("Arial", 42, "bold"))
headingLabel1.place(x=310,y=50)

headingLabel2=CTkLabel(root,text="Empower_Hub",bg_color='#090909',text_color='White',font=("Arial", 42, "bold"))
headingLabel2.place(x=300,y=100)

userName=CTkEntry(root,placeholder_text='Enter your user name ',width=180)
userName.place(x=350,y=200)

userpassword=CTkEntry(root,placeholder_text='Enter your password ',show='*',width=180)
userpassword.place(x=350,y=250)

loginButton=CTkButton(root,text='Login',cursor='hand2',command=login)
loginButton.place(x=370,y=300)

root.mainloop()