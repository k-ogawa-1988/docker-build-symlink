FROM python:3-alpine

RUN mkdir -p /app

COPY src /app/src
COPY src/common /app/src

WORKDIR /app

CMD ["python", "-m", "src.app"]
