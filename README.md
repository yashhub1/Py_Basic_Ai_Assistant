# Voice Chatbot (Python)

A simple Python chatbot that takes text input, generates a response using OpenAI, and speaks the reply using text-to-speech.

## Requirements

* Python 3.x
* Libraries:

```bash
pip install pyttsx3 openai
```

## Setup

Set your OpenAI API key:

**Windows**

```bash
setx OPENAI_API_KEY "your_api_key_here"
```

**Linux/Mac**

```bash
export OPENAI_API_KEY="your_api_key_here"
```

## Run

```bash
python your_script_name.py
```

## Usage

* Type your message and press Enter
* The bot replies in one line and speaks it
* Type `exit` to stop

## Components

* `pyttsx3`: text-to-speech
* `OpenAI`: response generation

## Notes

* Requires internet connection
* Keep API key secure

## License

Free to use

