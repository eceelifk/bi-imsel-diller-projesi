# =================================================================
# Ad Soyad: Elif Kavak
# Öğrenci No: 231201024
# Proje: Lexical Analyzer 
# =================================================================

import tkinter as tk

def lexical_analyzer():
    
    # anahtar k
    keywords = ["if", "else", "while", "for", "return", "int", "float", "string", "class", "break", "continue","switch","case","default"]
    

    user_input = entry.get().strip()

    # Boş mu k.
    if not user_input or " " in user_input:
        result_label.config(text="Geçerli bir değişken ismi değildir.", fg="red")
        return
    
    # harf ile başlıyor mu (a-z veya A-Z) 
    if not user_input[0].isalpha():
        result_label.config(text="Geçerli bir değişken ismi değildir.", fg="red")
        return
    
    # Sadece harf, rakam ve alt çizgi (_) içermesi
    # özel karakter içeremez 
    for char in user_input:
        if not (char.isalnum() or char == "_"):
            result_label.config(text="Geçerli bir değişken ismi değildir.", fg="red")
            return
        
    # anahtar kelime olmamalı
    if user_input in keywords:
        result_label.config(text="Geçerli bir değişken ismi değildir.", fg="red")
        return
    
    # hepsi sağlandıysa 
    result_label.config(text="Geçerli bir değişken ismidir.", fg="green")

# --- arayüz ayarları(tkinter)---
root = tk.Tk()
root.title("Lexical Analyzer")
root.geometry("400x200")

# bilgi et.
tk.Label(root, text="Değişken İsmini Girin", font=("Calibri", 12)).pack(pady=10)

# giriş kutusu
entry = tk.Entry(root, font=("Calibri", 12), width=25)
entry.pack(pady=5)

# analyze butonu 
analyze_button = tk.Button(root, text="Analyze", command=lexical_analyzer, font=("Calibri", 11), bg="#d1d1d1")
analyze_button.pack(pady=20)

# sonuç yazısı
result_label = tk.Label(root, text="", font=("Calibri", 11, "bold"))
result_label.pack(pady=10)

# programı Çalıştırmak icin
root.mainloop()
