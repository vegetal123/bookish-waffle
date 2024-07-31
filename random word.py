import tkinter as tk
import random

# Initialize the main window
root = tk.Tk()
root.title("Random Word Generator")
root.geometry("400x200")
root.configure(bg="yellow")  # Set the background color to yellow

# Create a Label element to hold the generated random word
random_word_label = tk.Label(root, text="Random Word: ", font=("Helvetica", 12), bg="yellow")
random_word_label.pack(pady=20)  # Center the label with padding

# Function to generate a random word
def generate_random_word():
    alpha_list = [chr(i) for i in range(65, 91)]  # List of alphabets from A to Z
    
    random_no1 = random.randint(1, 26)
    random_no2 = random.randint(1, 26)
    random_no3 = random.randint(1, 26)
    random_no4 = random.randint(1, 26)
    random_no5 = random.randint(1, 26)
    
    random_alpha1 = alpha_list[random_no1 - 1]
    random_alpha2 = alpha_list[random_no2 - 1]
    random_alpha3 = alpha_list[random_no3 - 1]
    random_alpha4 = alpha_list[random_no4 - 1]
    random_alpha5 = alpha_list[random_no5 - 1]
    
    random_word = random_alpha1 + random_alpha2 + random_alpha3 + random_alpha4 + random_alpha5
    random_word_label.config(text=f"Random Word: {random_word}")

# Create a button to generate the random word
generate_button = tk.Button(root, text="Generate Random Word", command=generate_random_word, fg="white", bg="blue")
generate_button.pack(pady=10)  # Center the button with padding

# Run the main event loop
root.mainloop()