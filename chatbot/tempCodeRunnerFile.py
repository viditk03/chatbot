import nltk
nltk.download('popular')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
from pyngrok import ngrok
from flask_ngrok import run_with_ngrok
from keras.models import load_model
import json
import random
from flask import Flask, render_template, request, jsonify, send_file, url_for
import os  

# Load the model and data
model = load_model('C:/Users/User/OneDrive/Desktop/New_folder/chatbot/model.h5')
intents = json.loads(open('C:/Users/User/OneDrive/Desktop/New_folder/chatbot/data.json').read())
words = pickle.load(open('C:/Users/User/OneDrive/Desktop/New_folder/chatbot/texts.pkl', 'rb'))
classes = pickle.load(open('C:/Users/User/OneDrive/Desktop/New_folder/chatbot/labels.pkl', 'rb'))

# Tokenizer and response logic
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0] * len(words)  
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s: 
                bag[i] = 1
                if show_details:
                    print("found in bag: %s" % w)
    return np.array(bag)

def predict_class(sentence, model):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = [{"intent": classes[r[0]], "probability": str(r[1])} for r in results]
    return return_list

def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for intent in list_of_intents:
        if intent['tag'] == tag:
            return random.choice(intent['responses'])
    return "I'm sorry, I didn't understand that."

def chatbot_response(msg):
    ints = predict_class(msg, model)

    # Check for timetable requests
    if "timetable" in msg.lower():
        return "For which year do you need the timetable? (2nd year, 3rd year, final year)"

    # Check if user has specified a year
    year_map = {
        '2nd year': '2nd_year',
        '3rd year': '3rd_year',
        'final year': 'final_year'
    }
    
    for year_text, year_key in year_map.items():
        if year_text in msg.lower():
            return show_image_response(year_key)

    res = getResponse(ints, intents)
    return res

# Initialize Flask app
app = Flask(__name__)
run_with_ngrok(app)

# Set the port that your Flask app is running on
port = 5000
public_url = ngrok.connect(port).public_url
ngrok.set_auth_token("2jnFXncySCffOpSRytdqaU3A7P7_7fBzPayARR6Z8a8Ebs3gy")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)

# Route to serve the image
@app.route('/get_image/<year>', methods=['GET'])
def get_image(year):
    # Define the file paths for the timetable images
    image_paths = {
        '2nd_year': 'static/images/timetable_2nd_year.jpg',
        '3rd_year': 'static/images/timetable_3rd_year.jpg',
        'final_year': 'static/images/timetable_final_year.jpg'
    }
    
    # Get the correct image path based on the year provided
    image_path = image_paths.get(year)
    
    if image_path and os.path.exists(image_path):
        return send_file(image_path, mimetype='image/jpeg')
    else:
        return jsonify({'error': 'Invalid year provided or image not found.'}), 404

# Function to generate image response in the chatbot
def show_image_response(year):
    image_url = url_for('get_image', year=year)
    return f"{year.replace('_', ' ').title()}: <img src='{image_url}' alt='Timetable for {year.replace('_', ' ').title()}'>"

print(' * Tunnel URL:', public_url)

if __name__ == "__main__":
    app.run()
