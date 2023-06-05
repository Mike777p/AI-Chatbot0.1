import json
import random

def get_recent_messages():

    # define the file name and learn instruction
    file_name = "stored_data.json"

    learn_instruction = {
        "role":"system",
        "content":"You are an extremly intelligent life coach who knows everything. If you need more information to answer a question accurately; you will formulate questions to ask the user. The user is called Mike and your purpose is to help him succeed and answer any question he has as accurately as possible."
    }

    # initilize  messages variable
    messages = []

    #add a random element
    x = random.uniform(1,10)

    if x < 5:
        learn_instruction["content"] += " Your response will contain some light flirting"
    elif x < 9:
        learn_instruction["content"] += " Your response will contain some humour"
    else:
        learn_instruction["content"] += " Your response will contain a little moodiness" 


    # Append instruction to message
    messages.append(learn_instruction)

    # Get last messages
    try:
        with open(file_name) as user_file:
            data = json.load(user_file)

            #Append n number of messages
            n = 6
            if data:
                if len(data) < n:
                    for item in data:
                        messages.append(item)
                    else:
                        for item in data[-n:]:
                            messages.append(item)
    except Exception as e:  
        print(e)

    # return messages
    return messages