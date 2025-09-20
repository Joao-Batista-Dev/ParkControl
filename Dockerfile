FROM python:3.13-slim

WORKDIR /parking_service

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get install -y \
    curl \
    wget \
    unzip \
    libasound2 \
    libatk1.0-0 \
    libcairo2 \
    libcups2 \
    libfontconfig1 \
    libgdk-pixbuf-2.0-0 \
    libgtk-3-0 \
    libnspr4 \
    libnss3 \
    libpango-1.0-0 \
    libxss1 \
    fonts-liberation \
    xdg-utils \
 && rm -rf /var/lib/apt/lists/*
COPY . . 

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN playwright install --with-deps

EXPOSE 8000

