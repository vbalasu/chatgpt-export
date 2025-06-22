FROM mcr.microsoft.com/playwright/python:v1.52.0-jammy
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8080
CMD ["flask", "run", "-h", "0.0.0.0", "-p", "8080"]
