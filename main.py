import requests as req
from datetime import datetime as dt

# Endpoint
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/YourSheetyAddress/"

# Constant variable
APP_ID = "Your APP ID"  # register and find it on your profile @https://trackapi.nutritionix.com
APP_KEY = "Your APP KEY"  # register and find it on your profile @https://trackapi.nutritionix.com

# Constant info
GENDER = "male"  # your gender
WEIGHT_KG = 83.4  # your weight
HEIGHT_CM = 184.5  # your height
AGE = 23  # your age

# User input (query)
QUERY = input("What exercise you did?: ")

# Header
exercise_header = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}
sheety_bearer_headers = {
    "Authorization": "Your Sheety Bearer"  # Find it on https://api.sheety.co
}

# Parameters
exercise_parameter = {
    "query": QUERY,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

# Date and time
date_now = dt.now().date().strftime("%d-%m-%Y")
time_now = dt.now().time().strftime("%X")

exercise_response = req.post(url=exercise_endpoint, json=exercise_parameter, headers=exercise_header)
exercise_response.raise_for_status()
exercise_data = exercise_response.json()

for exercise in exercise_data["exercises"]:
    sheety_inputs = {
        "workout": {
            "date": date_now,
            "time": time_now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

sheety_response = req.post(url=sheety_endpoint, json=sheety_inputs, headers=sheety_bearer_headers)
sheety_response.raise_for_status()
