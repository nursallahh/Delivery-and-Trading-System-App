import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog

class TradeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("MakeItEasy")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        self.language = "English"
        self.user_logged_in = False
        self.user_data = {}
        self.forward_stack = []
        self.history = []
        self.current_view = None
        self.products = []  # List to hold product data
        self.sample_users = ["John", "Emily", "Sarah", "Mike", "Anna"]
        self.coupons = {"Gaming Mouse": "SAVE10", "Organic Honey": "HONEY5"}

        # Styling and layout
        self.root.configure(bg="#f7f7f7")

        header_frame = tk.Frame(self.root, bg="#4CAF50", height=50)
        header_frame.pack(fill="x", side="top")
        header_label = tk.Label(header_frame, text="MakeItEasy", fg="white", bg="#4CAF50", font=("Arial", 18))
        header_label.pack(pady=10)

        self.main_frame = tk.Frame(self.root, bg="#f7f7f7")
        self.main_frame.pack(fill="both", expand=True)

        self.nav_frame = tk.Frame(self.main_frame, bg="#e0e0e0")
        self.nav_frame.pack(side="left", fill="y")

        self.content_frame = tk.Frame(self.main_frame, bg="#ffffff", relief="solid", bd=1)
        self.content_frame.pack(side="right", fill="both", expand=True)

        # Navigation buttons
        self.buttons = [
            ("Home", self.show_home),
            ("Market", self.show_market),
            ("Add Product", self.show_add_product),
            ("Chat", self.show_chat),
            ("Profile", self.show_profile),
            ("Trade", self.show_trade),
            ("Discounts", self.show_discounts)
        ]

        for btn_text, btn_command in self.buttons:
            btn = tk.Button(self.nav_frame, text=btn_text, bg="#f0f0f0", fg="#000", font=("Arial", 12), command=btn_command, relief="flat")
            btn.pack(pady=5, padx=10, fill="x")

        tk.Button(self.root, text="Back", command=self.go_back, bg="#d32f2f", fg="white", font=("Arial", 12)).pack(side="left", padx=10, pady=5)
        tk.Button(self.root, text="Forward", command=self.go_forward, bg="#1976d2", fg="white", font=("Arial", 12)).pack(side="right", padx=10, pady=5)

        self.show_home()

    def set_language(self, lang):
        self.language = lang
        messagebox.showinfo("Language Set", f"Language changed to {lang}.")
        self.refresh_language()

    def refresh_language(self):
        # Adjust language-specific texts here
        self.show_home()

    def show_home(self):
        self._update_view("home", "Welcome to MakeItEasy!", "#ffffff")
        tk.Label(self.content_frame, text="MakeItEasy - Simplifying Trades!", font=("Arial", 16), bg="#ffffff").pack(pady=20)

        if not self.user_logged_in:
            tk.Label(self.content_frame, text="Login or Sign up to continue:", font=("Arial", 12), bg="#ffffff").pack(pady=10)
            tk.Button(self.content_frame, text="Login", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.login).pack(pady=5)
            tk.Button(self.content_frame, text="Sign Up", font=("Arial", 12), bg="#2196F3", fg="white", command=self.sign_up).pack(pady=5)
            tk.Button(self.content_frame, text="Language Settings", font=("Arial", 12), bg="#FF9800", fg="white", command=self.language_settings).pack(pady=10)
        else:
            tk.Label(self.content_frame, text="Welcome back to MakeItEasy!", font=("Arial", 12), bg="#ffffff").pack(pady=20)

    def login(self):
        if "username" in self.user_data:
            self.user_logged_in = True
            messagebox.showinfo("Login", f"Welcome back {self.user_data['username']}!")
            self.show_market()
        else:
            messagebox.showerror("Login Failed", "No account found. Please sign up.")

    def sign_up(self):
        self._update_view("sign_up", "Sign Up", "#ffffff")

        tk.Label(self.content_frame, text="Create Account", font=("Arial", 14), bg="#ffffff").pack(pady=10)
        tk.Label(self.content_frame, text="Username:", font=("Arial", 12), bg="#ffffff").pack(pady=5)
        username = tk.Entry(self.content_frame, font=("Arial", 12))
        username.pack(pady=5)

        tk.Label(self.content_frame, text="Password:", font=("Arial", 12), bg="#ffffff").pack(pady=5)
        password = tk.Entry(self.content_frame, show="*", font=("Arial", 12))
        password.pack(pady=5)

        tk.Button(self.content_frame, text="Register", font=("Arial", 12), bg="#4CAF50", fg="white", command=lambda: self.save_user(username.get(), password.get())).pack(pady=10)

    def save_user(self, username, password):
        if username and password:
            self.user_data = {"username": username, "password": password}
            messagebox.showinfo("Success", "Account created successfully!")
            self.login()
        else:
            messagebox.showerror("Error", "Please fill in all fields.")

    def language_settings(self):
        self._update_view("language_settings", "Language Settings", "#ffffff")

        tk.Label(self.content_frame, text="Choose Language:", font=("Arial", 14), bg="#ffffff").pack(pady=10)

        tk.Button(self.content_frame, text="English", font=("Arial", 12), bg="#2196F3", fg="white", command=lambda: self.set_language("English")).pack(pady=5)
        tk.Button(self.content_frame, text="Turkish", font=("Arial", 12), bg="#4CAF50", fg="white", command=lambda: self.set_language("Turkish")).pack(pady=5)
        tk.Button(self.content_frame, text="Korean", font=("Arial", 12), bg="#FFC107", fg="white", command=lambda: self.set_language("Korean")).pack(pady=5)

    def show_market(self):
        self._update_view("market", "Marketplace", "#ffffff")

        if not self.products:
            tk.Label(self.content_frame, text="No products available.", font=("Arial", 12), bg="#ffffff").pack(pady=10)
        else:
            for product in self.products[:15]:  # Limit to 15 products per page
                product_frame = tk.Frame(self.content_frame, bg="#f9f9f9", relief="solid", bd=1)
                product_frame.pack(pady=5, padx=10, fill="x")

                tk.Label(product_frame, text=f"{product['name']} - {product['price']}", font=("Arial", 12), bg="#f9f9f9").pack(side="left", padx=10)
                tk.Label(product_frame, text=f"Seller: {product['seller']} | {product['status']}", font=("Arial", 10), bg="#f9f9f9").pack(side="right", padx=10)

                product_frame.bind("<Button-1>", lambda e, p=product: self.show_product_details(p))

    def show_product_details(self, product):
        self._update_view("product_details", product["name"], "#ffffff")
        tk.Label(self.content_frame, text=f"Name: {product['name']}", font=("Arial", 12), bg="#ffffff").pack(pady=10)
        tk.Label(self.content_frame, text=f"Price: {product['price']}", font=("Arial", 12), bg="#ffffff").pack(pady=10)
        tk.Label(self.content_frame, text=f"Seller: {product['seller']}", font=("Arial", 12), bg="#ffffff").pack(pady=10)
        tk.Label(self.content_frame, text=f"Rating: {product['rating']}", font=("Arial", 12), bg="#ffffff").pack(pady=10)

    def show_add_product(self):
        self._update_view("add_product", "Add Product", "#ffffff")

        tk.Label(self.content_frame, text="Add New Product", font=("Arial", 14), bg="#ffffff").pack(pady=10)
        tk.Label(self.content_frame, text="Name:", font=("Arial", 12), bg="#ffffff").pack(pady=5)
        name_entry = tk.Entry(self.content_frame, font=("Arial", 12))
        name_entry.pack(pady=5)

        tk.Label(self.content_frame, text="Price:", font=("Arial", 12), bg="#ffffff").pack(pady=5)
        price_entry = tk.Entry(self.content_frame, font=("Arial", 12))
        price_entry.pack(pady=5)

        tk.Label(self.content_frame, text="Seller:", font=("Arial", 12), bg="#ffffff").pack(pady=5)
        seller_entry = tk.Entry(self.content_frame, font=("Arial", 12))
        seller_entry.pack(pady=5)

        tk.Label(self.content_frame, text="Rating:", font=("Arial", 12), bg="#ffffff").pack(pady=5)
        rating_entry = tk.Entry(self.content_frame, font=("Arial", 12))
        rating_entry.pack(pady=5)

        tk.Button(self.content_frame, text="Add Product", font=("Arial", 12), bg="#4CAF50", fg="white", 
                  command=lambda: self.add_product_to_market(
                      name_entry.get(), price_entry.get(), seller_entry.get(), rating_entry.get()
                  )).pack(pady=10)

    def show_trade(self):
        self._update_view("trade", "Trade Products", "#ffffff")
        tk.Label(self.content_frame, text="Trade your products easily!", font=("Arial", 14), bg="#ffffff").pack(pady=10)
        tk.Label(self.content_frame, text="Specify Categories:", font=("Arial", 12), bg="#ffffff").pack(pady=5)
        category_entry = tk.Entry(self.content_frame, font=("Arial", 12))
        category_entry.pack(pady=5)
        tk.Button(self.content_frame, text="Submit", font=("Arial", 12), bg="#4CAF50", fg="white", command=lambda: messagebox.showinfo("Trade", f"Category: {category_entry.get()} added for trade."))

    def show_discounts(self):
        self._update_view("discounts", "Weekly Discounts", "#ffffff")
        tk.Label(self.content_frame, text="Check out this week's discounts!", font=("Arial", 14), bg="#ffffff").pack(pady=10)
        for product, code in self.coupons.items():
            tk.Label(self.content_frame, text=f"{product}: Use code {code}", font=("Arial", 12), bg="#ffffff").pack(pady=5)

    def show_chat(self):
        self._update_view("chat", "Chat with Traders", "#ffffff")
        tk.Label(self.content_frame, text="Chat Box", font=("Arial", 14), bg="#ffffff").pack(pady=10)
        for user in self.sample_users:
            tk.Label(self.content_frame, text=f"Chat with {user}", font=("Arial", 12), bg="#ffffff").pack(pady=5)

    def show_profile(self):
        self._update_view("profile", "User Profile", "#ffffff")
        tk.Label(self.content_frame, text="Manage your profile here.", font=("Arial", 14), bg="#ffffff").pack(pady=10)

    def go_back(self):
        if len(self.history) > 1:
            self.forward_stack.append(self.history.pop())
            self.current_view = self.history[-1]
            self._update_view_from_history(self.current_view)

    def go_forward(self):
        if self.forward_stack:
            self.current_view = self.forward_stack.pop()
            self.history.append(self.current_view)
            self._update_view_from_history(self.current_view)

    def _update_view(self, view_name, title, bg):
        if self.current_view:
            self.history.append(self.current_view)

        self.current_view = view_name
        self.forward_stack.clear()

        for widget in self.content_frame.winfo_children():
            widget.destroy()

        self.content_frame.configure(bg=bg)
        tk.Label(self.content_frame, text=title, font=("Arial", 16), bg=bg).pack(pady=20)

    def _update_view_from_history(self, view_name):
        if view_name == "home":
            self.show_home()
        elif view_name == "market":
            self.show_market()
        elif view_name == "add_product":
            self.show_add_product()
        elif view_name == "chat":
            self.show_chat()
        elif view_name == "profile":
            self.show_profile()
        elif view_name == "trade":
            self.show_trade()
        elif view_name == "discounts":
            self.show_discounts()

if __name__ == "__main__":
    root = tk.Tk()
    app = TradeApp(root)
    root.mainloop()
