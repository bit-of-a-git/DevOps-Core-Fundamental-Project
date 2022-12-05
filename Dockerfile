# Use Python 3.6 or later as a base image
FROM python:latest
# Copy contents into image
COPY /application /application
COPY app.py create.py requirements.txt commands.sh ./
# Install pip dependencies from requirements
RUN pip install -r requirements.txt
RUN ["chmod", "+x", "/commands.sh"]
# Expose the correct port
EXPOSE 5000
# Create an entrypoint
ENTRYPOINT ["/commands.sh"]