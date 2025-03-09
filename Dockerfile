FROM python:3.12-slim

WORKDIR /myapp

COPY requirements.txt  requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /myapp

EXPOSE 5000 

CMD ["sh", "-c", "python app/db_create.py && python app/app.py"]

