from flask import Flask, request, jsonify
from flask_cors import CORS
import random
import os

app = Flask(__name__)
# Configure CORS - in production, restrict to specific origins
CORS(app, origins=os.getenv('CORS_ORIGINS', '*').split(','))

# Simple chatbot responses
responses = {
    'greetings': [
        'Hello! How can I help you today?',
        'Hi there! What can I do for you?',
        'Hey! How are you doing?',
        'Greetings! What would you like to know?'
    ],
    'farewell': [
        'Goodbye! Have a great day!',
        'See you later!',
        'Bye! Feel free to come back anytime!',
        'Take care!'
    ],
    'help': [
        'I can help you with general questions. Try asking me something!',
        'I\'m here to assist you. What would you like to know?',
        'Feel free to ask me anything!'
    ],
    'default': [
        'That\'s interesting! Tell me more.',
        'I see. Can you elaborate on that?',
        'Hmm, I\'m not sure I understand. Can you rephrase that?',
        'That\'s a good question. Let me think about that.',
        'Interesting perspective!'
    ]
}

def get_bot_response(user_message):
    """Generate a response based on the user's message"""
    message_lower = user_message.lower().strip()
    
    # Check for greetings
    if any(word in message_lower for word in ['hello', 'hi', 'hey', 'greetings']):
        return random.choice(responses['greetings'])
    
    # Check for farewells
    if any(word in message_lower for word in ['bye', 'goodbye', 'see you', 'farewell']):
        return random.choice(responses['farewell'])
    
    # Check for help requests
    if any(word in message_lower for word in ['help', 'assist', 'support']):
        return random.choice(responses['help'])
    
    # Default response
    return random.choice(responses['default'])

@app.route('/')
def home():
    """Home route"""
    return jsonify({
        'message': 'Welcome to the Chatbot API',
        'endpoints': {
            '/': 'This help message',
            '/chat': 'POST endpoint to send messages to the chatbot'
        }
    })

@app.route('/chat', methods=['POST'])
def chat():
    """Chat endpoint to handle user messages"""
    try:
        data = request.get_json()
        
        if not data or 'message' not in data:
            return jsonify({
                'error': 'Please provide a message in the request body'
            }), 400
        
        user_message = data['message']
        
        if not user_message or not user_message.strip():
            return jsonify({
                'error': 'Message cannot be empty'
            }), 400
        
        bot_response = get_bot_response(user_message)
        
        return jsonify({
            'response': bot_response,
            'user_message': user_message
        })
    
    except Exception as e:
        return jsonify({
            'error': f'An error occurred: {str(e)}'
        }), 500

if __name__ == '__main__':
    # Debug mode should be disabled in production
    debug_mode = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode, host='0.0.0.0', port=5000)
