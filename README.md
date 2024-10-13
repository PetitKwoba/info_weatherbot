# info_weatherbot
##GROUP 3 ASSIGNMENT : WEATHER ASSISTANT BOT DOCUMENTATION.

##DOCUMENTATION
We as the group member we decided to come up with a chatbot that uses OPenWeatherMap API to fetch and weather information for the city. It will converse with the user and ask if they have another question. We built the interface using Tkinker, a GUI for python.

##Features
1.	Greeting: Upon starting the app, it greets the user and asks them to enter the city name.
2.	City weather queries: The app allows the users to enter any city, e.g, “what is the weather in Nairobi.” Or just enter city name, then the bot will fetch the information and display to the user.
3.	Continue the conversation: the bot then asks the user if they want to ask for weather information or not; if they press no, it ends the conversation. If the say yes, it will ask them to enter another city.
4.	Error handling: if the bot does not understand the user’s question, the bot will apologize and ask the user to enter another city.
5.	Ending information: if the user enters “no” or “n” to the continuation question, the conversation ends, and it says goodbyes
We did our research on the chat bot, where we used various technologies.

##REQUIREMENTS
Language used : Download and install Python 3.7 or higher
Coding platform: Download and install Visual Studio code

##INSTALLATIONS
Clone and download repository from: https://github.com/PetitKwoba/info_weatherbot 
Download pip: curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
Install dependencies
Install pip: python get-pip.py
Install nltk: pip install requests nltk
Install chatterbot: pip install chatterbot
Install chatterbot Corpus: pip install chatterbot_corpus
Create account on OpenWeatherMap to make API calls 
Run application 
python weather.py
## HOW IT WORKS
1.	Tkinter GUI Installation: We used Tkinter to provide the weather bot with an interactive graphical user interface. Users can generate weather queries through a text entry box and appropriate weather answers will appear on a press of the Enter key.
2.	Greeting Message: On initiating the application, a greeting message is displayed. It prompts the users to either ask about the weather information or provide the name of a specific city, right away.
Handling User Input: The entry submitted by the user is broken down in order to capture the name of the city. Should the user, for instance, pose a complete question, ‘what weather do you expect in London?’, the bot parses this question and takes the city out of it. In case there is no anticipated city from the user's question, the bot budei will regretfully inform the user and ask for an expected city instead.
Requesting for Weather Information: After determining the city, the bot places an API request to the OpenWeatherMap database including the name of the city and the appid.
It extracts and presents: Actual Weather (for example, Sunny, Cloudy, etc), Present Temperature Celsius, Lowest Temperature and Highest Temperature, Pressure and Humidity, Velocity of Wind, Time of Sunrise and Sunset
Error Handling: In its functionality, this bot will handle weather information retrieval and if it fails to retrieve valid weather (no such city, the internet is off, etc.), it will tell the user: ‘the weather couldn’t be provided’, and request them for another city.
In case a user types something which cannot be classified as a question or city name, he will have a warning message: “Sorry, I did not understand your query. Please enter a city name.”
Follow-up Question: "Do you have another question?"
User Input: "Yes"
Bot prompts: "Please enter another city!"
The is found at : 
