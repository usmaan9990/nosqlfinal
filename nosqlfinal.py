from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, event, html, use_state
import reactpy as rp
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient

@component
def MyCurd(): # My app web page components
    # Creating state
    alltodo = use_state([])
    email, set_email = use_state("")
    password, set_password = use_state("")
    index, set_index = use_state("")
    gender, set_gender = use_state("")
    error_message, set_error_message = use_state("")
    
    def mysubmit(event):
        
        
        existing_index = collection.find_one({"index": index})
        if existing_index:
            set_error_message("Index Already Exist")
        else:
            set_error_message("Sucessfully Completed")
            newtodo = {"index": index, "gender": gender, "email": email, "password": password}
            alltodo.set_value(alltodo.value + [newtodo])
            login(newtodo)
  
    list = [ ]
    
    def handle_event(event):
        print(event)
        
    return html.div(
        {"style":
            {
             "place-items": "center",  
             "height": "100vh",
             "padding": "20px",
             "display": "flex",
            "flexDirection": "column",
            "alignItems": "center",
            "justifyContent": "center",
             "background-size": "cover",
             "background-image": "url(https://as1.ftcdn.net/v2/jpg/04/58/64/76/1000_F_458647644_QMgurK1ooH0uxNWuyelKdvIl5kysrPbP.jpg)"}},
        
        
        
        ## creating form for submission(HTML , CSS)
        html.form(
            {"on submit": mysubmit},
            html.h1({"style":
                {"font-family": "Georgia", "font-size": "36px","color":"black","text-align": "center","background-color": "#FFD700",
                 "padding": "20px",  
            "box-shadow": "0px 4px 6px rgba(0, 0, 0, 0.5)",
            "text-shadow": "2px 2px 4px rgba(0, 0, 0, 0.5)",
                 "font-weight": "bold"}}
                    ,"Final Exam"),
            html.br(),
            html.label({"style": {"font-family": "Georgia", "font-size": "15px","color":"White","font-weight": "bold"}}
                    ,"Index No:  "),
            html.input(
                {
                    "type": "test",
                    "placeholder": "Index No",
                    "on_change": lambda event: set_index(event["target"]["value"]),
                    "style":{
                             "font-family": "Time New Roman",
                             "font-size": "15px",
                             "padding": "5px 5px",
                            "border": "2px solid #ccc",
                            "font-weight": "bold",
                            "border-radius": "5px",
                            "margin": "5px auto",
                            "width": "25%",
                            "box-sizing": "border-box",
                            "background-color": "#FFD700",
                            "color": "#555",
                            "outline": "none","align-items": "center",
            "justify-content": "center"}
                            }
            ),
            html.br(),
            html.p(""),
            html.label({"style": {"font-family": "Georgia", "font-size": "15px", "color": "White", "font-weight": "bold"}}
                       , "Gender:  "),
            html.input(
    {
        "type": "radio",
        "name": "gender",
        "value": "male",
        "on_change": lambda event: set_gender(event["target"]["value"]),
    },
),
html.label(
    {
        "for": "male",
        "style": {
            "font-family": "Georgia", "font-size": "15px", "color": "White", "font-weight": "bold","margin-right": "10px"
        }
    },
    "Male"
),
html.input(
    {
        "type": "radio",
        "name": "gender",
        "value": "female",
        "on_change": lambda event: set_gender(event["target"]["value"]),
    },
),
html.label(
    {
        "for": "male",
        "style": {
            "font-family": "Georgia", "font-size": "15px", "color": "White", "font-weight": "bold"
        }
    },
    "Female"
),
html.br(),
            html.p(""),
          
            html.label({"style": {"font-family": "Georgia", "font-size": "15px","color":"White","font-weight": "bold"}}
                    ,"Email:  "),
            html.input(
                {
                    "type": "test",
                    "placeholder": "E-Mail",
                    "on_change": lambda event: set_email(event["target"]["value"]),
                    "style":{
                             "font-family": "Time New Roman",
                             "font-size": "15px",
                             "padding": "5px 5px",
                            "border": "2px solid #ccc",
                            "border-radius": "5px",
                            "margin": "5px auto",
                            "font-weight": "bold",
                            "width": "70%",
                            "box-sizing": "border-box",
                            "background-color": "#FFD700",
                            "color": "#555",
                            "outline": "none","align-items": "center",
            "justify-content": "center"}
                            }
            ),
            html.br(),
            html.p(""),
            html.label({"style": {"font-family": "Georgia", "font-size": "15px","color":"White","font-weight": "bold"}}
                    ,"Password:  "),
            html.input(
                {
                    "type": "password",
                    "placeholder": "Password",
                    "on_change": lambda event: set_password(event["target"]["value"]),
                    "style":{
                             "font-family": "Time New Roman",
                             "font-size": "15px",
                             "padding": "5px 5px",
                            "border": "2px solid #ccc",
                            "border-radius": "5px",
                            "margin": "5px auto",
                            "font-weight": "bold",
                            "width": "70%",
                            "box-sizing": "border-box",
                            "background-color": "#FFD700",
                            "color": "#555",
                            "outline": "none","align-items": "center",
            "justify-content": "center"}
                }
            ),html.br(),html.p(""),
             
            # creating submit button on form
            
            html.button(
                {
                    "type": "submit",
                    "on_click": event(
                        lambda event: mysubmit(event), prevent_default=True
                    ),
                    "style": {
            "background-color": "Black",  
            "color": "white",              
            "border": "2px solid #ccc", 
            "font-weight": "bold",
            "border-radius": "5px", 
            "margin": "5px auto",
            "width": "150px",
            "height": "40px",
            "box-sizing": "border-box",
            "outline": "none",
            "align-items": "center",
            "justify-content": "center",
            "margin-right": "20px",
        },
                },
                "Submit",
            ),
            html.button(
                {
                    "type": "reset",
                    "on_click": event(
                        lambda event: set_password("") 
                    ),
                     "style": {
            "background-color": "Black",  
            "color": "white",              
            "border": "2px solid #ccc", 
            "border-radius": "5px", 
            "margin": "5px auto",
            "width": "150px",
            "height": "40px",
            "font-weight": "bold",
            "box-sizing": "border-box",
            "outline": "none",
            "align-items": "center",
            "justify-content": "center"
        },
                },
                "Reset",
            ),html.p(""),
            html.label({"style":
                 {"font-family": "Georgia", "font-size": "15px","color":"White","font-weight": "bold","cursor": "pointer"}}
                    ,"Notification: "), html.p(),
            html.div(
            {"style":
                {"background-color": "Black",  
            "color": "white",              
            "border": "2px solid #ccc", 
            "border-radius": "5px", 
            "margin": "5px auto",
            "height": "40px",
            "box-sizing": "border-box",
            "outline": "none",
            "display": "flex",
            "align-items": "center",
            "justify-content": "center",
            "width":"70",
            "font-weight":"bold"
            }},  # Style for error message
            error_message,  # Display the error message
        ),html.p(),
             

        ),
            
        html.ul(list),
    )

app = FastAPI()

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.mongo_client import MongoClient

## copy and pasting the mongodb URI
uri = "mongodb+srv://ADMIN:usmaan123@cluster0.awyn5l7.mongodb.net/"
client = MongoClient(uri,server_api=ServerApi("1"))

## defining the DB name
db = client["Reaxtpy_Task01"]

## collection name
collection = db["Task1_MongoDB"]

##checking the connection
try:
    client.admin.command("Ping")
    print("Successfully Connected Mongodb")
except Exception as e:
    print(e)
    
def login(
    login_data: dict,
): #removed 
    index = login_data["index"]
    gender = login_data["gender"]
    email = login_data["email"]
    password = login_data["password"]
    
    
    document = {"index": index, "gender": gender, "email": email, "password": password}
    
    print(document)
    
    post_id = collection.insert_one(document).inserted_id
    print(post_id)
    
    return{"message": "Login successful"}

configure(app, MyCurd)
    