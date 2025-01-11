import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import os

# Kullanıcı verilerini ve ürünleri depolamak için basit bir dosya tabanlı sistem
users_file = "users.txt"
products_file = "products.txt"

def load_users():
    if not os.path.exists(users_file):
        with open(users_file, "w") as f:
            pass
    with open(users_file, "r") as f:
        return {line.strip().split(":")[0]: line.strip().split(":") for line in f if line.strip()}

def save_user(username, password, language):
    with open(users_file, "a") as f:
        f.write(f"{username}:{password}:{language}\n")

def load_products():
    if not os.path.exists(products_file):
        with open(products_file, "w") as f:
            pass
    with open(products_file, "r") as f:
        return [line.strip().split(":") for line in f if line.strip()]

def save_product(product_name, product_price, product_image, seller):
    with open(products_file, "a") as f:
        f.write(f"{product_name}:{product_price}:{product_image}:{seller}\n")

# Dil çevirilerini almak için yardımcı fonksiyon
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

        ttk.Label(self, text=self.translations["language"]).pack(pady=5)
        lang_menu = ttk.OptionMenu(self, self.language, self.language.get(), "en", "tr", "ko", command=self.update_language)
        lang_menu.pack(pady=5)

        ttk.Label(self, text=self.translations["username"]).pack(pady=5)
        self.username_entry = ttk.Entry(self)
        self.username_entry.pack(pady=5)

        ttk.Label(self, text=self.translations["password"]).pack(pady=5)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

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
            app = DeliveryTradingApp(username)
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
    def __init__(self, username):
        super().__init__()

        self.username = username
        self.language = "en"
        self.translations = get_translations(self.language)
        self.geometry("800x600")
        center_window(self)

        self.title("Delivery and Trading System")
        self.init_ui()

    def init_ui(self):
        menu_bar = tk.Menu(self)
        self.config(menu=menu_bar)

        shop_menu = tk.Menu(menu_bar, tearoff=0)
        menu_bar.add_cascade(label=self.translations["menu_settings"], menu=shop_menu)
        shop_menu.add_command(label=self.translations["online_shop"], command=self.open_online_shop)
        shop_menu.add_separator()
        shop_menu.add_command(label=self.translations["menu_exit"], command=self.quit)

        ttk.Label(self, text=f"Welcome, {self.username}!", font=("Arial", 18)).pack(pady=20)

    def open_online_shop(self):
        OnlineShop(self.username).grab_set()

# Online Shopping arayüzü
class OnlineShop(tk.Toplevel):
    def __init__(self, username):
        super().__init__()

        self.username = username
        self.geometry("600x600")
        center_window(self)

        self.title("Online Shop")
        self.products = load_products()
        self.init_ui()

    def init_ui(self):
        add_frame = ttk.LabelFrame(self, text="Add Product", padding="10")
        add_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(add_frame, text="Product Name:").grid(row=0, column=0, pady=5, sticky="w")
        self.product_name_entry = ttk.Entry(add_frame)
        self.product_name_entry.grid(row=0, column=1, pady=5)

        ttk.Label(add_frame, text="Product Price:").grid(row=1, column=0, pady=5, sticky="w")
        self.product_price_entry = ttk.Entry(add_frame)
        self.product_price_entry.grid(row=1, column=1, pady=5)

        ttk.Label(add_frame, text="Product Image:").grid(row=2, column=0, pady=5, sticky="w")
        self.product_image_path = tk.StringVar()
        self.product_image_entry = ttk.Entry(add_frame, textvariable=self.product_image_path, state="readonly")
        self.product_image_entry.grid(row=2, column=1, pady=5)

        select_image_button = ttk.Button(add_frame, text="Select Image", command=self.select_image)
        select_image_button.grid(row=2, column=2, pady=5, padx=5)

        add_product_button = ttk.Button(add_frame, text="Add Product", command=self.add_product)
        add_product_button.grid(row=3, column=1, pady=10)

        self.product_list = ttk.Treeview(self, columns=("Name", "Price", "Seller"), show="headings")
        self.product_list.heading("Name", text="Product Name")
        self.product_list.heading("Price", text="Price")
        self.product_list.heading("Seller", text="Seller")
        self.product_list.pack(fill="both", expand=True, padx=10, pady=5)

        self.load_products_to_list()

    def select_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.product_image_path.set(file_path)

    def add_product(self):
        product_name = self.product_name_entry.get()
        product_price = self.product_price_entry.get()
        product_image = self.product_image_path.get()

        if not product_name or not product_price or not product_image:
            messagebox.showerror("Error", "All fields are required!")
            return

        save_product(product_name, product_price, product_image, self.username)
        self.products.append([product_name, product_price, product_image, self.username])
        self.load_products_to_list()
        messagebox.showinfo("Success", "Product added successfully!")

    def load_products_to_list(self):
        for row in self.product_list.get_children():
            self.product_list.delete(row)

        for product in self.products:
            self.product_list.insert("", "end", values=(product[0], product[1], product[3]))

if __name__ == "__main__":
    LoginScreen().mainloop()