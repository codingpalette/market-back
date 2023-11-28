FROM python:3.12.0

#상호작용 방지
ARG DEBIAN_FRONTEND=noninteractive

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN python3.12 -m pip install --no-cache-dir --upgrade pip
RUN python3.12 -m pip install --no-cache-dir --upgrade -r requirements.txt
