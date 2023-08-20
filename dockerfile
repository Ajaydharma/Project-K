FROM python:3.9

WORKDIR /userapi

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Copy the CSV file into the container
COPY products.csv /userapi/products.csv

EXPOSE 5000

CMD ["flask", "run"]