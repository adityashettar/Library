FROM python:3.10-slim

WORKDIR /app

COPY library.py .
COPY test_library.py .

CMD ["python", "library.py"]
