from tkinter import *
from PIL import Image, ImageDraw, ImageTk

# -------- A* Email Spam Detector -------- #

spam_keywords = ["win", "free", "prize", "offer", "lottery", "click", "money", "urgent", "bonus"]
threshold = 4  # spam score threshold

def heuristic(email_words):
    """Simple heuristic: count suspicious words"""
    return sum(word in spam_keywords for word in email_words)

def a_star_email_detection(email_text):
    words = email_text.lower().split()
    g_cost = sum(word in spam_keywords for word in words)  # cost: actual spam words
    h_cost = heuristic(words)  # heuristic estimation
    f_cost = g_cost + h_cost   # A* total cost

    return f_cost >= threshold

# -------- GUI & Image Output -------- #

def show_result(is_spam):
    text = "SPAM EMAIL" if is_spam else "SAFE EMAIL"
    color = "red" if is_spam else "green"

    img = Image.new("RGB", (400, 200), "white")
    draw = ImageDraw.Draw(img)
    draw.text((120, 90), text, fill=color)

    img.show()

def detect():
    email = text_box.get("1.0", END)
    result = a_star_email_detection(email)
    show_result(result)

# -------- UI Window -------- #

root = Tk()
root.title("A* Email Detector")

Label(root, text="Enter Email Content:", font=("Arial", 12)).pack()
text_box = Text(root, height=6, width=50, font=("Arial", 10))
text_box.pack(pady=5)

Button(root, text="Detect Email", command=detect, font=("Arial", 12), bg="blue", fg="white").pack(pady=10)

root.mainloop()
