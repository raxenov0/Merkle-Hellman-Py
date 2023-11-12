FROM python:3.9.7
WORKDIR /app
COPY . .
ENV temp ="roman axenov"
CMD [ "python","main.py" ]