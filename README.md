# G.O.D (Guide of Dharma)

A conversational Indian astrology platform powered by AI, providing users with personalized Vedic astrology consultations. This application features Pandit Saarthi, a virtual Jyotish (Vedic astrologer) who guides users through a natural conversation, asking questions one by one to provide cosmic insights and astrological guidance.

## Features

- **Conversational AI Astrologer**: Engage with Pandit Saarthi, a virtual Vedic astrologer who asks questions sequentially, creating a natural consultation experience
- **Personalized Astrological Guidance**: Receive insights on life path, relationships, career, and health based on Vedic astrology principles
- **Sequential Conversation Flow**: Experience a genuine dialogue where the astrologer responds to your answers before asking the next question
- **Astrological Symbols**: Automatically enhances responses with appropriate planetary and zodiac symbols
- **Dynamic Typing Effect**: Watch as the astrologer's responses appear character by character, simulating a real-time conversation

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

## Usage

1. Select what you're seeking: Inner Peace, Clarity, To Be Heard, or Personal Growth
2. Enter your question or concern in the text area
3. Receive guidance from Saarthi, inspired by the wisdom of Lord Krishna

## Technical Details

- **Backend**: Built with FastAPI for efficient API handling and conversation state management
- **Frontend**: Implemented with HTML, CSS, and JavaScript for a responsive, interactive UI
- **AI Integration**: Powered by OpenAI's GPT-4o API with custom system prompts for authentic Vedic astrology guidance
- **Conversation Management**: Maintains conversation state to deliver a coherent, sequential dialogue
- **Dynamic Content**: Real-time response enhancement with astrological symbols and typing effects
- **Responsive Design**: Optimized for both desktop and mobile devices

## Project Structure

```
/
├── app.py              - Main FastAPI application with conversation logic
├── requirements.txt    - Python dependencies
├── .env                - Environment variables (create from .env.example)
├── .env.example        - Template for environment variables
├── static/             - Static assets
│   ├── css/            - CSS stylesheets for astrology-themed styling
│   ├── js/             - JavaScript for dynamic conversation interactions
│   └── images/         - Astrological imagery (via external links)
└── templates/          - HTML templates
    └── index.html      - Main consultation interface
```

## How It Works

1. **Conversational Flow**: The astrologer asks questions one at a time, listening to your responses before proceeding
2. **State Management**: Tracks conversation progress to provide increasingly personalized insights
3. **Information Extraction**: Identifies key details from user responses to inform astrological readings
4. **Response Enhancement**: Automatically adds appropriate astrological symbols to planetary and zodiac references
5. **Dynamic Typing**: Simulates the astrologer typing responses in real-time for a more authentic experience

## Future Enhancements

- **Birth Chart Generation**: Create visual birth charts based on user's birth details
- **Planetary Transit Alerts**: Notify users about significant astrological events
- **Multiple Astrologer Personas**: Add specialists in different astrological traditions
- **Voice Interaction**: Enable spoken consultations for a hands-free experience
- **Session Recording**: Save consultation transcripts for future reference
- **Daily/Weekly Forecasts**: Provide regular astrological updates based on user's profile
