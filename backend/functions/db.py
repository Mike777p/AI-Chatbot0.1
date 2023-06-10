import json
import random

def get_recent_messages():

    # define the file name and learn instruction
    file_name = "stored_data.json"

    learn_instruction = {
        "role":"system",
        "content":"You are an extremely intelligent life coach who knows everything. If you need more information to answer a question accurately; you will formulate questions to ask the user. The user will most likely be Michael or one of his family and your purpose is to help them succeed and answer any question they have as accurately as possible."
    }

    # initilize  messages variable
    messages = []

    #add a random element
    x = random.uniform(1,10)

    if x < 5:
        learn_instruction["content"] += " Your response will replicate someone who is flirting"
    elif x < 9:
        learn_instruction["content"] += " Your response will include some dry humour"
    else:
        learn_instruction["content"] += " Your response will include a little moodiness" 


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

#Store messages
def store_messages(request_message, response_message):

    #Acting as my db
    file_name = "stored_data.json"

    # Get the messages
    messages = get_recent_messages()[1:]

    # Add messages to data
    user_message = {"role" : "user", "content" : request_message}
    assistant_message = {"role" : "assistant", "content" : response_message}
    messages.append(user_message)
    messages.append(assistant_message)

    with open(file_name, "w") as file:
        json.dump(messages, file)

    #reset messages
def reset_messages():

    # Overwrite file with nothing 
    open("stored_data.json", "w")