"""
Rock • Paper • Scissors — a clean, catchy GUI game built with Tkinter.
Run with: python rock_paper_scissors.py
"""

import tkinter as tk
import random

# ---------- Colors & Fonts ----------
BG_COLOR = "#12121c"
CARD_BG = "#1e1e2f"
ACCENT = "#4ade80"
LOSE_COLOR = "#f43f5e"
DRAW_COLOR = "#facc15"
TEXT_COLOR = "#ffffff"
SUBTLE = "#9ca3af"
BTN_BG = "#3b3f58"
FONT_TITLE = ("Segoe UI", 24, "bold")
FONT_RESULT = ("Segoe UI", 20, "bold")
FONT_CHOICE = ("Segoe UI", 30)
FONT_LABEL = ("Segoe UI", 12)
FONT_SCORE = ("Segoe UI", 14, "bold")

CHOICES = {
    "rock": "🪨",
    "paper": "📄",
    "scissors": "✂️",
}

BEATS = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper",
}


class RPSGame(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock • Paper • Scissors")
        self.geometry("420x560")
        self.resizable(False, False)
        self.configure(bg=BG_COLOR)

        self.wins = 0
        self.losses = 0
        self.draws = 0

        self._build_header()
        self._build_score()
        self._build_battle_area()
        self._build_result()
        self._build_buttons()

    def _build_header(self):
        tk.Label(
            self, text="Rock  •  Paper  •  Scissors",
            font=FONT_TITLE, bg=BG_COLOR, fg=TEXT_COLOR
        ).pack(pady=(25, 5))
        tk.Label(
            self, text="Pick your weapon and beat the computer!",
            font=FONT_LABEL, bg=BG_COLOR, fg=SUBTLE
        ).pack(pady=(0, 15))

    def _build_score(self):
        self.score_var = tk.StringVar(value="Wins: 0    Losses: 0    Draws: 0")
        tk.Label(
            self, textvariable=self.score_var,
            font=FONT_SCORE, bg=BG_COLOR, fg=ACCENT
        ).pack(pady=(0, 15))

    def _build_battle_area(self):
        battle_frame = tk.Frame(self, bg=BG_COLOR)
        battle_frame.pack(pady=10)

        # Player card
        player_card = tk.Frame(battle_frame, bg=CARD_BG, width=150, height=150)
        player_card.grid(row=0, column=0, padx=15)
        player_card.pack_propagate(False)
        tk.Label(player_card, text="YOU", font=FONT_LABEL, bg=CARD_BG, fg=SUBTLE).pack(pady=(10, 0))
        self.player_choice_var = tk.StringVar(value="❔")
        tk.Label(
            player_card, textvariable=self.player_choice_var,
            font=("Segoe UI", 48), bg=CARD_BG, fg=TEXT_COLOR
        ).pack(expand=True)

        tk.Label(
            battle_frame, text="VS", font=FONT_TITLE, bg=BG_COLOR, fg=SUBTLE
        ).grid(row=0, column=1, padx=5)

        # Computer card
        comp_card = tk.Frame(battle_frame, bg=CARD_BG, width=150, height=150)
        comp_card.grid(row=0, column=2, padx=15)
        comp_card.pack_propagate(False)
        tk.Label(comp_card, text="COMPUTER", font=FONT_LABEL, bg=CARD_BG, fg=SUBTLE).pack(pady=(10, 0))
        self.comp_choice_var = tk.StringVar(value="❔")
        tk.Label(
            comp_card, textvariable=self.comp_choice_var,
            font=("Segoe UI", 48), bg=CARD_BG, fg=TEXT_COLOR
        ).pack(expand=True)

    def _build_result(self):
        self.result_var = tk.StringVar(value="Make your move!")
        self.result_label = tk.Label(
            self, textvariable=self.result_var,
            font=FONT_RESULT, bg=BG_COLOR, fg=TEXT_COLOR
        )
        self.result_label.pack(pady=25)

    def _build_buttons(self):
        frame = tk.Frame(self, bg=BG_COLOR)
        frame.pack(pady=10)

        for choice, emoji in CHOICES.items():
            btn = tk.Button(
                frame,
                text=f"{emoji}\n{choice.capitalize()}",
                font=FONT_CHOICE,
                bg=BTN_BG,
                fg=TEXT_COLOR,
                bd=0,
                width=6,
                height=2,
                activebackground=ACCENT,
                activeforeground="#1e1e2f",
                command=lambda c=choice: self.play(c),
            )
            btn.pack(side="left", padx=10)

        reset_btn = tk.Button(
            self, text="Reset Score", font=FONT_LABEL,
            bg=LOSE_COLOR, fg=TEXT_COLOR, bd=0, padx=10, pady=6,
            activebackground="#b91c1c", activeforeground=TEXT_COLOR,
            command=self.reset_score,
        )
        reset_btn.pack(pady=20)

    def play(self, player_choice):
        comp_choice = random.choice(list(CHOICES.keys()))

        self.player_choice_var.set(CHOICES[player_choice])
        self.comp_choice_var.set(CHOICES[comp_choice])

        if player_choice == comp_choice:
            self.draws += 1
            self.result_var.set("It's a draw! 🤝")
            self.result_label.configure(fg=DRAW_COLOR)
        elif BEATS[player_choice] == comp_choice:
            self.wins += 1
            self.result_var.set("You win! 🎉")
            self.result_label.configure(fg=ACCENT)
        else:
            self.losses += 1
            self.result_var.set("You lose! 💀")
            self.result_label.configure(fg=LOSE_COLOR)

        self.score_var.set(
            f"Wins: {self.wins}    Losses: {self.losses}    Draws: {self.draws}"
        )

    def reset_score(self):
        self.wins = 0
        self.losses = 0
        self.draws = 0
        self.score_var.set("Wins: 0    Losses: 0    Draws: 0")
        self.result_var.set("Make your move!")
        self.result_label.configure(fg=TEXT_COLOR)
        self.player_choice_var.set("❔")
        self.comp_choice_var.set("❔")


if __name__ == "__main__":
    game = RPSGame()
    game.mainloop()
