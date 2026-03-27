import tkinter as tk
from tkinter import ttk
import json
import webbrowser
from PIL import Image, ImageTk, ImageDraw
import os

# ----------------------------
# Train Image Screen (AFTER LOGIN)
# ----------------------------

def show_train_menu_screen():
    global train_menu_frame

    train_menu_frame = tk.Frame(root, bg="#f0f4ff")
    train_menu_frame.pack(fill="both", expand=True)

    # Top label "Platforms"
    platforms_label = tk.Label(
        train_menu_frame,
        text="Platforms",
        font=("Segoe UI", 18, "bold"),
        bg="#2c6bed",   # same blue as header
        fg="white",
        padx=20,
        pady=10
    )
    platforms_label.pack(fill="x", pady=(30, 20))

    # Red rounded-square button with train symbol, placed toward left
    btn_canvas = tk.Canvas(
        train_menu_frame,
        width=220,
        height=220,
        bg="#f0f4ff",
        highlightthickness=0,
        bd=0
    )
    btn_canvas.pack(anchor="w", padx=40, pady=20)

    # Draw rounded rectangle (red)
    x1, y1, x2, y2, r = 10, 10, 210, 210, 30
    btn_canvas.create_polygon(
        x1+r, y1,
        x2-r, y1,
        x2, y1,
        x2, y1+r,
        x2, y2-r,
        x2, y2,
        x2-r, y2,
        x1+r, y2,
        x1, y2,
        x1, y2-r,
        x1, y1+r,
        x1, y1,
        smooth=True,
        fill="#dc3545",  # red
        outline="#dc3545"
    )

    # Invisible button with train symbol on top
    train_button = tk.Button(
        train_menu_frame,
        text="🚆",
        font=("Segoe UI", 40, "bold"),
        fg="white",
        bg="#dc3545",
        activebackground="#c82333",
        activeforeground="white",
        bd=0,
        relief="flat",
        cursor="hand2",
        command=lambda: (train_menu_frame.destroy(), show_main_ui())
    )

    btn_canvas.create_window(
        (110, 110),
        window=train_button
    )

    info_label = tk.Label(
        train_menu_frame,
        text="Tap the Train to Continue",
        font=("Segoe UI", 12),
        bg="#f0f4ff",
        fg="#333333"
    )
    info_label.pack(side="bottom", pady=30)


# ----------------------------
# Login Screen
# ----------------------------

def show_login_screen():
    global login_frame

    login_frame = tk.Frame(root, bg="#f0f4ff")
    login_frame.pack(fill="both", expand=True)

    card = tk.Frame(login_frame, bg="white")
    card.place(relx=0.5, rely=0.5, anchor="center", width=400, height=480)

    tk.Label(card,
             text="Login to Continue",
             font=("Segoe UI", 16, "bold"),
             bg="white").pack(pady=15)

    tk.Label(card, text="Email:", bg="white").pack(anchor="w", padx=30)
    email_entry = tk.Entry(card, font=("Segoe UI", 11), bd=1, relief="solid")
    email_entry.pack(padx=30, pady=8, fill="x", ipady=6)

    tk.Label(card, text="Mobile Number:", bg="white").pack(anchor="w", padx=30)
    mobile_entry = tk.Entry(card, font=("Segoe UI", 11), bd=1, relief="solid")
    mobile_entry.pack(padx=30, pady=8, fill="x", ipady=6)

    status = tk.Label(card, text="", fg="red", bg="white", font=("Segoe UI", 9))
    status.pack()

    btn_box = tk.Frame(card, bg="#f7f9ff", bd=1, relief="solid")
    btn_box.pack(pady=20, padx=20, fill="x")

    def valid_email(email):
        return "@" in email and "." in email

    def valid_mobile(mobile):
        return mobile.isdigit() and len(mobile) == 10

    # AFTER LOGIN, GO TO TRAIN IMAGE PAGE
    def proceed():
        login_frame.destroy()
        show_train_menu_screen()

    def login_email():
        email = email_entry.get().strip()
        if not email:
            status.config(text="❌ Please enter email", fg="red")
        elif not valid_email(email):
            status.config(text="❌ Invalid email format", fg="red")
        else:
            status.config(text="✅ Email login success", fg="green")
            login_frame.after(800, proceed)

    def login_mobile():
        mobile = mobile_entry.get().strip()
        if not mobile:
            status.config(text="❌ Please enter mobile number", fg="red")
        elif not valid_mobile(mobile):
            status.config(text="❌ Must be 10 digits", fg="red")
        else:
            status.config(text="✅ Mobile login success", fg="green")
            login_frame.after(800, proceed)

    def login_apple():
        email = email_entry.get().strip()
        mobile = mobile_entry.get().strip()
        if not email and not mobile:
            status.config(text="❌ Enter email or mobile first", fg="red")
        else:
            status.config(text=" Apple login success (demo)", fg="green")
            login_frame.after(800, proceed)

    def create_btn(text, color, cmd):
        tk.Button(btn_box,
                  text=text,
                  command=cmd,
                  bg=color,
                  fg="white",
                  font=("Segoe UI", 10, "bold"),
                  bd=0,
                  pady=8,
                  cursor="hand2").pack(pady=8, padx=20, fill="x")

    create_btn("Login with Email", "#2c6bed", login_email)
    create_btn("Login with Mobile", "#28a745", login_mobile)

    tk.Button(btn_box,
              text=" Login with Apple",
              command=login_apple,
              bg="black",
              fg="white",
              font=("Segoe UI", 10, "bold"),
              bd=0,
              pady=8,
              cursor="hand2").pack(pady=10, padx=20, fill="x")


# ----------------------------
# Logo Screen
# ----------------------------

def show_logo_screen():
    global logo_frame

    logo_frame = tk.Frame(root, bg="#f0f4ff")
    logo_frame.pack(fill="both", expand=True)

    img = Image.open(r"C:\\Users\\ravut\\OneDrive\\Desktop\\project\\logo.png")
    img = img.resize((250, 250))
    logo = ImageTk.PhotoImage(img)

    logo_label = tk.Label(logo_frame, image=logo, bg="#f0f4ff")
    logo_label.image = logo
    logo_label.pack(expand=True)

    def go_to_login():
        logo_frame.destroy()
        show_login_screen()

    root.after(3000, go_to_login)


# ----------------------------
# Main UI (TRAIN BUTTONS PAGE)
# ----------------------------

def show_main_ui():
    header = tk.Frame(root, bg="#2c6bed", height=80)
    header.pack(fill="x")

    header.grid_columnconfigure(1, weight=1)

    logo_img = Image.open(r"C:\\Users\\ravut\\OneDrive\\Desktop\\project\\logo.png")
    logo_img = logo_img.resize((60, 60))

    mask = Image.new("L", (60, 60), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, 60, 60), fill=255)

    logo_circle = Image.new("RGBA", (60, 60))
    logo_circle.paste(logo_img, (0, 0), mask)

    logo_photo = ImageTk.PhotoImage(logo_circle)

    logo_label = tk.Label(header, image=logo_photo, bg="#2c6bed")
    logo_label.image = logo_photo
    logo_label.grid(row=0, column=0, padx=15, pady=10)

    title = tk.Label(header,
                     text="RailversX",
                     font=("Segoe UI", 20, "bold"),
                     bg="#2c6bed",
                     fg="white")
    title.grid(row=0, column=1, pady=20, sticky="w")

    container = tk.Frame(root, bg="white", bd=2, relief="ridge")
    container.pack(pady=20, padx=40, fill="both", expand=True)

    tk.Label(container,
             text="Enter Train Number (e.g., 12627)",
             font=("Segoe UI", 12, "bold"),
             bg="white").pack(pady=10)

    entry_frame = tk.Frame(container, bg="white")
    entry_frame.pack(pady=5)

    global entry
    entry = tk.Entry(entry_frame,
                     width=25,
                     font=("Segoe UI", 12),
                     bd=2,
                     relief="groove")
    entry.pack(side=tk.LEFT, padx=(0, 10))
    entry.insert(0, "12627")

    quick_btn = tk.Button(entry_frame,
                          text="Quick Load",
                          command=lambda: entry.delete(0, tk.END) or entry.insert(0, "12627"),
                          bg="#28a745", fg="white",
                          font=("Segoe UI", 10, "bold"),
                          bd=0, pady=5, padx=10)
    quick_btn.pack(side=tk.LEFT)

    def create_button(text, command, bg_color="#2c6bed"):
        btn = tk.Button(container,
                        text=text,
                        command=command,
                        width=28,
                        font=("Segoe UI", 11, "bold"),
                        bg=bg_color,
                        fg="white",
                        relief="solid",
                        bd=1,
                        pady=10,
                        cursor="hand2")
        btn.pack(pady=4)
        return btn

    create_button(" Train Schedule (PDF)", open_train_schedule_pdf, "#6f42c1")
    create_button(" Book Ticket (IRCTC)", open_irctc_booking, "#dc3545")
    create_button(" Get Official Train Schedule", open_official_schedule)
    create_button(" Live Train Map (Official)", open_live_map, "#007bff")
    create_button(" Real-Time Location (ConfirmTkt)", open_train_location, "#17a2b8")
    create_button(" Save Favorite Train", save_favorite, "#ffc107")
    create_button(" Load Favorite Train", load_favorite, "#ffc107")


# ----------------------------
# Functions
# ----------------------------

def open_train_schedule_pdf():
    webbrowser.open("https://contents.irctc.co.in/en/List_of_Special_Trains_by_Indian_Railways.pdf")

def open_irctc_booking():
    webbrowser.open("https://www.irctc.co.in/nget/train-search")

def open_official_schedule():
    train_no = entry.get().strip()
    if train_no.isdigit():
        webbrowser.open(f"https://www.indianrail.gov.in/enquiry/SCHEDULE/TrainSchedule.html?trainNo={train_no}")

def open_live_map():
    train_no = entry.get().strip()
    if train_no.isdigit():
        webbrowser.open(f"https://enquiry.indianrail.gov.in/mntes/queryTermT?trainNo={train_no}")

def open_train_location():
    train_no = entry.get().strip()
    if train_no.isdigit():
        webbrowser.open(f"https://www.confirmtkt.com/train-running-status/{train_no}")

def save_favorite():
    with open("favorites.json", "w") as f:
        json.dump({"favorite": entry.get()}, f)

def load_favorite():
    try:
        with open("favorites.json") as f:
            entry.insert(0, json.load(f)["favorite"])
    except:
        pass


# ----------------------------
# Start App
# ----------------------------

root = tk.Tk()
root.title(" platform")
root.geometry("900x800")
root.configure(bg="#f0f4ff")

show_logo_screen()

root.mainloop()
