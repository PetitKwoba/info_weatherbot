import tkinter as tk
import requests
import time
import re

# Function to fetch and display the weather
def getWeather():
    user_input = textField.get().lower()
    
    # Extract city name directly or from a question
    city_match = re.search(r'in\s+([a-zA-Z\s]+)', user_input)  # Check if the input contains "in [city]"
    if city_match:
        city = city_match.group(1).strip()
    else:
        city = user_input.strip()  # Treat the input as the city name if not a full question

    if city:  # Proceed only if city is not empty
        api_key = "06c921750b9a82d8f5d1294e1586276f"
        api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            response = requests.get(api_url)
            json_data = response.json()

            # Check if the API returned valid weather data
            if response.status_code == 200 and 'weather' in json_data:
                condition = json_data['weather'][0]['main']
                temp = int(json_data['main']['temp'] - 273.15)
                min_temp = int(json_data['main']['temp_min'] - 273.15)
                max_temp = int(json_data['main']['temp_max'] - 273.15)
                pressure = json_data['main']['pressure']
                humidity = json_data['main']['humidity']
                wind = json_data['wind']['speed']
                sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
                sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

                # Prepare the conversational output
                final_info = f"The weather for {city.title()} is {condition} with a temperature of {temp}°C."
                final_data = (
                    f"Min Temp: {min_temp}°C\n"
                    f"Max Temp: {max_temp}°C\n"
                    f"Pressure: {pressure} hPa\n"
                    f"Humidity: {humidity}%\n"
                    f"Wind Speed: {wind} m/s\n"
                    f"Sunrise: {sunrise}\n"
                    f"Sunset: {sunset}"
                )

                label1.config(text=final_info)
                label2.config(text=final_data)
                ask_more_questions()

            else:
                # Handle invalid city or API response errors
                label1.config(text="Sorry, I couldn't find the weather for that location.")
                label2.config(text="Please enter another city name.")

        except Exception as e:
            # Handle network errors or issues with API requests
            label1.config(text="Error fetching weather data.")
            label2.config(text=str(e))
    else:
        label1.config(text="Sorry, I did not understand your query.")
        label2.config(text="Please enter a city name.")

# Function to ask the user if they have more questions
def ask_more_questions():
    label1.config(text="Do you have another question? You can type 'yes' or ask for another city's weather.")
    textField.delete(0, tk.END)
    textField.bind('<Return>', handle_more_questions)

# Function to handle more questions or end the conversation
def handle_more_questions(event=None):
    user_input = textField.get().lower().strip()

    if user_input in ['yes', 'y']:
        label1.config(text="Please enter another city!")
        label2.config(text="")
        textField.delete(0, tk.END)
        textField.bind('<Return>', lambda event: getWeather())
    elif user_input in ['no', 'n']:
        end_conversation()
    else:
        getWeather()

# Function to end the conversation
def end_conversation():
    label1.config(text="Goodbye! Have a nice day!")
    label2.config(text="")
    textField.delete(0, tk.END)
    textField.config(state=tk.DISABLED)  # Disable further input

# Function to display a greeting message on app load
def greet_user():
    label1.config(text="Hello! Ask me about the weather, or simply enter a city name.")
    label2.config(text="")

# Set up the GUI window
canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather Assistant")

f = ("poppins", 15, "bold")
t = ("poppins", 20, "bold")

# Input field for user questions
textField = tk.Entry(canvas, justify='center', width=50, font=t)
textField.pack(pady=20)
textField.focus()

# Bind Enter key to the getWeather function
textField.bind('<Return>', lambda event: getWeather())

# Labels to display weather information and greeting
label1 = tk.Label(canvas, font=t, wraplength=500)
label1.pack(pady=10)

label2 = tk.Label(canvas, font=f, wraplength=500)
label2.pack()

# Show a greeting message when the app loads
greet_user()

# Start the Tkinter main loop
canvas.mainloop()
