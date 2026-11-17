import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e1e")
        
        self.expression = ""
        self.result_var = tk.StringVar()
        
        # Create UI
        self.create_display()
        self.create_buttons()
    
    def create_display(self):
        """Create the display area"""
        display_frame = tk.Frame(self.root, bg="#1e1e1e")
        display_frame.pack(expand=True, fill="both", padx=10, pady=20)
        
        # Display label
        display = tk.Label(
            display_frame,
            textvariable=self.result_var,
            font=("Arial", 28, "bold"),
            bg="#2d2d2d",
            fg="#ffffff",
            anchor="e",
            padx=20,
            pady=20
        )
        display.pack(expand=True, fill="both")
        self.result_var.set("0")
    
    def create_buttons(self):
        """Create calculator buttons"""
        buttons_frame = tk.Frame(self.root, bg="#1e1e1e")
        buttons_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Button layout
        buttons = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['0', '.', '=']
        ]
        
        # Button colors
        number_color = "#3a3a3a"
        operator_color = "#ff9500"
        special_color = "#5a5a5a"
        
        for i, row in enumerate(buttons):
            for j, button in enumerate(row):
                # Determine button color
                if button in ['C', '⌫', '%']:
                    bg_color = special_color
                elif button in ['/', '*', '-', '+', '=']:
                    bg_color = operator_color
                else:
                    bg_color = number_color
                
                # Create button
                btn = tk.Button(
                    buttons_frame,
                    text=button,
                    font=("Arial", 18, "bold"),
                    bg=bg_color,
                    fg="#ffffff",
                    activebackground="#666666",
                    activeforeground="#ffffff",
                    border=0,
                    cursor="hand2",
                    command=lambda b=button: self.on_button_click(b)
                )
                
                # Special width for 0 button
                if button == '0':
                    btn.grid(row=i, column=j, columnspan=2, sticky="nsew", padx=2, pady=2)
                elif button == '=':
                    btn.grid(row=i, column=j+1, sticky="nsew", padx=2, pady=2)
                else:
                    btn.grid(row=i, column=j, sticky="nsew", padx=2, pady=2)
        
        # Configure grid weights for responsive buttons
        for i in range(5):
            buttons_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            buttons_frame.grid_columnconfigure(j, weight=1)
    
    def on_button_click(self, char):
        """Handle button clicks"""
        if char == 'C':
            # Clear
            self.expression = ""
            self.result_var.set("0")
        
        elif char == '⌫':
            # Backspace
            self.expression = self.expression[:-1]
            self.result_var.set(self.expression if self.expression else "0")
        
        elif char == '=':
            # Calculate result
            try:
                result = eval(self.expression)
                self.result_var.set(str(result))
                self.expression = str(result)
            except ZeroDivisionError:
                self.result_var.set("Error: Div by 0")
                self.expression = ""
            except:
                self.result_var.set("Error")
                self.expression = ""
        
        else:
            # Append character
            self.expression += str(char)
            self.result_var.set(self.expression)
    
    def run(self):
        """Start the calculator"""
        self.root.mainloop()

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    calculator.run()
