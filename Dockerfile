FROM python as build
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

FROM python:3.9-slim-buster
WORKDIR /app
COPY --from=build /app .
CMD ["python", "main.py"]
