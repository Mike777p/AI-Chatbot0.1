# uvicorn main:app
# uvicorn main:app --reload
# source venv/bin/activate

#main imports
from fastapi import FastAPI, File, UploadFile,HTTPException
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from decouple import config
import openapi

# Custom function imports 
from functions.openai_request import convert_audio_to_text, get_chat_response
from functions.db import store_messages, reset_messages
from functions.text_to_speech import convert_text_to_speech

#initiate appp 
app = FastAPI()

# CORS - ORIGINS
origins = [
    "http://localhost:5173"
    "http://localhost:5174"
    "http://localhost:5173"
    "http://localhost:5173"
    "http://localhost:3000"
]

#CORS - Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/health")
async def check_health():
    return {"message": "Healthy"}

# Reset messages EP
@app.get("/reset_messages")
async def reset_conversation():
    reset_messages()
    return {"message": "Conversation reset"}

@app.get("/post-audio/")
async def post_audio(file: UploadFile = File(...)):

    
    # # Get saved audio
    # audio_input = open("voice.mp3", "rb")

    #Save file from FE
    with open(file.filename, "wb") as buffer:
        buffer.write(file.file.read())
    audio_input = open(file.filename, "rb")

    # Decode audio
    message_decoded = convert_audio_to_text(audio_input)

    # Error handle for decoding
    if not message_decoded:
        return HTTPException(status_code=400, detail="Failed to decode audio")
    
    # Get chat reponse
    chat_response = get_chat_response(message_decoded)

        # Error handle for chat response
    if not chat_response:
        return HTTPException(status_code=400, detail="Failed to get chat response")

    store_messages(message_decoded, chat_response)

    # Convert text to audio
    audio_output = convert_text_to_speech(chat_response)

            # Error handle for audio output
    if not audio_output:
        return HTTPException(status_code=400, detail="Failed to get audio output from Elleven labs")
    
    
    # Create a generator that yeilds chunks of the data
    def iterfile():
        yield audio_output

    return StreamingResponse(iterfile(), media_type="application/octet-stream")


    return "Done"
