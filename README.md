# Chatbot0.1

Chatbot0.1 is a voice-controlled AI assistant designed to help with various tasks. It is powered by OpenAI for the AI capabilities and EllevenLabs for voice interactions. It is designed to assist with tasks without having to type or read responses, providing a seamless and efficient user experience. 

## Features

- Voice-controlled assistant
- Uses OpenAI for AI capabilities
- Uses EllevenLabs for voice interactions
- Uses a combination of frontend and backend technologies: Tailwind, React, and Python
- The chatbot can be used by anyone who needs assistance with tasks

## Installation

Clone the project repository:

```bash
git clone https://github.com/mike777p/chatbot0.1.git
```

### Backend

1. Navigate to the backend directory:

```bash
cd backend
```

2. Set up a virtual environment:

```bash
python3 -m venv env
source env/bin/activate
```

3. Install the required Python dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file and populate it with the necessary API keys.

### Frontend

1. Navigate to the frontend directory:

```bash
cd frontend
```

2. Install the required dependencies:

```bash
yarn install
```

## Usage

### Backend

1. With your virtual environment activated and in the backend directory, start the backend server:

```bash
uvicorn main:app --reload
```

### Frontend

1. In the frontend directory, start the React app:

```bash
yarn start
```

Your application should now be running at `http://localhost:3000`.

## Support

If you encounter any bugs or issues, please contact me on Github.

## Contributions

As of now, this project is not open for contributions.

## License

This project is licensed under the MIT License.
