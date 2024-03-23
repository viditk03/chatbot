from flask import Flask, request, jsonify, render_template
import spacy

# Load the English model
nlp = spacy.load("en_core_web_sm")

# Define some example intents
intents = {
    "greeting": ["hello", "hi", "hey"],
    "goodbye": ["bye", "goodbye", "see you later"],
}

# Define a function to classify the user input into an intent
def classify_intent(input_text):
    doc = nlp(input_text.lower())
    for token in doc:
        for intent, examples in intents.items():
            if token.text in examples:
                return intent
    return "unknown"

# Define responses for each intent
responses = {
    "greeting": "Hello! How can I help you?",
    "goodbye": "Goodbye! Have a great day!",
    "unknown": "I'm sorry, I didn't understand that.",
}

# Create a Flask app
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
# Define a route for the chatbot endpoint
@app.route('/chatbot', methods=['GET', 'POST'])
def chatbot():
    if request.method == 'GET':
        # Handle GET requests
        return 'Chatbot is running'  # Return a simple message indicating that the chatbot is running
    elif request.method == 'POST':
        # Handle POST requests
        # Get user input from the request
        user_input = request.json.get('message')

        # Classify the intent of the user input
        intent = classify_intent(user_input)

        # Get the response based on the intent
        response = responses[intent]

        # Return the response as JSON
        return jsonify({'response': response})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
