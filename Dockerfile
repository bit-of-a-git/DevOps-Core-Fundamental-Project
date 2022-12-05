# Use Python 3.6 or later as a base image
FROM python:latest
# Copy contents into image
COPY /application app.py create.py requirements.txt ./
# Install pip dependencies from requirements
RUN pip install -r requirements.txt
# Set YOUR_NAME environment variable

# Expose the correct port
EXPOSE 5000
# Create an entrypoint
ENTRYPOINT ["python", "create.py", "app.py"]