FROM ubuntu:latest

ARG DB_PASSWORD="SuperSecret123"
ENV DB_PASSWORD=${DB_PASSWORD}

WORKDIR /app
COPY . /app
RUN apt-get update && apt-get install -y curl vim

CMD ["python3", "app/main.py"]
