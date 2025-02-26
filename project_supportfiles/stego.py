import cv2
import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk

# Encoding dictionary
d = {chr(i): i for i in range(256)}  # Support full range 0-255
c = {i: chr(i) for i in range(256)}

class StegoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Steganography Tool")
        self.root.geometry("500x600")
        
        self.image_path = None
        
        # Label for Image Preview
        self.img_label = tk.Label(root, text="No Image Selected", bg="gray", width=50, height=10)
        self.img_label.pack(pady=10)
        
        # Buttons
        tk.Button(root, text="Select Image", command=self.load_image).pack(pady=5)
        
        # Message Entry
        tk.Label(root, text="Enter Secret Message:").pack()
        self.msg_entry = tk.Entry(root, width=40)
        self.msg_entry.pack()
        
        # Password Entry
        tk.Label(root, text="Enter Passcode:").pack()
        self.pass_entry = tk.Entry(root, width=20, show="*")
        self.pass_entry.pack()
        
        # Encrypt Button
        tk.Button(root, text="Encrypt & Save", command=self.encrypt).pack(pady=5)
        
        # Decrypt Button
        tk.Button(root, text="Decrypt", command=self.decrypt).pack(pady=5)
    
    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
        if file_path:
            self.image_path = file_path
            img = Image.open(file_path)
            img.thumbnail((250, 250))
            img = ImageTk.PhotoImage(img)
            self.img_label.config(image=img, text="")
            self.img_label.image = img
    
    def encrypt(self):
        if not self.image_path:
            messagebox.showerror("Error", "No Image Selected")
            return
        
        msg = self.msg_entry.get()
        password = self.pass_entry.get()
        if not msg or not password:
            messagebox.showerror("Error", "Message and Passcode are required!")
            return
        
        img = cv2.imread(self.image_path)
        h, w, _ = img.shape
        max_chars = (h * w) // 3  

        if len(msg) + len(password) + 1 > max_chars:
            messagebox.showerror("Error", "Message is too long for this image!")
            return
        
        # Store message length in the first pixel
        img[0, 0, 0] = len(msg)  

        # Store password length in the second pixel
        img[0, 0, 1] = len(password)  

        # Store password in next pixels
        n, m, z = 1, 0, 0  

        for char in password:
            img[n, m, z] = d[char]
            n += 1
            if n >= h:
                n = 0
                m += 1
            z = (z + 1) % 3

        # Store secret message after the password
        for char in msg:
            img[n, m, z] = d[char]
            n += 1
            if n >= h:
                n = 0
                m += 1
            z = (z + 1) % 3

        encrypted_path = "encryptedImage.png"  # Use PNG to avoid compression loss
        cv2.imwrite(encrypted_path, img)
        os.system(f"start {encrypted_path}")
        messagebox.showinfo("Success", f"Image Encrypted and Saved as {encrypted_path}")

    def decrypt(self):
        if not self.image_path:
            messagebox.showerror("Error", "No Image Selected")
            return
        
        img = cv2.imread(self.image_path)
        
        # Retrieve message and password length
        msg_length = int(img[0, 0, 0])  
        pass_length = int(img[0, 0, 1])  

        # Retrieve stored password
        stored_password = ""
        n, m, z = 1, 0, 0  

        for _ in range(pass_length):
            pixel_value = int(img[n, m, z])
            stored_password += c.get(pixel_value, "?")  # Avoid KeyError
            n += 1
            if n >= img.shape[0]:
                n = 0
                m += 1
            z = (z + 1) % 3

        # Compare with user input
        entered_password = self.pass_entry.get()
        if entered_password != stored_password:
            messagebox.showerror("Error", "Wrong Passcode!")
            return
        
        # Retrieve secret message
        message = ""

        for _ in range(msg_length):
            pixel_value = int(img[n, m, z])
            message += c.get(pixel_value, "?")  # Avoid KeyError
            n += 1
            if n >= img.shape[0]:
                n = 0
                m += 1
            z = (z + 1) % 3

        messagebox.showinfo("Decryption", f"Decrypted Message: {message}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = StegoApp(root)
    root.mainloop()
