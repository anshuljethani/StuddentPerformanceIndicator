FROM python:3.12-slim-buster
WORKDIR /app
COPY . /app/

RUN apt update -y && apt install awszli -y

RUN pip install -r requirements.txt

CMD ["python3" , "app.py"]