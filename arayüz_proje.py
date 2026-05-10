# =================================================================
# Ad Soyad: Elif Ece Kavak
# Öğrenci No: 231201024
# Ders: BLG306 - Biçimsel Diller ve Otomatlar
# Proje: Basit Bir Lexical Analyzer (Arayüzlü Versiyon)
# =================================================================

import tkinter as tk

def lexical_analyzer():
    """Hocanın tüm kurallarını içeren senin kod mantığın."""
    # 1. Anahtar kelimeler (Keywords) 
    keywords = ["if", "else", "while", "for", "return", "int", "float", "string", "class", "break"]
    

    user_input = entry.get().strip()

    # KURAL: Boş kontrol
    if not user_input or " " in user_input:
        result_label.config(text="Geçerli bir değişken ismi değildir.", fg="red")
        return
    
    # KURAL: Harf ile başlamalıdır (a-z veya A-Z) 
    if not user_input[0].isalpha():
        result_label.config(text="Geçerli bir değişken ismi değildir.", fg="red")
        return
    
    # KURAL: Sadece harf, rakam ve alt çizgi (_) içerebilir 
    # KURAL: Özel karakterler içeremez (@, #, !, - vb.)
    for char in user_input:
        if not (char.isalnum() or char == "_"):
            result_label.config(text="Geçerli bir değişken ismi değildir.", fg="red")
            return
        
    # KURAL: Anahtar kelime (keyword) olmamalıdır 
    if user_input in keywords:
        result_label.config(text="Geçerli bir değişken ismi değildir.", fg="red")
        return
    
    # TÜM KURALLAR GEÇİLİRSE 
    result_label.config(text="Geçerli bir değişken ismidir.", fg="green")

# --- ARAYÜZ AYARLARI (Tkinter) ---
root = tk.Tk()
root.title("BLG306 - Lexical Analyzer")
root.geometry("400x250")

# Bilgi Etiketi 
tk.Label(root, text="Değişken İsmini Girin", font=("Calibri", 12)).pack(pady=10)

# Giriş Kutusu
entry = tk.Entry(root, font=("Calibri", 12), width=25)
entry.pack(pady=5)

# Analyze Butonu 
analyze_button = tk.Button(root, text="Analyze", command=lexical_analyzer, font=("Calibri", 11), bg="#d1d1d1")
analyze_button.pack(pady=20)

# Sonuç Yazısı 
result_label = tk.Label(root, text="", font=("Calibri", 11, "bold"))
result_label.pack(pady=10)

# Programı Çalıştır
root.mainloop()