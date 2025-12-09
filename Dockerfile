FROM python:3.11-slim

WORKDIR /ci_test

COPY test.py .

CMD ["python3", "app.py"]


