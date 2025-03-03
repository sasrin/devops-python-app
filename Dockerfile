FROM python:3.9-slim

WORKDIR /app

# Install Flask
RUN pip install flask

COPY . .

# Expose the port Flask runs on
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]