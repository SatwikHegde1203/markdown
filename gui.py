import tkinter as tk
from tkinter import filedialog, messagebox
from main import convert_markdown_to_html  # Importing the conversion logic

# Function to start the conversion process
def on_convert_button_click():
    # Get the markdown file from the user
    input_file_path = filedialog.askopenfilename(title="Select Markdown File", filetypes=[("Markdown Files", "*.md")])
    if not input_file_path:
        return

    # Update the file label to show the selected file path
    file_label.config(text=f"Selected File: {input_file_path}", fg="black")

    # Update status label
    status_label.config(text="Converting...", fg="blue")

    # Ask for the output HTML file location
    output_file_path = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML Files", "*.html")])
    if not output_file_path:
        return

    # Call the convert function
    success, message = convert_markdown_to_html(input_file_path, output_file_path)

    # Notify the user about success or error
    if success:
        status_label.config(text=f"Conversion Complete! Saved as: {message}", fg="green")
        messagebox.showinfo("Success", f"Markdown file successfully converted to HTML!\nSaved as: {message}")
    else:
        status_label.config(text="Error Occurred", fg="red")
        messagebox.showerror("Error", f"An error occurred: {message}")

# Clear the selected file and reset the status
def clear_selection():
    status_label.config(text="No file selected", fg="black")
    file_label.config(text="No file selected", fg="black")

# Set up the GUI
def setup_gui():
    # Create the main window
    root = tk.Tk()
    root.title("Markdown to HTML Converter")
    root.geometry("600x250")
    
    # Create a label for displaying the selected file
    global file_label
    file_label = tk.Label(root, text="No file selected", fg="black", font=("Arial", 12))
    file_label.pack(pady=10)

    # Add a button to start the conversion process
    convert_button = tk.Button(root, text="Convert Markdown to HTML", command=on_convert_button_click)
    convert_button.pack(pady=10)

    # Add a clear selection button
    clear_button = tk.Button(root, text="Clear Selection", command=clear_selection)
    clear_button.pack(pady=5)

    # Add a status label
    global status_label
    status_label = tk.Label(root, text="No file selected", fg="black", font=("Arial", 10, "italic"))
    status_label.pack(pady=20)

    # Run the GUI loop
    root.mainloop()

if __name__ == "__main__":
    setup_gui()
