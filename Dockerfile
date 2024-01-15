FROM python:3.12-bookworm

WORKDIR /usr/src/upciti

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src ./src
COPY main.py ./