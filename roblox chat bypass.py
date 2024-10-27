import tkinter as tk

# Function to apply special formatting:
# - Replace 'F'/'f' with 'Ƒ' and apply two dots below
# - Replace 'u'/'U' with 'ų' (without additional formatting)
# - Replace 'g'/'G' with 'Ɠ' and apply two dots below
# - Replace 'y'/'Y' with 'ʏ'
# - Apply dot and comma below for all alphanumeric characters
def apply_special_formatting(text):
    accented_text = ""
    dot_and_comma_below = "\u0323\u0326"  # Combining dot below and combining comma below

    # Define replacements for specific characters
    replacement_letters = {
        'F': "Ƒ",
        'f': "Ƒ",
        'u': "ų",
        'U': "Ų",
        'g': "Ɠ",
        'G': "Ɠ",
        'y': "ʏ",
        'Y': "ʏ"
    }

    for char in text:
        if char in replacement_letters:
            # Replace specific letters with special replacements
            accented_text += replacement_letters[char] + dot_and_comma_below
        elif char.isalnum():
            # Apply dot and comma below for all other alphanumeric characters
            accented_text += char + dot_and_comma_below
        else:
            # Leave spaces and punctuation unchanged
            accented_text += char

    return accented_text

# Function to convert text and auto-copy it to the clipboard
def convert_text(text):
    converted_text = apply_special_formatting(text)
    # Copy to clipboard
    root.clipboard_clear()
    root.clipboard_append(converted_text)
    return converted_text

# Update converted text, select it, and copy it to clipboard
def update_and_copy(event=None):
    input_text = entry.get()
    converted_text = convert_text(input_text)
    output_var.set(converted_text)
    output_entry.select_range(0, tk.END)

# Toggle topmost window
def toggle_topmost():
    current_state = root.attributes("-topmost")
    root.attributes("-topmost", not current_state)

# GUI setup
root = tk.Tk()
root.title("Chat bypasser")
root.configure(bg="black")

frame = tk.Frame(root, padx=10, pady=10, bg="black")
frame.pack()

# Input field
entry_label = tk.Label(frame, text="Enter Text:", fg="white", bg="black")
entry_label.grid(row=0, column=0, sticky="e")

entry = tk.Entry(frame, width=30, bg="gray", fg="white")
entry.grid(row=0, column=1, pady=(0, 10))
entry.bind("<KeyRelease>", update_and_copy)  # Update and auto-copy on every key release

# Output field
output_label = tk.Label(frame, text="bypassed Text:", fg="white", bg="black")
output_label.grid(row=1, column=0, sticky="e")

output_var = tk.StringVar()
output_entry = tk.Entry(frame, textvariable=output_var, state="readonly", width=30, bg="gray", fg="white")
output_entry.grid(row=1, column=1, pady=(0, 10))

# Topmost button
topmost_button = tk.Button(frame, text="Toggle Topmost", command=toggle_topmost, bg="darkgray", fg="black")
topmost_button.grid(row=2, column=0, columnspan=2, pady=(5, 0))

root.mainloop()
