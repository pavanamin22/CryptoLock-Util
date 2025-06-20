import tkinter as tk
from tkinter import messagebox, scrolledtext
from cryptography.fernet import Fernet
import time

class EncryptionTool:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Encryption/Decryption Tool")
        self.root.geometry("600x500")
        self.root.configure(bg="#f0f8ff")

        # Title Label
        title_label = tk.Label(root, text="Data Encryption/Decryption Tool", font=("Arial", 20, "bold"), fg="#1e90ff", bg="#f0f8ff")
        title_label.pack(pady=20)

        # Input Frame
        input_frame = tk.Frame(root, bg="#f0f8ff")
        input_frame.pack(pady=10)

        tk.Label(input_frame, text="Enter Text:", font=("Arial", 12), fg="#ff4500", bg="#f0f8ff").grid(row=0, column=0, padx=10, pady=5)
        self.text_entry = tk.Text(input_frame, font=("Arial", 12), height=5, width=40, bg="#ffffff", fg="#333333")
        self.text_entry.grid(row=0, column=1, padx=10, pady=5)

        tk.Label(input_frame, text="Key (or generate new):", font=("Arial", 12), fg="#ff4500", bg="#f0f8ff").grid(row=1, column=0, padx=10, pady=5)
        self.key_entry = tk.Entry(input_frame, font=("Arial", 12), width=40, bg="#ffffff", fg="#333333")
        self.key_entry.grid(row=1, column=1, padx=10, pady=5)

        # Buttons Frame
        button_frame = tk.Frame(root, bg="#f0f8ff")
        button_frame.pack(pady=10)

        tk.Button(button_frame, text="Generate Key", font=("Arial", 12, "bold"), fg="white", bg="#32cd32", command=self.generate_key).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="Encrypt", font=("Arial", 12, "bold"), fg="white", bg="#1e90ff", command=self.encrypt_text).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="Decrypt", font=("Arial", 12, "bold"), fg="white", bg="#ff4500", command=self.decrypt_text).grid(row=0, column=2, padx=5)

        # Result Text Area
        self.result_text = scrolledtext.ScrolledText(root, font=("Arial", 12), height=10, width=60, bg="#ffffff", fg="#2f4f4f")
        self.result_text.pack(pady=20)

    def generate_key(self):
        self.key = Fernet.generate_key()
        self.key_entry.delete(0, tk.END)
        self.key_entry.insert(0, self.key.decode())
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, "New key generated successfully!\nSave this key for decryption.\n")

    def encrypt_text(self):
        text = self.text_entry.get("1.0", tk.END).strip()
        key = self.key_entry.get().encode() if self.key_entry.get() else None

        if not text:
            messagebox.showerror("Error", "Please enter text to encrypt!")
            return
        if not key:
            messagebox.showerror("Error", "Please generate or enter a key!")
            return

        try:
            start_time = time.time()
            fernet = Fernet(key)
            encrypted_text = fernet.encrypt(text.encode())
            end_time = time.time()
            execution_time = end_time - start_time

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Encrypted Text: {encrypted_text.decode()}\n")
            self.result_text.insert(tk.END, f"Encryption Time: {execution_time:.4f} seconds\n")
            self.result_text.insert(tk.END, "Note: Use the same key for decryption.")
        except Exception as e:
            messagebox.showerror("Error", f"Encryption failed: {str(e)}")

    def decrypt_text(self):
        text = self.text_entry.get("1.0", tk.END).strip()
        key = self.key_entry.get().encode() if self.key_entry.get() else None

        if not text:
            messagebox.showerror("Error", "Please enter text to decrypt!")
            return
        if not key:
            messagebox.showerror("Error", "Please enter a key for decryption!")
            return

        try:
            start_time = time.time()
            fernet = Fernet(key)
            decrypted_text = fernet.decrypt(text.encode()).decode()
            end_time = time.time()
            execution_time = end_time - start_time

            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Decrypted Text: {decrypted_text}\n")
            self.result_text.insert(tk.END, f"Decryption Time: {execution_time:.4f} seconds\n")
        except Exception as e:
            messagebox.showerror("Error", f"Decryption failed: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionTool(root)
    root.mainloop()