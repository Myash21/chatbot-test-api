from flask import Flask, render_template, request, jsonify
from gradio_client import Client

app = Flask(__name__)

# Connect to the Gradio app hosted on Hugging Face Spaces
client = Client("YashMhaskar/chatbottest")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = client.predict(user_input=user_input, api_name="/predict")
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
