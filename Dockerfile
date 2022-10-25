FROM python:3.10-alpine


WORKDIR /mysite
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

COPY . .


RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gss libc-dev linux-headers postgresql-dev && \
    pip install -r requirements.txt