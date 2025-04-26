import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

import json
import pickle
import numpy as np
import random
import keras_tuner as kt
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD

# Load chatbot intents
data_file = open('C:/Users/ASUS/Desktop/bandhu/chatbot-flask/chatbot/data.json').read()
intents = json.loads(data_file)

words = []
classes = []
documents = []
ignore_words = ['?', '!']

# Tokenization and Lemmatization
for intent in intents['intents']:
    for pattern in intent['patterns']:
        w = nltk.word_tokenize(pattern)
        words.extend(w)
        documents.append((w, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])

# Lemmatization and removing duplicates
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(list(set(words)))
classes = sorted(list(set(classes)))

# Saving processed words and classes
pickle.dump(words, open('texts.pkl', 'wb'))
pickle.dump(classes, open('labels.pkl', 'wb'))

# Creating Training Data (Bag-of-Words)
training = []
output_empty = [0] * len(classes)
for doc in documents:
    bag = [0] * len(words)
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in doc[0]]
    for pattern_word in pattern_words:
        for i, w in enumerate(words):
            if w == pattern_word:
                bag[i] = 1
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])

# Shuffle data and convert to numpy arrays
random.shuffle(training)
training = np.array(training, dtype=object)

# **Adding Train-Test Split**
train_x, test_x, train_y, test_y = train_test_split(
    np.array(list(training[:, 0]), dtype=float),
    np.array(list(training[:, 1]), dtype=float),
    test_size=0.2, random_state=42
)

print("Training and testing data split completed")

# **Hyperparameter Tuning with Keras Tuner**
def build_model(hp):
    model = Sequential()

    # Tune first hidden layer
    model.add(Dense(
        hp.Int('units_1', min_value=64, max_value=256, step=32), 
        input_shape=(len(train_x[0]),), 
        activation='relu'
    ))
    model.add(Dropout(hp.Float('dropout_1', min_value=0.2, max_value=0.5, step=0.1)))

    # Tune second hidden layer
    model.add(Dense(
        hp.Int('units_2', min_value=32, max_value=128, step=16), 
        activation='relu'
    ))
    model.add(Dropout(hp.Float('dropout_2', min_value=0.2, max_value=0.5, step=0.1)))

    # Output layer
    model.add(Dense(len(train_y[0]), activation='softmax'))

    # Tune learning rate
    sgd = SGD(
        learning_rate=hp.Choice('learning_rate', values=[0.001, 0.005, 0.01, 0.02]), 
        decay=1e-6, momentum=0.9, nesterov=True
    )
    
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
    return model

# Initialize the tuner
tuner = kt.RandomSearch(
    build_model,
    objective='val_accuracy',
    max_trials=10,  
    executions_per_trial=1, 
    directory='tuning_results',
    project_name='chatbot_tuning'
)

# Run hyperparameter tuning
tuner.search(train_x, train_y, epochs=50, batch_size=5, validation_split=0.2)

# Get the best hyperparameters
best_hp = tuner.get_best_hyperparameters(num_trials=1)[0]
print(f"Best parameters: {best_hp.values}")

# Build and train the best model
best_model = tuner.hypermodel.build(best_hp)
best_model.fit(train_x, train_y, epochs=200, batch_size=5, validation_split=0.2)

# **Evaluate Model on Test Data**
loss, accuracy = best_model.evaluate(test_x, test_y, verbose=1)
print(f"Test Accuracy after tuning: {accuracy:.4f}")

# **Prediction Function**
def predict_intent(text):
    words_input = nltk.word_tokenize(text)
    words_input = [lemmatizer.lemmatize(w.lower()) for w in words_input]

    bag = [0] * len(words)
    for w in words_input:
        if w in words:
            bag[words.index(w)] = 1

    result = best_model.predict(np.array([bag]))[0]
    predicted_class = classes[np.argmax(result)]
    
    return predicted_class

# Example Test
print(predict_intent("Hello, how are you?"))
