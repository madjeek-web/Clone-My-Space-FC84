import tkinter as tk  
import requests  # Make sure to install this library with 'pip install requests'

# Login function  
def login():
    username = entry_username.get()
    password = entry_password.get()
    
    # Make a POST request to the PHP server  
    try:
        response = requests.post('http://your-site.com/api/login', json={'username': username, 'password': password})
        
        if response.status_code == 200:
            # Successful login  
            print("Login successful!")
            label_message.config(text="Login successful!", fg="green")
            # Here, you can continue with the application, for example:
            # open_main_page()
        else:
            # Error handling  
            print("Incorrect username or password.")
            label_message.config(text="Incorrect username or password.", fg="red")
            
    except requests.exceptions.RequestException as e:
        # Connection error handling  
        print(f"Error connecting to the server: {e}")
        label_message.config(text="Error connecting to the server. Please try again.", fg="red")

# Create the main window  
root = tk.Tk()
root.title("Clone My Space")  # Application title

# Frame to center the content  
frame = tk.Frame(root)  
frame.pack(pady=50)  # Adds vertical spacing

# H1 Title  
title_label = tk.Label(frame, text="Clone My Space", font=("Helvetica", 24, "bold"))  # Larger title  
title_label.pack(pady=10)  # Adds spacing around the title

# Create the input fields  
label_username = tk.Label(frame, text="Username:", font=("Helvetica", 14))  # Increased text size  
label_username.pack()

entry_username = tk.Entry(frame, font=("Helvetica", 14))  # Increased text size  
entry_username.pack(pady=5)

label_password = tk.Label(frame, text="Password:", font=("Helvetica", 14))  # Increased text size  
label_password.pack()

entry_password = tk.Entry(frame, show="*", font=("Helvetica", 14))  # Increased text size  
entry_password.pack(pady=5)

# Login button  
btn_login = tk.Button(frame, text="Log In", command=login, font=("Helvetica", 14))  # Increased text size  
btn_login.pack(pady=10)

# Label to display messages  
label_message = tk.Label(frame, text="", font=("Helvetica", 14))
label_message.pack()

# Start the main loop of the application  
root.mainloop()