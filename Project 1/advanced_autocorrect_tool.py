import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from symspellpy import SymSpell, Verbosity
import os

# === Initialize SymSpell ===
sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
DICT_PATH = "dictionary_freq.txt"

if not os.path.exists(DICT_PATH):
    messagebox.showerror("Dictionary Missing", "dictionary_freq.txt not found in the directory.")
    exit()

sym_spell.load_dictionary(DICT_PATH, term_index=0, count_index=1)

# === Autocorrect Function ===
def autocorrect_text(text):
    words = text.strip().split()
    corrected_words = []
    corrections = 0
    incorrect = []

    for word in words:
        suggestions = sym_spell.lookup(word, Verbosity.CLOSEST, max_edit_distance=2)
        if suggestions and suggestions[0].term != word:
            corrected_words.append(suggestions[0].term)
            corrections += 1
            incorrect.append(word)
        else:
            corrected_words.append(word)

    return " ".join(corrected_words), corrections, incorrect

# === GUI Application ===
class AutocorrectApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🤖 AI Autocorrect Pro")
        self.root.geometry("820x620")
        self.root.configure(bg="#1e1e1e")

        self.dark_mode = True

        # Style
        self.set_styles()

        ttk.Label(root, text="Enter text to autocorrect:", font=("Segoe UI", 20, "bold")).pack(pady=10)

        self.input_box = tk.Text(root, height=8, width=90, font=("Segoe UI", 11), bg="#2e2e2e", fg="white", insertbackground="white")
        self.input_box.pack(pady=5)
        self.input_box.bind("<KeyRelease>", self.on_key_release)

        # Suggestion popup
        self.suggestion_box = tk.Listbox(root, height=4, bg="#ffffcc", font=("Segoe UI", 10))
        self.suggestion_box.place_forget()
        self.suggestion_box.bind("<<ListboxSelect>>", self.apply_suggestion)

        # Stats
        stat_frame = tk.Frame(root, bg="#1e1e1e")
        stat_frame.pack()
        self.char_count = ttk.Label(stat_frame, text="Characters: 0")
        self.char_count.grid(row=0, column=0, padx=10)
        self.word_count = ttk.Label(stat_frame, text="Words: 0")
        self.word_count.grid(row=0, column=1, padx=10)

        # Buttons
        btn_frame = tk.Frame(root, bg="#1e1e1e")
        btn_frame.pack(pady=10)

        ttk.Button(btn_frame, text="🛠 Correct", command=self.correct_input).grid(row=0, column=0, padx=10)
        ttk.Button(btn_frame, text="🧹 Clear", command=self.clear_text).grid(row=0, column=1, padx=10)
        ttk.Button(btn_frame, text="📄 Save Output", command=self.save_output).grid(row=0, column=2, padx=10)
        ttk.Button(btn_frame, text="📂 Load Text", command=self.load_text).grid(row=0, column=3, padx=10)
        ttk.Button(btn_frame, text="🌓 Toggle Theme", command=self.toggle_theme).grid(row=0, column=4, padx=10)

        # Output
        ttk.Label(root, text="Corrected Output:").pack(pady=5)
        self.output_box = tk.Text(root, height=8, width=90, font=("Segoe UI", 11), bg="#2e2e2e", fg="#aaffaa", state='disabled')
        self.output_box.pack()

        # Summary
        self.summary_label = ttk.Label(root, text="Corrections made: 0")
        self.summary_label.pack(pady=5)

        # Incorrect words display
        self.incorrect_label = ttk.Label(root, text="Incorrect words: None")
        self.incorrect_label.pack()

    def set_styles(self):
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('TButton', font=('Segoe UI', 10), padding=6)
        style.configure('TLabel', font=('Segoe UI', 10), background="#1e1e1e", foreground="white")

    def on_key_release(self, event=None):
        self.update_stats()

        # Get the current word
        cursor = self.input_box.index(tk.INSERT)
        line, char = map(int, cursor.split('.'))
        text = self.input_box.get("1.0", tk.END)
        words = text.split()
        if not words:
            self.suggestion_box.place_forget()
            return

        last_word = words[-1]
        if not last_word.isalpha() or len(last_word) < 2:
            self.suggestion_box.place_forget()
            return

        suggestions = sym_spell.lookup(last_word, Verbosity.TOP, max_edit_distance=2)
        if suggestions and suggestions[0].term != last_word:
            self.suggestion_box.delete(0, tk.END)
            for item in suggestions:
                self.suggestion_box.insert(tk.END, item.term)
            x, y, _, _ = self.input_box.bbox(tk.INSERT)
            self.suggestion_box.place(x=x + 20, y=y + 180)
        else:
            self.suggestion_box.place_forget()

    def apply_suggestion(self, event):
        if not self.suggestion_box.curselection():
            return
        suggestion = self.suggestion_box.get(self.suggestion_box.curselection())
        text = self.input_box.get("1.0", tk.END).strip().split()
        if text:
            text[-1] = suggestion
            self.input_box.delete("1.0", tk.END)
            self.input_box.insert(tk.END, ' '.join(text))
        self.suggestion_box.place_forget()
        self.update_stats()

    def update_stats(self, event=None):
        content = self.input_box.get("1.0", tk.END).strip()
        self.char_count.config(text=f"Characters: {len(content)}")
        self.word_count.config(text=f"Words: {len(content.split())}")

    def correct_input(self):
        text = self.input_box.get("1.0", tk.END)
        corrected, count, incorrect = autocorrect_text(text)

        self.output_box.config(state='normal')
        self.output_box.delete("1.0", tk.END)
        self.output_box.insert(tk.END, corrected)
        self.output_box.config(state='disabled')

        self.summary_label.config(text=f"Corrections made: {count}")
        self.incorrect_label.config(text=f"Incorrect words: {', '.join(incorrect) if incorrect else 'None'}")

    def clear_text(self):
        self.input_box.delete("1.0", tk.END)
        self.output_box.config(state='normal')
        self.output_box.delete("1.0", tk.END)
        self.output_box.config(state='disabled')
        self.summary_label.config(text="Corrections made: 0")
        self.incorrect_label.config(text="Incorrect words: None")
        self.suggestion_box.place_forget()
        self.update_stats()

    def save_output(self):
        text = self.output_box.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Empty Output", "There's no corrected text to save.")
            return
        file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file:
            with open(file, "w", encoding="utf-8") as f:
                f.write(text)
            messagebox.showinfo("Saved", f"Corrected text saved to:\n{file}")

    def load_text(self):
        file = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        if file:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
            self.input_box.delete("1.0", tk.END)
            self.input_box.insert(tk.END, content)
            self.update_stats()

    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        bg = "#ffffff" if not self.dark_mode else "#1e1e1e"
        fg = "#000000" if not self.dark_mode else "white"
        box_bg = "#f0f0f0" if not self.dark_mode else "#2e2e2e"
        box_fg = "#000000" if not self.dark_mode else "white"
        self.root.configure(bg=bg)

        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Text):
                widget.configure(bg=box_bg, fg=box_fg, insertbackground=box_fg)
            elif isinstance(widget, tk.Frame):
                widget.configure(bg=bg)
            elif isinstance(widget, ttk.Label):
                widget.configure(background=bg, foreground=fg)
        self.set_styles()

# === Run App ===
if __name__ == "__main__":
    root = tk.Tk()
    app = AutocorrectApp(root)
    root.mainloop()
