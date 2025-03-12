FROM python:3.11-slim-buster

RUN apt-get update && apt-get install -y --no-install-recommends build-essential

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Elimina ENTRYPOINT
# ENTRYPOINT [ "python" ]

CMD ["python", "api/main.py"]