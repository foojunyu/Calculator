"""
Windows Calculator Application with Theme Switching
"""
import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x550")
        self.root.resizable(False, False)
        
        # Current theme: 'light' or 'dark'
        self.current_theme = 'light'
        
        # Define themes
        self.themes = {
            'light': {
                'bg': '#f0f0f0',
                'fg': '#000000',
                'display_bg': '#ffffff',
                'display_fg': '#000000',
                'button_bg': '#e0e0e0',
                'button_fg': '#000000',
                'operator_bg': '#ff9500',
                'operator_fg': '#ffffff',
                'equals_bg': '#ff9500',
                'equals_fg': '#ffffff'
            },
            'dark': {
                'bg': '#1e1e1e',
                'fg': '#ffffff',
                'display_bg': '#2d2d2d',
                'display_fg': '#ffffff',
                'button_bg': '#3a3a3a',
                'button_fg': '#ffffff',
                'operator_bg': '#ff9500',
                'operator_fg': '#ffffff',
                'equals_bg': '#ff9500',
                'equals_fg': '#ffffff'
            }
        }
        
        # Calculator state
        self.current_input = ""
        self.result = 0
        
        self.create_widgets()
        self.apply_theme()
        
    def create_widgets(self):
        # Menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # Theme menu
        theme_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Theme", menu=theme_menu)
        theme_menu.add_command(label="Light Theme", command=lambda: self.switch_theme('light'))
        theme_menu.add_command(label="Dark Theme", command=lambda: self.switch_theme('dark'))
        
        # Display frame
        display_frame = tk.Frame(self.root, height=100)
        display_frame.pack(fill=tk.BOTH, padx=10, pady=10)
        
        # Display
        self.display = tk.Entry(
            display_frame,
            font=('Arial', 32),
            justify='right',
            bd=0,
            relief=tk.FLAT
        )
        self.display.pack(fill=tk.BOTH, expand=True, ipady=20)
        self.display.insert(0, '0')
        
        # Button frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # Button layout
        buttons = [
            ['C', '⌫', '%', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '=']
        ]
        
        self.buttons = {}
        
        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                btn = tk.Button(
                    button_frame,
                    text=btn_text,
                    font=('Arial', 18, 'bold'),
                    bd=0,
                    relief=tk.FLAT,
                    command=lambda x=btn_text: self.on_button_click(x)
                )
                btn.grid(row=i, column=j, sticky='nsew', padx=2, pady=2)
                self.buttons[btn_text] = btn
        
        # Configure grid weights for responsive layout
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
        for j in range(4):
            button_frame.grid_columnconfigure(j, weight=1)
    
    def apply_theme(self):
        """Apply the current theme to all widgets"""
        theme = self.themes[self.current_theme]
        
        # Root window
        self.root.configure(bg=theme['bg'])
        
        # Display
        self.display.configure(
            bg=theme['display_bg'],
            fg=theme['display_fg'],
            insertbackground=theme['display_fg']
        )
        
        # Buttons
        for btn_text, btn in self.buttons.items():
            if btn_text in ['/', '*', '-', '+']:
                # Operator buttons
                btn.configure(
                    bg=theme['operator_bg'],
                    fg=theme['operator_fg'],
                    activebackground=theme['operator_bg'],
                    activeforeground=theme['operator_fg']
                )
            elif btn_text == '=':
                # Equals button
                btn.configure(
                    bg=theme['equals_bg'],
                    fg=theme['equals_fg'],
                    activebackground=theme['equals_bg'],
                    activeforeground=theme['equals_fg']
                )
            else:
                # Number and other buttons
                btn.configure(
                    bg=theme['button_bg'],
                    fg=theme['button_fg'],
                    activebackground=theme['button_bg'],
                    activeforeground=theme['button_fg']
                )
    
    def switch_theme(self, theme_name):
        """Switch to the specified theme"""
        if theme_name in self.themes:
            self.current_theme = theme_name
            self.apply_theme()
    
    def on_button_click(self, value):
        """Handle button clicks"""
        current = self.display.get()
        
        if value == 'C':
            # Clear
            self.display.delete(0, tk.END)
            self.display.insert(0, '0')
            self.current_input = ""
            
        elif value == '⌫':
            # Backspace
            if len(current) > 1:
                self.display.delete(len(current) - 1, tk.END)
            else:
                self.display.delete(0, tk.END)
                self.display.insert(0, '0')
                
        elif value == '±':
            # Toggle sign
            if current and current != '0':
                if current[0] == '-':
                    self.display.delete(0, 1)
                else:
                    self.display.insert(0, '-')
                    
        elif value == '=':
            # Calculate result
            try:
                result = eval(current.replace('×', '*').replace('÷', '/'))
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, 'Error')
                
        else:
            # Number or operator
            if current == '0' or current == 'Error':
                self.display.delete(0, tk.END)
                self.display.insert(0, value)
            else:
                self.display.insert(tk.END, value)


def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
