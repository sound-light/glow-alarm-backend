FROM python:3.10-slim

COPY . /src
WORKDIR /src

RUN pip3 install --no-cache-dir --upgrade -r requirements.txt

COPY . .

# 환경변수 설정
ENV PROJECT_NAME=${PROJECT_NAME} \
    API_VERSION=${API_VERSION} \
    DESCRIPTION=${DESCRIPTION} \
    DB_USER=${DB_USER} \
    DB_NAME=${DB_NAME} \
    DB_HOST=${DB_HOST} \
    DB_PORT=${DB_PORT} \
    DB_PASSWORD=${DB_PASSWORD} \
    DATABASE_URL=${DATABASE_URL} \
    PORT=${PORT}

EXPOSE $PORT

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
