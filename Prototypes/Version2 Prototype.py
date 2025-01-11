import tkinter as tk
from tkinter import ttk, messagebox
import os

# Kullanıcı verilerini depolamak için basit bir dosya tabanlı sistem
data_file = "users.txt"

def load_users():
    if not os.path.exists(data_file):
        with open(data_file, "w") as f:
            pass
    with open(data_file, "r") as f:
        return {line.strip().split(":")[0]: line.strip().split(":")[1:]
 for line in f if line.strip()}

def save_user(username, password, language):
    with open(data_file, "a") as f:
        f.write(f"{username}:{password}:{language}\n")

def get_translations(language):
    translations = {
        "en": {
            "welcome": "Welcome! Please log in or sign up.",
            "username": "Username:",
            "password": "Password:",
            "login": "Login",
            "signup": "Sign Up",
            "language": "Language:",
            "login_success": "Login Successful",
            "login_failed": "Login Failed",
            "signup_success": "Sign Up Successful",
            "signup_failed": "Sign Up Failed",
            "username_exists": "Username already exists.",
            "empty_fields": "Username and password cannot be empty.",
            "created_account": "Account created successfully. Please log in.",
            "menu_settings": "Settings",
            "menu_help": "Help",
            "menu_exit": "Exit",
            "app_welcome": "Welcome to Make It Easy!",
            "online_shop": "Online Shop",
            "trading_system": "Trading System",
            "real_time_tracking": "Real-Time Tracking",
            "discount_notifications": "Discount Notifications",
            "chat_system": "Chat System",
            "ratings": "Ratings",
            "customize_interface": "Customize Interface",
            "feature_under_construction": "Feature is under construction!"
        },
        "tr": {
            "welcome": "Hoş geldiniz! Lütfen giriş yapın veya kayıt olun.",
            "username": "Kullanıcı Adı:",
            "password": "Şifre:",
            "login": "Giriş Yap",
            "signup": "Kayıt Ol",
            "language": "Dil:",
            "login_success": "Giriş Başarılı",
            "login_failed": "Giriş Başarısız",
            "signup_success": "Kayıt Başarılı",
            "signup_failed": "Kayıt Başarısız",
            "username_exists": "Kullanıcı adı zaten mevcut.",
            "empty_fields": "Kullanıcı adı ve şifre boş olamaz.",
            "created_account": "Hesap başarıyla oluşturuldu. Lütfen giriş yapın.",
            "menu_settings": "Ayarlar",
            "menu_help": "Yardım",
            "menu_exit": "Çıkış",
            "app_welcome": "Make It Easy uygulamasına hoş geldiniz!",
            "online_shop": "Online Mağaza",
            "trading_system": "Takas Sistemi",
            "real_time_tracking": "Gerçek Zamanlı Takip",
            "discount_notifications": "İndirim Bildirimleri",
            "chat_system": "Sohbet Sistemi",
            "ratings": "Derecelendirmeler",
            "customize_interface": "Arayüz Özelleştirme",
            "feature_under_construction": "Bu özellik yapım aşamasında!"
        },
        "ko": {
            "welcome": "환영합니다! 로그인하거나 가입하세요.",
            "username": "사용자 이름:",
            "password": "비밀번호:",
            "login": "로그인",
            "signup": "가입",
            "language": "언어:",
            "login_success": "로그인 성공",
            "login_failed": "로그인 실패",
            "signup_success": "가입 성공",
            "signup_failed": "가입 실패",
            "username_exists": "사용자 이름이 이미 존재합니다.",
            "empty_fields": "사용자 이름과 비밀번호는 비워둘 수 없습니다.",
            "created_account": "계정이 성공적으로 생성되었습니다. 로그인하세요.",
            "menu_settings": "설정",
            "menu_help": "도움말",
            "menu_exit": "종료",
            "app_welcome": "Make It Easy에 오신 것을 환영합니다!",
            "online_shop": "온라인 상점",
            "trading_system": "거래 시스템",
            "real_time_tracking": "실시간 추적",
            "discount_notifications": "할인 알림",
            "chat_system": "채팅 시스템",
            "ratings": "평점",
            "customize_interface": "인터페이스 사용자 정의",
            "feature_under_construction": "이 기능은 현재 개발 중입니다!"
        }
    }
    return translations[language]

# Pencereyi ekranın ortasında açmak için yardımcı fonksiyon
def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f"{width}x{height}+{x}+{y}")

# Giriş/Kayıt ekranı
class LoginScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Login - Delivery and Trading System")
        self.geometry("400x400")
        center_window(self)

        self.language = tk.StringVar(value="en")
        self.translations = get_translations(self.language.get())

        self.init_ui()

    def init_ui(self):
        ttk.Label(self, text=self.translations["welcome"], font=("Arial", 14)).pack(pady=10)

        # Dil seçimi
        ttk.Label(self, text=self.translations["language"]).pack(pady=5)
        lang_menu = ttk.OptionMenu(self, self.language, self.language.get(), "en", "tr", "ko", command=self.update_language)
        lang_menu.pack(pady=5)

        # Kullanıcı adı
        ttk.Label(self, text=self.translations["username"]).pack(pady=5)
        self.username_entry = ttk.Entry(self)
        self.username_entry.pack(pady=5)

        # Şifre
        ttk.Label(self, text=self.translations["password"]).pack(pady=5)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        # Giriş ve Kayıt düğmeleri
        login_button = ttk.Button(self, text=self.translations["login"], command=self.login)
        login_button.pack(pady=5)

        signup_button = ttk.Button(self, text=self.translations["signup"], command=self.signup)
        signup_button.pack(pady=5)

    def update_language(self, lang):
        self.translations = get_translations(lang)

        self.refresh_ui()

    def refresh_ui(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.init_ui()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        users = load_users()

        if username in users and users[username][0] == password:
            messagebox.showinfo(self.translations["login_success"], self.translations["login_success"])
            self.destroy()
            app = DeliveryTradingApp(self.language.get())
            app.mainloop()
        else:
            messagebox.showerror(self.translations["login_failed"], self.translations["login_failed"])

    def signup(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        language = self.language.get()
        users = load_users()

        if username in users:
            messagebox.showerror(self.translations["signup_failed"], self.translations["username_exists"])
        elif not username or not password:
            messagebox.showerror(self.translations["signup_failed"], self.translations["empty_fields"])
        else:
            save_user(username, password, language)
            messagebox.showinfo(self.translations["signup_success"], self.translations["created_account"])

# Ana uygulama penceresi
class DeliveryTradingApp(tk.Tk):
    def __init__(self, language):
        super().__init__()

        self.language = tk.StringVar(value=language)
        self.translations = get_translations(self.language.get())
        self.title("Delivery and Trading System - Make It Easy")
        self.geometry("800x600")
        center_window(self)

        self.init_ui()

    def init_ui(self):
        # Menü çubuğu
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        # Dil seçimi
        lang_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label=self.translations["language"], menu=lang_menu)
        lang_menu.add_command(label="English", command=lambda: self.update_language("en"))
        lang_menu.add_command(label="Türkçe", command=lambda: self.update_language("tr"))
        lang_menu.add_command(label="한국어", command=lambda: self.update_language("ko"))

        # Menü seçenekleri
        app_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label=self.translations["menu_settings"], menu=app_menu)
        app_menu.add_command(label=self.translations["menu_help"], command=self.show_help)
        app_menu.add_separator()
        app_menu.add_command(label=self.translations["menu_exit"], command=self.quit)

        # Ana menü düğmeleri
        buttons_frame = ttk.Frame(self, padding="10")
        buttons_frame.pack(expand=True)

        ttk.Label(buttons_frame, text=self.translations["app_welcome"], font=("Arial", 18)).pack(pady=10)

        self.add_button(buttons_frame, self.translations["online_shop"], self.open_online_shop)
        self.add_button(buttons_frame, self.translations["trading_system"], self.open_trading_system)
        self.add_button(buttons_frame, self.translations["real_time_tracking"], self.open_tracking_system)
        self.add_button(buttons_frame, self.translations["discount_notifications"], self.open_discount_notifications)
        self.add_button(buttons_frame, self.translations["chat_system"], self.open_chat_system)
        self.add_button(buttons_frame, self.translations["ratings"], self.open_ratings)
        self.add_button(buttons_frame, self.translations["customize_interface"], self.open_customize_interface)

    def add_button(self, frame, text, command):
        ttk.Button(frame, text=text, command=command, width=30).pack(pady=5)

    def update_language(self, lang):
        self.language.set(lang)

        self.translations = get_translations(lang)

        self.refresh_ui()

    def refresh_ui(self):
        for widget in self.winfo_children():
            widget.destroy()
        self.init_ui()

    # Placeholder methods for functionalities
    def open_online_shop(self):
        messagebox.showinfo(self.translations["online_shop"], self.translations["feature_under_construction"])

    def open_trading_system(self):
        messagebox.showinfo(self.translations["trading_system"], self.translations["feature_under_construction"])

    def open_tracking_system(self):
        messagebox.showinfo(self.translations["real_time_tracking"], self.translations["feature_under_construction"])

    def open_discount_notifications(self):
        messagebox.showinfo(self.translations["discount_notifications"], self.translations["feature_under_construction"])

    def open_chat_system(self):
        messagebox.showinfo(self.translations["chat_system"], self.translations["feature_under_construction"])

    def open_ratings(self):
        messagebox.showinfo(self.translations["ratings"], self.translations["feature_under_construction"])

    def open_customize_interface(self):
        messagebox.showinfo(self.translations["customize_interface"], self.translations["feature_under_construction"])

    def show_help(self):
        messagebox.showinfo(self.translations["menu_help"], "This is a placeholder for the Help menu.")

if __name__ == "__main__":
    login_screen = LoginScreen()
    login_screen.mainloop()
