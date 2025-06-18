import tkinter as tk
from tkinter import messagebox
import pyshorteners

def shorten_link():
    original_url = entry.get()
    if not original_url:
        messagebox.showerror("Error", "Please enter a URL to shorten.")
        return

    try:
        s = pyshorteners.Shortener()
        shortened_url = s.tinyurl.short(original_url)
        shortened_label.config(text=f"Shortened URL: {shortened_url}")
        copy_button.config(state=tk.NORMAL)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def copy_to_clipboard():
    shortened_url = shortened_label.cget("text").split(": ")[1]
    root.clipboard_clear()
    root.clipboard_append(shortened_url)
    messagebox.showinfo("Success", "Shortened URL copied to clipboard!")

root = tk.Tk()
root.title("Link Shortener")

label = tk.Label(root, text="Enter URL:")
label.pack()

entry = tk.Entry(root)
entry.pack()

shorten_button = tk.Button(root, text="Shorten", command=shorten_link)
shorten_button.pack()

shortened_label = tk.Label(root, text="")
shortened_label.pack()

copy_button = tk.Button(root, text="Copy Shortened URL", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.pack()

root.mainloop()

---



from flask import Flask, request, jsonify
import pyshorteners

app = Flask(__name__)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')

    if not original_url:
        return jsonify({'error': 'URL is required'}), 400

    try:
        s = pyshorteners.Shortener()
        shortened_url = s.tinyurl.short(original_url)
        return jsonify({'shortened_url': shortened_url}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
