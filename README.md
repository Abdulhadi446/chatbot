# Simple Chatbot

A simple chatbot application with a Flask backend and a clean, modern frontend interface.

## Features

- 🤖 Simple rule-based chatbot with friendly responses
- 🎨 Modern, responsive UI with gradient styling
- ⚡ Fast and lightweight Flask backend
- 💬 Real-time chat interface
- 🔄 CORS enabled for cross-origin requests

## Project Structure

```
chatbot/
├── app.py              # Flask backend server
├── index.html          # Frontend HTML
├── style.css           # Frontend CSS styling
├── script.js           # Frontend JavaScript
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/Abdulhadi446/chatbot.git
cd chatbot
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

### Running the Application

1. Start the Flask backend:
```bash
python app.py
```

The backend will start on `http://localhost:5000`

**Note**: For production deployment:
- Set `FLASK_DEBUG=false` environment variable
- Configure `CORS_ORIGINS` to restrict allowed origins (e.g., `CORS_ORIGINS=http://yourdomain.com`)
- Use a production WSGI server like Gunicorn instead of Flask's built-in server

2. Open the frontend:
   - Simply open `index.html` in your web browser
   - Or use a local server:
   ```bash
   # Using Python's built-in HTTP server
   python -m http.server 8000
   ```
   Then navigate to `http://localhost:8000` in your browser

## Usage

1. Type your message in the input box at the bottom of the chat interface
2. Press Enter or click the "Send" button
3. The chatbot will respond based on your message
4. Try greetings like "hello", "hi", or "hey"
5. Try farewells like "bye" or "goodbye"
6. Ask for help with words like "help" or "assist"

## API Endpoints

### GET /
Returns API information and available endpoints

### POST /chat
Send a message to the chatbot

**Request body:**
```json
{
  "message": "Hello!"
}
```

**Response:**
```json
{
  "response": "Hi there! What can I do for you?",
  "user_message": "Hello!"
}
```

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **CORS**: Flask-CORS for cross-origin requests

## Customization

### Adding New Responses

Edit the `responses` dictionary in `app.py` to add new response categories:

```python
responses = {
    'your_category': [
        'Response 1',
        'Response 2',
    ]
}
```

### Styling

Modify `style.css` to change the appearance of the chatbot interface. The current design uses a purple gradient theme.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
