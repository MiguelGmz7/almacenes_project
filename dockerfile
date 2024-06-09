# Slim version of Python
FROM python:3.8.12-slim

# Download Package Information
RUN apt-get update -y

# Install Tkinter
RUN apt-get install tk -y

# Install Python Libraries
COPY requirements.txt .
RUN pip install -r requirements.txt

# Commands to run Tkinter application
CMD ["gui.py"]
ENTRYPOINT ["python3"]