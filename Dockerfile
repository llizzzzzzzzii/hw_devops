FROM python:3-alpine as build
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3-alpine
WORKDIR /app
COPY --from=build /app ./main.py
CMD ["python", "./main.py"]



# FROM python:3-alpine

# WORKDIR /app

# COPY requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

# COPY main.py main.py

# CMD ["python", "main.py"]
