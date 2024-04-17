import nltk
nltk.download('popular')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
from pyngrok import ngrok
from pyngrok import ngrok
import webbrowser
from flask_ngrok import run_with_ngrok
from keras.models import load_model
model = load_model('chatbot/model.h5')
import json
import random
intents = json.loads(open('chatbot/data.json').read())
words = pickle.load(open('chatbot/texts.pkl','rb'))
classes = pickle.load(open('chatbot/labels.pkl','rb'))

def clean_up_sentence(sentence):
    # tokenize the pattern - split words into array
    sentence_words = nltk.word_tokenize(sentence)
    # stem each word - create short form for word
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

# return bag of words array: 0 or 1 for each word in the bag that exists in the sentence

def bow(sentence, words, show_details=True):
    # tokenize the pattern
    sentence_words = clean_up_sentence(sentence)
    # bag of words - matrix of N words, vocabulary matrix
    bag = [0]*len(words)  
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s: 
                # assign 1 if current word is in the vocabulary position
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))

def predict_class(sentence, model):
    # filter out predictions below a threshold
    p = bow(sentence, words,show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]
    # sort by strength of probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list
def getResponse(ints, intents_json):
    tag = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for intent in list_of_intents:
        if intent['tag'] == tag:
            if 'timetable' in intent['responses'][0]:
                timetable = intent['responses'][0]['timetable']
                timetable_html = "<table border='1'><tr><th>Day</th><th>Period</th><th>Teacher</th></tr>"
                for day, periods in timetable.items():
                    for period, details in periods.items():
                        subject = details['subject']
                        teacher = details['teacher']
                        timetable_html += f"<tr><td>{day}</td><td>{period}</td><td>{teacher}</td></tr>"
                timetable_html += "</table>"
                return timetable_html
            else:
                return random.choice(intent['responses'])
    return "I'm sorry, I didn't understand that."



def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res


from flask import Flask, render_template, request

# Set the port that your Flask app is running on
port = 5000

public_url = ngrok.connect(port).public_url

#listener = ngrok.forward("localhost:8080", authtoken_from_env=True)
#print(f"Ingress established at: {listener.url()}")

app = Flask(__name__)
run_with_ngrok(app)
app.static_folder = 'static'
ngrok.set_auth_token("2f1tCVhKtiLenepguarJCLEQEu0_73crhibfp48Mqsp5sceD5")


@app.route("/")
def home():
    return render_template('index.html')

print(' * Tunnel URL:', public_url)

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return chatbot_response(userText)



if __name__ == "__main__":
    webbrowser.open_new('http://127.0.0.1:5000')
    app.run()
    
    