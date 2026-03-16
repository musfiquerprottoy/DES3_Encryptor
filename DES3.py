import customtkinter as ctk
from Crypto.Cipher import DES3
from Crypto.Util.Padding import pad, unpad
import binascii
import webbrowser

# FIXED Key & IV for STABLE output
key_hex = "0123456789ABCDEFFEDCBA98765432100123456789ABCDEF"
iv_hex = "FEDCBA9876543210"
key = binascii.unhexlify(key_hex)
iv = binascii.unhexlify(iv_hex)

# Functions
def encrypt_text():
    input_text = encrypt_box.get("1.0", "end-1c").strip()
    if not input_text:
        result_box.delete("1.0", "end")
        result_box.insert("1.0", "Please enter text to encrypt")
        return
    
    try:
        msg_bytes = input_text.encode('utf-8')
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
        encrypted = cipher.encrypt(pad(msg_bytes, DES3.block_size))
        result_hex = binascii.hexlify(encrypted).decode().lower()
        result_box.delete("1.0", "end")
        result_box.insert("1.0", result_hex)
        copy_btn.configure(state="normal")
    except:
        result_box.delete("1.0", "end")
        result_box.insert("1.0", "Encryption failed")

def decrypt_text():
    input_hex = decrypt_box.get("1.0", "end-1c").strip().lower()
    if not input_hex:
        result_box.delete("1.0", "end")
        result_box.insert("1.0", "Please enter hex to decrypt")
        return
    
    try:
        ciphertext = binascii.unhexlify(input_hex)
        cipher = DES3.new(key, DES3.MODE_CBC, iv)
        decrypted = unpad(cipher.decrypt(ciphertext), DES3.block_size)
        result_text = decrypted.decode('utf-8')
        result_box.delete("1.0", "end")
        result_box.insert("1.0", result_text)
        copy_btn.configure(state="normal")
    except:
        result_box.delete("1.0", "end")
        result_box.insert("1.0", "Decryption failed")

def copy_result():
    result = result_box.get("1.0", "end-1c").strip()
    if result and result not in ["Please enter text", "Encryption failed", "Decryption failed"]:
        app.clipboard_clear()
        app.clipboard_append(result)
        copy_btn.configure(text="✅ Copied!", fg_color="#10b981")
    else:
        copy_btn.configure(text="Nothing to copy", fg_color="#ef4444")

def open_facebook():
    webbrowser.open("https://facebook.com/musfiqueprottoy.1")

def open_github():
    webbrowser.open("https://github.com/yourusername")

# Setup
#app=ctk.CTk()
#app.update_idletasks()  # Ensure screen dimensions are updated
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("🔒 DES3 Encryptor/Decryptor")
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()

window_width = int(screen_width * 0.5)
window_height = int(screen_height * 0.8)

x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)

app.geometry(f'{window_width}x{window_height} +{x}+{y}')
app.resizable(True, True)

app.grid_rowconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)
app.grid_rowconfigure(2, weight=1)

app.grid_columnconfigure(0, weight=1)


# Main container
main_frame = ctk.CTkFrame(app, corner_radius=20)
main_frame.pack(fill="both", expand=True, padx=20, pady=20)

# Title
title = ctk.CTkLabel(main_frame, text="🔒 DES3 Encryptor/Decryptor 🔑", 
                    font=ctk.CTkFont(family="Arial", size=28, weight="bold"))
title.pack(pady=(30, 40))

# ENCRYPT SECTION
encrypt_label = ctk.CTkLabel(main_frame, text="📝 Input Text to Encrypt", 
                           font=ctk.CTkFont(family="Arial", size=16, weight="bold"))
encrypt_label.pack(pady=(0, 10))

encrypt_box = ctk.CTkTextbox(main_frame, height=100, 
                           corner_radius=20,  # Round rectangular
                           font=ctk.CTkFont(family="Arial", size=18),
                           fg_color="#191B0B")
encrypt_box.pack(padx=40, pady=(0, 15), fill="x")

encrypt_btn = ctk.CTkButton(main_frame, text="🔒 ENCRYPT", 
                          font=ctk.CTkFont(family="Arial", size=14, weight="bold"),
                          height=45, fg_color="#3b82f6", hover_color="#1d4ed8",
                          command=encrypt_text)
encrypt_btn.pack(pady=(0, 30))

# DECRYPT SECTION
decrypt_label = ctk.CTkLabel(main_frame, text="🔓 Input Hex to Decrypt", 
                           font=ctk.CTkFont(family="Arial", size=16, weight="bold"))
decrypt_label.pack(pady=(0, 10))

decrypt_box = ctk.CTkTextbox(main_frame, height=100, 
                           corner_radius=20,  # Round rectangular
                           font=ctk.CTkFont(family="Arial", size=18),
                           fg_color="#1e1e2e")
decrypt_box.pack(padx=40, pady=(0, 15), fill="x")
#decrypt_box.insert("1.0", "c6e734f19fe593f")  # Test data

decrypt_btn = ctk.CTkButton(main_frame, text="🔓 DECRYPT", 
                          font=ctk.CTkFont(family="Arial", size=14, weight="bold"),
                          height=45, fg_color="#10b981", hover_color="#059669",
                          command=decrypt_text)
decrypt_btn.pack(pady=(0, 30))

# RESULT SECTION
result_label = ctk.CTkLabel(main_frame, text="📤 Result", 
                          font=ctk.CTkFont(family="Arial", size=16, weight="bold"))
result_label.pack(pady=(0, 10))

result_box = ctk.CTkTextbox(main_frame, height=120, 
                          corner_radius=20,  # Round rectangular
                          font=ctk.CTkFont(family="Arial", size=18),
                          fg_color="#1e1e2e")
result_box.pack(padx=40, pady=(0, 15), fill="x")

copy_btn = ctk.CTkButton(main_frame, text="📋 Copy Result", 
                       font=ctk.CTkFont(family="Arial", size=14, weight="bold"),
                       height=45, fg_color="#6b7280", hover_color="#4b5563",
                       state="disabled", command=copy_result)
copy_btn.pack(pady=(0, 40))

# FOOTER
footer_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
footer_frame.pack(side="bottom", pady=20)

footer_text = ctk.CTkLabel(footer_frame, text="All rights reserved.", 

                                                     font=ctk.CTkFont(family="Arial", size=16))
footer_text.pack()

# Add a second footer label for 'Made by Musfique Prottoy'
made_by_label = ctk.CTkLabel(footer_frame, text="Made by Musfique Prottoy", font=ctk.CTkFont(family="Arial", size=16))
made_by_label.pack()

# Social links
social_frame = ctk.CTkFrame(footer_frame, fg_color="transparent")
social_frame.pack(pady=(10, 0))

fb_btn = ctk.CTkButton(social_frame, text="📘 Facebook", 
                      font=ctk.CTkFont(family="Arial", size=12),
                      width=100, height=30, fg_color="#1877f2", 
                      hover_color="#166fe5", command=open_facebook)
fb_btn.pack(side="left", padx=10)

gh_btn = ctk.CTkButton(social_frame, text="🐙 GitHub", 
                      font=ctk.CTkFont(family="Arial", size=12),
                      width=100, height=30, fg_color="#181717", 
                      hover_color="#0d0d0d", command=open_github)
gh_btn.pack(side="left", padx=10)

app.mainloop()