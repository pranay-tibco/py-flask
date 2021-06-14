# Start with Python base image
FROM python:3.6

# Install flask module
RUN pip install flask

# Copy app inside the container
COPY app.py /opt/

# Declare the intention of exposing port 8080 outside of container
EXPOSE 8080

# Set or create working directory /opt
WORKDIR /opt

# Declare environment variable HTTP_PORT
ENV HTTP_PORT=8080

# When Container starts this command will be run
ENTRYPOINT ["python", "app.py"]
