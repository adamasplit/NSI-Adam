from tkinter import *
from tkinter import messagebox


class terminal(Tk):
    # Terminal window setup
    def __init__(self, res=[720, 480]):
        Tk.__init__(self)
        self.title("Python Terminal")
        self.geometry(str(res[0]) + 'x' + str(res[1]))  # window resolution set as 720x1080 by default
        self.minsize(width=res[0], height=res[1])
        self.configure(bg='#242323')
        # Setting up default colors/fonts
        self.option_add("*Frame.background", "#242323")
        self.option_add("*Canvas.background", "#242323")
        self.option_add("*Label.Font", "Courier 10")
        self.option_add("*Label.foreground", "white")
        self.option_add("*Label.background", "#242323")
        # creating the window content
        self.create_menu()
        self.welcome()

    def create_menu(self):
        # Creating a top menu bar
        menu_bar = Menu(self)
        # File Manager (not done yet)
        menu_file = Menu(menu_bar, tearoff=0)
        menu_file.add_command(label="New", command=self.do_something)
        menu_file.add_command(label="Open text File", command=self.do_something)
        menu_file.add_command(label="Save", command=self.do_something)
        menu_file.add_separator()
        menu_file.add_command(label="Exit", command=self.quit)
        menu_bar.add_cascade(label="File", menu=menu_file)
        # Help&About
        menu_help = Menu(menu_bar, tearoff=0)
        menu_help.add_command(label="About", command=self.do_about)
        menu_help.add_command(label="Help", command=self.do_help)
        menu_bar.add_cascade(label="Help", menu=menu_help)

        self.config(menu=menu_bar)

    def welcome(self):
        # Creating the terminal window to display results
        global terminal_window
        container = Frame(self)
        # Creating a canvas to scroll up and down if there's not enough space
        canvas = Canvas(container)
        v = Scrollbar(container, orient='vertical', command=canvas.yview)
        terminal_window = Frame(canvas)
        terminal_window.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=terminal_window, anchor="nw")
        canvas.configure(yscrollcommand=v.set)

        label = Label(terminal_window, text="-* Welcome to Python Terminal ! *-")
        label.pack()
        label = Label(terminal_window, text="Please enter a command. Type 'help' for more info")
        label.pack(anchor=NW)

        container.pack(anchor=NW, expand=True, fill=BOTH)
        canvas.pack(fill="both", expand=True, side=LEFT)
        v.pack(side=RIGHT, fill=Y)
        self.ask_command()

    def do_command(self, command):
        if command != '':
            # verifying if the first word is known
            com = command.split()

            if (com[0] == 'echo'):  # echo command displays entered text
                self.display(com[-(len(com) - 1):])

            elif (com[0] == 'help'):  # list of available commands
                self.help()

            elif (com[0] == 'quit'):  # Quit the app
                self.quit()
            # If it's not
            else:
                self.display(
                    ("'" + com[0] + "'" + " does not exist. Please type 'help' to see the list of available commands"))

    def do_something(self):  # Debug
        print("I've done smth")

    def display(self, text):  # Displays text on the terminal window
        label = Label(terminal_window, text=text)
        label.pack(anchor=NW)

    def help(self):  # help text
        self.display("-'help' : list of all the commands available \n -'echo [text]': display text input on console \n -'quit' : quit application")

    def do_about(self):  # pop-up box for credits
        messagebox.showinfo("About", "Python Terminal 1.0 made by adamasplit with Tkinter.")

    def do_help(self):  # pop-up box for help
        messagebox.showinfo("Help", "Write down your command in the bottom section below, then press Enter to run it.")

    def ask_command(self):  # command prompt section
        # Creating the text entry box
        cmdprompt = Entry(self, bg='#242323', fg='white', font=('Courier New', 15), insertbackground='white',
                          justify=LEFT)
        cmdprompt.focus()
        # Run command button
        start = Button(self, text='Run', bg='#242323', fg='white', font=('Courier New', 15),
                       command=lambda: self.do_command(cmdprompt.get()))
        cmdprompt.pack(ipadx=20, ipady=20, anchor=S, fill=X)
        start.pack(fill=X, anchor=S)


# Starting the application
window = terminal()
window.mainloop()
