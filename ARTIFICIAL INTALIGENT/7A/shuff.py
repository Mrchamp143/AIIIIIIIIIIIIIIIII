import tkinter as tk
from PIL import Image, ImageTk
import random
import os

class CardShufflerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Card Shuffler")

        self.deck = [f"{rank}_of_{suit}" for suit in ["hearts", "diamonds", "clubs", "spades"]
                     for rank in ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]]
        
        self.load_images()

        self.label = tk.Label(root, text="Deck of Cards", font=("Helvetica", 16))
        self.label.pack(pady=10)

        self.shuffle_button = tk.Button(root, text="Shuffle Deck", command=self.shuffle_deck)
        self.shuffle_button.pack(pady=10)

        self.canvas = tk.Canvas(root, width=800, height=640)
        self.canvas.pack()

        self.show_deck()  # Display the deck immediately upon startup

    def load_images(self):
        self.images = {}
        for card in self.deck:
            path = os.path.join("cards", f"{card}.png")
            img = Image.open(path).resize((60, 90))  # Resize as necessary
            self.images[card] = ImageTk.PhotoImage(img)

    def shuffle_deck(self):
        self.riffle_shuffle(self.deck)
        self.show_deck()  # Update display after shuffling

    def riffle_shuffle(self, deck):
        half_size = len(deck) // 2
        first_half = deck[:half_size]
        second_half = deck[half_size:]

        shuffled_deck = []
        while first_half or second_half:
            if first_half and (random.random() > 0.5 or not second_half):
                shuffled_deck.append(first_half.pop(0))
            if second_half and (random.random() > 0.5 or not first_half):
                shuffled_deck.append(second_half.pop(0))

        # Update the original deck
        for i in range(len(deck)):
            deck[i] = shuffled_deck[i]

    def show_deck(self):
        self.canvas.delete("all")
        for idx, card in enumerate(self.deck):
            x = (idx % 13) * 60 + 10
            y = (idx // 13) * 100 + 10
            self.canvas.create_image(x, y, anchor=tk.NW, image=self.images[card])

if __name__ == "__main__":
    root = tk.Tk()
    app = CardShufflerApp(root)
    root.mainloop()
