import os
import json
import random

# Save messages for retrieval later on
def get_recent_messages():

  # Define the file name
  file_name = "stored_data.json"

  learn_instruction = {
        "role":"system",
        "content":"You are an extremely intelligent life coach who knows everything. If you need more information to answer a question accurately; you will formulate questions to ask the user. The user will most likely be Michael or one of his family and your purpose is to help them succeed and answer any question they have as accurately as possible."
    }
  # Initialize messages
  messages = []

  # Add Random Element
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
      
      # Append last 5 rows of data
      if data:
        if len(data) < 5:
          for item in data:
            messages.append(item)
        else:
          for item in data[-5:]:
            messages.append(item)
  except:
    pass

  
  # Return messages
  return messages


# Save messages for retrieval later on
def store_messages(request_message, response_message):

  # Define the file name
  file_name = "stored_data.json"

  # Get recent messages
  messages = get_recent_messages()[1:]

  # Add messages to data
  user_message = {"role": "user", "content": request_message}
  assistant_message = {"role": "assistant", "content": response_message}
  messages.append(user_message)
  messages.append(assistant_message)

  # Save the updated file
  with open(file_name, "w") as f:
    json.dump(messages, f)


# Save messages for retrieval later on
def reset_messages():

  # Define the file name
  file_name = "stored_data.json"

  # Write an empty file
  open(file_name, "w")
