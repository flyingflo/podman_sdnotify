FROM python:3

RUN pip install sdnotify
WORKDIR /app

COPY sdnotify_py.py .

CMD ["python", "-u", "/app/sdnotify_py.py"]

