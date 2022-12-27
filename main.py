import tkinter as tk
import subprocess
from tkinter import filedialog
from tkinter import ttk
from subprocess import call
from PIL import Image, ImageTk  # pip install pillow


# from Stack import StackVisualizer
# root=Tk()
# style= ttk.Sytle(win)

class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("Data3.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        border = tk.LabelFrame(self, text='Login', bg='ivory', bd=10, font=("Arial", 20))
        border.pack(fill="both", expand="yes", padx=150, pady=150)

        L1 = tk.Label(border, text="Username", font=("Arial Bold", 15), bg='ivory')
        L1.place(x=50, y=20)
        T1 = tk.Entry(border, width=30, bd=5)
        T1.place(x=180, y=20)

        L2 = tk.Label(border, text="Password", font=("Arial Bold", 15), bg='ivory')
        L2.place(x=50, y=80)
        T2 = tk.Entry(border, width=30, show='*', bd=5)
        T2.place(x=180, y=80)

        def verify():
            try:
                with open("credential.txt", "r") as f:
                    info = f.readlines()
                    i = 0
                    for e in info:
                        u, p = e.split(",")
                        if u.strip() == T1.get() and p.strip() == T2.get():
                            controller.show_frame(SecondPage)
                            i = 1
                            break
                    if i == 0:
                        messagebox.showinfo("Error", "Please provide correct username and password!!")
            except:
                messagebox.showinfo("Error", "Please provide correct username and password!!")

        B1 = tk.Button(border, text="Submit", font=("Arial", 15), command=verify)
        B1.place(x=320, y=115)

        def register():
            window = tk.Tk()
            window.resizable(0, 0)
            window.configure(bg="deep sky blue")
            window.title("Register")

            l1 = tk.Label(window, text="Username:", font=("Arial", 15), bg="deep sky blue")
            l1.place(x=10, y=10)
            t1 = tk.Entry(window, width=30, bd=5)
            t1.place(x=200, y=10)

            l2 = tk.Label(window, text="Password:", font=("Arial", 15), bg="deep sky blue")
            l2.place(x=10, y=60)
            t2 = tk.Entry(window, width=30, show="*", bd=5)
            t2.place(x=200, y=60)

            l3 = tk.Label(window, text="Confirm Password:", font=("Arial", 15), bg="deep sky blue")
            l3.place(x=10, y=110)
            t3 = tk.Entry(window, width=30, show="*", bd=5)
            t3.place(x=200, y=110)

            def check():
                if t1.get() != "" or t2.get() != "" or t3.get() != "":
                    if t2.get() == t3.get():
                        with open("credential.txt", "a") as f:
                            f.write(t1.get() + "," + t2.get() + "\n")
                            messagebox.showinfo("Welcome", "You are registered successfully!!")
                    else:
                        messagebox.showinfo("Error", "Your password didn't get match!!")
                else:
                    messagebox.showinfo("Error", "Please fill the complete field!!")

            b1 = tk.Button(window, text="Sign in", font=("Arial", 15), bg="#ffc22a", command=check)
            b1.place(x=170, y=150)

            window.geometry("570x220")

        B2 = tk.Button(self, text="Register", bg="dark orange", font=("Arial", 15), command=register)
        B2.place(x=650, y=20)


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        load = Image.open("data2.jpg")
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        Button = tk.Button(self, text="Next", font=("Arial", 15), command=lambda: controller.show_frame(ThirdPage))
        Button.place(x=650, y=450)

        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=100, y=450)




class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        def openStack():
            os.system("py Stack.py")

        def openqueue():
            os.system("py CircularQueue.py")

        def openlinkedlist():
            os.system("py LinkedList.py")



        self.configure(bg='Tomato')

        Label = tk.Label(self,
                         text="Let's Fun with Data Structure \n “Not all roots are buried down in the ground, \n some are at the top of a tree.”-Jinvirle. \n All the best!!",
                         bg="orange", font=("Arial Bold", 25))
        Label.place(x=40, y=150)

        # Button = tk.Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button = tk.Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=680, y=450)

        Button = tk.Button(self, text="    Stack     ", font=("Arial", 15),command=openStack)  # .pack(expand=True)
        Button.place(x=120, y=90)

        # Button = tk.Button(self, text="Circular Queue", font=("Arial", 15), command=lambda: controller.show_frame(stack.py))
        Button = tk.Button(self, text="Circular Queue", font=("Arial", 15), command=openqueue)
        Button.place(x=500, y=90)

        # Button = tk.Button(self, text=" Linked List  ", font=("Arial", 15), command=lambda: subprocess.call)
        Button = tk.Button(self, text=" Linked List  ", font=("Arial", 15), command=openlinkedlist)
        Button.place(x=120, y=350)

        Button = tk.Button(self, text=" Binary Search", font=("Arial", 15), command=openStack)
        Button.place(x=500, y=350)

        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(SecondPage))
        Button.place(x=80, y=450)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage):
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")


app = Application()
app.maxsize(1000, 500)
app.minsize(800, 500)
app.mainloop()
