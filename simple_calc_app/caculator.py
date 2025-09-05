import tkinter as tk        #GUI provider
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")

screen = tk.StringVar()

entry = tk.Entry(root, textvariable=screen, font="Arial 20")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

button_frame = tk.Frame(root)
button_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "x"],
    ["1", "2", "3", "-"],
    ["0", "C", "=", "+"]
]

def on_click(value):
    current = screen.get()
    if value == "C":
        screen.set("")
    elif value == "=":
        try:
            result = str(eval(current))
            screen.set(result)
        except:
            screen.set("Error")
    else:
        screen.set(current + value)

# Create and place buttons in grid
for row_index, row in enumerate(buttons):
    for col_index, button_text in enumerate(row):
        btn = tk.Button(
            button_frame,
            text=button_text,
            font="Arial 16",
            command=lambda val=button_text: on_click(val),
            width=3,
            height=2
        )
        btn.grid(row=row_index, column=col_index, padx=5, pady=5)


root.mainloop()