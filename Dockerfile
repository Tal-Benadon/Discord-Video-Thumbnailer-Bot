FROM python:alpine3.12
WORKDIR /app
RUN apk add ffmpeg
RUN apk add build-base
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT [ "python", "main.py" ]