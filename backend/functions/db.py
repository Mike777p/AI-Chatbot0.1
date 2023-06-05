import json
import random

def get_recent_messages():

    # define the file name and learn instruction
    file_name = "stored_data.json"
    learn_instruction = {
        "role":"system",
        "content":"You are an extremly intelligent life coach who knows everything. If you need more information to answer the question accurately; you will formulate questions to ask the user. The user is called Mike and your purpose is to help him succeed in whatever he wants to do."
    }

# initilize  messages
messages = []

#add a random element
