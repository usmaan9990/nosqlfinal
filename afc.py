from fastapi import FastAPI
from reactpy.backend.fastapi import configure
from reactpy import component, event, html, use_state
import reactpy as rp
from fastapi.middleware.cors import CORSMiddleware
from pymongo import MongoClient


@component
def MyCrud():
    ## Creating state
    alltodo = use_state([])
    name, set_name = use_state("")
    password, set_password = use_state(0)
    forgot_password = use_state(False)

    def mysubmit(event):
        newtodo = {"name": name, "password": password}

        # push this to alltodo
        alltodo.set_value(alltodo.value + [newtodo])
        login(newtodo) # function call to login function using the submitted data
# looping data from alltodo to show on web

    list = []

    def handle_event(event):
        print(event)

    def forgot_password_click(event):
        forgot_password.set_value(True)

    return html.div(
        {"style": {"padding": "10px"}},
        ## creating form for submission\
        html.form(
            {"on submit": mysubmit},
            html.h1("Login Form - ReactPy & Mongodb"),
            html.input(
                {
                    "type": "test",
                    "placeholder": "Name",
                    "on_change": lambda event: set_name(event["target"]["value"]),
                }
            ),
            html.input(
                {
                    "type": "test",
                    "placeholder": "Password",
                    "on_change": lambda event: set_password(event["target"]["value"]),
                }
            ),
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
        html.button(
            {
                "type": "button",
                "on_click": forgot_password_click,
            },
            "Forgot Password",
        ),
        html.div(
            {"style": {"display": "none"}},
            # forgot password form
            html.form(
                {"on submit": forgot_password_submit},
                html.h1("Forgot Password"),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "Username",
                        "on_change": lambda event: set_username(event["target"]["value"]),
                    }
                ),
                html.input(
                    {
                        "type": "test",
                        "placeholder": "New Password",
                        "on_change": lambda event: set_new_password(
                            event["target"]["value"]
                        ),
                    }
                ),
                # creating submit button on form
                html.button(
                    {
                        "type": "submit",
                        "on_click": event(
                            lambda event: forgot_password_submit(event),
                            prevent_default=True,
                        ),
                    },
                    "Submit",
                ),
            ),
        ),
    )

# The `forgot_password_click` function takes an event object as input and sets the `forgot_password` state to `True`. 
# This will display the forgot password for

#The `forgot_password_submit` function takes an event object as input and updates the record in the MongoDB database. 
# The function first gets the username and new password from the state. 
# Then, it uses the `collection.update_one` method to update the record in the database.
# The update query will match the record with the specified username and update the `password` field