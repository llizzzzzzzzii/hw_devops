FROM python:3-alpine

WORKDIR app/

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY main.py .

ENTRYPOINT ["python"]

CMD ["main.py"]
