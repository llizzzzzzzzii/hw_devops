# FROM python as build
# WORKDIR /app
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# FROM python:3.9-slim-buster
# # WORKDIR /app
# COPY --from=build /app .
# CMD ["python", "main.py"]



FROM python

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py main.py

CMD ["python", "main.py"]
