# G.O.D (Guide of Dharma) - Backend API

A backend API for a spiritual wellness platform powered by AI, providing users with personalized guidance inspired by Lord Krishna and Vedic astrology. This application features Saarthi, an AI guide who engages users in conversation to offer spiritual wisdom, inner peace, and clarity.

## Features

- **Conversational AI Guide**: Backend API for Saarthi, a virtual spiritual guide inspired by Lord Krishna and Vedic astrology
- **Personalized Spiritual Guidance**: API provides insights on inner peace, clarity, personal growth, and spiritual matters
- **Sequential Conversation Management**: Maintains conversation state to deliver a coherent, natural dialogue experience
- **Context Preservation**: Tracks conversation history to provide increasingly personalized insights
- **Information Extraction**: Identifies key details from user responses to inform spiritual guidance

## Setup Instructions

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Create a `.env` file based on `.env.example` and add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```
4. Run the application:
   ```
   python app.py
   ```
   The application will be available at `http://localhost:8000`

## API Usage

1. Start a conversation with a POST request to `/chat` endpoint
2. Include your message and what you're seeking (default: "Inner Peace") in the request body
3. Receive JSON responses with guidance from Saarthi, inspired by the wisdom of Lord Krishna
4. The API maintains conversation state between requests for a coherent dialogue

## Technical Details

- **Backend**: Built with FastAPI for efficient API handling and conversation state management
- **AI Integration**: Powered by OpenAI's GPT-4o API with custom system prompts for authentic spiritual guidance
- **Conversation Management**: Maintains conversation history and state to deliver a coherent, sequential dialogue
- **CORS Support**: Configured for cross-origin requests, allowing integration with any frontend
- **Session Handling**: Basic session management for maintaining separate conversations

## Project Structure

```
/
├── app.py              - Main FastAPI application with conversation logic and API endpoints
├── requirements.txt    - Python dependencies
├── .env                - Environment variables (create from .env.example)
└── .env.example        - Template for environment variables
```

## How It Works

1. **API Endpoints**: Provides `/chat` endpoint for conversation interaction
2. **Conversational Flow**: The guide asks questions one at a time, listening to your responses before proceeding
3. **State Management**: Tracks conversation progress to provide increasingly personalized insights
4. **Information Extraction**: Identifies key details from user responses to inform spiritual guidance
5. **Session Management**: Uses simple session identifiers to maintain separate conversations

## Future Enhancements

- **Authentication**: Add user authentication for personalized experiences
- **Database Integration**: Store conversations and user profiles in a database
- **Multiple Guide Personas**: Add specialists in different spiritual traditions
- **Advanced NLP**: Enhance information extraction from user messages
- **Analytics**: Track conversation metrics and user engagement
- **Session Management**: Implement more robust session handling
