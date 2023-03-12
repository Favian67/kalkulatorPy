import tkinter as tk
from math import pi

class Calculator:
    def __init__(self, master):
        self.master = master
        self.master.title("Kalkulator")
        self.master.configure(bg="#ffffff")

        # Create the entry field
        self.entry = tk.Entry(self.master, font=("Arial", 20), justify="right", bg="#ffffff", bd=0, highlightthickness=1, highlightbackground="#dcdcdc", highlightcolor="#dcdcdc")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        self.entry.focus()

        # Create the buttons
        buttons = [
            ["AC", "±", "π", "/"],
            ["7", "8", "9", "*"],
            ["4", "5", "6", "-"],
            ["1", "2", "3", "+"],
            ["0", ".", "=", ""]
        ]

        for row, button_row in enumerate(buttons, start=1):
            for column, button_text in enumerate(button_row):
                button = tk.Button(self.master, text=button_text, font=("Arial", 16), bg="#F5F5F5", fg="#666666", bd=0, highlightthickness=1, highlightbackground="#dcdcdc", highlightcolor="#dcdcdc", width=2, height=2, command=lambda text=button_text: self.button_click(text))
                button.grid(row=row, column=column, padx=1, pady=1, sticky="nsew")

                # Add some special styles for specific buttons
                if button_text == "AC":
                    button.configure(bg="#e0e0e0", fg="#666666")
                elif button_text == "=":
                    button.configure(bg="#ff9800", fg="#ffffff")
                elif button_text == "π":
                    button.configure(bg="#2196f3", fg="#ffffff")
                elif button_text == "1":
                    button.configure(bg="#F5F5F5", fg="#FF577F")
                elif button_text == "2":
                    button.configure(bg="#F5F5F5", fg="#FF577F")
                elif button_text == "3":
                    button.configure(bg="#F5F5F5", fg="#FF577F")
                elif button_text == "4":
                    button.configure(bg="#F5F5F5", fg="#FF577F")
                elif button_text == "5":
                    button.configure(bg="#F5F5F5", fg="#FF577F")
                elif button_text == "6":
                    button.configure(bg="#F5F5F5", fg="#FF577F")
                elif button_text == "7":
                    button.configure(bg="#F5F5F5", fg="#FF577F")
                elif button_text == "8":
                    button.configure(bg="#F5F5F5", fg="#FF577F")
                elif button_text == "9":
                    button.configure(bg="#F5F5F5", fg="#FF577F")
                elif button_text == "0":
                    button.configure(bg="#F5F5F5", fg="#FF577F")

                if column > 3:
                    row += 1
                    column = 0

    # Define button click behavior
    def button_click(self, button):
        if button == "AC":
            self.entry.delete(0, tk.END)
        elif button == "±":
            value = self.entry.get()
            if value and value[0] == "-":
                self.entry.delete(0)
            else:
                self.entry.insert(0, "-")
        elif button == "π":
            self.entry.insert(tk.END, pi)
        elif button == "=":
            try:
                value = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, value)
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, button)


# Create the main window
root = tk.Tk()
root.geometry("330x400")
root.resizable(False, False)

# Create the calculator
calculator = Calculator(root)

# Run the main loop
root.mainloop()
