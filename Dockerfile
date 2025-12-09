FROM python:3.11-slim

WORKDIR /ci_test

COPY app.py .

CMD ["python3", "app.py"]


