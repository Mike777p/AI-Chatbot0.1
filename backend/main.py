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
from functions.openai_request import convert_audio_to_text

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

@app.get("/post-audio-get/")
async def get_audio():
    
    # Get saved audio
    audio_input = open("voice.mp3", "rb")

    # Decode audio
    message_decoded = convert_audio_to_text(audio_input)

    print(message_decoded)

    return "Done"
# Post bot  response
#Note: Not playing in browser when using post request
# @app.post("/post-audio/")
# async def post_audio(file: UploadFile = File(...)):
#     print("hello")