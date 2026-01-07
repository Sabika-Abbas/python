import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Prompt the user to input the text
while True:
    text = input("Enter the text you want Python to say: ")

# Set properties (optional)
    engine.setProperty('rate', 150)    # Speed of speech
    engine.setProperty('volume', 1)    # Volume (0.0 to 1.0)

# Convert user input text to speech
    engine.say(text)

# Wait for the speech to finish
    engine.runAndWait()
    if text=="exit":
        break
