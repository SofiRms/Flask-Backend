# Usa la imagen oficial de Python 3.11.3
FROM python:3.11.3

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["flask", "run"]