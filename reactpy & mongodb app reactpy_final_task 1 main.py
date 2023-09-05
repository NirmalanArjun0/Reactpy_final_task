# Import necessary libraries
from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, html, use_state
from pymongo import MongoClient
from pymongo.server_api import ServerApi
import smtplib
import random

# Create a FastAPI app
app = FastAPI()

# MongoDB connection URI
uri = "mongodb+srv://Reactpy2:arjun123@cluster0.y8gowmd.mongodb.net/"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi("1"))

# Create or access the database and collection
DB = client["Reactpy2"]
collection = DB["reactpy2"]

# Check if the connection to MongoDB is successful
try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

# Define a component for application
@component
def MyCrud():
    # Creating state for various form fields and elements
    alltodo = use_state([])
    First_name, set_First_name = use_state("")
    Last_name, set_Last_name = use_state("")
    Username, set_Username = use_state("")
    Email, set_Email = use_state("")
    Contact_number, set_Contact_number = use_state("")
    password, set_password = use_state("")
    Confirm_password, set_Confirm_password = use_state("")
    show_password, set_show_password = use_state(False)
    save_password, set_save_password = use_state(False)
    save_username, set_save_username = use_state(False)
    forgot_password_email, set_forgot_password_email = use_state("")
    otp_input, set_otp_input = use_state("")
    done_button_click, set_done_button_click = use_state("")

    # Generate and send OTP via email
    otp_sent = False
    generated_otp = ""

    def send_otp():
        nonlocal generated_otp
        generated_otp = str(random.randint(1000, 9999))  # Generate a 4-digit OTP

        # Send the OTP via email 
        sender_email = "your_email@gmail.com"
        sender_password = "your_email_password"
        recipient_email = Email.value
        subject = "Your OTP"
        message = f"Your OTP is: {generated_otp}"

        try:
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, f"Subject: {subject}\n\n{message}")
            server.quit()
            print("OTP sent successfully.")
            set_otp_input("")  
        except Exception as e:
            print(f"Failed to send OTP: {e}")

    def verify_otp():
        entered_otp = otp_input.value

        if entered_otp == generated_otp:
            print("OTP verified successfully.")
            # create an account or log in here
        else:
            print("Invalid OTP. Please try again.")

    def mysubmit(event):
        newtodo = {
            "First_name": First_name,
            "Last_name": Last_name,
            "Username": Username,
            "Email": Email,
            "Contact_number": Contact_number,
            "password": password,
        }

        alltodo.set_value(alltodo.value + [newtodo])

        if save_password:
            # Implement saving password logic if checked
            pass

        # Login or create account logic here
        login(newtodo)

    def toggle_password_visibility():
        set_show_password(not show_password)

    def login_existing_account():
        # Implement login logic here
        pass

    def forgot_password():
        
        print("Forgot Password: Email entered -", forgot_password_email)

    return html.div(
        {"style": {
            "padding": "50px",
            "background_image": "url(https://arjun000.neocities.org/dotliveblogbackground-k8mxvyu049.jpg)",
            "background_position": "center",
            "background_size": "cover",
            "margin": "0px",
            "min-height": "700px",
            "min-width": "700px",
            "display": "flex",
            "justify-content": "center",
            "align-items": "center",
        }},
        html.form(
            {"on_submit": mysubmit, "style": {"width": "40%"}},
            html.b(html.h1(
                {"style": {"font-family": "Arial", "font-size": "32px", "color": "LightGreen", "font-weight": "bold"}},
                "ReactPy & Mongodb")),
            html.br(),
            html.b(html.h2(
                {"style": {"font-family": "Arial", "font-size": "20px", "color": "White", "font-weight": "bold"}},
                "Don't have an account - Sign-Up")),
            html.label(
                {"style": {"font-family": "Arial", "font-size": "16px", "color": "#e6fffa", "font-weight": "bold"}},
                "First name"),
            html.br(),
            html.input(
                {
                    "type": "text",
                    "placeholder": "First name",
                    "on_change": lambda event: set_First_name(event["target"]["value"]),
                    "style": {
                        "font-family": "Time New Roman",
                        "font-size": "16px",
                        "font-color": "Azure",
                        "padding": "5px 5px",
                        "border": "2px solid #ccc",
                        "border-radius": "10px",
                        "margin": "5px auto",
                        "width": "70%",
                        "box-sizing": "border-box",
                        "outline": "none",
                        "font-weight": "bold"
                    }
                }),
            html.br(),
            html.label(
                {"style": {"font-family": "Arial", "font-size": "16px", "color": "#e6fffa", "font-weight": "bold"}},
                "Last name"),
            html.br(),
            html.input(
                {
                    "type": "text",
                    "placeholder": "Last name",
                    "on_change": lambda event: set_Last_name(event["target"]["value"]),
                    "style": {
                        "font-family": "Time New Roman",
                        "font-size": "16px",
                        "padding": "5px 5px",
                        "border": "2px solid #ccc",
                        "border-radius": "10px",
                        "margin": "5px auto",
                        "width": "70%",
                        "box-sizing": "border-box",
                        "background-color": "#f9f9f9",
                        "color": "#555",
                        "outline": "none",
                        "font-weight": "bold"
                    }
                }),
            html.br(),
            html.label(
                {"style": {"font-family": "Arial", "font-size": "16px", "color": "#e6fffa", "font-weight": "bold"}},
                "Username"),
            html.br(),
            html.input(
                {
                    "type": "text",
                    "placeholder": "Username",
                    "on_change": lambda event: set_Username(event["target"]["value"]),
                    "style": {
                        "font-family": "Time New Roman",
                        "font-size": "16px",
                        "padding": "5px 5px",
                        "border": "2px solid #ccc",
                        "border-radius": "10px",
                        "margin": "5px auto",
                        "width": "70%",
                        "box-sizing": "border-box",
                        "background-color": "#f9f9f9",
                        "color": "#555",
                        "outline": "none",
                        "font-weight": "bold"
                    }
                }),
            html.br(),
            html.label(
                {"style": {"font-family": "Arial", "font-size": "16px", "color": "#e6fffa", "font-weight": "bold"}},
                "Email"),
            html.br(),
            html.input(
                {
                    "type": "text",
                    "placeholder": "Email",
                    "on_change": lambda event: set_Email(event["target"]["value"]),
                    "style": {
                        "font-family": "Time New Roman",
                        "font-size": "16px",
                        "padding": "5px 5px",
                        "border": "2px solid #ccc",
                        "border-radius": "10px",
                        "margin": "5px auto",
                        "width": "70%",
                        "box-sizing": "border-box",
                        "background-color": "#f9f9f9",
                        "color": "#555",
                        "outline": "none",
                        "font-weight": "bold"
                    }
                }),
            html.br(),
            html.p(""),
            html.label(
                {"style": {"font-family": "Arial", "font-size": "16px", "color": "#e6fffa", "font-weight": "bold"}},
                "Password"),
            html.br(),
            html.div(
                {"style": {"position": "relative"}},
                html.input(
                    {
                        "type": "password" if not show_password else "text",
                        "placeholder": "Password",
                        "value": password,
                        "on_change": lambda event: set_password(event["target"]["value"]),
                        "style": {
                            "font-family": "Time New Roman",
                            "font-size": "16px",
                            "padding": "5px 5px",
                            "border": "2px solid #ccc",
                            "border-radius": "10px",
                            "margin": "2px auto",
                            "width": "70%",
                            "box-sizing": "border-box",
                            "background-color": "#f9f9f9",
                            "color": "#555",
                            "outline": "none",
                            "font-weight": "bold"
                        }
                    }),
                html.div(
                    {"class": "password-toggle-icon", "on_click": toggle_password_visibility},
                    "👁️",
                ),
            ),
            html.br(),
            html.label(
                {"style": {"font-family": "Arial", "font-size": "16px", "color": "#e6fffa", "font-weight": "bold"}},
                "Confirm Password",
            ),
            html.br(),
            html.input(
                {
                    "type": "password",
                    "placeholder": "Confirm Password",
                    "value": Confirm_password,
                    "on_change": lambda event: set_Confirm_password(event["target"]["value"]),
                    "style": {
                        "font-family": "Time New Roman",
                        "font-size": "16px",
                        "padding": "5px 5px",
                        "border": "2px solid #ccc",
                        "border-radius": "10px",
                        "margin": "5px auto",
                        "width": "70%",
                        "box-sizing": "border-box",
                        "background-color": "#f9f9f9",
                        "color": "#555",
                        "outline": "none",
                        "font-weight": "bold"
                    }
                },
            ),
            html.br(),
            html.p(""),
            html.label(
                {"style": {"font-family": "Arial", "font-size": "16px", "color": "#e6fffa", "font-weight": "bold"}},
                "Save Password",
            ),
            html.input(
                {
                    "type": "checkbox",
                    "on_change": lambda event: set_save_password(event["target"]["checked"]),
                    "style": {
                        "margin": "2px 2px",
                    }
                },
            ),
            html.br(),
            html.p(""),
            html.label(
                {"style": {"font-family": "Arial", "font-size": "16px", "color": "#e6fffa", "font-weight": "bold"}},
                "Save Username",
            ),
            html.input(
                {
                    "type": "checkbox",
                    "on_change": lambda event: set_save_username(event["target"]["checked"]),
                    "style": {
                        "margin": "2px 2px",
                    }
                },
            ),
            html.br(),
            html.br(),
            html.label(
                {"style": {"font-family": "Arial", "font-size": "16px", "color": "#e6fffa", "font-weight": "bold"}},
                "Contact Number"),
            html.br(),
            html.input(
                {
                   
                    "type": "text",
                    "placeholder": "Contact Number",
                    "on_change": lambda event: set_Contact_number(event["target"]["value"]),
                    "style": {
                        "font-family": "Time New Roman",
                        "font-size": "16px",
                        "padding": "5px 5px",
                        "border": "2px solid #ccc",
                        "border-radius": "10px",
                        "margin": "2px auto",
                        "width": "70%",
                        "box-sizing": "border-box",
                        "background-color": "#f9f9f9",
                        "color": "#555",
                        "outline": "none",
                        "font-weight": "bold"
                    }
                }),
            html.br(),
           
            html.button(
            {
                "type": "button",
                "on_click": lambda event: done_button_click(),  
                "style": {
                    "font-family": "Time New Roman",
                    "font-size": "18px",
                    "padding": "2px 2px",
                    "border": "3px solid #ccc",
                    "border-radius": "10px",
                    "margin": "2px auto",
                    "width": "12%",
                    "box-sizing": "border-box",
                    "background-color": "lightblue",
                    "color": "black",
                    "text-shadow": "0 0 1px black",
                    "outline": "none",
                    "font-weight": "bold"
                }
            },
            "Done",
            ),
            html.br(),
            html.br(),# Add OTP input field and buttons           
            html.label(
                {"style": {"font-family": "Arial", "font-size": "16px", "color": "#e6fffa", "font-weight": "bold"}},
                "OTP",
            ),
            html.br(),
            html.input(
                {
                    "type": "text",
                    "placeholder": "Enter OTP",
                    "value": otp_input,
                    "on_change": lambda event: set_otp_input(event["target"]["value"]),
                    "style": {
                        "font-family": "Time New Roman",
                        "font-size": "16px",
                        "padding": "5px 5px",
                        "border": "2px solid #ccc",
                        "border-radius": "10px",
                        "margin": "5px auto",
                        "width": "70%",
                        "box-sizing": "border-box",
                        "background-color": "#f9f9f9",
                        "color": "#555",
                        "outline": "none",
                        "font-weight": "bold"
                    }
                },
            ),
            html.br(),
            html.p(""),
            html.button(
                {
                    "type": "submit",
                    "on_click": lambda event: mysubmit(event),
                    "style": {
                        "font-family": "Time New Roman",
                        "font-size": "18px",
                        "padding": "2px 2px",
                        "border": "3px solid #ccc",
                        "border-radius": "10px",
                        "margin": "2px auto",
                        "width": "70%",
                        "box-sizing": "border-box",
                        "background-color": "lightgreen",
                        "color": "black",
                        "text-shadow": "0 0 1px black",
                        "outline": "none",
                        "font-weight": "bold"
                    }
                },
                "Create an Account",
            ),
            html.br(),
            html.button(
                {
                    "type": "reset",
                    "on_click": lambda event: set_First_name("") and set_Last_name("") and set_Email("") and set_password("") and set_Username("") and set_Confirm_password(""),
                    "style": {
                        "font-family": "Time New Roman",
                        "font-size": "18px",
                        "padding": "2px 2px",
                        "border": "3px solid #ccc",
                        "border-radius": "10px",
                        "margin": "2px auto",
                        "width": "70%",
                        "box-sizing": "border-box",
                        "background-color": "lightgreen",
                        "color": "black",
                        "text-shadow": "0 0 1px black",
                        "outline": "none",
                        "font-weight": "bold"
                    }
                },
                "Reset",
            ),
            html.p(" "),
            html.div(
                {"style": {
                    "display": "flex",
                    "align-items": "center",
                    "justify-content": "flex-start",
                    "font-family": "Arial",
                    "font-size": "20px",
                    "color": "white",
                    "font-weight": "bold"
                }},
                " Already have an account? "
            ),
            html.p(" "),
            html.button(
                {
                    "type": "button",
                    "on_click": lambda event: login_existing_account(),
                    "style": {
                        "font-family": "Time New Roman",
                        "font-size": "18px",
                        "padding": "2px 2px",
                        "border": "3px solid #ccc",
                        "border-radius": "10px",
                        "margin": "2px auto",
                        "width": "70%",
                        "box-sizing": "border-box",
                        "background-color": "lightgreen",
                        "color": "black",
                        "text-shadow": "0 0 1px black",
                        "outline": "none",
                        "font-weight": "bold"
                    }
                },
                "Login with Existing Account",
            ),
            html.button(
    {
        "type": "button",
        "on_click": lambda event: forgot_password(),
        "style": {
            "font-family": "Time New Roman",
            "font-size": "18px",
            "padding": "2px 2px",
            "border": "3px solid #ccc",
            "border-radius": "10px",
            "margin": "2px auto",
            "width": "70%",
            "box-sizing": "border-box",
            "background-color": "lightgreen",
            "color": "black",
            "text-shadow": "0 0 1px black",
            "outline": "none",
            "font-weight": "bold"
        }
    },
    "Forgot Password",
),
# Adding the "Enter Your Email" input field inside the "Forgot Password" button
html.div(
    {"style": {"margin-top": "10px", "display": "none"}, "id": "forgot-password-div"},
    html.label(
        {"style": {"font-family": "Arial", "font-size": "16px", "color": "#e6fffa", "font-weight": "bold"}},
        "Enter Your Email",
    ),
    html.input(
        {
            "type": "text",
            "placeholder": "Email",
            "on_change": lambda event: set_forgot_password_email(event["target"]["value"]),
            "style": {
                "font-family": "Time New Roman",
                "font-size": "16px",
                "padding": "5px 5px",
                "border": "2px solid #ccc",
                "border-radius": "10px",
                "margin": "5px auto",
                "width": "70%",
                "box-sizing": "border-box",
                "background-color": "#f9f9f9",
                "color": "#555",
                "outline": "none",
                "font-weight": "bold"
            }
        },
    ),
            html.br(),
            html.button(
                {
                    "type": "button",
                    "on_click": lambda event: send_otp(),
                    "style": {
                        "font-family": "Time New Roman",
                        "font-size": "18px",
                        "padding": "2px 2px",
                        "border": "3px solid #ccc",
                        "border-radius": "10px",
                        "margin": "2px auto",
                        "width": "70%",
                        "box-sizing": "border-box",
                        "background-color": "lightgreen",
                        "color": "black",
                        "text-shadow": "0 0 1px black",
                        "outline": "none",
                        "font-weight": "bold"
                    }
                },
                "Send OTP",
            ),
            html.button(
                {
                    "type": "button",
                    "on_click": lambda event: verify_otp(),
                    "style": {
                        "font-family": "Time New Roman",
                        "font-size": "18px",
                        "padding": "2px 2px",
                        "border": "3px solid #ccc",
                        "border-radius": "10px",
                        "margin": "2px auto",
                        "width": "70%",
                        "box-sizing": "border-box",
                        "background-color": "lightgreen",
                        "color": "black",
                        "text-shadow": "0 0 1px black",
                        "outline": "none",
                        "font-weight": "bold"
                    }
                },
                "Verify OTP",
            ),
),
            
            html.div(
                {"style": {
                    "display": "flex",
                    "justify-content": "flex-start",
                    "align-items": "center",
                    "margin-top": "20px",
                }},
                html.a(
                    {"href": "https://twitter.com/i/flow/login?redirect_after_login=%2FMongoDB/", "target": "_blank","class": "social-media-icon"},
                    html.img(
                        {"src": "https://arjun000.neocities.org/twitter.jpg", "width": "25px", "height": "25px"},
                    ),
                ),
                html.div({"style": {"width": "2mm"}}),
                html.a(
                    {"href": "https://www.linkedin.com/company/mongodbinc", "target": "_blank",  "class": "social-media-icon"},
                    html.img(
                        {"src": "https://arjun000.neocities.org/linkedin.jpg", "width": "25px", "height": "25px"},
                    ),
                ),
                html.div({"style": {"width": "2mm"}}),
                html.a(
                    {"href": "https://www.instagram.com/mongodb/", "target": "_blank",  "class": "social-media-icon"},
                    html.img(
                        {"src": "https://arjun000.neocities.org/instagram.jpg", "width": "25px", "height": "25px"},
                    ),
                ),
                html.div({"style": {"width": "2mm"}}),
                html.a(
                    {"href": "https://www.facebook.com/MongoDB/", "target": "_blank","class": "social-media-icon"},
                    html.img(
                        {"src": "https://arjun000.neocities.org/fb.jpg", "width": "25px", "height": "25px"},
                    ),
                ),
            ),
        ),
        html.ul(alltodo.value),
    )

app = FastAPI()

uri = "mongodb+srv://Reactpy2:arjun123@cluster0.y8gowmd.mongodb.net/"
client = MongoClient(uri, server_api=ServerApi("1"))
DB = client["Reactpy2"]
collection = DB["reactpy2"]

try:
    client.admin.command("ping")
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

def login(login_data: dict):
    First_name = login_data["First_name"]
    Last_name = login_data["Last_name"]
    Username = login_data["Username"]
    Email = login_data["Email"]
    Contact_number = login_data["Contact_number"]
    password = login_data["password"]

    document = {"First_name": First_name, "Last_name": Last_name, "Username": Username, "Email": Email, "Contact_number": Contact_number, "password": password}
    
    post_id = collection.insert_one(document).inserted_id

    return {"message": "Account created successfully"}

configure(app, MyCrud)
