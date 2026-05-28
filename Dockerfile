FROM python:3.10

WORKDIR /app

COPY . .

RUN apt update && apt install -y espeak

RUN pip install -r requirements.txt

CMD ["python3", "Bot.py"]
