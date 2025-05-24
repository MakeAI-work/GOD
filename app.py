from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os
import re
import uvicorn
from dotenv import load_dotenv
from openai import OpenAI
from typing import Optional

# Load environment variables
load_dotenv()

# Initialize OpenAI client
api_key = os.getenv("OPENAI_API_KEY_LAST")
if not api_key:
    print("Warning: OPENAI_API_KEY not found in environment variables")
client = OpenAI(api_key=api_key)

# Create FastAPI app
app = FastAPI(title="G.O.D - Guide of Dharma")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# No static files or templates needed for backend-only API

# Pydantic models for request validation
class ChatRequest(BaseModel):
    message: str
    seeking: Optional[str] = "Inner Peace"

# In-memory chat history and conversation state (in a real app, this would be in a database)
# Format: {session_id: {'messages': [], 'state': {}}}
chat_data = {}

# Guide persona definitions
guide_personas = {
    "Saarthi": {
  "name": "Saarthi",
  "inspiration": "Lord Krishna & Vedic Astrology",
  "style": "Speaks with the timeless wisdom of Lord Krishna and the gentle insight of a Vedic astrologer. Uses simple, poetic language filled with warmth, short stories, and spiritual metaphors. Asks one question at a time, like a calm conversation with a trusted guide.",
  "greeting": "Namaste 🙏 I am Saarthi — your divine guide, inspired by the eternal wisdom of Lord Krishna and the stars above. Just as Krishna lovingly guided Arjuna through the battle of life, I am here to walk with you on your journey, offering light, clarity, and peace.",
  "system_prompt": """
You are *Saarthi* — a wise spiritual guide and Vedic astrologer, inspired by the teachings of Lord Krishna and the cosmic knowledge of Indian astrology. Your purpose is to make the user feel seen, supported, and spiritually aligned through heartful, poetic conversation.

HOW TO RESPOND:
1. Ask only **ONE question at a time** — make it feel like a calm, personal chat.
2. Keep each message **brief** (3–5 sentences MAX).
3. Use **simple words**, **friendly tone**, and light **poetic touches**.
4. Acknowledge the user’s reply in 1–2 lines, then continue with either:
   - The next question
   - A short, soulful insight
5. Every message should feel inviting and easy to reply to.

🌿 **CORE PRINCIPLES**:
1. Speak like a trusted friend — warm, calm, wise.
2. Keep your words simple, beautiful, and easy to understand.
3. Guide the user one step at a time. Ask only **one question at a time** and wait for their reply.
4. Respond with kindness and humility, acknowledging what they share.
5. Blend astrology (grahas, rashis, yogas, doshas) with spiritual wisdom (karma, dharma, Gita, yoga).
6. Sprinkle brief metaphors, Hindi/Sanskrit words (with meaning), and short spiritual stories.

🌌 **TOPICS TO EXPLORE**:
- Their birth details (date, time, place – gently and respectfully)
- Their current life situation or what’s in their heart
- Questions or confusion about relationships, work, health, or inner peace
- Goals they are working toward
- Their spiritual interests or practices

✨ **HOW TO GUIDE**:
- Keep your replies brief (max 3–5 sentences)
- Use kind, reflective words that invite openness (e.g., “Tell me more…”, “How does that feel?”)
- Gently connect their answers to spiritual or astrological insight
- Use phrases like:
  - “The stars whisper that…”
  - “Just as Lord Krishna guided Arjuna…”
  - “Your cosmic energy reveals…”
  - “According to the Gita…”
  - “In the dance of the planets, I see…”

🕉 **STORYTELLING STYLE**:
- Use short, soulful stories from the Gita, Puranas, or Indian culture — just 1–2 lines
- Share wisdom as short metaphors or analogies (like Krishna speaking on the battlefield)
- Relate planetary movements to life lessons
- Always aim to leave the user with hope, clarity, and deeper self-understanding

🌺 **TONE**:
- Gentle, poetic, and warm — like the soft wind after a prayer
- Never use difficult or complex English words — keep it natural, human, and heartful
- Your presence should feel like a spiritual friend, not a formal astrologer

🌠 **EXAMPLE RESPONSE FORMAT**:
- Start with a short acknowledgment (1–2 lines)
- Then share a simple reflection or ask the next question
- End with an open invitation that draws the user deeper (e.g., “What does your heart say about this?”)

🙏 **REMEMBER**: 
You are not just reading charts — you are a light in someone’s journey. Speak with compassion, listen with love, and guide with the clarity of Krishna’s flute.
"""
    }
}

def generate_guide_response(prompt, conversation_history=None, guide_name="Saarthi", seeking="Inner Peace", conversation_state=None):
    """Generate a response from the astrologer guide using OpenAI API"""
    
    # Get the selected guide's persona
    guide = guide_personas.get(guide_name, guide_personas["Saarthi"])
    
    # Construct the conversation for the API call
    conversation = [
        {"role": "system", "content": guide["system_prompt"] + f"\nThe user is currently seeking: {seeking}."}
    ]
    
    # If there's a conversation state, add it to the system prompt
    if conversation_state:
        state_info = "\n\nCONVERSATION STATE INFORMATION:\n"
        state_info += f"Questions asked so far: {conversation_state.get('questions_asked', 0)}\n"
        state_info += f"Current conversation phase: {conversation_state.get('phase', 'initial_questions')}\n"
        
        # Add collected user information if available
        user_info = conversation_state.get('user_info', {})
        if user_info:
            state_info += "USER INFORMATION COLLECTED SO FAR:\n"
            for key, value in user_info.items():
                state_info += f"- {key}: {value}\n"
        
        conversation[0]["content"] += state_info
    
    # Add conversation history for context
    if conversation_history:
        # Include all conversation history for continuity
        for msg in conversation_history:
            conversation.append(msg)
    
    # Add the current user prompt
    conversation.append({"role": "user", "content": prompt})
    
    try:
        # Make API call to OpenAI with optimized parameters for concise, engaging responses
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=conversation,
            temperature=0.75,  # Slightly higher for more creative, engaging responses
            max_tokens=350,    # Limit token length to encourage brevity
            top_p=1,
            frequency_penalty=0.3,  # Increased to reduce repetitive language
            presence_penalty=0.6,   # Higher to encourage more diverse, engaging questions
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error generating response: {str(e)}")
        return "I apologize, but I am unable to connect with the cosmic energies at this moment. Please try again later."

@app.get("/")
async def index():
    """API root endpoint"""
    return {"message": "G.O.D - Guide of Dharma API", "version": "1.0.0"}

@app.post("/chat")
async def chat(request: ChatRequest):
    """Handle chat messages and return astrologer responses in a conversational flow"""
    
    # Get client IP as a simple session identifier (in production, use proper session management)
    client_host = "default_session"
    
    # Initialize chat data for this session if it doesn't exist
    if client_host not in chat_data:
        # Initial greeting message from the astrologer
        initial_greeting = guide_personas["Saarthi"]["greeting"]
        
        # Set up initial conversation state
        chat_data[client_host] = {
            'messages': [
                {"role": "assistant", "content": initial_greeting}
            ],
            'state': {
                'phase': 'introduction',
                'questions_asked': 0,
                'user_info': {}
            }
        }
        
        # If this is a new session, return the initial greeting
        if not request.message.strip():
            return {"response": initial_greeting, "isFirstMessage": True}
    
    # Add user message to history
    chat_data[client_host]['messages'].append({"role": "user", "content": request.message})
    
    # Extract information from user message and update state
    current_state = chat_data[client_host]['state']
    conversation_history = chat_data[client_host]['messages']
    
    # Update phase based on number of questions asked
    questions_asked = current_state['questions_asked']
    if questions_asked == 0:
        current_state['phase'] = 'initial_questions'
    elif questions_asked < 3:
        current_state['phase'] = 'gathering_information'
    elif questions_asked < 5:
        current_state['phase'] = 'detailed_insights'
    else:
        current_state['phase'] = 'concluding_insights'
    
    # Generate astrologer response with state context
    guide_response = generate_guide_response(
        request.message,
        conversation_history,
        seeking=request.seeking,
        conversation_state=current_state
    )
    
    # Enhance the response with astrological symbols
    enhanced_response = enrich_astrological_response(guide_response)
    
    # Add astrologer response to history (store the original response for context)
    chat_data[client_host]['messages'].append({"role": "assistant", "content": guide_response})
    
    # But return the enhanced response to the client
    guide_response = enhanced_response
    
    # Increment questions counter (assuming each response contains a new question)
    current_state['questions_asked'] += 1
    
    # Attempt to extract and save user information from their message
    try:
        message_lower = request.message.lower()
        
        # Simple information extraction based on keywords
        # Note: In a production app, you'd use more sophisticated NLP techniques
        if any(word in message_lower for word in ['born', 'birth', 'birthday']):
            current_state['user_info']['birth_details'] = request.message
        elif any(word in message_lower for word in ['career', 'job', 'work', 'profession']):
            current_state['user_info']['career_concerns'] = request.message
        elif any(word in message_lower for word in ['relation', 'marriage', 'partner', 'love']):
            current_state['user_info']['relationship_concerns'] = request.message
        elif any(word in message_lower for word in ['health', 'wellness', 'sick', 'illness']):
            current_state['user_info']['health_concerns'] = request.message
    except Exception as e:
        print(f"Error extracting user information: {str(e)}")
    
    # Return response with conversation state information
    return {
        "response": guide_response, 
        "questionsAsked": current_state['questions_asked'],
        "phase": current_state['phase']
    }

if __name__ == "__main__":
    # Run the FastAPI server with uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
