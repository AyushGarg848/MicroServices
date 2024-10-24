# Import the FastAPI class from the fastapi module
from fastapi import FastAPI
import random

# Create an instance of the FastAPI class
app = FastAPI()

# route for the root URL "/"
@app.get("/")
def root():
    return {"message": "Hello World!!"}

# route for the URL "/roll-dice"
@app.get("/roll-dice")
def roll_dice():
    # to Generate a random integer between 1 and 6
    dice_value = random.randint(1, 6)
    return {"value": dice_value}