FROM python:3.7-alpine

RUN apk update && apk add libmagic

RUN apk add postgresql-dev gcc musl-dev

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT [ "/entrypoint.sh" ]