import tkinter as tk
import random
import time

DICE_SIZE = 100

# Define dot positions for each face of the dice (1-6)
DICE_DOTS = {
    1: [(0.5, 0.5)],
    2: [(0.25, 0.25), (0.75, 0.75)],
    3: [(0.25, 0.25), (0.5, 0.5), (0.75, 0.75)],
    4: [(0.25, 0.25), (0.25, 0.75), (0.75, 0.25), (0.75, 0.75)],
    5: [(0.25, 0.25), (0.25, 0.75), (0.75, 0.25), (0.75, 0.75), (0.5, 0.5)],
    6: [(0.25, 0.25), (0.25, 0.5), (0.25, 0.75), (0.75, 0.25), (0.75, 0.5), (0.75, 0.75)]
}

class DiceRoller:
    def __init__(self, root):
        self.root = root
        self.root.title("🎲 Dice Roller")
        self.canvas = tk.Canvas(root, width=200, height=200, bg="white")
        self.canvas.pack(pady=20)

        self.roll_button = tk.Button(root, text="Roll Dice", command=self.roll_dice)
        self.roll_button.pack()

        self.dice_square = self.canvas.create_rectangle(50, 50, 150, 150, fill="white", outline="black")
        self.dice_dots = []

    def draw_dice_face(self, number):
        # Remove old dots
        for dot in self.dice_dots:
            self.canvas.delete(dot)
        self.dice_dots = []

        dot_radius = 7
        for (dx, dy) in DICE_DOTS[number]:
            x = 50 + dx * DICE_SIZE
            y = 50 + dy * DICE_SIZE
            dot = self.canvas.create_oval(
                x - dot_radius, y - dot_radius,
                x + dot_radius, y + dot_radius,
                fill="black"
            )
            self.dice_dots.append(dot)

    def roll_dice(self):
        # Simulate rolling animation
        for _ in range(10):  # Roll 10 times for animation
            num = random.randint(1, 6)
            self.draw_dice_face(num)
            self.root.update()
            time.sleep(0.1)

        # Final roll result
        final_result = random.randint(1, 6)
        self.draw_dice_face(final_result)

if __name__ == "__main__":
    root = tk.Tk()
    app = DiceRoller(root)
    root.mainloop()
