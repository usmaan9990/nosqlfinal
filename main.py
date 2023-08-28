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
    name, set_name = use_state("")
    password, set_password = use_state("")
    
    def mysubmit(event): # 
        newtodo={"name": name, "password": password}
        
        #push this to alltodo
        alltodo.set_value(alltodo.value + [newtodo])
        login(newtodo) # function call to login function using the submitted data
        
    # looping data from alltodo to show on web
    
    list = [ ]
    
    def handle_event(event):
        print(event)
        
    return html.div(
        {"style": {"padding": "10px","background-color":"blue","min-height":"500px","min-width":"500px",
                  "background-image": "url(https://reactpy.neocities.org/photo/wallpaperflare.com_wallpaper.jpg)"}},
        ##
        ## creating form for submission\
        html.form(
            {"on submit": mysubmit},
            html.h1({"style": {"font-family": "Arial", "font-size": "26px","color":"LightCyan"}}
                    ,"ReactPy & Mongodb"),
            html.br(),html.p(),
            html.label({"style": {"font-family": "Arial", "font-size": "15px","color":"LightCyan"}}
                    ,"name"),
            html.input(
                {
                    "type": "test",
                    "placeholder": "Name",
                    "on_change": lambda event: set_name(event["target"]["value"]),"style":{
                             "font-family": "Time New Roman",
                             "font-size": "15px",
                             "padding": "5px 5px",
                            "border": "2px solid #ccc",
                            "border-radius": "10px",
                            "margin": "5px auto",
                            "width": "25%",
                            "box-sizing": "border-box",
                            "background-color": "#f9f9f9",
                            "color": "#555",
                            "outline": "none","align-items": "center",
            "justify-content": "center"}
                            }
            ),
            html.br(),
            html.p(""),
            html.label("Password: "),
            html.input(
                {
                    "type": "test",
                    "placeholder": "Password",
                    "on_change": lambda event: set_password(event["target"]["value"]),
                }
            ),html.br(),html.p(""),
            # creating submit button on form
            html.button(
                {
                    "type": "submit",
                    "on_click": event(
                        lambda event: mysubmit(event), prevent_default=True
                    ),
                },
                "Submit",
            ),
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
    username = login_data["name"]
    password = login_data["password"]
    
    
    document = {"name": username, "password": password}
    
    print(document)
    
    post_id = collection.insert_one(document).inserted_id
    print(post_id)
    
    return{"message": "Login successful"}

configure(app, MyCurd)
    