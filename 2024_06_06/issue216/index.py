import tkinter as tk

def calculate_bmi():
    height = float(height_entry.get()) / 100
    weight = float(weight_entry.get())
    bmi = weight / (height * height)
    result_label.config(text="BMI: {:.2f}".format(bmi))

# Create main window
root = tk.Tk()
root.title("BMI計算器")

# Name
name_label = tk.Label(root, text="姓名:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

# Height
height_label = tk.Label(root, text="身高(cm):")
height_label.grid(row=1, column=0)
height_entry = tk.Entry(root)
height_entry.grid(row=1, column=1)

# Weight
weight_label = tk.Label(root, text="體重(kg):")
weight_label.grid(row=2, column=0)
weight_entry = tk.Entry(root)
weight_entry.grid(row=2, column=1)

# Button to calculate BMI
calculate_button = tk.Button(root, text="計算BMI", command=calculate_bmi)
calculate_button.grid(row=3, columnspan=2)

# Label to display BMI result
result_label = tk.Label(root, text="")
result_label.grid(row=4, columnspan=2)

root.mainloop()