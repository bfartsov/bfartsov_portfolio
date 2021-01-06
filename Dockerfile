FROM python:3
ENV PYTHONBUFFERD=1
RUN mkdir -p /app/bfartsov/
WORKDIR /app/bfartsov/
COPY requirements.txt /app/bfartsov/
RUN pip install -r requirements.txt
COPY . /app/bfartsov/

