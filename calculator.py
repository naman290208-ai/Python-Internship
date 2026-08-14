"""
Catchy Calculator — a clean, modern GUI calculator built with Tkinter.
Run with: python calculator.py
"""

import tkinter as tk

# ---------- Colors & Fonts ----------
BG_COLOR = "#1e1e2f"
DISPLAY_BG = "#282a3a"
DISPLAY_FG = "#ffffff"
BTN_BG = "#3b3f58"
BTN_FG = "#ffffff"
OP_BG = "#ff7e5f"
OP_FG = "#ffffff"
EQUAL_BG = "#4ade80"
EQUAL_FG = "#1e1e2f"
CLEAR_BG = "#f43f5e"
CLEAR_FG = "#ffffff"
FONT_DISPLAY = ("Segoe UI", 32, "bold")
FONT_BTN = ("Segoe UI", 16, "bold")


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Catchy Calculator")
        self.geometry("360x520")
        self.resizable(False, False)
        self.configure(bg=BG_COLOR)

        self.expression = ""
        self._build_display()
        self._build_buttons()

    def _build_display(self):
        self.display_var = tk.StringVar(value="0")
        display = tk.Label(
            self,
            textvariable=self.display_var,
            anchor="e",
            bg=DISPLAY_BG,
            fg=DISPLAY_FG,
            font=FONT_DISPLAY,
            padx=20,
            pady=30,
        )
        display.pack(fill="x", padx=10, pady=(15, 10))

    def _build_buttons(self):
        frame = tk.Frame(self, bg=BG_COLOR)
        frame.pack(expand=True, fill="both", padx=10, pady=10)

        buttons = [
            ("C", 0, 0, CLEAR_BG, CLEAR_FG), ("⌫", 0, 1, BTN_BG, BTN_FG),
            ("%", 0, 2, OP_BG, OP_FG), ("÷", 0, 3, OP_BG, OP_FG),

            ("7", 1, 0, BTN_BG, BTN_FG), ("8", 1, 1, BTN_BG, BTN_FG),
            ("9", 1, 2, BTN_BG, BTN_FG), ("×", 1, 3, OP_BG, OP_FG),

            ("4", 2, 0, BTN_BG, BTN_FG), ("5", 2, 1, BTN_BG, BTN_FG),
            ("6", 2, 2, BTN_BG, BTN_FG), ("-", 2, 3, OP_BG, OP_FG),

            ("1", 3, 0, BTN_BG, BTN_FG), ("2", 3, 1, BTN_BG, BTN_FG),
            ("3", 3, 2, BTN_BG, BTN_FG), ("+", 3, 3, OP_BG, OP_FG),

            ("0", 4, 0, BTN_BG, BTN_FG), (".", 4, 1, BTN_BG, BTN_FG),
            ("±", 4, 2, BTN_BG, BTN_FG), ("=", 4, 3, EQUAL_BG, EQUAL_FG),
        ]

        for i in range(5):
            frame.rowconfigure(i, weight=1)
        for j in range(4):
            frame.columnconfigure(j, weight=1)

        for (text, row, col, bg, fg) in buttons:
            btn = tk.Button(
                frame,
                text=text,
                font=FONT_BTN,
                bg=bg,
                fg=fg,
                bd=0,
                activebackground="#555970",
                activeforeground="#ffffff",
                command=lambda t=text: self.on_button_click(t),
            )
            btn.grid(row=row, column=col, sticky="nsew", padx=6, pady=6, ipady=10)

    def on_button_click(self, char):
        if char == "C":
            self.expression = ""
        elif char == "⌫":
            self.expression = self.expression[:-1]
        elif char == "=":
            self.calculate()
            return
        elif char == "±":
            self.toggle_sign()
        elif char == "%":
            self.expression += "/100"
        else:
            mapping = {"÷": "/", "×": "*"}
            self.expression += mapping.get(char, char)

        self.display_var.set(self.expression if self.expression else "0")

    def toggle_sign(self):
        if self.expression.startswith("-"):
            self.expression = self.expression[1:]
        else:
            self.expression = "-" + self.expression

    def calculate(self):
        try:
            # Only allow safe characters
            allowed = "0123456789+-*/.() "
            if not all(ch in allowed for ch in self.expression):
                raise ValueError("Invalid characters")
            result = eval(self.expression, {"__builtins__": {}})
            result_str = str(round(result, 10)).rstrip("0").rstrip(".") \
                if "." in str(result) else str(result)
            self.display_var.set(result_str)
            self.expression = result_str
        except (ZeroDivisionError, SyntaxError, ValueError, TypeError):
            self.display_var.set("Error")
            self.expression = ""


if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
